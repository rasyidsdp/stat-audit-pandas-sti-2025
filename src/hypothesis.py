import numpy as np
import scipy.stats as stats

def z_test_two_sample(x_bar1, x_bar2, sigma1, sigma2, n1, n2, alternative='two-sided', alpha=0.05):
    """
    Menghitung Uji Z Dua Sampel Bebas secara manual berdasarkan Tsun (2020) hal. 309.
    """
    # Menghitung standar error gabungan
    pooled_se = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    
    # Menghitung nilai Z-statistik
    z_stat = (x_bar1 - x_bar2) / pooled_se
    
    # Menghitung P-value
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
        
    # Keputusan formal tanpa kata "Accept H0" sesuai panduan akademik
    if p_value < alpha:
        decision = "Reject H0"
        interpretation = f"Tolk H0 pada tingkat signifikansi {alpha}. Rata-rata kedua kelompok berbeda secara signifikan."
    else:
        decision = "Fail to reject H0"
        interpretation = f"Gagal menolak H0 pada tingkat signifikansi {alpha}. Tidak ada perbedaan rata-rata yang signifikan."
        
    return {
        "z_stat": z_stat,
        "p_value": p_value,
        "decision": decision,
        "interpretation": interpretation
    }