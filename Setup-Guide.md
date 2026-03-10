# Snowpark Connect Demo — Setup Guide

## What is this demo?

A side-by-side comparison of **Classic Spark** vs **Snowpark Connect** code.
The goal: show that only the **session setup changes** — everything else stays the same.

---

## Prerequisites

| Requirement | Classic Spark | Snowpark Connect |
|---|---|---|
| Python 3.10–3.12 | Yes | Yes |
| Java (JDK 17) | Yes (Spark runtime) | Yes (Spark Connect server) |
| PySpark | `pip install pyspark==3.5.3` | Included with `snowpark-connect` |
| Snowpark Connect | Not needed | `pip install snowpark-connect` |
| Snowflake account | Not needed | Yes |
| Key pair auth | Not needed | Yes (`.p8` private key) |

---

## Step-by-step Setup

### Step 1 — Install Java

Spark (both classic and Snowpark Connect) needs a JVM. Without Java, you get:

```
subprocess.CalledProcessError: Command '['/usr/libexec/java_home']' returned non-zero exit status 1
```

**Install via Homebrew:**

```bash
brew install openjdk@17
```

### Step 2 — Set JAVA_HOME

Homebrew installs OpenJDK as "keg-only" — it is NOT automatically linked. The system `java_home` tool cannot find it, so you must set `JAVA_HOME` manually.

```bash
export JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home
```

**Make it permanent** (add to shell profile):

```bash
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home' >> ~/.zshrc
```

> **Gotcha:** After adding to `~/.zshrc`, the current terminal still has the old environment.
> Run `source ~/.zshrc` or open a new terminal for it to take effect.

### Step 3 — Install Python packages

```bash
# For Classic Spark demos
pip install pyspark==3.5.3

# For Snowpark Connect demos
pip install snowpark-connect
```

> **Note:** The PyPI package name is `snowpark-connect`, NOT `snowflake-snowpark-connect`.

### Step 4 — Configure Snowflake connection

Snowpark Connect reads a connection named **`spark-connect`** from `~/.snowflake/connections.toml`.

Add this block to the file:

```toml
[spark-connect]
account = "SFSEAPAC-VYADAV_AWS_AU"
user = "VYADAV"
authenticator = "SNOWFLAKE_JWT"
private_key_file = "/Users/vyadav/.snowflake/keys/rsa_key_aws_au.p8"
warehouse = "SNOWFLAKE_LEARNING_WH"
database = "SNOWFLAKE_LEARNING_DB"
schema = "PUBLIC"
```

> **The connection name MUST be `spark-connect`** — that is the default name `snowpark_connect.init_spark_session()` looks for.

---

## Gotchas We Hit (and fixes)

| # | Error | Root Cause | Fix |
|---|---|---|---|
| 1 | `subprocess.CalledProcessError: '/usr/libexec/java_home'` | Java not installed | `brew install openjdk@17` |
| 2 | `JAVA_HOME` empty after adding to `~/.zshrc` | Shell profile not reloaded | Run `source ~/.zshrc` or open new terminal |
| 3 | `pip install snowflake-snowpark-connect` — no matching distribution | Wrong package name | Correct name: `pip install snowpark-connect` |
| 4 | `TypeError: Expected bytes or RSAPrivateKey, got <class 'NoneType'>` | `private_key_path` not recognized by Python Connector | Rename to **`private_key_file`** in `connections.toml` |
| 5 | Same RSAPrivateKey error with `~` in path | `~` not expanded by the library | Use absolute path: `/Users/vyadav/.snowflake/keys/...` |

### Detail on Gotcha #4 — `private_key_path` vs `private_key_file`

This is a known inconsistency in the Snowflake ecosystem:

| Tool | Expects |
|---|---|
| Snow CLI (`snow connection add`) | `private_key_path` |
| Snowflake Python Connector / Snowpark Connect | `private_key_file` |

