import math
from scipy.stats import norm

# -------------------------------------------------
# Black-Scholes-Merton pricing for European Options
# -------------------------------------------------

# Time steps
one_month   = 1.0 / 12.0
two_month   = 2.0 / 12.0
one_month   = 3.0 / 12.0
four_month  = 4.0 / 12.0
six_month   = 6.0 / 12.0
one_year    = 1.0

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
    return S * norm.cdf(v1) - K * math.exp(-r*t) * norm.cdf(v2)

# ---------------------------------------------
# Black-Scholes pricing for European Put Option 
# ---------------------------------------------
def put(S, K, sigma, r, t):
    v1 = d1(S, K, sigma, r, t)
    v2 = d2(S, K, sigma, r, t)
    return K * math.exp(-r*t) * norm.cdf(-v2) - S * norm.cdf(-v1) 
