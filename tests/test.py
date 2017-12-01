import unittest
import sys
import pandas as pd
from pyspark.sql import SparkSession
sys.path.append('../')
from pyscythe.linearInterpolate import interpolate as interp
from pyscythe.patterMatch import patternFindExact as pfe


class MyTestCase(unittest.TestCase):
    def test_interpolation(self):

        print('Interpolation Test')
        print('- - - - - - - - - - - - - - - - - - - - -')

        # switch to docs/inputDataSample before release so Makefile will work.
        df = pd.read_csv('testDataSample', header='infer', sep=',')
        # expected Result
        expectList = [2.0, 2.75, 3.5, 4.25, 5.0, 4.0, 3.0, 2.0, 1.0, 1.25, 1.5, 1.75, 2.0]
        list = ['sig1Raw','sig2Raw']
        testResult = interp('sig1Raw', list, 'function', df)

        print(testResult)

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


    def test_interpolation_mil(self):
        print('Interpolation Test ***** ms ******')
        print('- - - - - - - - - - - - - - - - - - - - -')

        # switch to docs/inputDataSample before release so Makefile will work.
        df = pd.read_csv('testDataSample2', header='infer', sep=',')
        # expected Result is not accurate just a place holder
        expectList = [2.0, 2.75, 3.5, 4.25, 5.0, 4.0, 3.0, 2.0, 1.0, 1.25, 1.5, 1.75, 2.0]
        list = ['sig1Raw', 'sig2Raw']
        testResult = interp('sig1Raw', list, 'function', df)

        print(testResult)

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


    def test_spark_data_frame(self):
        spark = SparkSession \
            .builder \
            .appName("Python Spark SQL pyscythe") \
            .config("spark.pyscythe", "args") \
            .getOrCreate()
        expectList = [2.0, 2.75, 3.5, 4.25, 5.0, 4.0, 3.0, 2.0, 1.0, 1.25, 1.5, 1.75, 2.0]
        print('Spark DataFrame Test')
        print('- - - - - - - - - - - - - - - - - - - - -')
        df1 = spark.read.csv('testDataSample', header='true',
                             inferSchema='true')
        list = ['sig1Raw', 'sig2Raw']
        testResult = interp('sig1Raw', list, 'function', df1)

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



    def test_pattern_match(self):

        sig = [1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]
        pattern = [0.0, 1.0, 1.0, 0.0]
        expectDict = {4: 1.0, 5: 0.0, 6: -1.0, 10: 1.0, 11: 0.0, 12: -1.0}

        resultDict = pfe(sig, pattern)

        print(resultDict == expectDict)
        print(resultDict)


        self.assertEqual(expectDict, resultDict)


if __name__ == '__main__':
    unittest.main()
