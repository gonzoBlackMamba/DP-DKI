#!/usr/bin/env python
# -*- coding : utf-8 -*-
#---------------------------------------------------------------------
# Package Management
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Package Management
#---------------------------------------------------------------------
import argparse  # ArgumentParser, add_argument
import glob  # recursive file search
import json
import textwrap  # dedent
import sys as sys
import os # mkdir
import os.path as op # path
import subprocess
import shutil
from shutil import copyfile
import numpy as np # array, ndarray
import numpy.matlib as npm
import nibabel as nib

import warnings
warnings.filterwarnings('ignore')