from fastapi import Depends
from strawberry.fastapi import BaseContext

from database import get_db
from domain.service.task_service import TaskService
from infra.repository.task_repository import TaskRepository


def init_task_repository(db=Depends(get_db)):
    return TaskRepository(db)


def init_task_service(task_repository: TaskRepository = Depends(init_task_repository)):
    return TaskService(
        task_repository
    )


class TaskContext(BaseContext):
    def __init__(self, task: TaskService):
        self.__task: TaskService = task

    def get_task(self):
        return self.__task


class TaskServicesContext(BaseContext):
    def __init__(self, task: TaskService):
        self.__task: TaskService = task

    def get_task(self):
        return self.__task


async def get_context(
        task_service: TaskService = Depends(init_task_service)
) -> TaskContext:
    return TaskContext(
        task=task_service
    )