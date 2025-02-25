#!/usr/bin/env python
# -*- coding : utf-8 -*-

""" 
	Runs the DP-DKI program

	Hunter G. Moss, PhD (02/25/2025)
  
"""
from packages import *
from functions import *

# plt.rcParams["font.family"] = "Times New Roman"

#
# Locate mrtrix3 via which-ing dwidenoise
dwidenoise_location = shutil.which("dwidenoise")
if dwidenoise_location is None:
    raise Exception("Cannot find mrtrix3, please see " "https://github.com/m-ama/PyDesigner/wiki" " to troubleshoot.")

# Extract mrtrix3 path from dwidenoise_location
mrtrix3path = op.dirname(dwidenoise_location)

# Locate FSL via which-ing fsl
fsl_location = shutil.which("fsl")
if fsl_location is None:
    raise Exception("Cannot find FSL, please see " "https://github.com/m-ama/PyDesigner/wiki" " to troubleshoot.")

# Extract FSL path from fsl_location
fslpath = op.dirname(fsl_location)


def main():
    
	# -----------------------------------------------------------------
    # Parse Arguments
    # -----------------------------------------------------------------
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(
        prog="dpdki",
        formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog=textwrap.dedent(
            """\
        
                                    """
        ),
    )
    
    # Mandatory
    parser.add_argument(
        "dwi",
        nargs="+",
        help="The diffusion dataset you would like " "to process. ",
        type=str,
    )
  
if __name__ == "__main__":
	main()