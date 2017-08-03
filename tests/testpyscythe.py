import sys

import pandas as pd

sys.path.append('../')
from pyscythe.interpolate import interpolate as interp
#switch to docs/inputDataSample before release so Makefile will work.
df = pd.read_csv('../docs/inputDataSample', header='infer', sep=',')

list = ['mpg2']
testResult = interp('mpg1', list, 'function', df)

print(testResult)
print(testResult.keys())
print(testResult.items())




