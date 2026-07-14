import pytensor

pytensor.config.cxx = ""
import pymc as pm
import arviz as az
import numpy as np


def build_change_point_model(prices):
    """
    Bayesian single change point model.
    """

    prices = np.asarray(prices)

    n = len(prices)

    with pm.Model() as model:

        tau = pm.DiscreteUniform(
            "tau",
            lower=0,
            upper=n - 1
        )

        mu_1 = pm.Normal(
            "mu_1",
            mu=prices.mean(),
            sigma=prices.std()
        )

        mu_2 = pm.Normal(
            "mu_2",
            mu=prices.mean(),
            sigma=prices.std()
        )

        sigma = pm.HalfNormal(
            "sigma",
            sigma=prices.std()
        )

        mu = pm.math.switch(
            np.arange(n) < tau,
            mu_1,
            mu_2
        )

        pm.Normal(
            "obs",
            mu=mu,
            sigma=sigma,
            observed=prices
        )

    return model
def run_sampling(model):

    with model:

        trace = pm.sample(
            draws=500,
            tune=500,
            chains=1,
            cores=1,
            target_accept=0.90,
            random_seed=42,
            progressbar=True,
        )

    return trace
def summarize_results(trace):

    return az.summary(trace)

