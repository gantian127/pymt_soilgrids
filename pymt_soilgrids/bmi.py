from __future__ import absolute_import

import pkg_resources

from soilgrids import BmiSoilGrids as SoilData

SoilData.__name__ = "SoilData"
SoilData.METADATA = pkg_resources.resource_filename(__name__, "data/SoilData")

__all__ = [
    "SoilData",
]
