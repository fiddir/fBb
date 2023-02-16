import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fBb",
    version="0.1.11",
    description="Python Package for Stochastic Interpolation via multipoint fractional Brownian bridges",
    long_description= long_description,
    maintainer = "Jan Friedrich",
    license="MIT",
    keywords="complex systems, stochastic interpolation, fractional Brownian motion",
    url="https://github.com/fiddir/fBb",
    packages=setuptools.find_packages(),
    install_requires=['requests','scipy','numpy','h5py','matplotlib', 'stochastic'],
    platforms=['any'],
    classifiers=[],
    entry_points={"console_scripts": ["fBb = fBb.fBb:main"]},
)
 
