# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:25:05 2020

@author: OediP
"""

# -*- coding: utf-8 -*-
import numpy as np
from scipy.signal import sawtooth

import segmentation_tools

x = np.arange(0,20,0.1)
sin_curve = np.sin(x)
saw_curve = sawtooth(x,0.1)
saw_sin = sin_curve*saw_curve 

#max_error = 1
max_error = 0.1
k = segmentation_tools.top_down()
k.fit(saw_sin.reshape(len(saw_sin),1),max_error)
print(k.segment_borders)

assert k.error > max_error, "error to big"
assert np.max(k.labels) == 6, "wrong segments"
print("everything fine")