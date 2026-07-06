from pawpal_system import Owner, Pet, Scheduler, Task


def build_demo_owner() -> Owner:
    owner = Owner(name="Jordan")

    mochi = Pet(name="Mochi", species="dog", care_needs="Needs daily exercise")
    mochi.add_task(Task(title="Morning walk", duration_minutes=30, priority="high"))
    mochi.add_task(Task(title="Feeding", duration_minutes=15, priority="high"))

    luna = Pet(name="Luna", species="cat", care_needs="Needs quiet playtime")
    luna.add_task(Task(title="Play session", duration_minutes=20, priority="medium"))
    luna.add_task(Task(title="Litter box check", duration_minutes=10, priority="medium"))

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

    print("\nWhy this plan:")
    print(scheduler.explain_plan(owner))
