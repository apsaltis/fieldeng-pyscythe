# fieldeng-pyscythe

# Example Calling Scala Function:

from py4j.java_gateway import java_import
jvm = sc._gateway.jvm
java_import(jvm, "com.hortonworks.scythe.LinearInterpolation.pyTest")
a = sc._jvm.com.hortonworks.scythe.LinearInterpolation()
a.pyTest()



