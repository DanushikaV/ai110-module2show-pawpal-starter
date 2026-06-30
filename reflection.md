# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each? 

Add and manage pets.
Schedule pet care tasks such as feeding, walking, medication, or appointments.
View today's scheduled tasks in priority order.

My initial design focused on four main classes: Owner, Pet, Task, and Scheduler. The system was designed to allow users to add and manage pets, schedule pet care activities, and view daily tasks in a prioritized order.

The Owner class stores information about the pet owner and manages the pets they own. The Pet class stores information about each pet and maintains a list of its care tasks. The Task class represents individual pet care activities such as feeding, walking, grooming, medication, or veterinary appointments, including details like due time, priority, completion status, and whether the task recurs. The Scheduler class is responsible for organizing tasks, sorting them by priority and due time, detecting scheduling conflicts, and generating a daily care schedule.

This design separates responsibilities across different classes, making the system modular, easier to maintain, and easier to expand with additional features in the future.



**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

After reviewing my initial design with AI assistance, I identified potential issues with inconsistent relationships between classes. To improve this, I added a two way coonection between Owner–Pet and Pet–Task using assign_owner() and assign_pet() methods. This ensures that updates to one object are properly reflected in related objects, preventing data inconsistencies.

These changes made the system more robust and reduced potential logical bottlenecks when managing relationships between owners, pets, and tasks.

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
