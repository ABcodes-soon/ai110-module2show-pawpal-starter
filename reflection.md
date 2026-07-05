# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- My initial UML design centers on four main classes: Owner, Pet, Task, and Scheduler.
- The Owner class represents the person using the app and can manage one or more pets.
- The Pet class stores the pet’s basic details and keeps track of that pet’s care tasks.
- The Task class represents a single care activity such as a walk, feeding, medication, or grooming, with attributes like title, duration, priority, and recurrence.
- The Scheduler class evaluates the tasks for a pet and produces a daily plan that respects the owner’s available time and task priorities.
- Three core actions a user should be able to perform are: 1) add a pet profile for their animal, 2) create or edit care tasks with details such as duration and priority, and 3) generate and view a daily schedule that shows what needs to be done today.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

**c. Building blocks**

- Owner: holds the owner’s name and contact information, and can add pets and view the daily plan.
- Pet: holds the pet’s name, species, and care needs, and can receive tasks and report its current care status.
- Task: holds the task title, duration, priority, category, and whether it repeats, and can be updated or marked as complete.
- Scheduler: holds the available time window and the list of tasks to consider, and can generate a daily schedule based on priority and time constraints.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
