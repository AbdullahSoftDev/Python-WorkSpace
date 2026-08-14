from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName('WordLengthCount') \
    .master("local[*]") \
    .getOrCreate()
try:
  rdd1=spark.sparkContext.parallelize([1,2,3,4,5,6])
  rdd2=spark.sparkContext.parallelize([7,8,9,10,11])
  rdd2=rdd1.union(rdd2)
  print(rdd2.collect())
finally:
    spark.stop()
