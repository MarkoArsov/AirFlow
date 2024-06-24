#!/bin/bash

# Run airflow database initialization
airflow db init

# Start the Airflow web server
exec airflow webserver