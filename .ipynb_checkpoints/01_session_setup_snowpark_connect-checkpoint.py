from snowflake import snowpark_connect

spark = snowpark_connect.init_spark_session()

df = spark.createDataFrame([(1, "hello"), (2, "world")], ["id", "msg"])
df.show()

spark.stop()
