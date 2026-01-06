# End-to-End Data Engineering Pipeline using Databricks, PySpark & Delta Lake

## Project Overview
This project demonstrates an end-to-end *Lakehouse data engineering pipeline* built using *Databricks Free Edition*, *PySpark*, and *Delta Lake*.  
The pipeline ingests raw financial transaction data, cleans and validates it, and produces analytics-ready datasets following the *Bronze–Silver–Gold architecture*.

Dataset Used: *PaySim – Synthetic Financial Dataset for Fraud Detection (Kaggle)*


## Architecture
[Lakehouse Architecture](architecture/lakehouse_architecture.png)

The pipeline follows a layered Lakehouse design:
- *Bronze*: Raw ingestion (Delta format)
- *Silver*: Cleaned and validated data
- *Gold*: Aggregated business metrics


## Tech Stack
- Databricks Community Edition
- Apache Spark (PySpark)
- Delta Lake
- Python
- GitHub

## Data Source
*PaySim Synthetic Financial Dataset*
- Simulates mobile money transactions
- Includes fraud and non-fraud transactions
- Suitable for large-scale batch and incremental processing

Key columns:
- step
- type
- amount
- nameOrig
- nameDest
- isFraud


## Bronze Layer – Raw Ingestion
- Ingested CSV data as-is
- No business logic applied
- Stored in Delta Lake format

## Silver Layer – Cleaning & Transformation
Applied:
- Schema enforcement
- Deduplication
- Business rules (amount > 0)
- Data quality checks (nulls, invalid values)

## Gold Layer – Analytics & Aggregation
Produced analytics-ready datasets:
- Fraud metrics by transaction type
- Transaction volume and amount summaries

## Incremental Load Strategy
- Used `step` column as a time surrogate
- Processed only new records
- Implemented **Delta Lake MERGE** for idempotent upserts

---

## Data Quality Checks
- Null checks on key columns
- Amount validation (> 0)
- Duplicate detection

All validations were enforced at the Silver layer.

---

## Performance Optimizations
- Shuffle partition tuning
- Delta Lake optimizations
- Efficient aggregations

---

## Challenges Faced
- Handling schema inference issues
- Managing large CSV ingestion in Community Edition
- Designing incremental logic without streaming

---

## Future Improvements
- Convert batch ingestion to Structured Streaming
- Add Databricks Jobs orchestration
- Build BI dashboards on Gold layer
- Implement alerting on fraud spikes


