{{ config(materialized='view') }}

SELECT 
	city,
	timestamp,
	temperature,
	humidity,
	pressure,
	wind_speed
FROM WEATHER_DB.RAW.WEATHER_RAW
WHERE temperature IS NOT NULL
