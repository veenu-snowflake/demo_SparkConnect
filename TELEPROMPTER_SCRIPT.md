# SNOWPARK CONNECT FOR APACHE SPARK
## Teleprompter Script (Pitch + Live Demo)

---

## PART 1: THE PITCH

---

### [SLIDE 1 — TITLE + PAIN POINTS]
**⏱ ~2 min**

> Hey everyone, thanks for joining.
>
> Today I want to talk about something that solves a very real pain point for anyone running Spark.
>
> If you're running Apache Spark today — whether it's on Databricks, EMR, or your own cluster — you already know the drill:
>
> **Unpredictable costs.** You've got clusters running, sometimes idle, sometimes over-provisioned. You need specialized talent just to keep things optimized. And that bill? It's a moving target.
>
> **Performance bottlenecks.** You're tuning shuffle partitions, picking partition keys, managing compaction — and still hitting concurrency issues.
>
> **Time spent on maintenance.** Version upgrades, cluster setup, driver issues. Your engineers are spending more time babysitting infrastructure than building pipelines.
>
> **Fragmented governance.** Your data catalog needs manual setup. RBAC is bolted on. Audit trails? Good luck.
>
> So the question is: **What if you could keep your Spark code... but drop all of that overhead?**
>
> That's exactly what Snowpark Connect does.

---

### [SLIDE 4 — FEATURE OVERVIEW TITLE]
**⏱ ~30 sec**

> **Snowpark Connect for Apache Spark.**
>
> In one line:
>
> *"Your Spark code, Snowflake's engine — zero rewrite, zero clusters."*
>
> It's GA since November 2025. Production-ready. Battle-tested.

---

### [SLIDE 6 — CHALLENGES AT SCALE]
**⏱ ~1.5 min**

> Let's look at the traditional architecture.
>
> You've got your data sitting in secure storage — Snowflake, S3, wherever. Then you pull it out into an external processing environment — a Spark cluster.
>
> That means:
> - **Data movement.** You're extracting data out, processing it externally, and pushing it back.
> - **Higher costs.** You're paying for compute that sits idle between jobs.
> - **Governance risk.** The moment data leaves your governed perimeter, you lose control.
>
> Your developers aren't writing transformations — they're provisioning infrastructure, tuning clusters, and managing version upgrades.
>
> *"Process data where it lives — no extract, no egress, no lag."*

---

### [SLIDE 7 — SPARK CONNECT PROTOCOL]
**⏱ ~1 min**

> Here's the clever part. Spark itself introduced a client-server split in version 3.4 — called **Spark Connect**.
>
> Your PySpark app becomes a thin client. It builds a logical plan and sends it over gRPC to a server.
>
> Normally, that server is a Spark cluster. With Snowpark Connect, **Snowflake IS the server.**
>
> *"Your app talks Spark protocol; Snowflake does the heavy lifting."*

---

### [SLIDE 8 — SNOWPARK CONNECT OVERVIEW]
**⏱ ~1 min**

> So what does this actually support?
>
> Three things — the big three that cover the vast majority of real-world Spark workloads:
>
> 1. **Apache Spark DataFrames** — select, filter, groupBy, join, window functions. All of it.
> 2. **Spark SQL** — CREATE TABLE, SELECT, JOINs, aggregations. Standard SQL through `spark.sql()`.
> 3. **Python UDFs** — your custom Python logic, running natively on Snowflake.
>
> *"DataFrames, SQL, UDFs — the APIs that matter, ready today."*
>
> And you get this on the Snowflake engine — the same vectorized engine that runs your SQL, with auto-scaling, auto-suspend, and zero cluster management.

---

### [SLIDE 9 — SNOWPARK EXECUTION LANDSCAPE]
**⏱ ~1 min**

