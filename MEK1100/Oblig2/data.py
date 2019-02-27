import pandas as pd
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
data = sio.loadmat("data.mat")

u = data.get("u").T

x1 = u[:,159][34:70]*0.5
print x1
