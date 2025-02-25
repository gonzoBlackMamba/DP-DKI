#!/usr/bin/env python
import os.path as op # path

subj = 'IAM_DEV_001' # subject name

root = op.join('/Volumes/Bindy/DPDKI',subj)  # main parent directory path the subject
dcmPath = op.join(root,'dicom') # obviously, a dicom folder path for the subject

# We acquired two averages for b = 1000 and b = 2000 s/mm^2
# These are the b1000 run 1 and run 2
dpdkib1r1Dir = op.join(root,'DPDKI_b1_r1')
dpdkib1r2Dir = op.join(root,'DPDKI_b1_r2')

# These are the b2000 run 1 and run 2
dpdkib2r1Dir = op.join(root,'DPDKI_b2_r1')
dpdkib2r2Dir = op.join(root,'DPDKI_b2_r2')

# We also gathered a seperate DDE scan with 63 directions
dpdki63Dir = op.join(root,'DPDKI63')

# This is the final directory that will store all the processed data following 
# running PyDesigner (w/o the fitting routines, only pre-processing steps)
dpdkiDir = op.join(root,'DPDKI')

# File names and such (shouldn't need to change)
dpdki_all = op.join(dpdki63Dir,'dwi_preprocessed.nii')

b1_run1 = op.join(dpdkib1r1Dir,'dwi_preprocessed.nii')
b1_run2 = op.join(dpdkib1r2Dir,'dwi_preprocessed.nii')

b2_run1 = op.join(dpdkib2r1Dir,'dwi_preprocessed.nii')
b2_run2 = op.join(dpdkib2r2Dir,'dwi_preprocessed.nii')

dpdki_b1 = op.join(dpdkiDir,'dpdki_b1.nii')
dpdki_b2 = op.join(dpdkiDir,'dpdki_b2.nii')
dpdki63 = op.join(dpdkiDir,'dpdki63.nii')