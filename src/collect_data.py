"""

Mengumpulkan data isu dan pull request dari pandas-dev/pandas melalui GitHub REST API, lalu menyimpan hasilnya ke data/raw/ dan data/clean/

"""

import os
import time
import json
import requests
import pandas as pd
from pathlib import Path

# Konfigurasi
REPO      = "pandas-dev/pandas"
BASE_URL  = f"https://api.github.com/repos/{REPO}/issues"
PER_PAGE  = 100
MAX_PAGES = 30
SINCE     = "2020-01-01T00:00:00Z"

RAW_DIR   = Path("data/raw")
CLEAN_DIR = Path("data/clean")
RAW_DIR.mkdir(parents=True, exist_ok=True)
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

TOKEN = os.getenv("GITHUB_TOKEN", "")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def fetch_issues(state: str = "closed", max_pages: int = MAX_PAGES) -> list[dict]:
    """
    Mengambil isu dan PR dari GitHub API secara terpaginasi.

    Args:
        state: status isu - "open", "closed", atau "all"
        max_pages: batas halaman yang diambil

    Returns:
        list of dict dari respons JSON API
    """
    all_items = []

    for page in range(1, max_pages + 1):
        params = {
            "state": state,
            "since": SINCE,
            "per_page": PER_PAGE,
            "page": page,
        }
        resp = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=30)

        # Jika terkena rate limit, tunggu hingga jendela reset terbuka
        if resp.status_code == 403:
            reset_at = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            tunggu = max(reset_at - int(time.time()), 5)
            print(f"  Rate limit tercapai. Menunggu {tunggu} detik...")
            time.sleep(tunggu)
            resp = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=30)

        resp.raise_for_status()
        items = resp.json()

        if not items:
            print(f"  Halaman {page} kosong, pengambilan selesai.")
            break

        all_items.extend(items)
        print(f"  Halaman {page}: {len(items)} item (total: {len(all_items)})")
        time.sleep(0.5)

    return all_items


def clean_issues(raw_items: list[dict]) -> pd.DataFrame:
    """
    Mengekstrak kolom yang diperlukan dan menghitung kolom turunan.

    Kolom hasil:
        number          - nomor isu/PR
        title           - judul
        is_pr           - True jika item adalah pull request
        state           - "open" atau "closed"
        created_at      - waktu dibuat
        closed_at       - waktu ditutup (NaT jika masih terbuka)
        days_to_close   - selisih hari antara dibuat dan ditutup
        labels          - label yang melekat, dipisah koma
        has_bug         - True jika ada label mengandung "bug"
        has_enhancement - True jika ada label mengandung "enhancement"
        merged          - True jika PR digabungkan (None untuk isu biasa)
        user_login      - username pembuat
    """
    rows = []

    for item in raw_items:
        created = pd.to_datetime(item.get("created_at"))
        closed  = pd.to_datetime(item.get("closed_at")) if item.get("closed_at") else pd.NaT
        days    = (closed - created).days if pd.notna(closed) else None

        label_names = [lbl["name"] for lbl in item.get("labels", [])]

        is_pr  = "pull_request" in item
        merged = None
        if is_pr:
            merged = item.get("pull_request", {}).get("merged_at") is not None

        rows.append({
            "number":          item.get("number"),
            "title":           item.get("title", ""),
            "is_pr":           is_pr,
            "state":           item.get("state"),
            "created_at":      created,
            "closed_at":       closed,
            "days_to_close":   days,
            "labels":          ", ".join(label_names),
            "has_bug":         any("bug" in l.lower() for l in label_names),
            "has_enhancement": any("enhancement" in l.lower() for l in label_names),
            "merged":          merged,
            "user_login":      item.get("user", {}).get("login", ""),
        })

    return pd.DataFrame(rows)


def main():
    print(f"Mengambil data dari {REPO}...")
    raw_items = fetch_issues(state="closed", max_pages=MAX_PAGES)

    raw_path = RAW_DIR / "issues_raw.json"
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(raw_items, f, ensure_ascii=False, indent=2)
    print(f"\nData mentah disimpan ke {raw_path} ({len(raw_items)} item).")

    df = clean_issues(raw_items)
    clean_path = CLEAN_DIR / "dataset.csv"
    df.to_csv(clean_path, index=False)
    print(f"Data bersih disimpan ke {clean_path} ({len(df)} baris, {df.shape[1]} kolom).")

    n_issues = df[~df["is_pr"]].shape[0]
    n_prs    = df[df["is_pr"]].shape[0]
    n_merged = (df["merged"] == True).sum()
    print(f"\nRingkasan:")
    print(f"  Isu biasa    : {n_issues}")
    print(f"  Pull request : {n_prs}")
    print(f"  PR merged    : {n_merged}")
    if n_prs > 0:
        print(f"  Tingkat merge: {n_merged / n_prs:.2%}")


if __name__ == "__main__":
    main()