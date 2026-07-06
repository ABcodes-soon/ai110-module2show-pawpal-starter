# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

Run the full automated test suite with:

```bash
python -m pytest
```

These tests cover the core scheduler behaviors, including:
- sorting tasks by time and priority
- filtering tasks by pet name or completion status
- recurring daily-task creation after completion
- conflict detection for overlapping task times
- basic pet and owner task management

Successful test run output:

```text
============================= test session starts ==============================
platform win32 -- Python 3.13.11, pytest-9.1.1, pluggy-1.5.0
rootdir: C:\Users\abhin\Downloads\project_learn\ai110-module2show-pawpal-starter
collected 10 items

tests\test_pawpal.py .....                                               [ 50%]
tests\test_pawpal_system.py .....                                        [100%]

============================== 10 passed in 0.12s ==============================
```

Confidence Level: ⭐⭐⭐⭐⭐

## Sample Output

```text
Today's Schedule
====================
1. Morning walk (30 min, high)
2. Feeding (15 min, high)
3. Litter box check (10 min, medium)

Why this plan:
Planned tasks:
- Morning walk (30 min, high)
- Feeding (15 min, high)
- Litter box check (10 min, medium)
```

## 📐 Smarter Scheduling

The scheduler now includes a few lightweight intelligence features to make task planning more useful for a busy pet owner.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Sorting behavior | `Scheduler.sort_by_time()` | Orders tasks by their scheduled time of day, then by priority and duration. |
| Filtering behavior | `Scheduler.filter_tasks()` | Lets the program view only tasks that match a completion state or a specific pet name. |
| Conflict detection | `Scheduler.detect_conflicts()` | Warns when two tasks overlap in time so the owner can adjust the plan. |
| Recurring tasks | `Task.mark_complete()` | When a daily or weekly task is completed, a new incomplete task is created for the next occurrence. |

## � Demo Walkthrough

PawPal+ is designed as a lightweight pet-care planning assistant with a simple Streamlit interface and an underlying scheduler that makes the plan more useful.

### Main UI features
- Add or update owner and pet information
- Create tasks with a title, duration, priority, and time of day
- View all tasks in a sorted table
- Filter tasks by pet name
- See scheduling conflict warnings when tasks overlap
- Generate a daily plan based on the available time window

### Example workflow
1. Open the app and enter an owner name and pet profile.
2. Add tasks such as a morning walk, feeding, or litter check with specific times.
3. Review the sorted task list and any conflict warnings.
4. Generate the daily schedule to see which tasks fit into the available time.
5. Mark recurring tasks complete to create the next occurrence for the following day or week.

### Scheduler behaviors shown in the demo
- Sorting by time with `Scheduler.sort_by_time()`
- Filtering by pet with `Scheduler.filter_tasks()`
- Conflict warnings with `Scheduler.detect_conflicts()`
- Recurring-task creation through `Task.mark_complete()`

### Sample CLI output
```text
Today's Schedule
====================
1. Play session (20 min, medium)
2. Morning walk (30 min, high)
3. Litter box check (10 min, medium)

Sorted tasks by time:
- Play session at 07:30 for Luna
- Morning walk at 08:00 for Mochi
- Feeding conflict at 08:00 for Luna
- Feeding at 09:30 for Mochi
- Litter box check at 10:00 for Luna

Conflict warnings:
- Warning: 'Feeding conflict' (08:00) overlaps with 'Morning walk' (08:00) for Luna.
```
