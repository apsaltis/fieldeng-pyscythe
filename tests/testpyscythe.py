import sys

import pandas as pd

sys.path.append('../')
from pyscythe.interpolate import interpolate as interp

df = pd.read_csv('../docs/inputDataSample', header='infer', sep=',')

testResult = interp('mpg1', 'list', 'function', df)

print(testResult)