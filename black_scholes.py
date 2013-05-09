import math
from scipy.stats import norm

"""
This module provides an interface for pricing European Financial Options with
the Black-Scholes-Merton pricing model. Additionally, it provides an interface
for pricing European Options with the Put-Call Parity.
"""


def d1(S, K, sigma, r, t):
    """
    d1 term used in B.S. formula
    """
    numerator = math.log(S/K) + (r + (sigma*sigma)/2.0) * t
    denom = sigma * math.sqrt(t)
    return numerator / denom


def d2(S, K, sigma, r, t):
    """
    d2 term used in B.S. formula
    """
    return d1(S, K, sigma, r, t) - sigma*math.sqrt(t)


def call(S, K, sigma, r, t):
    """
    Return the price of a European Call Option using the Black-Scholes pricing
    model

    S: initial spot price of stock
    K: strike price of option
    sigma: volatility
    r: risk-free interest rate
    t: time to maturity (in years)
    """
    v1 = d1(S, K, sigma, r, t)
    v2 = d2(S, K, sigma, r, t)
    return S * norm.cdf(v1) - K * math.exp(-r * t) * norm.cdf(v2)


def put(S, K, sigma, r, t):
    """
    Return the price of a European Put Option using the Black-Scholes pricing
    model

    S: initial spot price of stock
    K: strike price of option
    sigma: volatility
    r: risk-free interest rate
    t: time to maturity (in years)
    """
    v1 = d1(S, K, sigma, r, t)
    v2 = d2(S, K, sigma, r, t)
    return K * math.exp(-r * t) * norm.cdf(-v2) - S * norm.cdf(-v1)


def put_call_put(S, K, r, t, c):
    """
    Return the price of a European Put Option using the put-call parity

    S: initial spot price of stock
    K: strike price of option
    r: risk-free interest rate
    t: time to maturity (in years)
    c: call option price
    """
    return K * math.exp(-r * t) + c - S


def put_call_call(S, K, r, t, p):
    """
    Return the price of a European Call Option using the put-call parity

    S: initial spot price of stock
    K: strike price of option
    r: risk-free interest rate
    t: time to maturity (in years)
    p: put option price
    """
    return S + p - K * math.exp(-r * t)
