from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('Square') \
    .master("local[*]") \
    .getOrCreate()

try:
    rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5, 6, 7])
    even_rdd = rdd.filter(lambda x: x % 2 == 0)
    print("Even numbers:", even_rdd.collect())
    odd_rdd = rdd.filter(lambda x: x % 2 != 0)
    print("Odd numbers:", odd_rdd.collect())
finally:
    spark.stop()
