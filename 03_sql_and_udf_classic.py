from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType, IntegerType

# --- Session (Classic) ---
spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("SQL & UDF - Classic")
    .getOrCreate()
)


# ===== 1. SPARK SQL — NO CHANGE =====
print("=" * 60)
print("1. spark.sql() — NO CHANGE needed")
print("=" * 60)

employees = spark.createDataFrame([
    (1, "Alice",   "Engineering", 120000),
    (2, "Bob",     "Engineering", 110000),
    (3, "Charlie", "Marketing",   90000),
    (4, "Diana",   "Marketing",   95000),
    (5, "Eve",     "Sales",       85000),
    (6, "Frank",   "Sales",      105000),
], ["id", "name", "department", "salary"])

# Register as temp view
employees.createOrReplaceTempView("employees")

# Run SQL
result = spark.sql("""
    SELECT department,
           COUNT(*) as headcount,
           ROUND(AVG(salary), 2) as avg_salary
    FROM employees
    GROUP BY department
    ORDER BY avg_salary DESC
""")
result.show()


# ===== 2. TEMP VIEWS & MULTI-STATEMENT SQL — NO CHANGE =====
print("=" * 60)
print("2. Temp Views & chained SQL — NO CHANGE needed")
print("=" * 60)

spark.sql("""
    SELECT name, salary,
           CASE
               WHEN salary >= 110000 THEN 'Senior'
               WHEN salary >= 90000  THEN 'Mid'
               ELSE 'Junior'
           END as level
    FROM employees
""").createOrReplaceTempView("employee_levels")

spark.sql("SELECT level, COUNT(*) as cnt FROM employee_levels GROUP BY level").show()


# ===== 3. PYTHON UDFs — NO CHANGE (same API) =====
print("=" * 60)
print("3. Python UDFs — NO CHANGE in code")
print("=" * 60)
print("   BEHAVIORAL NOTE: UDFs are lazily serialized in Snowpark Connect.")
print("   Serialization/import errors surface at .show()/.collect() time,")
print("   not when the UDF is defined. The code itself is unchanged.")

@F.udf(returnType=StringType())
def classify_salary(salary: int) -> str:
    if salary >= 110000:
        return "HIGH"
    elif salary >= 90000:
        return "MEDIUM"
    else:
        return "LOW"

employees.select(
    "name", "salary",
    classify_salary(F.col("salary")).alias("salary_band")
).show()


# ===== 4. UDF WITH EXTERNAL LOGIC — NO CHANGE =====
print("=" * 60)
print("4. UDF with logic — NO CHANGE in code")
print("=" * 60)

@F.udf(returnType=IntegerType())
def name_length(name: str) -> int:
    return len(name) if name else 0

employees.select(
    "name",
    name_length(F.col("name")).alias("name_len")
).orderBy("name_len").show()


# ===== 5. WHAT'S NOT SUPPORTED ON SNOWPARK CONNECT =====
print("5. Features NOT available on Snowpark Connect")


spark.stop()
print("Done.")
