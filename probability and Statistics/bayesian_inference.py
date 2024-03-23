import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
# Define the prior distribution ( Beta distribution)
def prior(alpha, beta):
    return stats.beta(alpha, beta)

# Define the likelihood function ( Binomial Distribution)
def likelihoof(data, theta):
    return np.prod(stats.binom.pmf(data, n=len(data), p=theta))

# Define the posterior distribution
def posterior(data, alpha, beta):
    return stats.beta(alpha + np.sum(data), beta + len((data) - np.sum(data)))

# Generate som example data
np.random.seed(42)
data = np.random.binomial(n=1, p=0.7, size=100) # Example binary data

# Define the prior hyperparameters
alpha_prior = 1
beta_prior = 1

# Computer posterios distribution
posterior_dist = posterior(data, alpha_prior, beta_prior)

# For visualization we use matplotlib.pyplot
theta_values = np.linspace(0,1,1000)
plt.plot(theta_values, (prior(alpha_prior, beta_prior).pdf(theta_values)), label='Prior')
plt.plot(theta_values, posterior_dist.pdf(theta_values), label='Posterior')
plt.xlabel('Parameter (θ)')
plt.ylabel('Density')
plt.title('Prior and Posterior Distributions')
plt.legend()
plt.show()







