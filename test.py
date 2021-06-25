# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

Load(
    Filename=
    '/home/8cz/Workbench/MANTID/SCD363_ConvertPeaksWorkspace/data/corelli_lean.nxs',
    OutputWorkspace='corelli_lean')
Load(
    Filename=
    '/home/8cz/Workbench/MANTID/SCD363_ConvertPeaksWorkspace/data/corelli_peak.nxs',
    OutputWorkspace='corelli_peak')
ConvertPeaksWorkspace(PeakWorkspace='corelli_peak', OutputWorkspace='lpws')

lpws = mtd["lpws"]
corelli_peak = mtd["corelli_peak"]

print(corelli_peak.getPeak(0).getGoniometerMatrix())
print(lpws.getPeak(0).getGoniometerMatrix())