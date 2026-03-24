# -*- coding: utf-8 -*-
# -----------------------------------------------------------
#
# Profilers
# Copyright (C) 2017  Javier Becerra
# -----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, print to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# ---------------------------------------------------------------------

import numpy as np
from qgis.PyQt.QtCore import QCoreApplication, QT_TRANSLATE_NOOP

# ---------------------------------------------------------------------
# Traduction (UI-facing strings uniquement)
# ---------------------------------------------------------------------

def tr(text):
    """
    Fonction de traduction centralisée pour les libellés des profileurs.
    Contexte volontairement stable pour les TS.
    """
    return QCoreApplication.translate("Profilers", text)

def height(p):
    """Return the height profile for given track p."""
    return p["l"], p["z"]

def slopes_pct(p):
    """Return a profile's slope in percentage."""
    x = np.array(p["l"], dtype=float)
    y = np.array(p["z"], dtype=float)
    slope_pct = 100.0 * (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    slope_pct = np.concatenate(
        (slope_pct[0:1], 0.5 * (slope_pct[1:] + slope_pct[:-1]), slope_pct[-1:])
    )
    slope_pct[np.isnan(slope_pct)] = 0
    slope_pct[np.isinf(slope_pct)] = 0
    return x, slope_pct

def slopes_deg(p):
    """Return a profile's slope in degrees."""
    x, slope_pct = slopes_pct(p)
    slope_deg = np.degrees(np.arctan(slope_pct / 100.0))
    return x, slope_deg

# ---------------------------------------------------------------------
# Clés internes STABLES → fonctions
# ---------------------------------------------------------------------

PLOT_PROFILERS = {
    "HEIGHT": height,
    "SLOPE_PCT": slopes_pct,
    "SLOPE_DEG": slopes_deg,
}

# ---------------------------------------------------------------------
# Libellés UI NON traduits (source only)
# ---------------------------------------------------------------------

# PLOT_PROFILER_LABELS = {
#     "HEIGHT": "Height",
#     "SLOPE_PCT": "Slope (%)",
#     "SLOPE_DEG": "Slope (°)",
# }

PLOT_PROFILER_LABELS = {
    "HEIGHT": QT_TRANSLATE_NOOP("ProfileToolCore", "Height"),
    "SLOPE_PCT": QT_TRANSLATE_NOOP("ProfileToolCore", "Slope (%)"),
    "SLOPE_DEG": QT_TRANSLATE_NOOP("ProfileToolCore", "Slope (°)"),
}
