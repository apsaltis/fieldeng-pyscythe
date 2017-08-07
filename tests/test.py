import unittest
import sys
import pandas as pd

sys.path.append('../')
from pyscythe.linearInterpolate import interpolate as interp


class MyTestCase(unittest.TestCase):
    def test_interpolation(self):
        # switch to docs/inputDataSample before release so Makefile will work.
        df = pd.read_csv('../docs/testDataSample', header='infer', sep=',')
        # expected Result
        expectList = [2.0, 2.75, 3.5, 4.25, 5.0, 4.0, 3.0, 2.0, 1.0, 1.25, 1.5, 1.75, 2.0]
        list = ['sig1Raw','sig2Raw']
        testResult = interp('sig1Raw', list, 'function', df)

        index = 0
        resultList = []

        for i in testResult['sig2Raw']:
            resultList.append(testResult['sig2Raw'][index][0][2])
            index = index + 1


        print(resultList)
        print('==')
        print(expectList)
        print(resultList == expectList)

        self.assertEqual(expectList, resultList)


if __name__ == '__main__':
    unittest.main()
