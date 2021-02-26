#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_soilgrids").version


from .bmi import SoilData

__all__ = [
    "SoilData",
]
