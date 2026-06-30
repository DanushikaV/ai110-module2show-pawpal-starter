from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


# =========================
# TASK
# =========================
@dataclass
class Task:
    task_id: str
    title: str
    category: str
    due_date: date
    priority: int
    completed: bool = False
    recurring: bool = False
    pet: Optional["Pet"] = None

    def mark_complete(self) -> None:
        """Mark task as completed."""
        self.completed = True

    def reschedule(self, new_due_date: date) -> None:
        """Update task due date."""
        self.due_date = new_due_date

    def assign_pet(self, pet: Optional["Pet"]) -> None:
        """Assign task to a pet while keeping relationships synced."""
        if self.pet is not None and self.pet is not pet:
            if self in self.pet.tasks:
                self.pet.tasks.remove(self)

        self.pet = pet

        if pet is not None and self not in pet.tasks:
            pet.tasks.append(self)


# =========================
# PET
# =========================
@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)
    owner: Optional["Owner"] = None

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        if task not in self.tasks:
            self.tasks.append(task)
        task.assign_pet(self)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet."""
        if task in self.tasks:
            self.tasks.remove(task)
        if task.pet is self:
            task.assign_pet(None)

    def get_tasks(self) -> List[Task]:
        """Return a copy of tasks."""
        return list(self.tasks)

    def assign_owner(self, owner: Optional["Owner"]) -> None:
        """Sync owner relationship."""
        if self.owner is not None and self.owner is not owner:
            if self in self.owner.pets:
                self.owner.pets.remove(self)

        self.owner = owner

        if owner is not None and self not in owner.pets:
            owner.pets.append(self)


# =========================
# OWNER
# =========================
@dataclass
class Owner:
    owner_id: str
    name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add pet to owner."""
        if pet not in self.pets:
            self.pets.append(pet)
        pet.assign_owner(self)

    def remove_pet(self, pet: Pet) -> None:
        """Remove pet from owner."""
        if pet in self.pets:
            self.pets.remove(pet)
        if pet.owner is self:
            pet.assign_owner(None)

    def get_pets(self) -> List[Pet]:
        """Return copy of pets."""
        return list(self.pets)


# =========================
# SCHEDULER
# =========================
class Scheduler:
    def __init__(self, tasks: Optional[List[Task]] = None) -> None:
        self.tasks: List[Task] = list(tasks) if tasks else []

    def add_task(self, task: Task) -> None:
        """Add task to scheduler only if it belongs to a pet."""
        if task.pet is None:
            raise ValueError("Task must belong to a pet before scheduling")
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove task from scheduler."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_upcoming_tasks(self) -> List[Task]:
        """Return all tasks."""
        return list(self.tasks)

    def sort_tasks(self) -> None:
        """Sort tasks by due date then priority."""
        self.tasks.sort(key=lambda t: (t.due_date, t.priority))

    def detect_conflicts(self) -> List[Task]:
        """
        Detect tasks with same due_date.
        Returns list of conflicting tasks.
        """
        seen: dict[date, Task] = {}
        conflicts: List[Task] = []

        for task in self.tasks:
            if task.due_date in seen:
                other = seen[task.due_date]

                if other not in conflicts:
                    conflicts.append(other)
                if task not in conflicts:
                    conflicts.append(task)
            else:
                seen[task.due_date] = task

        return conflicts