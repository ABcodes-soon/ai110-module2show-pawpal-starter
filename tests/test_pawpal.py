from pawpal_system import Pet, Scheduler, Task


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


def test_scheduler_sorts_tasks_by_time_and_filters_by_pet():
    scheduler = Scheduler()
    morning = Task(title="Morning walk", duration_minutes=30, priority="high", time_of_day="08:00", pet_name="Mochi")
    feeding = Task(title="Feeding", duration_minutes=15, priority="high", time_of_day="09:30", pet_name="Mochi")
    play = Task(title="Play session", duration_minutes=20, priority="medium", time_of_day="07:30", pet_name="Luna")

    sorted_tasks = scheduler.sort_by_time([feeding, morning, play])
    filtered_tasks = scheduler.filter_tasks(sorted_tasks, pet_name="Mochi")

    assert [task.title for task in sorted_tasks] == ["Play session", "Morning walk", "Feeding"]
    assert [task.title for task in filtered_tasks] == ["Morning walk", "Feeding"]
