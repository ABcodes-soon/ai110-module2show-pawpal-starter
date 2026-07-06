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
