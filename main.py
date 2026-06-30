from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date


# Create Owner
owner = Owner("O1", "Alex", "alex@email.com")


# Create Pets
dog = Pet("P1", "Nico", "Dog", 3)
cat = Pet("P2", "Mimi", "Cat", 2)

owner.add_pet(dog)
owner.add_pet(cat)


# Create Tasks (different dates)
task1 = Task("T1", "Morning Walk", "Walk", date(2026, 6, 30), 1)
task2 = Task("T2", "Feed Cat", "Feeding", date(2026, 6, 30), 2)
task3 = Task("T3", "Vet Visit", "Medical", date(2026, 7, 1), 3)

# Assign tasks to pets
dog.add_task(task1)
cat.add_task(task2)
dog.add_task(task3)

# Scheduler
scheduler = Scheduler()

scheduler.add_task(task1)
scheduler.add_task(task2)
scheduler.add_task(task3)

scheduler.sort_tasks()

# Print Schedule
print("\nTODAY'S SCHEDULE")
print("-" * 30)

for task in scheduler.get_upcoming_tasks():
    pet_name = task.pet.name if task.pet else "Unknown"
    print(f"{task.due_date} | {task.title} | Pet: {pet_name} | Priority {task.priority}")
