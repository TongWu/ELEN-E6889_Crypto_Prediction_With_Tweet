# -*- coding: utf-8 -*-
"""LSTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ovm6h3LafL8fNGuCRLw0CKU-hEnLu1WP
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import math
import sklearn
import sklearn.preprocessing
import datetime
import os
import matplotlib.pyplot as plt
import tensorflow as tf
# %matplotlib inline
from sklearn import metrics

from google.colab import drive
drive.mount('/content/drive')

# Fetch BTC trade raw data
BTC_raw = pd.read_csv("/content/drive/My Drive/ELEN-E6889/BTC_20220101-20230410.csv")
BTC_raw.columns = ['date', 'close_price', 'open_price', 'high', 'low', 'volume', 'change']
BTC_raw

# Split the raw data into parts
BTC_basic = BTC_raw[['date', 'close_price', 'open_price']]
BTC_quant = BTC_raw[['date', 'close_price', 'high', 'low', 'volume', 'change']]
