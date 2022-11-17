from datetime import datetime
from typing import Optional

import strawberry

from domain.model.task import Status, Task

StatusType = strawberry.enum(Status, name='Status')


@strawberry.type(name='Task')
class TaskType:
    id: strawberry.ID
    title: str
    description: Optional[str]
    status: StatusType
    updated_at: datetime