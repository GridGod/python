
## **Phase 2 — Intermediate Python and software development**



Days 11–20

&#x20;Goal: Start building structured applications.



| Day    | Topics                                             | Practical assignment                 |
| ------ | -------------------------------------------------- | ------------------------------------ |
| **11** | File handling, read/write/append, context managers | Persistent notes application         |
| **12** | JSON, serialization, deserialization               | Save and load your to-do list        |
| **13** | Exceptions, `try`, `except`, `finally`             | Error-resistant calculator           |
| **14** | Modules, packages, pip, external APIs              | Fetch and filter API data            |
| **15** | OOP, classes, objects, attributes                  | User and Invitation classes          |
| **16** | Constructors, methods, `self`, encapsulation       | Invitation Management System         |
| **17** | Inheritance, polymorphism, abstraction             | Admin and regular user permissions   |
| **18** | Integration and OOP revision                       | **Project 2: Contact Book**          |
| **19** | Debugging, refactoring, code quality               | Improve and modularize Contact Book  |
| **20** | Git, GitHub, branches, commits, README             | Publish your projects professionally |

### **Detailed assignments**

**Day 11 — File handling**

Understand:

- Files and directories.
- `open()`, `read()`, `write()`, `append()`.
- `with open()` context managers.

Build a notes application that can create, save and retrieve notes.

**Day 12 — JSON**

Understand:

- JSON structure.
- `json.dump()`, `json.load()`.
- Python objects versus JSON data.

Upgrade your to-do application so data survives when the program closes.

**Day 13 — Exception handling**

Understand:

- Syntax errors versus runtime errors.
- `try` and `except`.
- Specific exception types.
- `finally` and `raise`.

Upgrade the calculator to handle invalid input, division by zero and unexpected errors.

**Day 14 — Modules and APIs**

Understand:

- Importing modules.
- Standard library.
- Installing packages using pip.
- HTTP requests and JSON responses.

Build a program that retrieves posts from JSONPlaceholder and filters them by keyword.

Resource: [JSONPlaceholder](https://jsonplaceholder.typicode.com/?utm_source=chatgpt.com) and [Requests documentation](https://requests.readthedocs.io/?utm_source=chatgpt.com).

**Day 15 — Object-oriented programming**

Understand:

- Classes and objects.
- Attributes.
- Constructors.
- `self`.

Build:

- `User` class.
- `Invitation` class.
- Create multiple users and invitations.

**Day 16 — OOP methods**

Understand:

- Instance methods.
- Constructors using `__init__`.
- `__str__`.
- Encapsulation.

Build an invitation manager that creates, updates and lists invitations.

**Day 17 — Inheritance and polymorphism**

Understand:

- Parent and child classes.
- Method overriding.
- Inheritance.
- Polymorphism.
- Introduction to abstraction.

Build:

- `User`.
- `AdminUser`.
- `RegularUser`.

Implement permissions to demonstrate the differences.

**Day 18 — Project 2**

[File Handling: Create your contacts book in a notepad in 7 steps | by Console Flare | Medium](https://images.openai.com/static-rsc-4/DEiKAfxOcBHHo7r3D45JrmVWlLgO4YQJiP6QSCJmo3ls2B9OhImfMof-DzpMq2tZvPmF4W_ZmZTu_7QDnUYW32r3zbIU0t7lDPrzxTy0LDXzfmkMRpLAS9lH5RF1zatyEcxW1wZwan125PamUidav03Q2WqYopjclM6_E6e3FQw?purpose=inline)

[medium.com](https://medium.com/%40consoleflare/file-handling-create-your-contacts-book-in-a-notepad-in-7-steps-351d8edb330b?utm_source=chatgpt.com)

**Contact Book Management System**

Required features:

- Add contacts.
- Update contact details.
- Search by name.
- Delete contacts.
- Display all contacts.
- Save contacts in JSON.
- Load contacts after restarting the program.

Technical requirements: OOP, functions, dictionaries, JSON and error handling.

**Day 19 — Debugging and clean code**

Learn:

- Breakpoints.
- Debugger.
- Reading tracebacks.
- Refactoring.
- Naming conventions.
- Separation of responsibilities.

Refactor Contact Book into separate modules such as:

```
contact_book/
├── main.py
├── models.py
├── services.py
├── storage.py
└── README.md
```

**Day 20 — Git and GitHub**

Learn:

- Git versus GitHub.
- Repository.
- Commits.
- Branches.
- Merge.
- Pull and push.
- `.gitignore`.

Assignment:

- Publish all projects.
- Create meaningful READMEs.
- Make at least one branch.
- Make a change, commit it and merge it back.

**Resources for Phase 2**

- Python Crash Course: Chapters 6–11.
- Automate the Boring Stuff: Chapters 5–16 selectively.
- Corey Schafer: OOP and modules series.
- Harvard CS50P: Exceptions, libraries, testing, file I/O and OOP.
- Official Git documentation: [Git documentation](https://git-scm.com/doc?utm_source=chatgpt.com).