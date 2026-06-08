# Weather Data Pipeline

## Overview

This project implements an end-to-end data engineering pipeline that ingests weather data from the Weatherstack API, stores it in PostgreSQL, transforms it using DBT, and orchestrates the workflow with Apache Airflow. The entire environment is containerized using Docker.

## Architecture

Weatherstack API → Python Ingestion → PostgreSQL → DBT Transformations → Superset Dashboard

## Technologies Used

* Python
* PostgreSQL
* Apache Airflow
* DBT (Data Build Tool)
* Docker & Docker Compose
* Apache Superset

## Pipeline Workflow

1. Weather data is retrieved from the Weatherstack API.
2. Raw records are inserted into PostgreSQL.
3. An Airflow DAG orchestrates the workflow.
4. DBT models transform and clean the raw data.
5. Curated tables are generated for analytics and reporting.
6. Data can be visualized in Apache Superset.

## DBT Models

### stg_weather_data

Staging model that:

* Reads data from the raw weather table.
* Removes duplicate records using a window function.
* Standardizes timestamps and weather attributes.

### daily_avg

Aggregated model used to calculate daily weather metrics.

### weather_report

Reporting model used to generate analytics-ready weather information.

## Airflow Orchestration

The Airflow DAG performs two tasks:

1. Execute Python ingestion code to load weather data into PostgreSQL.
2. Execute DBT transformations using a Docker container.

The tasks run sequentially:

Ingest Data → Transform Data

## Running the Project

### Prerequisites

* Docker
* Docker Compose

### Start Services

```bash
docker-compose up -d
```

### Trigger the Pipeline

Use the Airflow UI to run the DAG:

weather_api_dbt_orchestrator

## Future Improvements

* Build interactive dashboards in Apache Superset.
* Add data quality tests in DBT.
* Parameterize API configuration through environment variables.
* Extend the pipeline with additional weather metrics.

## Project Structure

```text
airflow/         Airflow DAGs
dbt/             DBT project and profiles
docker/          Docker initialization scripts
postgres/        Database initialization scripts
api-request/     Python ingestion code
```
