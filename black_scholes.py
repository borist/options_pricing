import math
from scipy.stats import norm

# -------------------------------------------------
# Black-Scholes-Merton pricing for European Options
# -------------------------------------------------


# d1 term used in B.S. formula
def d1(S, K, sigma, r, t):
    numerator = math.log(S/K) + (r + (sigma*sigma)/2.0) * t
    denom = sigma * math.sqrt(t)
    return numerator / denom


# d2 term used in B.S. formula
def d2(S, K, sigma, r, t):
    return d1(S, K, sigma, r, t) - sigma*math.sqrt(t)


# ----------------------------------------------
# Black-Scholes pricing for European Call Option
# ----------------------------------------------
def call(S, K, sigma, r, t):
    v1 = d1(S, K, sigma, r, t)
    v2 = d2(S, K, sigma, r, t)
    return S * norm.cdf(v1) - K * math.exp(-r * t) * norm.cdf(v2)


# ---------------------------------------------
# Black-Scholes pricing for European Put Option
# ---------------------------------------------
def put(S, K, sigma, r, t):
    v1 = d1(S, K, sigma, r, t)
    v2 = d2(S, K, sigma, r, t)
    return K * math.exp(-r * t) * norm.cdf(-v2) - S * norm.cdf(-v1)


# ------------------------------------------
# Calculate call price using put-call parity
# ------------------------------------------
#   S: equity spot price
#   K: option strike price
#   r: risk-free interest rate
#   c: call option price
#
def put_call_put(S, K, r, t, c):
    return K * math.exp(-r * t) + c - S


# ------------------------------------------
# Calculate call price using put-call parity
# ------------------------------------------
#   S: equity spot price
#   K: option strike price
#   r: risk-free interest rate
#   p: put option price
#
def put_call_call(S, K, r, t, p):
    return S + p - K * math.exp(-r * t)
