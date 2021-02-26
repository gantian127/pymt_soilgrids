==============
pymt_soilgrids
==============


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_soilgrids-green.svg
        :target: https://anaconda.org/conda-forge/pymt_soilgrids

.. image:: https://img.shields.io/travis/gantian127/pymt_soilgrids.svg
        :target: https://travis-ci.org/gantian127/pymt_soilgrids

.. image:: https://readthedocs.org/projects/pymt-soilgrids/badge/?version=latest
        :target: https://pymt-soilgrids.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT plugin for soilgrids data


* Free software: MIT License
* Documentation: https://pymt-soilgrids.readthedocs.io.




========= ===================================
Component PyMT
========= ===================================

SoilData  `from pymt.models import SoilData`
========= ===================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

-------------------------
Installing pymt_soilgrids
-------------------------



To install `pymt_soilgrids`,

.. code::

  conda install pymt_soilgrids
