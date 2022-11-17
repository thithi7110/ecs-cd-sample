import uvicorn
from fastapi import FastAPI

from database import database_context
from router import task_app

api = FastAPI()
print('start app.py process ....')


def register_controller():
    api.include_router(task_app, prefix='/task')

if __name__ != '__main__':
    print('start not main process ....'+__name__ )

if __name__ == '__main__':
    print('start main process ....')
    database_context.initialize()
    register_controller()
    uvicorn.run(app=api, host='0.0.0.0', port=80)