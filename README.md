Options Pricing
===============

A series of python modules that can be used to price financial options using either the Black Scholes formula or the Binomal Options Pricing Model. More information about financial options can be found [here](http://www.investopedia.com/terms/o/option.asp).

Black Scholes
-------------

`black_scholes.py` is a python module for pricing financial options with the black-scholes-merton formula.

Binomial Options Pricing
------------------------

`binomial.py` is a python module for pricing financial options with the binomial options pricing model. It contains two implementations of the model (for both call and put options), the first of which, `call` and `put`, is a more straight-forward implementation, and the second of which, `call2` and `put2` is a faster implementation.
