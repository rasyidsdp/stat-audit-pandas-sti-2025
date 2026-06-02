import numpy as np
from scipy import stats


class Inference:

    def confidence_interval(
        self,
        theta_hat: float,
        sigma: float,
        n: int,
        confidence: float = 0.95
    ) -> dict:
        """
    Menghitung confidence interval (CI) untuk estimasi parameter menggunakan distribusi normal (Z-interval).

    CI : theta_hat ± z_critical * (sigma / sqrt(n))

    Args:
        theta_hat (float): Nilai estimasi parameter (point estimate).
        sigma (float): Simpangan baku populasi yang diketahui.
        n (int): Ukuran sampel.
        confidence (float, optional): Tingkat kepercayaan interval. Default = 0.95 (95%).

    Returns:
        dict:
            Dictionary yang berisi:
            - theta_hat (float): estimasi parameter.
            - lower (float): batas bawah confidence interval.
            - upper (float): batas atas confidence interval.
            - margin (float): margin of error.
            - z_critical (float): nilai kritis distribusi normal.
            - confidence (float): tingkat kepercayaan yang digunakan.

    Raises:
        ValueError:
            Jika n <= 0, sigma < 0, atau confidence tidak berada pada rentang (0, 1).
    """
       
        if n <= 0:
            raise ValueError("n harus lebih besar dari 0")

        if sigma < 0:
            raise ValueError("sigma tidak boleh negatif")

        if not 0 < confidence < 1:
            raise ValueError("confidence harus berada antara 0 dan 1")

        alpha = 1.0 - confidence
        z_critical = stats.norm.ppf(1.0 - alpha / 2.0)

        margin = z_critical * sigma / np.sqrt(n)

        return {
            "theta_hat" : theta_hat,
            "lower"     : theta_hat - margin,
            "upper"     : theta_hat + margin,
            "margin"    : margin,
            "z_critical": z_critical,
            "confidence": confidence
        }

    def ci_bernoulli(
        self,
        k: int,
        n: int,
        confidence: float = 0.95
    ) -> dict:
        """
    Menghitung confidence interval untuk proporsi Bernoulli (binomial) menggunakan pendekatan distribusi normal (Wald Confidence Interval).

    MLE Bernoulli: 
        p_hat = k / n

    Confidence Interval (CI):
        p_hat ± z * sqrt(p_hat * (1 - p_hat) / n)

    Batas interval dibatasi pada rentang [0, 1] karena proporsi tidak dapat bernilai di luar rentang tersebut.

    Args:
        k (int): Jumlah keberhasilan (successes) dalam sampel.
        n (int): Jumlah total observasi atau percobaan.
        confidence (float, optional): Tingkat kepercayaan interval. Default = 0.95 (95%).

    Returns:
        dict:
            Dictionary yang berisi:
            - p_hat (float): estimasi proporsi sampel.
            - lower (float): batas bawah confidence interval.
            - upper (float): batas atas confidence interval.
            - margin (float): margin of error.
            - z_critical (float): nilai kritis distribusi normal.
            - confidence (float): tingkat kepercayaan yang digunakan.

    Raises:
        ValueError:
            Jika n <= 0, k berada di luar rentang [0, n], atau confidence tidak berada pada rentang (0, 1).
    """
        
        if n <= 0:
            raise ValueError("n harus lebih besar dari 0")

        if k < 0 or k > n:
            raise ValueError("k harus berada antara 0 dan n")

        if not 0 < confidence < 1:
            raise ValueError("confidence harus berada antara 0 dan 1")

        p_hat = k / n

        alpha = 1 - confidence
        z = stats.norm.ppf(1 - alpha / 2)

        se = np.sqrt(p_hat * (1 - p_hat) / n)
        margin = z * se

        lower = max(0, p_hat - margin)
        upper = min(1, p_hat + margin)

        if k == 0:
            lower = 0.0
            upper = 3.0 / n
            margin = upper - lower

        elif k == n:
            lower = 1.0 - 3.0 / n
            upper = 1.0
            margin = upper - lower

        return {
            "p_hat"     : p_hat,
            "lower"     : lower,
            "upper"     : upper,
            "margin"    : margin,
            "z_critical": z,
            "confidence": confidence
        }


    def ci_poisson(
        self,
        data: list | np.ndarray,
        confidence: float = 0.95
    ) -> dict:
        """
    Menghitung confidence interval untuk parameter λ (lambda) dari distribusi Poisson menggunakan pendekatan distribusi normal.

    Estimasi parameter λ diperoleh dari rata-rata sampel:
        lambda_hat = mean(data)

    Dengan standard error:
        SE = sqrt(lambda_hat / n)

    Confidence interval dihitung dengan rumus:
        lambda_hat ± z * SE

    Batas bawah interval dibatasi minimum 0 karena parameter λ pada distribusi Poisson tidak dapat bernilai negatif.

    Args:
        data (list | np.ndarray):
            Data sampel yang diasumsikan mengikuti distribusi Poisson.
            Seluruh nilai harus berupa bilangan non-negatif.
        confidence (float, optional):
            Tingkat kepercayaan interval. Default = 0.95 (95%).

    Returns:
        dict:
            Dictionary yang berisi:
            - lambda_hat (float): estimasi parameter λ.
            - lower (float): batas bawah confidence interval.
            - upper (float): batas atas confidence interval.
            - margin (float): margin of error.
            - z_critical (float): nilai kritis distribusi normal.
            - confidence (float): tingkat kepercayaan yang digunakan.
            - n (int): ukuran sampel.
            - se (float): standard error estimasi λ.

    Raises:
        ValueError:
            Jika data kosong, terdapat nilai negatif dalam data, atau confidence tidak berada pada rentang (0, 1).
    """

        data = np.asarray(data, dtype=float)

        if len(data) == 0:
            raise ValueError("data tidak boleh kosong")

        if np.any(data < 0):
            raise ValueError("data Poisson tidak boleh bernilai negatif")

        if not 0 < confidence < 1:
            raise ValueError("confidence harus berada antara 0 dan 1")

        n = len(data)

        lambda_hat = np.mean(data)
        alpha = 1 - confidence
        z = stats.norm.ppf(1 - alpha / 2)

        se = np.sqrt(lambda_hat / n)
        margin = z * se

        return {
            "lambda_hat": lambda_hat,
            "lower"     : max(0.0, lambda_hat - margin),
            "upper"     : lambda_hat + margin,
            "margin"    : margin,
            "z_critical": z,
            "confidence": confidence,
            "n"         : n,
            "se"        : se,
        }


    def credible_interval(
        self,
        alpha: float,
        beta: float,
        confidence: float = 0.95
    ) -> dict:
        """
    Menghitung Bayesian credible interval untuk distribusi Beta berdasarkan parameter posterior alpha dan beta.

    Credible interval dihitung menggunakan kuantil distribusi Beta:
        lower = Beta^{-1}(tail)
        upper = Beta^{-1}(1 - tail)

    dengan:
        tail = (1 - confidence) / 2

    Selain interval, fungsi juga menghitung nilai mean posterior dan mode posterior (jika terdefinisi).

    Untuk distribusi Beta(alpha, beta):
        mean = alpha / (alpha + beta)
        mode = (alpha - 1) / (alpha + beta - 2)

    Mode hanya terdefinisi jika alpha > 1 dan beta > 1.

    Args:
        alpha (float):
            Parameter alpha dari distribusi Beta posterior.
            Harus bernilai positif.
        beta (float):
            Parameter beta dari distribusi Beta posterior.
            Harus bernilai positif.
        confidence (float, optional):
            Tingkat kepercayaan credible interval.
            Default = 0.95 (95%).

    Returns:
        dict:
            Dictionary yang berisi:
            - lower (float): batas bawah credible interval.
            - upper (float): batas atas credible interval.
            - confidence (float): tingkat kepercayaan yang digunakan.
            - mean (float): nilai rata-rata posterior.
            - mode (float | None): modus posterior jika terdefinisi.
            - alpha (float): parameter alpha posterior.
            - beta (float): parameter beta posterior.

    Raises:
        ValueError:
            Jika alpha <= 0, beta <= 0, atau confidence tidak berada pada rentang (0, 1).
    """

        if alpha <= 0:
            raise ValueError("alpha harus lebih besar dari 0")

        if beta <= 0:
            raise ValueError("beta harus lebih besar dari 0")

        if not 0 < confidence < 1:
            raise ValueError("confidence harus berada antara 0 dan 1")

        tail = (1 - confidence) / 2

        lower = stats.beta.ppf(tail, alpha, beta)
        upper = stats.beta.ppf(1 - tail, alpha, beta)

        mean = alpha / (alpha + beta)                   
    
        if alpha > 1 and beta > 1:
            mode = (alpha - 1.0) / (alpha + beta - 2.0) 
        else:
            mode = None

        return {
            "lower"      : lower,
            "upper"      : upper,
            "confidence" : confidence,
            "mean"       : mean,
            "mode"       : mode,
            "alpha"      : alpha,
            "beta"       : beta,
        }