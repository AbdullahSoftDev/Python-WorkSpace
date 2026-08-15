from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName('WordLengthCount') \
    .master("local[*]") \
    .getOrCreate()
try:
    nameee="my name is abdullah"
    words=nameee.split(" ")
    rdd=spark.sparkContext.parallelize(words)
    long=rdd.map(lambda word:(word,len(word)))
    results=long.collect()
    for word,length in results:
        print(f"{word}:{length}")
finally:
    spark.stop()