The Snow CLI writes `private_key_path` to your TOML, but the Python Connector ignores it and gets `None` for the key — causing the `TypeError`. The fix is to use `private_key_file` in your `[spark-connect]` block.

---

## Running the Demo

### Classic Spark

```bash
python3 01_session_setup_classic.py
python3 02_dataframe_ops_classic.py
python3 03_sql_and_udf_classic.py
```

### Snowpark Connect

```bash
python3 01_session_setup_snowpark_connect.py
python3 02_dataframe_ops_snowpark_connect.py
python3 03_sql_and_udf_snowpark_connect.py
```

---

## Demo File Structure

| File Pair | What it shows | Code change needed? |
|---|---|---|
| `01_session_setup_classic.py` vs `01_session_setup_snowpark_connect.py` | Session creation (TOML-based) | **YES** — only this changes |
| `01.02_session_setup_classic.py` vs `01.02_session_setup_snowpark_connect.py` | Session creation (PAT-based) | **YES** — only this changes |
| `02_dataframe_ops_classic.py` vs `02_dataframe_ops_snowpark_connect.py` | select, filter, groupBy, join, window functions | **NO** — identical code |
| `03_sql_and_udf_classic.py` vs `03_sql_and_udf_snowpark_connect.py` | spark.sql(), temp views, Python UDFs | **NO** — identical code |
| `04_unsupported_classic.ipynb` vs `04_unsupported_snowpark_connect.ipynb` | Features that **DON'T** work on Snowpark Connect | N/A — shows failures |

### Jupyter Notebooks — What's NOT supported

The `04` pair are Jupyter notebooks that demonstrate features available on Classic Spark but **not on Snowpark Connect**:

| Feature | Classic Notebook | Snowpark Connect Notebook |
|---|:---:|:---:|
| RDDs (parallelize, map, reduce) | Works | **FAILS** — no SparkContext |
| Structured Streaming (readStream) | Works | **FAILS** — not supported |
| MLlib (Pipeline, LogisticRegression) | Works | **FAILS** — pyspark.ml not supported |
| SparkContext (broadcast, accumulator) | Works | **FAILS** — no SparkContext |
| Repartition / Coalesce | Works | **No-op** — silently ignored |

The Snowpark Connect notebook wraps each cell in `try/except` so it runs end-to-end, printing the actual error messages and Snowflake alternatives.

### Two ways to create a Snowpark Connect session

The `01` and `01.02` pairs show two different authentication approaches:

| File | Method | How it works | Best for |
|---|---|---|---|
| `01_session_setup_snowpark_connect.py` | **TOML config** | `snowpark_connect.init_spark_session()` — reads `[spark-connect]` from `~/.snowflake/connections.toml` | Local development, credentials stay out of code |
| `01.02_session_setup_snowpark_connect.py` | **Explicit PAT** | `SparkSession.builder.remote("sc://<host>/;token=...;...")` — connection string built in code | CI/CD pipelines, remote clients, no TOML available |

Both produce the same result — a `SparkSession` backed by Snowflake. Pick whichever fits your environment.

---

## Key Takeaway

> **"Change the connection string, not the code."**

| What | Changes? |
|---|---|
| `SparkSession.builder.master("local[*]")` → `.remote("sc://...")` | Yes |
| DataFrame API (select, filter, groupBy, join, window) | No |
| `spark.sql()` queries | No |
| Python UDFs (`@F.udf`) | No |
| `createDataFrame`, `show`, `collect` | No |
| Temp views | No |

### What is NOT supported on Snowpark Connect

| Spark Feature | Snowflake Alternative |
|---|---|
| RDDs | Use DataFrame API |
| Structured Streaming | Snowpipe Streaming / Dynamic Tables |
| MLlib | Snowpark ML / Cortex ML |
| GraphX | No direct equivalent |
| Delta Lake | Iceberg Tables |
| Avro / ORC readers | Parquet / CSV |
| Java / Scala UDFs | Python UDFs only |
