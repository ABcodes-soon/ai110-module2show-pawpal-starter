from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str = "medium"
    category: str = "general"
    recurring: bool = False
    completed: bool = False
    time_of_day: str = "09:00"
    pet_name: str = ""
    frequency: str = "none"
    due_date: date = field(default_factory=date.today)

    def update_task(self, details: dict) -> None:
        """Update task details."""
        for key, value in details.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def mark_complete(self) -> Optional["Task"]:
        """Mark the task as complete and create the next occurrence for recurring tasks."""
        self.completed = True

        if not self.recurring or self.frequency not in {"daily", "weekly"}:
            return None

        interval = timedelta(days=1) if self.frequency == "daily" else timedelta(weeks=1)
        next_task = Task(
            title=self.title,
            duration_minutes=self.duration_minutes,
            priority=self.priority,
            category=self.category,
            recurring=self.recurring,
            completed=False,
            time_of_day=self.time_of_day,
            pet_name=self.pet_name,
            frequency=self.frequency,
            due_date=self.due_date + interval,
        )
        return next_task


@dataclass
class Pet:
    name: str
    species: str
    care_needs: str = ""
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_task_summary(self) -> str:
        """Return a simple summary of the pet's tasks."""
        if not self.tasks:
            return f"{self.name} has no tasks yet."
        task_titles = ", ".join(task.title for task in self.tasks)
        return f"{self.name} has tasks: {task_titles}"


@dataclass
class Owner:
    name: str
    contact_info: Optional[str] = None
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all pets owned by this owner."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def view_daily_plan(self) -> str:
        """Return a daily plan for the owner's pets."""
        return "Daily plan is managed by the scheduler."


@dataclass
class Scheduler:
    available_time_minutes: int = 240
    tasks: List[Task] = field(default_factory=list)

    def generate_daily_plan(self, owner: Owner) -> List[Task]:
        """Create a daily plan from the available tasks."""
        candidate_tasks = self.sort_by_time(owner.get_all_tasks())
        plan: List[Task] = []
        used_time = 0

        for task in candidate_tasks:
            if task.completed:
                continue
            if used_time + task.duration_minutes <= self.available_time_minutes:
                plan.append(task)
                used_time += task.duration_minutes

        self.tasks = plan
        return plan

    def explain_plan(self, owner: Owner) -> str:
        """Explain why the plan was generated this way."""
        plan = self.generate_daily_plan(owner)
        if not plan:
            return "No tasks fit into the available time."

        descriptions = [f"- {task.title} ({task.duration_minutes} min, {task.priority})" for task in plan]
        return "Planned tasks:\n" + "\n".join(descriptions)

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by time of day, then by priority and duration."""
        return sorted(
            tasks,
            key=lambda task: (
                self._time_to_minutes(task.time_of_day),
                -self._priority_rank(task.priority),
                -task.duration_minutes,
            ),
        )

    def filter_tasks(self, tasks: List[Task], completed: Optional[bool] = None, pet_name: Optional[str] = None) -> List[Task]:
        """Filter tasks by completion status or pet name for easier review."""
        filtered_tasks = list(tasks)
        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed is completed]
        if pet_name:
            filtered_tasks = [task for task in filtered_tasks if task.pet_name.lower() == pet_name.lower()]
        return filtered_tasks

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return lightweight warnings when tasks overlap in time."""
        warnings: List[str] = []
        seen: List[tuple[int, Task]] = []

        for task in tasks:
            start_minutes = self._time_to_minutes(task.time_of_day)
            end_minutes = start_minutes + task.duration_minutes
            for other_start, other_task in seen:
                other_end = other_start + other_task.duration_minutes
                if start_minutes < other_end and end_minutes > other_start:
                    warnings.append(
                        f"Warning: '{task.title}' ({task.time_of_day}) overlaps with '{other_task.title}' ({other_task.time_of_day}) for {task.pet_name or other_task.pet_name}."
                    )
            seen.append((start_minutes, task))

        return warnings

    def _task_sort_key(self, task: Task) -> tuple[int, int]:
        """Return a sort key based on priority and duration."""
        priority_rank = {"high": 2, "medium": 1, "low": 0}
        return priority_rank.get(task.priority.lower(), 0), task.duration_minutes

    def _priority_rank(self, priority: str) -> int:
        """Convert a priority label into a numeric rank."""
        priority_rank = {"high": 2, "medium": 1, "low": 0}
        return priority_rank.get(priority.lower(), 0)

    def _time_to_minutes(self, time_of_day: str) -> int:
        """Convert a HH:MM string into minutes since midnight."""
        try:
            hours, minutes = map(int, time_of_day.split(":"))
            return hours * 60 + minutes
        except ValueError:
            return 0
