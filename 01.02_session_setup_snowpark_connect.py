import urllib.parse
from snowflake import snowpark_connect
from pyspark.sql import SparkSession

# Replace these with your actual values
PAT = "<your-programmatic-access-token>"
SNOWPARK_CONNECT_HOST = "<your-host>.snowflakecomputing.com"
DATABASE = "MY_DB"
SCHEMA = "PUBLIC"
WAREHOUSE = "MY_WH"

pat_encoded = urllib.parse.quote(PAT, safe="")
db_encoded = urllib.parse.quote(DATABASE, safe="")
schema_encoded = urllib.parse.quote(SCHEMA, safe="")
wh_encoded = urllib.parse.quote(WAREHOUSE, safe="")

connection_string = (
    f"sc://{SNOWPARK_CONNECT_HOST}/;"
    f"token={pat_encoded};"
    f"token_type=PAT;"
    f"database={db_encoded};"
    f"schema={schema_encoded};"
    f"warehouse={wh_encoded}"
)

spark = (
    SparkSession
    .builder
    .remote(connection_string)
    .getOrCreate()
)

df = spark.createDataFrame([(1, "hello"), (2, "world")], ["id", "msg"])
df.show()

spark.stop()
