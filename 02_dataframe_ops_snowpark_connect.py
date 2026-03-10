from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

from snowflake import snowpark_connect
spark = snowpark_connect.init_spark_session()

# ===== 1. CREATE DATAFRAMES =====
print("=" * 60)
print("1. createDataFrame — NO CHANGE needed")
print("=" * 60)

employees = spark.createDataFrame([
    (1, "Alice",   "Engineering", 120000),
    (2, "Bob",     "Engineering", 110000),
    (3, "Charlie", "Marketing",   90000),
    (4, "Diana",   "Marketing",   95000),
    (5, "Eve",     "Sales",       85000),
    (6, "Frank",   "Sales",      105000),
], ["id", "name", "department", "salary"])

departments = spark.createDataFrame([
    ("Engineering", "Building 1"),
    ("Marketing",   "Building 2"),
    ("Sales",       "Building 3"),
], ["dept_name", "location"])

employees.show()


# ===== 2. SELECT & FILTER =====
print("=" * 60)
print("2. select / filter — NO CHANGE needed")
print("=" * 60)

high_earners = (
    employees
    .select("name", "department", "salary")
    .filter(F.col("salary") > 100000)
)
high_earners.show()


# ===== 3. withColumn (derived columns) =====
print("=" * 60)
print("3. withColumn — NO CHANGE needed")
print("=" * 60)

with_bonus = employees.withColumn("bonus", F.col("salary") * 0.10)
with_bonus.select("name", "salary", "bonus").show()


# ===== 4. groupBy & agg =====
print("=" * 60)
print("4. groupBy / agg — NO CHANGE needed")
print("=" * 60)

dept_stats = (
    employees
    .groupBy("department")
    .agg(
        F.count("*").alias("headcount"),
        F.avg("salary").alias("avg_salary"),
        F.max("salary").alias("max_salary"),
    )
)
dept_stats.show()


# ===== 5. JOIN =====
print("=" * 60)
print("5. join — NO CHANGE needed")
print("=" * 60)

joined = employees.join(
    departments,
    employees["department"] == departments["dept_name"],
    "inner"
).select("name", "department", "salary", "location")

joined.show()


# ===== 6. ORDER BY =====
print("=" * 60)
print("6. orderBy — NO CHANGE needed")
print("=" * 60)

employees.orderBy(F.col("salary").desc()).show()


# ===== 7. WINDOW FUNCTIONS =====
print("=" * 60)
print("7. Window functions — NO CHANGE needed")
print("=" * 60)

window_spec = Window.partitionBy("department").orderBy(F.col("salary").desc())

ranked = (
    employees
    .withColumn("rank_in_dept", F.rank().over(window_spec))
    .withColumn("dept_avg", F.avg("salary").over(Window.partitionBy("department")))
)
ranked.select("name", "department", "salary", "rank_in_dept", "dept_avg").show()


# ===== 8. READ / WRITE =====
print("8. read/write — NO CHANGE needed (but storage differs). Example: spark.read.csv('@my_stage/data.csv')")
spark.stop()