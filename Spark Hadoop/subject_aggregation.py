from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('Square') \
    .master("local[*]") \
    .getOrCreate()
try:
  rdd = spark.sparkContext.parallelize([("Math",90),("English",80),("Math",95)])
  rdd2=rdd.reduceByKey(lambda a,b: a+b)
  print(rdd2.collect())
finally:
  spark.stop()