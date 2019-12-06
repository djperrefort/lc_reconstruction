#!/usr/bin/env python
# coding: utf-8

"""This module computes photometric data (e.g. flux, color) from a gaussian
regression.
"""

import numpy as np

from .utils import get_effective_wavelength


def predict_band_flux(gp, band_name, times):
    """Return the flux modeled by a gaussian regression in a single band

    Args:
        gp         (GP): A fitted gaussian process
        band_name (str): Name of band pass to return flux for
        times    (list): Times to predict flux for

    Returns:
        An array of flux values for the given times
        The errors in each flux value
    """

    effective_wavelength = get_effective_wavelength(band_name)
    wavelengths = np.ones(len(times)) * effective_wavelength
    predict_x_vals = np.vstack([times, wavelengths]).T
    return gp(predict_x_vals, return_var=True)


def predict_light_curve(gp, bands, times):
    """Return the flux modeled by a gaussian regression in multiple bands

    Times can either be a one dimensional list of times to be used for all
    bands or a two dimensional list specifying different times per band.

    Args:
        gp           (GP): A fitted gaussian process
        bands (list[str]): Name of band passes to return flux for
        times      (list): Times to predict flux for

    Returns:
        A 2d array of flux values for each band
        A 2d array of errors for the predicted fluxes
    """

    if np.ndim(times[0]) == 0:
        lc = np.array([predict_band_flux(gp, band, times) for band in bands])

    elif np.ndim(times[0]) == 1:
        lc = np.array(
            [predict_band_flux(gp, b, t) for b, t in zip(bands, times)])

    else:
        raise ValueError('Times must be a one or two dimensional list')

    return lc[:, 0], lc[:, 1]
