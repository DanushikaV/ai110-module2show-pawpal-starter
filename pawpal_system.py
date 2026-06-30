from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
	task_id: str
	title: str
	category: str
	due_date: str
	priority: int
	completed: bool = False
	recurring: bool = False

	def mark_complete(self) -> None:
		pass

	def reschedule(self, new_due_date: str) -> None:
		pass


@dataclass
class Pet:
	pet_id: str
	name: str
	species: str
	age: int
	tasks: List[Task] = field(default_factory=list)

	def add_task(self, task: Task) -> None:
		pass

	def remove_task(self, task: Task) -> None:
		pass

	def get_tasks(self) -> List[Task]:
		pass


@dataclass
class Owner:
	owner_id: str
	name: str
	email: str
	pets: List[Pet] = field(default_factory=list)

	def add_pet(self, pet: Pet) -> None:
		pass

	def remove_pet(self, pet: Pet) -> None:
		pass

	def get_pets(self) -> List[Pet]:
		pass


class Scheduler:
	def __init__(self, tasks: Optional[List[Task]] = None) -> None:
		self.tasks: List[Task] = tasks if tasks is not None else []

	def add_task(self, task: Task) -> None:
		pass

	def remove_task(self, task: Task) -> None:
		pass

	def get_upcoming_tasks(self) -> List[Task]:
		pass

	def sort_tasks(self) -> None:
		pass

	def detect_conflicts(self) -> List[Task]:
		pass
