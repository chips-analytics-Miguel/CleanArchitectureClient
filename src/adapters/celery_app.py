from typing import Dict, List
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

@app.task
def create_patient_task(result : str):
   return {result:"Patient create successfully"}

@app.task
def delete_patient_task(id : str):
   return {id:"Patient delete Successfully"}

if __name__ == '__main__':
   app.start()