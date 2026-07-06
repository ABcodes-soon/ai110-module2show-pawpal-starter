# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- My initial UML design centers on four main classes: Owner, Pet, Task, and Scheduler.
- The Owner class represents the person using the app and is responsible for managing one or more pets and viewing the overall daily plan.
- The Pet class represents an individual animal and stores basic information such as name, species, and care needs while also holding the tasks associated with that pet.
- The Task class represents one care activity, such as a walk, feeding, medication, or grooming, and holds details like title, duration, priority, category, and whether it repeats.
- The Scheduler class is responsible for reviewing the available tasks and generating a daily schedule that considers time limits and task priorities.
- Three core actions a user should be able to perform are: 1) add a pet profile for their animal, 2) create or edit care tasks with details such as duration and priority, and 3) generate and view a daily schedule that shows what needs to be done today.

**b. Design changes**

- I reviewed the class skeleton in the logic layer and confirmed that the core structure was already clear, so I kept the main design intact.
- One small refinement I made was to make the Scheduler responsible for evaluating tasks and generating a daily plan while keeping the Pet and Owner classes focused on storing data and managing relationships.
- This change helps keep the responsibilities separated and avoids putting too much scheduling logic into the Pet or Owner classes.

**c. Building blocks**

- Owner: holds the owner’s name and contact information, and can add pets and view the daily plan.
- Pet: holds the pet’s name, species, and care needs, and can receive tasks and report its current care status.
- Task: holds the task title, duration, priority, category, and whether it repeats, and can be updated or marked as complete.
- Scheduler: holds the available time window and the list of tasks to consider, and can generate a daily schedule based on priority and time constraints.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- The scheduler considers task time of day, duration, priority, and whether a task is completed. It also uses the available daily time window to decide which tasks fit into the plan.
- I treated time and priority as the most important constraints because they directly affect whether the schedule is realistic and useful for a busy pet owner. Completion status and pet filtering were added as secondary constraints to keep the view organized rather than to change the core plan.

**b. Tradeoffs**

- One tradeoff my scheduler makes is that it uses a lightweight conflict check based on each task's start time and duration, rather than a more complex calendar-style planner. This keeps the logic simple and easy to understand, but it means the program warns about overlaps in a straightforward way without trying to solve every scheduling edge case.
- I also reviewed a more compact, Pythonic version of the conflict-detection logic, but I kept the explicit loop-based version because it is easier for a human reader to follow and debug.

---

## 3. AI Collaboration

**a. How you used AI**

- I used my AI coding assistant for design brainstorming, refactoring, debugging, and writing tests. It was especially helpful when I needed to turn the initial UML ideas into working Python classes and when I wanted help deciding how to structure new methods like sorting and conflict detection.
- The most helpful prompts were ones that asked for a concrete plan or a small change, such as asking how to implement recurring-task behavior or how to keep the scheduler logic readable while adding new features.

**b. Judgment and verification**

- One example was when the AI suggested a very compact version of the conflict-detection method. It was more Pythonic, but I felt it would be harder for a human reader to follow. I kept the more explicit version instead because it was clearer and easier to debug.
- I verified AI suggestions by running the tests and checking whether the behavior matched the requirements. In this project, pytest was the most useful verification tool because it confirmed both the happy paths and edge cases.

---

## 4. Testing and Verification

**a. What you tested**

- I tested sorting behavior, filtering behavior, recurring-task creation, conflict detection, and basic task management. These were the most important behaviors because they make the scheduler practical rather than just structurally complete.
- These tests were important because they verify that the system behaves correctly in everyday scenarios, such as planning a day with multiple tasks or handling overlaps without crashing.

**b. Confidence**

- I am fairly confident that the current scheduler works correctly for the core scenarios covered by the tests. The automated suite gives good evidence that the main behaviors are working as intended.
- If I had more time, I would test edge cases like invalid time formats, very long task lists, and tasks that overlap in more complex ways than a simple time-range check.

---

## 5. Reflection

**a. What went well**

- I am most satisfied with how the scheduler evolved from a simple prototype into a more useful planning tool. The combination of sorting, filtering, recurring logic, and conflict warnings made the app feel much more realistic and polished.

**b. What you would improve**

- In another iteration, I would improve the scheduler by making it smarter about conflicts, such as automatically moving a task to a later time instead of only warning the user. I would also make the UI more interactive so the owner can edit or remove tasks directly.

**c. Key takeaway**

- One important lesson was that AI is most effective when it is guided by a clear human architecture. I learned that I still needed to act as the lead architect: deciding what responsibilities belonged to each class, evaluating tradeoffs, and making sure the final design stayed simple and understandable.
