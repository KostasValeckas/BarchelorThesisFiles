# -*- coding: utf-8 -*-
"""
Simple usage example for PyReduce
Loads a sample X-shooter dataset, and runs the full extraction
"""

import os.path

import pyreduce
from pyreduce import datasets

# define parameters
instrument = "XSHOOTER"
target = ".*"
night = None
mode = "VIS"
steps = (
     "bias",
     "flat",
     "orders",
     "scatter",
     "norm_flat",
     "curvature",
     "wavecal_master",
     "science",
    # "continuum",
    # "finalize",
)
base_dir = "."
input_dir = "VISonly1x2"
output_dir = "OUTPUT"

config = pyreduce.configuration.get_configuration_for_instrument(instrument, plot=1)
#config["science"]["extraction_method"] = "arc"
#config["science"]["extraction_cutoff"] = 0

pyreduce.reduce.main(
    instrument,
    target,
    night,
    mode,
    steps,
    base_dir=base_dir,
    input_dir=input_dir,
    output_dir=output_dir,
    configuration=config,
    #order_range=(0,15),
)
