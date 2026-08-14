from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName('WordLengthCount') \
    .master("local[*]") \
    .getOrCreate()
try:
  list1=[1,2,3,4,5,6,7,8,9]
  list2=[10,11,12,7,5,2]
  rdd1=spark.sparkContext.parallelize(list1)
  rdd2=spark.sparkContext.parallelize(list2)
  rdd3=rdd1.union(rdd2)
  rdd4=rdd3.distinct()
  rdd5=rdd4.sortBy(lambda x: x)
  result=rdd5.collect()
  print("result:", result)
finally:
    spark.stop()
