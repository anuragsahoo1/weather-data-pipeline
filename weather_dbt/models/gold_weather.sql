{{ config(materialized='table') }} 
SELECT
	city,
	DATE(timestamp) AS date,
	AVG(temperature) AS avg_temp,
	MAX(temperature) AS MAX_temp,
	MIN(temperature) AS min_temp,
	AVG(humidity) AS avg_humidity
FROM {{ ref('silver_weather') }}
GROUP BY city, DATE(timestamp)
