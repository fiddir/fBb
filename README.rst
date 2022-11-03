fBb
==========

A python package for stochastic interpolation of sparse time
or incomplete time series by fractional Brownian motion.

J. Friedrich, S. Gallon, A. Pumir, and R. Grauer, Phys. Rev. Lett. 125, 170602 (2020).

Installation
------------

The ``fBb`` package is available on pypi and can be installed using pip

.. code-block:: shell

    pip install fBb

How to use this package
--------------

Stochastic interpolation
~~~~~~~~

To use ``fBb``, to interpolate a sparse measurement points ``X_i`` 
import the multipoint fractional Brownian bridge process with the desired
Hurst parameter ``H`` and the desired resolution of the interpolation ``N_fine``.

.. code-block:: python

    from fBb import MFBB


    mfbb = MFBB(X_i, t_i, H, N_fine)
    X_bridge = mfbb.bridge()