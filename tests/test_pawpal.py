from datetime import date

from pawpal_system import Task, Pet


# TEST 1: Task Completion
def test_task_completion():
    task = Task("T1", "Walk", "Walk", date(2026, 6, 30), 1)

    task.mark_complete()

    assert task.completed is True


# TEST 2: Task Addition
def test_task_addition_to_pet():
    pet = Pet("P1", "Buddy", "Dog", 3)
    task = Task("T2", "Feed", "Feeding", date(2026, 6, 30), 2)

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1