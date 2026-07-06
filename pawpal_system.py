from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str = "medium"
    category: str = "general"
    recurring: bool = False
    completed: bool = False

    def update_task(self, details: dict) -> None:
        """Update task details."""
        for key, value in details.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True


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
        candidate_tasks = sorted(owner.get_all_tasks(), key=self._task_sort_key, reverse=True)
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

    def _task_sort_key(self, task: Task) -> tuple[int, int]:
        """Return a sort key based on priority and duration."""
        priority_rank = {"high": 2, "medium": 1, "low": 0}
        return priority_rank.get(task.priority.lower(), 0), task.duration_minutes
