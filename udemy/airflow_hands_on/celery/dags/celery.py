from airflow.decorators import dag, task
from pendulum import datetime
from time import sleep

@dag(start_date=datetime(2025, 1, 1), schedule=None, catchup=False)
def celery():
    
    @task(queue="cpu")
    def a():
        print("A")
        sleep(15)
    
    @task(queue="gpu")
    def b():
        print("B")
        sleep(15)
    
    @task(queue="cpu")
    def c():
        print("C")
        sleep(15)

    @task(queue="cpu")
    def d():
        print("D")
        sleep(15)

    @task()
    def e():
        print("E")
        sleep(15)
        
    a() >> [b(), c(), d()] >> e()
    
celery()