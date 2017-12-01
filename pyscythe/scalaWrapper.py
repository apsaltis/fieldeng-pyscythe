import pandas as pd
from pyspark.sql import SparkSession
from py4j.java_gateway import java_import


'''
#
#Create variables used by all calls
#
'''
spark = SparkSession \
    .builder \
    .appName("pysythe") \
    .config("spark.driver.extraClassPath", "/Users/vvagias/Documents/Development/Java/IdeaProjects/fieldeng-scythe/target/scythe-0.0.1-SNAPSHOT-jar-with-dependencies.jar") \
    .getOrCreate()
jvm = spark._sc._gateway.jvm
java_import(jvm, "com.hortonworks.scythe.LinearInterpolation()")


'''
#
#Test Passing of Doubles
#
'''
spark._jvm.com.hortonworks.scythe.LinearInterpolation().pyTestDouble(12.0)


'''
#
#Test Passing of Data Frame and processing by scala
#'''
# timestamp option is on strict parsing
data = spark.read.csv('/Users/vvagias/PycharmProjects/fieldeng-pyscythe/docs/testSig1', header=True, inferSchema=True, timestampFormat="yyyy-MM-dd HH:mm")

spark._jvm.com.hortonworks.scythe.LinearInterpolation().pyTestDataframe(data._jdf)

'''
#
#Test Passing of Dates
#
'''
# uncomment for python date conversion
#df = data.toPandas()
#df['time'] = pd.to_datetime(df['time'])
#data2 = spark.createDataFrame(df)

#spark._jvm.com.hortonworks.scythe.LinearInterpolation().pyTestDate(data2._jdf)


