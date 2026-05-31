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

    def plot_beta_distribution(self, alpha, beta_param):

        x = np.linspace(0, 1, 1000)

        y = beta.pdf(x, alpha, beta_param)

        plt.figure(figsize=(8, 5))

        plt.plot(x, y)

        plt.title("Posterior Beta Distribution")
        plt.xlabel("Probability")
        plt.ylabel("Density")

        plt.grid(True)

        plt.show()
