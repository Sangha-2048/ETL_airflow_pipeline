from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt
from datetime import timedelta
from airflow.utils.dates import days_ago

# Task 1.1
default_args = {
    'owner' : 'Salil',
    'start_date' : days_ago(0),
    'email' : ['xyz@gmail.com'],
    'email_on_failure' : True,
    'email_on_retry' : True,
    'retries' : 1,
    'retry_delay' : dt.timedelta(minutes=2),
}

# Task 1.2
dag = DAG(
    dag_id = 'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval = '*/5 * * * *'
    )

# Task 1.3
unzip_data = BashOperator(
    task_id = 'unzip_data',
    bash_command = 'tar -xvf /home/test/Imp/Kafka-airflow/tolldata.tgz -C /home/test/Imp/Kafka-airflow/',
    dag = dag
    )

# Task 1.4
extract_data_from_csv = BashOperator(
    task_id = 'extract_data_from_csv',
    bash_command = '/home/test/Imp/Kafka-airflow/shell_scripts/extract_data_from_csv.sh ',
    dag = dag
)

# Task 1.5
extract_data_from_tsv = BashOperator(
    task_id = 'extract_data_from_tsv',
    bash_command = '/home/test/Imp/Kafka-airflow/shell_scripts/extract_data_from_tsv.sh ',
    dag = dag
)

# Task 1.6
extract_data_from_fixed_width = BashOperator(
    task_id = 'extract_data_from_fixed_width',
    bash_command = '/home/test/Imp/Kafka-airflow/shell_scripts/extract_data_from_fixed_width.sh ',
    dag = dag
)

# Task 1.7
consolidate_data = BashOperator(
    task_id = 'consolidate_data',
    bash_command = '/home/test/Imp/Kafka-airflow/shell_scripts/consolidate_data.sh ',
    dag = dag
    )

# Task 1.8
transformed_data = BashOperator(
    task_id = 'transformed_data',
    bash_command = '/home/test/Imp/Kafka-airflow/shell_scripts/transformed_data.sh ',
    dag = dag
    )

# Task 1.9
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transformed_data


