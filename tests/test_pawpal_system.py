from datetime import date, timedelta

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


def test_recurring_tasks_create_next_occurrence_when_completed():
    daily_task = Task(title="Water plants", duration_minutes=10, priority="medium", recurring=True, frequency="daily")
    weekly_task = Task(title="Bath time", duration_minutes=20, priority="low", recurring=True, frequency="weekly")

    next_daily_task = daily_task.mark_complete()
    next_weekly_task = weekly_task.mark_complete()

    assert daily_task.completed is True
    assert weekly_task.completed is True
    assert next_daily_task is not None
    assert next_weekly_task is not None
    assert next_daily_task.completed is False
    assert next_weekly_task.completed is False
    assert next_daily_task.frequency == "daily"
    assert next_weekly_task.frequency == "weekly"
    assert next_daily_task.due_date == date.today() + timedelta(days=1)
    assert next_weekly_task.due_date == date.today() + timedelta(weeks=1)


def test_scheduler_reports_conflicts_for_overlapping_tasks():
    scheduler = Scheduler()
    morning_walk = Task(title="Morning walk", duration_minutes=30, priority="high", time_of_day="08:00", pet_name="Mochi")
    feeding = Task(title="Feeding", duration_minutes=15, priority="high", time_of_day="08:00", pet_name="Luna")

    warnings = scheduler.detect_conflicts([morning_walk, feeding])

    assert len(warnings) == 1
    assert "08:00" in warnings[0]
    assert "Morning walk" in warnings[0]
    assert "Feeding" in warnings[0]
