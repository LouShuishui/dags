"""Example DAG demonstrating the usage of the SSHOperator."""

from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator


args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

dag = DAG(
    dag_id='msan_testSSH',
    default_args=args,
    schedule_interval=timedelta(days=1),
    dagrun_timeout=timedelta(minutes=60),
)

sshHook = SSHHook(
    remote_host='dltseb764000007.redmond.corp.microsoft.com', 
    username='weouyan', 
    key_file='/home/bitnami/.ssh/id_rsa_dlts', 
    port=32523, 
    timeout=10, 
    keepalive_interval=30)


t1 = SSHOperator(
    task_id="connectionDLTS",
    command='mkdir fromAirflow',
    ssh_hook=sshHook,
    dag=dag)

t2 = SSHOperator(
    ssh_hook=sshHook,
    task_id='writeToRemote',
    command='touch /tmp/test_ssh_in_airflow.txt', # create a file at remote machine
    dag=dag
)

t1>>t2
