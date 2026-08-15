from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName('Square') \
    .master("local[*]") \
    .getOrCreate()
try:
    rdd = spark.sparkContext.parallelize(["Abdullah","Hamza","Asad","Abdullah","Asad"])
    even_rdd = rdd.map(lambda x: x*x)
    even_rdd = rdd.map(lambda x: x*x*x)
    rdd=rdd.map(lambda x:(x,1))
    rdd=rdd.reduceByKey(lambda x,y:(x+y))
    print(rdd.collect())
    #print("Even numbers:", even_rdd.collect())
finally:
    spark.stop()
