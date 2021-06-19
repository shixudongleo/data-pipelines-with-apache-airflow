import airflow
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator


dag = DAG(
    dag_id='template_test',
    start_date=pendulum.datetime(2021, 6, 19, tz='Asia/Singapore'),
    schedule_interval=None
)

print_hello_script_same_folder = BashOperator(
    task_id='print_hello_script_same_folder',
    bash_command='hello_root.sh',
    dag=dag
)

print_hello_print_path = BashOperator(
    task_id='print_hello_print_path',
    bash_command=(
        "echo 'variable path:' $PATH && " 
        "echo 'template_searchpath:' {{ dag.template_searchpath }} && "
        "echo 'dag folder:' {{ dag.folder}}"
    ),
    dag=dag
)

print_hello_script_sub_folder = BashOperator(
    task_id='print_hello_script_sub_folder',
    bash_command="scripts/hello_subfolder.sh",
    dag=dag
)