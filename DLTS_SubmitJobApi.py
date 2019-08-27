import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('DLTASubmitJobApi', default_args=default_args, schedule_interval=timedelta(minutes=60))

t1 = BashOperator(
    task_id='postDLTSJob',
    bash_command='python /opt/bitnami/airflow/dags/dltsPostJobApi.py',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

t2.set_upstream(t1)