> And just to be clear — Snowpark Connect isn't replacing anything. It's **adding to** the Snowpark family.
>
> You've got:
> - **pandas on Snowflake** — if your team likes pandas.
> - **Snowpark DataFrames** — our native Python API.
> - **UDFs and Stored Procedures** — for custom logic.
> - And now, **Spark Client** — for teams that already have PySpark code and don't want to rewrite it.
>
> All of these run on the same Snowflake warehouse. Same engine. Same governance. Same bill.
>
> *"New projects? Use Snowpark. Existing Spark code? Use Snowpark Connect."*

---

### [SLIDE 10 — CUSTOMER PROOF POINTS]
**⏱ ~1 min**

> Now, don't just take my word for it.
>
> Customers are seeing on average **54% cost savings** by moving from managed Spark to Snowflake.
>
> One customer saved **$800K annually** just by eliminating data movement out of Snowflake and back.
>
> And here's a quote from David Trumbell at CTC:
>
> *"Now with fewer ephemeral failures and higher visibility in Snowflake, we have a platform that's much easier and cost-effective to operate than managed Spark."*

---

### [SLIDE 13–14 — BOOKING.COM]
**⏱ ~1 min**

> Booking.com — nearly 3,000 Spark pipelines. They had a mandate to keep a standardized Spark codebase.
>
> They deployed Snowpark Connect as a **drop-in replacement**. No code changes.
>
> The result? A pipeline that took **90 minutes went down to 25 minutes.** That's a 70% reduction.
>
> Their quote: *"We didn't have to sacrifice critical engineering time to migrate workloads — they just worked!"*
>
> *"Change the connection, keep the code — migrate in days, not quarters."*

---

### [SLIDE 15–17 — PERFORMANCE & TCO]
**⏱ ~1.5 min**

> Performance numbers:
>
> - **3x faster** on internal benchmarks derived from TPCx-BB workloads.
> - Tredence's independent study: **3x faster and 8x greater cost savings** compared to managed Spark.
> - Salesforce saw **70% price-performance gains** — a 2XL Snowflake warehouse outperforming a 6XL Spark cluster.
>
> On TCO:
> - **10–25% reduction** in direct compute costs.
> - **20–30% strategic productivity gain** because your engineers stop managing infrastructure.
> - Over 3 years, that's a **15–28% TCO reduction**.
>
> *"Keep the code. Drop the cost. That's the conversation."*

---

### [SLIDE 22 — COMPETE SUMMARY]
**⏱ ~1 min**

> Quick comparison.
>
> | | Databricks / EMR | Snowpark Connect |
> |---|---|---|
> | Costs | Complex, unpredictable | Elastic, per-second billing |
> | Performance | Manual tuning needed | Snowflake optimizer handles it |
> | Governance | Fragmented, bolt-on | Built-in RBAC, masking, audit |
> | Maintenance | Cluster setup, version mgmt | Zero — just pick a warehouse size |
>
> *"One bill. Per-second. No Spark license, no cluster overhead."*

---

### [SLIDE 27 — CONNECTOR vs CONNECT]
**⏱ ~1 min**

> One thing I want to clarify — **Spark Connector** and **Snowpark Connect** are NOT the same thing.
>
> - **Spark Connector** = data moves OUT of Snowflake to your Spark cluster. Fragmented. Slow.
> - **Snowpark Connect** = data stays IN Snowflake. Your Spark code runs on the Snowflake engine. Unified. Fast. Open.
>
> *"Connector = data moves to you. Connect = you move to the data."*

---

### [SLIDE 29–30 — HOW IT WORKS]
**⏱ ~1 min**

> Under the hood, it's straightforward:
>
> 1. Your client runs standard PySpark with Spark Connect.
> 2. Spark Connect sends the query plan to Snowflake.
> 3. Snowpark Connect interprets the plan.
> 4. It optimizes it for Snowflake's engine.
> 5. Hands it off to Snowpark.
> 6. Snowpark runs it on the vectorized engine.
>
> All you do? **Update the connection string.** That's it.
>
> *"Snowflake speaks Spark so you don't have to speak Snowflake."*

---

