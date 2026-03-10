from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("Classic Spark Demo")
    .config("spark.sql.shuffle.partitions", "4")
    .getOrCreate()
)

# Simple test
df = spark.createDataFrame([(1, "hello"), (2, "world")], ["id", "msg"])
df.show()

spark.stop()
