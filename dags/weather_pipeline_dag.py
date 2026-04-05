
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime
import subprocess

from ingestion.weather_to_s3 import main as fetch_weather

default_args = {
	'owner': 'anurag',
	'retires': 1
}

with DAG(
	dag_id='weather_pipeline'
	default_args=default_args,
	start_date=datetime(2024, 1, 1),
	schedule_interval='*5 * * * *',
	catchup=False
) as dag:
	fetch_task = PythonOperator(
		task_id='load_to_snowflake',
		sql=""
		COPY INTO WEATHER_DB.RAW.WEATHER_RAW
		FROM @WEATHER_STAGE
		MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;
		""",
		snowflake_conn_id='snowflake_default'
	)

run_dbt = PythonOperator(
	task_id='run_dbt',
	python_callable=lambda: subprocess.run(
		["dbt", "run"]
		cwd="/Users/anuragsahoo/weather-pipeline/weather_dbt"
	)
)
fetch_task >> load-to_snowflake >> run_dbt
