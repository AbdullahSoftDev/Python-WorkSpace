from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName('WordLengthCount') \
    .master("local[*]") \
    .getOrCreate()
try:
    sentences=["my name is abdullah"]
    rdd=spark.sparkContext.parallelize(sentences)
    word_counts=(
        rdd.flatMap(lambda sentence: sentence.split(" "))
           .map(lambda word: (word, len(word)))
    )
    results=word_counts.collect()
    for word, count in results:
        print(f"{word}:{count}")
      #print(f"'{word}':{count}")
finally:
    spark.stop()