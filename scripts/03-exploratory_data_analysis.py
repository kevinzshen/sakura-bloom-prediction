#### Preamble ####
# Purpose:
# Author: Kevin Shen
# Date: 30 November 2024
# Contact: kevinzshen3@gmail.com
# License: MIT
# Pre-requisites:
#  - `pandas` must be installed (pip install pandas)
#  - `numpy` must be installed (pip install numpy)

### Workspace Setup ###
import pandas as pd
import numpy as np

np.random.seed(2620)

# For better formatting in PyCharm's console
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

sm_df = pd.read_csv('../data/01-raw_data/sakura-modern.csv')
tm_df = pd.read_csv('../data/01-raw_data/temperatures-modern.csv')

