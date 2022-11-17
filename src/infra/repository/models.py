import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, String, Table
from sqlalchemy.orm import registry
from sqlalchemy.sql import func
from sqlalchemy_utils import ChoiceType, UUIDType

from domain.model.task import Status, Task

mapper_registry = registry()

# Taskテーブルの定義
task = Table(
    'task',
    mapper_registry.metadata,
    Column('id', UUIDType(binary=False), primary_key=True, default=uuid.uuid4),
    Column('description', String(200)),
    Column('title', String(200)),
    Column('status', Enum(Status)),
    Column('updated_at', DateTime, default=func.now())
)
mapper_registry.map_imperatively(Task, task)