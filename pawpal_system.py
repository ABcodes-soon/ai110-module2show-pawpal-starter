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

    def update_task(self, details: dict) -> None:
        """Update task details."""
        pass

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        pass


@dataclass
class Pet:
    name: str
    species: str
    care_needs: str = ""
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        pass

    def get_task_summary(self) -> str:
        """Return a simple summary of the pet's tasks."""
        return ""


@dataclass
class Owner:
    name: str
    contact_info: Optional[str] = None
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        pass

    def view_daily_plan(self) -> str:
        """Return a daily plan for the owner's pets."""
        return ""


@dataclass
class Scheduler:
    available_time_minutes: int = 240
    tasks: List[Task] = field(default_factory=list)

    def generate_daily_plan(self) -> List[Task]:
        """Create a daily plan from the available tasks."""
        return []

    def explain_plan(self) -> str:
        """Explain why the plan was generated this way."""
        return ""
