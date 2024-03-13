#!/usr/bin/env python
# -*- coding : utf-8 -*-
#---------------------------------------------------------------------
# Package Management
#---------------------------------------------------------------------
import sys as sys
import os # mkdir
import os.path as op # path
import glob as glob
from shutil import copyfile, rmtree
import subprocess
import pandas as pd
from mat73 import loadmat
import xml.etree.ElementTree as ET
import math

import numpy as np # array, ndarray
import numpy.matlib as npm

import nibabel as nib

import scipy as sp
from scipy import special
from scipy import interpolate
from scipy.interpolate import RectBivariateSpline
from scipy.interpolate import interp2d
from scipy.ndimage import generate_binary_structure
from scipy.ndimage import binary_erosion

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

import warnings
warnings.filterwarnings('ignore')