from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('Square') \
    .master("local[*]") \
    .getOrCreate()
try:
  text_data = "Deer Bear River Car Car River Deer Car River"
  rdd = spark.sparkContext.parallelize([text_data])
  word_count = rdd.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

  result = word_count.collect()

  for word, count in result:
      print(f"{word}: {count}")
finally:
  spark.stop()