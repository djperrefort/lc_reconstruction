#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""This module uses gaussian regressions to interpolate light curves in time"""

from .prediction import predict_band_flux, predict_light_curve
from .regression import fit_gaussian_process

__all__ = [
    'predict_band_flux',
    'predict_light_curve',
    'fit_gaussian_process'
]