### [SLIDE 32 — IDEAL WORKLOADS]
**⏱ ~45 sec**

> Best fit workloads:
>
> - Batch ETL — SQL, Python, or Java/Scala on roadmap.
> - Spark 3.5.x.
> - DataFrame API + SparkSQL.
> - Data in Snowflake or Iceberg tables.
>
> Not a fit today if you're using RDDs, MLlib, or GraphX. For ML, use Snowpark ML. For streaming, use Snowpipe or OpenFlow.
>
> *"RDDs are legacy. DataFrames are the future — and they're fully supported."*

---

### [SLIDE 33 — MIGRATION ACCELERATOR]
**⏱ ~30 sec**

> And if you want to check compatibility before you start, there's a free tool — the **Snowpark Migration Accelerator**.
>
> You feed it your Spark codebase, it gives you a compatibility score, tells you which files work out of the box, and flags anything that needs attention.
>
> *"99% of real-world Spark code works. The 1% has documented workarounds."*

---

### [TRANSITION TO DEMO]
**⏱ ~30 sec**

> Alright, enough slides. Let me show you this for real.
>
> I've got a side-by-side comparison ready — the exact same workloads running on **Classic Spark** and on **Snowpark Connect**.
>
> The punch line you'll see: **only the connection changes. Everything else is identical.**

---
---

## PART 2: LIVE DEMO — SIDE-BY-SIDE COMPARISON

---

### DEMO SETUP CONTEXT

> I have three pairs of scripts. Each pair does the exact same thing — one runs on Classic Spark (local cluster), the other runs on Snowpark Connect (Snowflake engine).
>
> Let me walk you through them one by one.

---

### DEMO 1: SESSION SETUP
**Files: `01_session_setup_classic.py` vs `01_session_setup_snowpark_connect.py`**

> Let's start with the foundation — how you create a Spark session.
>
> **Classic Spark:**
>
> ```python
> spark = SparkSession.builder.master("local[*]").appName("Classic Spark Demo").getOrCreate()
> ```
>
> You're telling Spark: use my local machine as the cluster. You pick the master, set shuffle partitions, manage everything.
>
> **Snowpark Connect:**
>
> ```python
> from snowflake import snowpark_connect
> spark = snowpark_connect.init_spark_session()
> ```
>
> Two lines. That's it. It reads your Snowflake connection from a TOML config file and connects to Snowflake as the backend.
>
> *"Size a warehouse, not a cluster."*
>
> Now watch — after this, the code is **IDENTICAL.**
>
> *(Run both scripts)*
>
> Same output. Same DataFrame. Different engine.

---

### DEMO 2: DATAFRAME OPERATIONS
**Files: `02_dataframe_ops_classic.py` vs `02_dataframe_ops_snowpark_connect.py`**

> This is where the magic really shows.
>
> I'm going to run through seven different DataFrame operations — these are the bread and butter of any Spark pipeline:
>
> 1. **createDataFrame** — building DataFrames from scratch.
> 2. **select & filter** — picking columns, filtering rows.
> 3. **withColumn** — adding derived columns (like a 10% bonus).
> 4. **groupBy & agg** — aggregations by department: headcount, avg salary, max salary.
> 5. **join** — inner join between employees and departments.
> 6. **orderBy** — sorting by salary.
> 7. **Window functions** — rank within department, running averages.
>
> Now here's the key: **look at the code side by side.**
>
> The ONLY difference is the session setup at the top — lines 1 through 6.
>
> Everything from line 8 onwards? **Character-for-character identical.**
>
> *(Show both files side by side — highlight the session block, then scroll through the rest)*
>
> Let me run the Classic version first.
>
> *(Run `02_dataframe_ops_classic.py`)*
>
> Now the Snowpark Connect version.
>
> *(Run `02_dataframe_ops_snowpark_connect.py`)*
>
> Same results. Same API. Same output. But one runs on your laptop's JVM, and the other runs on Snowflake's vectorized engine — with auto-scaling, governance, and per-second billing.
>
> *"No tuning knobs to turn. Snowflake optimizes for you — that's the point."*

