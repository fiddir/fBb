fBb
===

A python package for stochastic interpolation of sparse or incomplete time series by fractional Brownian motion.

For further references, see: J. Friedrich, S. Gallon, A. Pumir, and R. Grauer, Phys. Rev. Lett. 125, 170602 (2020).

Installation
------------

The ``fBb`` package is available on pypi and can be installed using pip

.. code-block:: shell

    pip install fBb

How to use this package
-----------------------

Stochastic interpolation
~~~~~~~~~~~~~~~~~~~~~~~~

To use ``fBb`` to interpolate sparse measurement points ``X_i`` at 
times ``t_i``
import the multipoint fractional Brownian bridge process with the desired
Hurst parameter ``H`` and the desired resolution of the interpolation ``N_fine``.

.. code-block:: python

    from fBb import MFBB

    mfbb = MFBB(X_i, t_i, H, N_fine)
    X_bridge = mfbb.bridge()
    t_bridge = mfbb.t_fine()

    plt.scatter(t_i, X_i)
    plt.plot(t_bridge, X_bridge)
    plt.show()

