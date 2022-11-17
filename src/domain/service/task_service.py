from datetime import datetime
from typing import Optional

from domain.model.task import Status, Task
from infra.repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository) -> None:
        self.__repo = repo

    @property
    def repo(self) -> type[TaskRepository]:
        return self.__repo

    def find(self, id: str) -> Task:
        task = self.repo.find_by_id(id)

        return task

    def find_all(self) -> list[Task]:
        tasks = self.repo.find_all()

        return tasks

    def create(self, *, title: str, description: Optional[str] = None) -> Task:
        task = Task(title=title, description=description)
        self.repo.save(task)

        return task

    def update(self, *, id: str, status: Status) -> Task:
        task = self.repo.find_by_id(id)
        task.status = status
        task.updated_at = datetime.utcnow()
        self.repo.save(task)

        return task

    def delete(self, id: str) -> Task:
        task = self.repo.find_by_id(id)
        self.repo.delete(task)

        return task