# Airflow Sandbox
## Disclaimer
- The version used here is the 2.3.1, versions lower than 2.2.0 won't work with the docker-compose.yml provided
by Airflow
## Installation
1. Clone the repository locally
2. cd into the root folder of the repository
3. Start Airflow with `docker-compose up`
4. Airflow webserver will be up and running in http://localhost:8080 (usr is `airflow` and pwd is `airflow`)
5. To bring Airflow down `control+c` in the terminal and `docker-compose down --remove-orphans` just in case

## Create a DAG
- DAGs live in `<repository>/dags` folder
- You don't need to start Airflow again if you change/create a DAG, just refresh the DAG
