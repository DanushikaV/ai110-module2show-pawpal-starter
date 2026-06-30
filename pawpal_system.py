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
    pet: Optional["Pet"] = None

    def mark_complete(self) -> None:
        pass

    def reschedule(self, new_due_date: str) -> None:
        pass

    def assign_pet(self, pet: Optional["Pet"]) -> None:
        if self.pet is not None and self.pet is not pet:
            if self in self.pet.tasks:
                self.pet.tasks.remove(self)

        self.pet = pet

        if pet is not None and self not in pet.tasks:
            pet.tasks.append(self)


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)
    owner: Optional["Owner"] = None

    def add_task(self, task: Task) -> None:
        if task not in self.tasks:
            self.tasks.append(task)
        task.assign_pet(self)

    def remove_task(self, task: Task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)
        if task.pet is self:
            task.assign_pet(None)

    def get_tasks(self) -> List[Task]:
        return list(self.tasks)

    def assign_owner(self, owner: Optional["Owner"]) -> None:
        if self.owner is not None and self.owner is not owner:
            if self in self.owner.pets:
                self.owner.pets.remove(self)

        self.owner = owner

        if owner is not None and self not in owner.pets:
            owner.pets.append(self)


@dataclass
class Owner:
    owner_id: str
    name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        if pet not in self.pets:
            self.pets.append(pet)
        pet.assign_owner(self)

    def remove_pet(self, pet: Pet) -> None:
        if pet in self.pets:
            self.pets.remove(pet)
        if pet.owner is self:
            pet.assign_owner(None)

    def get_pets(self) -> List[Pet]:
        return list(self.pets)


class Scheduler:
    def __init__(self, tasks: Optional[List[Task]] = None) -> None:
        self.tasks: List[Task] = list(tasks) if tasks is not None else []

    def add_task(self, task: Task) -> None:
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)

    def get_upcoming_tasks(self) -> List[Task]:
        return list(self.tasks)

    def sort_tasks(self) -> None:
        pass

    def detect_conflicts(self) -> List[Task]:
        return []
