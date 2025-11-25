from datetime import datetime, timedelta
import random
from airflow.decorators import dag, task

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=['assignment-answer']
)
def random_number_checker2():

    @task
    def generate_random_number():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number
 
    @task
    def check_even_odd(n):
        result = "even" if n % 2 == 0 else "odd"
        print(f"The number {n} is {result}.")

    check_even_odd(generate_random_number())

random_number_checker2()