---

### DEMO 3: SPARK SQL + PYTHON UDFs
**Files: `03_sql_and_udf_classic.py` vs `03_sql_and_udf_snowpark_connect.py`**

> Last one — and this is the one that usually surprises people.
>
> We're testing:
>
> 1. **spark.sql()** — running SQL queries through the Spark API. Group by department, calculate headcount and average salary.
> 2. **Temp Views & chained SQL** — create a temp view, then query it. Multi-step SQL, just like you'd do in any pipeline.
> 3. **Python UDFs** — a `@F.udf` decorator that classifies salaries as HIGH, MEDIUM, or LOW.
> 4. **Another UDF** — calculates name length. Simple, but proves custom Python logic works.
>
> Again — **the code is identical** except for the two-line session setup.
>
> *(Show the diff — highlight that lines 7-8 are the only change)*
>
> One behavioral note I'll call out: on Snowpark Connect, UDFs are **lazily serialized**. That means if there's a serialization error, it shows up when you call `.show()` or `.collect()`, not when you define the UDF. The code is the same — the timing of errors is slightly different. That's it.
>
> *(Run `03_sql_and_udf_classic.py`)*
>
> *(Run `03_sql_and_udf_snowpark_connect.py`)*
>
> Same results. Same UDFs. Same SQL. Different engine.
>
> And the Snowpark Connect version also prints a nice summary of what's NOT supported — so your team knows exactly what to expect:
>
> | Spark Feature | Snowflake Alternative |
> |---|---|
> | RDDs | DataFrame API |
> | Structured Streaming | Snowpipe Streaming / Dynamic Tables |
> | MLlib | Snowpark ML / Cortex ML |
> | Delta Lake | Iceberg Tables |
> | Java/Scala UDFs | Python UDFs only (for now) |
>
> *"Change the connection string, not the code."*

---
---

## PART 3: WRAP-UP

---

> So let me bring it all together.
>
> | What | Changes? |
> |---|---|
> | Session setup | YES — the only thing that changes |
> | DataFrame API (select, filter, groupBy, join, window) | NO |
> | spark.sql() queries | NO |
> | Python UDFs (@F.udf) | NO |
> | createDataFrame, show, collect | NO |
> | Temp views | NO |
>
> **One line changes. Everything else stays.**
>
> And what do you get for that one line?
>
> - **Zero cluster management** — no provisioning, no tuning, no version upgrades.
> - **Per-second billing** — warehouse auto-suspends when your job finishes.
> - **Built-in governance** — RBAC, masking, row access policies, audit trails. Day one.
> - **3x–5.6x faster performance** on real workloads.
> - **41–54% cost savings** compared to managed Spark.
> - **Zero vendor lock-in** — your code is standard PySpark. Your data can be open Iceberg.
>
> *"Your Spark code, Snowflake's engine — zero rewrite, zero clusters."*
>
> Questions?

---

## OBJECTION QUICK-REFERENCE (if questions come up)

| They say... | You say... |
|---|---|
| "We're happy on Databricks" | *"Keep the code. Drop the cost. That's the conversation."* |
| "What about streaming?" | *"Ingest real-time with OpenFlow. Process with Snowpark Connect. Best of both."* |
| "We need MLlib" | *"MLlib is DIY ML. Snowpark ML is managed ML. Same Snowflake bill."* |
| "It's only PySpark, we have Scala" | *"Start with PySpark — that's where most of your Spark code lives anyway."* |
| "What about lock-in?" | *"Standard PySpark code + open Iceberg tables = zero lock-in."* |
| "Compatibility concerns?" | *"99% of real-world Spark code works. The 1% has documented workarounds."* |
| "How is it priced?" | *"One bill. Per-second. No Spark license, no cluster overhead."* |

---

**END OF SCRIPT**

*Total estimated time: ~20–25 min (12–15 min pitch + 8–10 min demo)*
