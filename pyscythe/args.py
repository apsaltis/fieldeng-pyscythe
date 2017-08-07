import argparse
import sys
from linearInterpolate import interpolate as interp
import pandas as pd

#dev prints
#print('In first section')
#print(sys.argv)
#print(sys.argv[2])

# Using arg parse to pass args with flags
# Input example
# spark-submit --py-files pyscythe/linearInterpolate.py  pyscythe/args.py --signalName mpg1 --list mpg2 --columnName function --dataFrame df

parser = argparse.ArgumentParser(description='interpolate values for 2 incoming signals ...')

parser.add_argument("--signalName", help="name of the full signal")
parser.add_argument("--list", help="list of signals to interpolate")
parser.add_argument("--columnName", help="column name of column with signal names")
parser.add_argument("--dataFrame", help="data frame with data * not yet implemented...")

args = parser.parse_args()

#get dictionary from Namespace object
dict = vars(args)

#dev prints
#print(dict)
#print(dict['signalName'])

#run code

print('---------------------------------------------')

#todo ... How to pass and handle a dataframe in the call to this program ...

sys.path.append('../')

#switch to docs/inputDataSample before release so Makefile will work.
df = pd.read_csv('/Users/vvagias/PycharmProjects/fieldeng-pyscythe/docs/testDataSample', header='infer', sep=',')


signalName = str(dict['signalName'])
list1 = [dict['list']]
columnName = str(dict['columnName'])


testResult = interp(signalName, list1, columnName, df)

#print(testResult)
#print(testResult.keys())
#print(testResult.items())

#print(testResult['sig2Raw'][1][0][2])

index = 0
resultList = []

for i in testResult['sig2Raw']:
    resultList.append(testResult['sig2Raw'][index][0][2])
    index = index + 1

print(resultList)