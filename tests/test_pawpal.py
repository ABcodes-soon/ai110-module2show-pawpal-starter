from pawpal_system import Pet, Task


def test_mark_complete_changes_status():
    task = Task(title="Walk", duration_minutes=20, priority="high")

    task.mark_complete()

    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    task = Task(title="Feeding", duration_minutes=10, priority="medium")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Feeding"
