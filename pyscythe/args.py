import argparse
import sys
from interpolate import interpolate as interp
import pandas as pd

#dev prints
#print('In first section')
#print(sys.argv)
#print(sys.argv[2])

# Using arg parse to pass args with flags
parser = argparse.ArgumentParser()
parser.add_argument("--signalName", help="[signalName, list, columnName, dataFrame]")
parser.add_argument("--list", help="list of signals to interpolate")
parser.add_argument("--columnName", help="column name of column with signal names")
parser.add_argument("--dataFrame", help="data frame with data")

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
df = pd.read_csv('/Users/vvagias/PycharmProjects/fieldeng-pyscythe/docs/inputDataSample', header='infer', sep=',')


signalName = str(dict['signalName'])
list1 = [dict['list']]
columnName = str(dict['columnName'])


testResult = interp(signalName, list1, columnName, df)

print(testResult)
print(testResult.keys())
print(testResult.items())