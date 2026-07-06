from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_update_and_mark_complete():
    task = Task(title="Walk", duration_minutes=20, priority="low")
    task.update_task({"priority": "high", "duration_minutes": 30})
    assert task.priority == "high"
    assert task.duration_minutes == 30

    task.mark_complete()
    assert task.completed is True


def test_pet_and_owner_manage_tasks():
    pet = Pet(name="Mochi", species="dog")
    task = Task(title="Feeding", duration_minutes=10, priority="high")
    pet.add_task(task)

    owner = Owner(name="Jordan")
    owner.add_pet(pet)

    assert pet.get_task_summary().startswith("Mochi")
    assert owner.get_all_tasks()[0].title == "Feeding"


def test_scheduler_builds_plan_with_time_limit():
    pet = Pet(name="Mochi", species="dog")
    pet.add_task(Task(title="Morning walk", duration_minutes=30, priority="high"))
    pet.add_task(Task(title="Feeding", duration_minutes=20, priority="medium"))
    pet.add_task(Task(title="Grooming", duration_minutes=25, priority="low"))

    owner = Owner(name="Jordan")
    owner.add_pet(pet)

    scheduler = Scheduler(available_time_minutes=50)
    plan = scheduler.generate_daily_plan(owner)

    assert [task.title for task in plan] == ["Morning walk", "Feeding"]
    assert "Grooming" not in [task.title for task in plan]
    assert "Morning walk" in scheduler.explain_plan(owner)
