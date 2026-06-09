import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


class Estimator:

    def mle_merge_probability(self, merged, total):
        return merged / total

    def beta_posterior(self, success, failure, alpha=1, beta_prior=1):
        posterior_alpha = alpha + success
        posterior_beta = beta_prior + failure

        return posterior_alpha, posterior_beta

    def plot_beta_distribution(self, alpha, beta_param, credible_interval=None):
        """
        Memplot grafik Fungsi Densitas Peluang (PDF) dari Distribusi Beta Posterior
        dan menandai area Bayesian Credible Interval jika diisi.
        """
        x = np.linspace(0, 1, 1000)
        y = beta.pdf(x, alpha, beta_param)

        plt.figure(figsize=(9, 5))
        plt.plot(x, y, label=f"Posterior Beta (α={alpha}, β={beta_param})", color="blue", linewidth=2)

        # Jika parameter credible_interval diisi, tandai area batasnya
        if credible_interval and isinstance(credible_interval, dict):
            lower = credible_interval.get('lower')
            upper = credible_interval.get('upper')
            if lower is not None and upper is not None:
                plt.axvline(lower, color="red", linestyle="--", label=f"Batas Bawah ({lower:.4f})")
                plt.axvline(upper, color="red", linestyle="--", label=f"Batas Atas ({upper:.4f})")
                # Mewarnai area di dalam interval
                x_fill = np.linspace(lower, upper, 500)
                y_fill = beta.pdf(x_fill, alpha, beta_param)
                plt.fill_between(x_fill, y_fill, color="red", alpha=0.15, label="95% Credible Interval")

        plt.title("Posterior Beta Distribution dengan Bayesian Credible Interval", fontsize=12)
        plt.xlabel("Probabilitas", fontsize=10)
        plt.ylabel("Densitas", fontsize=10)
        plt.grid(True, linestyle=":", alpha=0.6)
        plt.legend(loc="upper left")
        plt.show()
