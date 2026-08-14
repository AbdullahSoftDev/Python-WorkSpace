from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName('WordLengthCount') \
    .master("local[*]") \
    .getOrCreate()
try:
    rdd = spark.sparkContext.parallelize(["Abdullah", "Hamza", "Asad"])
    lengths = rdd.map(lambda x:len(x))
    total_length = lengths.reduce(lambda a, b: a + b)
    print("Total length of all words:", total_length)
finally:
    spark.stop()
