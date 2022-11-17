import strawberry
from strawberry.types import Info

from web.task.inputs import AddTaskInput, UpdateTaskInput
from web.task.types import TaskType


def get_task(id: strawberry.ID, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.find(id)

    return task


def get_tasks(info: Info) -> list[TaskType]:

    service = info.context.get_task()
    tasks = service.find_all()

    return tasks


def add_task(task_input: AddTaskInput, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.create(**task_input.__dict__)

    return task


def update_task(task_input: UpdateTaskInput, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.update(**task_input.__dict__)

    return task


def delete_task(id: strawberry.ID, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.delete(id)

    return task