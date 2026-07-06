from pawpal_system import Owner, Pet, Scheduler, Task


def build_demo_owner() -> Owner:
    owner = Owner(name="Jordan")

    mochi = Pet(name="Mochi", species="dog", care_needs="Needs daily exercise")
    mochi.add_task(Task(title="Feeding", duration_minutes=15, priority="high", time_of_day="09:30", pet_name="Mochi"))
    mochi.add_task(Task(title="Morning walk", duration_minutes=30, priority="high", time_of_day="08:00", pet_name="Mochi"))

    luna = Pet(name="Luna", species="cat", care_needs="Needs quiet playtime")
    luna.add_task(Task(title="Litter box check", duration_minutes=10, priority="medium", time_of_day="10:00", pet_name="Luna"))
    luna.add_task(Task(title="Play session", duration_minutes=20, priority="medium", time_of_day="07:30", pet_name="Luna"))
    luna.add_task(Task(title="Feeding conflict", duration_minutes=15, priority="high", time_of_day="08:00", pet_name="Luna"))

    owner.add_pet(mochi)
    owner.add_pet(luna)
    return owner


if __name__ == "__main__":
    owner = build_demo_owner()
    scheduler = Scheduler(available_time_minutes=60)
    plan = scheduler.generate_daily_plan(owner)

    print("Today's Schedule")
    print("=" * 20)
    for index, task in enumerate(plan, start=1):
        print(f"{index}. {task.title} ({task.duration_minutes} min, {task.priority})")

    sorted_tasks = scheduler.sort_by_time(owner.get_all_tasks())
    print("\nSorted tasks by time:")
    for task in sorted_tasks:
        print(f"- {task.title} at {task.time_of_day} for {task.pet_name}")

    filtered_tasks = scheduler.filter_tasks(sorted_tasks, pet_name="Mochi")
    print("\nFiltered tasks for Mochi:")
    for task in filtered_tasks:
        print(f"- {task.title} at {task.time_of_day}")

    print("\nConflict warnings:")
    for warning in scheduler.detect_conflicts(owner.get_all_tasks()):
        print(f"- {warning}")

    print("\nWhy this plan:")
    print(scheduler.explain_plan(owner))
