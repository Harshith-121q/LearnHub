from formatter import format_lesson

def get_python_module_5():
    lessons = [
        format_lesson(
            "python",
            "Classes and objects", 25,
            [
                "Define custom classes using the class keyword",
                "Instantiate objects and access attributes and methods",
                "Understand state (attributes) and behavior (methods) in Python OOP"
            ],
            "In Python, everything is an object (including functions, numbers, and modules). A **Class** is a blueprint defining attributes (data) and methods (functions) for creating objects.\n- Defined using `class ClassName:` (PascalCase convention).\n- Instantiated by calling the class like a function: `obj = ClassName()`.\n- Attributes and methods are accessed using the dot operator: `obj.attribute`, `obj.method()`.",
            "class Course:\n    title = \"Python Masterclass\" # Class attribute\n    def start(self):\n        print(f\"Starting {self.title}\")\n\nc = Course()\nc.start()",
            "class Student:\n    def study(self, subject):\n        print(f\"Student is actively learning: {subject}\")\n\ns1 = Student()\ns1.name = \"Alex Morgan\" # Dynamic attribute assignment\ns1.study(\"Python Object-Oriented Programming\")\nprint(f\"Enrolled Student: {s1.name}\")",
            "Student is actively learning: Python Object-Oriented Programming\nEnrolled Student: Alex Morgan",
            [
                "Student class defines the study method.",
                "s1 is an instance of Student.",
                "Dynamic attribute s1.name is bound to the instance."
            ],
            [
                "Calling a method without self in its definition (`def study():`), causing a `TypeError: takes 0 positional arguments but 1 was given` when called on an instance.",
                "Overwriting class attributes on individual instances unintentionally."
            ],
            [
                ("What does the self parameter represent in Python class methods?", "The explicit reference to the current instance calling the method."),
                ("Can attributes be dynamically attached to existing Python objects at runtime?", "Yes, Python instances store attributes in a writable __dict__ by default."),
                ("What is the difference between a class and an object in Python?", "A class is the type blueprint; an object is an instance in memory.")
            ]
        ),
        format_lesson(
            "python",
            "__init__ and self", 25,
            [
                "Initialize object state using the special __init__ method",
                "Understand the self parameter and method binding",
                "Enforce required fields during instance creation"
            ],
            "The `__init__` method is Python's **initializer method** (constructor):\n- Executed automatically immediately after a new instance is created by `__new__`.\n- Sets up initial instance attributes: `self.field = arg`.\n- `self`: The first parameter of every instance method. When you call `s.study()`, Python translates it to `Student.study(s)`. `self` refers directly to the calling instance.",
            "class User:\n    def __init__(self, username, email):\n        self.username = username\n        self.email = email",
            "class CourseLesson:\n    def __init__(self, title, duration_minutes, sequence_order):\n        self.title = title\n        self.duration_minutes = duration_minutes\n        self.sequence_order = sequence_order\n        self.is_completed = False\n        \n    def complete(self):\n        self.is_completed = True\n        print(f\"Lesson #{self.sequence_order} '{self.title}' marked as completed!\")\n\nlesson = CourseLesson(\"__init__ and self in Python\", 25, 2)\nlesson.complete()\nprint(f\"Completed Status: {lesson.is_completed}\")",
            "Lesson #2 '__init__ and self in Python' marked as completed!\nCompleted Status: True",
            [
                "__init__ initializes 4 instance attributes upon instantiation.",
                "complete() uses self to mutate the instance attribute is_completed."
            ],
            [
                "Returning a value other than `None` from `__init__`, which raises `TypeError: __init__() should return None`.",
                "Forgetting `self` as the first argument in `__init__` or instance methods."
            ],
            [
                ("Why does Python require `self` to be explicitly listed in method headers?", "Explicit is better than implicit; clearly differentiates instance variables from local function variables."),
                ("How does `__init__` differ from `__new__` in Python?", "__new__ is the constructor that creates the instance; __init__ initializes it once created."),
                ("Can __init__ have default parameter values?", "Yes, standard default parameter rules apply.")
            ]
        ),
        format_lesson(
            "python",
            "Instance and class attributes", 25,
            [
                "Differentiate instance attributes (self.x) from class attributes",
                "Manage shared class-level state (counters, registry lists)",
                "Prevent accidental instance shadowing of class attributes"
            ],
            "Python distinguishes between two types of attributes:\n- **Instance Attributes**: Bound to `self` inside methods (`self.name`). Owned by an individual object; mutating it affects ONLY that specific instance.\n- **Class Attributes**: Defined directly inside the class body outside any method. Shared by **ALL instances** of the class. Accessed via `ClassName.attr` or `self.attr`.",
            "class Enrollment:\n    total_enrollments = 0 # Class attribute\n    def __init__(self, student):\n        self.student = student # Instance attribute\n        Enrollment.total_enrollments += 1",
            "class EnrollmentTracker:\n    global_enrolled_count = 0 # Class attribute shared across all instances\n    \n    def __init__(self, student_name, course_title):\n        self.student_name = student_name # Instance attribute\n        self.course_title = course_title # Instance attribute\n        EnrollmentTracker.global_enrolled_count += 1\n        self.enrollment_id = EnrollmentTracker.global_enrolled_count\n\ne1 = EnrollmentTracker(\"Alex Morgan\", \"Python Masterclass\")\ne2 = EnrollmentTracker(\"Sarah Connor\", \"Java Masterclass\")\n\nprint(f\"Enrollment 1: #{e1.enrollment_id} - {e1.student_name}\")\nprint(f\"Enrollment 2: #{e2.enrollment_id} - {e2.student_name}\")\nprint(f\"Total System Enrollments: {EnrollmentTracker.global_enrolled_count}\")",
            "Enrollment 1: #1 - Alex Morgan\nEnrollment 2: #2 - Sarah Connor\nTotal System Enrollments: 2",
            [
                "global_enrolled_count is incremented on the class itself.",
                "Each instance retains isolated student_name and enrollment_id values."
            ],
            [
                "Mutating a class attribute via `self.attr = value` when intent is to update the shared counter; this creates an instance variable that shadows the class attribute on that single object.",
                "Using mutable objects (e.g. `items = []`) as class attributes, which are shared across all instances."
            ],
            [
                ("How do you safely update a class attribute?", "Reference it explicitly via `ClassName.attribute_name`."),
                ("What does the `@classmethod` decorator do?", "Binds a method to the class itself (`cls`) rather than an instance (`self`)."),
                ("What does the `@staticmethod` decorator do?", "Defines a self-contained utility method inside a class that takes neither `self` nor `cls`.")
            ]
        ),
        format_lesson(
            "python",
            "Encapsulation conventions", 25,
            [
                "Understand Python's underscore privacy conventions (_protected, __private)",
                "Implement controlled attribute access using @property, @setter, and @deleter",
                "Understand name mangling in double underscore attributes"
            ],
            "Python does NOT have private keywords. Instead, it relies on conventions and properties ('We are all consenting adults here'):\n- `_single_underscore`: Internal convention. Signals to developers 'private implementation detail; do not touch directly'.\n- `__double_underscore`: Name mangling. Python renames `__attr` to `_ClassName__attr` to prevent accidental subclass collisions.\n- **@property**: Exposes getter/setter methods with natural attribute access syntax (`obj.score = 95`), validating mutations transparently.",
            "class Student:\n    def __init__(self, score):\n        self._score = score\n    @property\n    def score(self): return self._score\n    @score.setter\n    def score(self, val):\n        if not 0 <= val <= 100: raise ValueError(\"Invalid score\")\n        self._score = val",
            "class StudentAccount:\n    def __init__(self, username, initial_progress=0.0):\n        self.username = username\n        self._progress = 0.0\n        self.progress = initial_progress # Uses setter validation\n        \n    @property\n    def progress(self):\n        \"\"\"Getter for progress percentage.\"\"\"\n        return self._progress\n        \n    @progress.setter\n    def progress(self, value):\n        if not (0.0 <= value <= 100.0):\n            print(f\"Validation Warning: Progress must be between 0.0 and 100.0. Given: {value}\")\n            return\n        self._progress = round(value, 1)\n\naccount = StudentAccount(\"student_alex\", 45.5)\nprint(f\"Current Progress: {account.progress}%\")\n\n# Attempt invalid update\naccount.progress = 120.0\nprint(f\"Progress after invalid update: {account.progress}%\")",
            "Current Progress: 45.5%\nValidation Warning: Progress must be between 0.0 and 100.0. Given: 120.0\nProgress after invalid update: 45.5%",
            [
                "The @property decorator allows accessing progress like an attribute.",
                "The @progress.setter enforces validation boundaries, rejecting 120.0."
            ],
            [
                "Defining `@property` and setter with the exact same name as the underlying storage variable, causing infinite recursion (`RecursionError: maximum recursion depth exceeded`). Always use an underscore for backing field: `_progress`.",
                "Relying on double underscores `__var` thinking it provides cryptography or actual security; name mangling is easily inspected via `obj._Class__var`."
            ],
            [
                ("How does name mangling work for `__my_var` inside class `Foo`?", "Python internally renames the attribute to `_Foo__my_var`."),
                ("What is the primary benefit of the `@property` decorator?", "Allows changing implementation from a direct attribute to validated methods without breaking caller API syntax."),
                ("Can a property be made read-only?", "Yes, define only the `@property` getter without providing a `@setter`.")
            ]
        ),
        format_lesson(
            "python",
            "Inheritance", 25,
            [
                "Create subclasses that inherit from base classes",
                "Delegate constructor initialization using super()",
                "Understand multiple inheritance and Method Resolution Order (MRO)"
            ],
            "Inheritance allows a subclass to inherit attributes and methods from a superclass:\n- Syntax: `class Child(Parent):`.\n- `super()`: Returns a proxy object delegating method calls to the parent class. Primarily used in `__init__` to initialize inherited state: `super().__init__(args)`.\n- **Multiple Inheritance**: Python supports inheriting from multiple classes (`class C(A, B):`). Invocations are resolved using **C3 Linearization / Method Resolution Order (MRO)** (`ClassName.__mro__`).",
            "class Parent:\n    def __init__(self, name): self.name = name\nclass Child(Parent):\n    def __init__(self, name, age):\n        super().__init__(name)\n        self.age = age",
            "class User:\n    def __init__(self, username, email):\n        self.username = username\n        self.email = email\n        \n    def get_role_description(self):\n        return f\"General Platform User: {self.username}\"\n\nclass Instructor(User):\n    def __init__(self, username, email, specialty):\n        super().__init__(username, email) # Delegate to parent\n        self.specialty = specialty\n        \n    def get_role_description(self):\n        return f\"Instructor {self.username} (Specialty: {self.specialty})\"\n\ninst = Instructor(\"sarah_c\", \"sarah@learnhub.com\", \"Python & Distributed Systems\")\nprint(inst.get_role_description())\nprint(f\"Is instance of User? {isinstance(inst, User)}\")",
            "Instructor sarah_c (Specialty: Python & Distributed Systems)\nIs instance of User? True",
            [
                "Instructor inherits from User.",
                "super().__init__ initializes common username and email.",
                "Overrides get_role_description with specialized instructor text."
            ],
            [
                "Forgetting to call `super().__init__()` in the child class, leaving parent attributes uninitialized.",
                "Diamond inheritance confusion in multiple inheritance without understanding MRO."
            ],
            [
                ("How can you inspect the Method Resolution Order (MRO) of a class in Python?", "Via `ClassName.__mro__` or `ClassName.mro()`."),
                ("What does `issubclass(Child, Parent)` return?", "True if Child is a direct or indirect subclass of Parent."),
                ("Why does Python support multiple inheritance while Java does not?", "Python uses C3 linearization to provide deterministic method resolution without ambiguity.")
            ]
        ),
        format_lesson(
            "python",
            "Polymorphism", 20,
            [
                "Leverage Python's dynamic Duck Typing ('If it walks like a duck...')",
                "Design polymorphic interfaces without rigid inheritance",
                "Use the collections.abc module for formal abstract protocols"
            ],
            "In Python, **Polymorphism** is predominantly realized through **Duck Typing**: 'If it walks like a duck and quacks like a duck, it is a duck'.\n- You do NOT need explicit abstract interfaces or shared class inheritance for two objects to be used interchangeably.\n- As long as an object provides the expected methods (e.g. `.render()`, `.start()`), any function can process it interchangeably at runtime.",
            "def launch_activity(item):\n    item.start() # Duck typing: works on any object with a start() method",
            "class VideoLecture:\n    def start(self):\n        return \"Streaming high-definition video lesson...\"\n\nclass InteractiveQuiz:\n    def start(self):\n        return \"Launching interactive quiz assessment...\"\n\nclass CodingExercise:\n    def start(self):\n        return \"Initializing embedded Python code editor...\"\n\ndef launch_course_item(item):\n    print(f\"[Curriculum Runner] -> {item.start()}\")\n\ncurriculum = [VideoLecture(), InteractiveQuiz(), CodingExercise()]\nfor activity in curriculum:\n    launch_course_item(activity)",
            "[Curriculum Runner] -> Streaming high-definition video lesson...\n[Curriculum Runner] -> Launching interactive quiz assessment...\n[Curriculum Runner] -> Initializing embedded Python code editor...",
            [
                "Three unrelated classes provide identical start() interface.",
                "launch_course_item handles all three interchangeably through dynamic polymorphism."
            ],
            [
                "Checking `if type(item) is SpecificClass:` which breaks duck typing and polymorphism.",
                "Invoking a method on an object that does not implement it, raising `AttributeError`."
            ],
            [
                ("What is Duck Typing in Python?", "A programming approach where an object's suitability is determined by the presence of certain methods/properties rather than its inheritance hierarchy."),
                ("What is EAFP in Python?", "'Easier to Ask for Forgiveness than Permission'—try an operation and catch the exception rather than checking types beforehand."),
                ("What does the abc module provide in Python?", "Abstract Base Classes (ABCs) to define formal interface contracts via `@abstractmethod`.")
            ]
        ),
        format_lesson(
            "python",
            "Special methods", 25,
            [
                "Implement Python data model special dunder methods (__str__, __repr__, __len__)",
                "Overload comparison operators (__eq__, __lt__)",
                "Customize arithmetic behavior (__add__) and container indexing (__getitem__)"
            ],
            "Python classes participate in language syntax through **Special Methods** (also called 'dunder' methods for double underscore):\n- `__str__(self)`: Human-friendly string representation (called by `print()` and `str()`).\n- `__repr__(self)`: Unambiguous developer representation (called in REPL or debugging).\n- `__len__(self)`: Enables `len(obj)`.\n- `__eq__(self, other)`: Enables `obj1 == obj2`.\n- `__lt__(self, other)`: Enables `obj1 < obj2` and allows sorting with `sorted()`.\n- `__getitem__(self, key)`: Enables square-bracket indexing `obj[key]`.",
            "class Item:\n    def __repr__(self): return f\"Item({self.name!r})\"\n    def __len__(self): return len(self.items)",
            "class CourseTrack:\n    def __init__(self, title, lesson_count):\n        self.title = title\n        self.lesson_count = lesson_count\n        \n    def __str__(self):\n        return f\"CourseTrack: '{self.title}' ({self.lesson_count} lessons)\"\n        \n    def __repr__(self):\n        return f\"CourseTrack(title={self.title!r}, lesson_count={self.lesson_count})\"\n        \n    def __len__(self):\n        return self.lesson_count\n        \n    def __lt__(self, other):\n        return self.lesson_count < other.lesson_count\n\nt1 = CourseTrack(\"Python Fundamentals\", 10)\nt2 = CourseTrack(\"Python Masterclass\", 79)\n\nprint(str(t1))\nprint(f\"len(t2): {len(t2)}\")\nprint(f\"Is t1 smaller than t2? {t1 < t2}\")",
            "CourseTrack: 'Python Fundamentals' (10 lessons)\nlen(t2): 79\nIs t1 smaller than t2? True",
            [
                "__str__ provides clean user-facing formatting.",
                "__len__ enables len(t2) seamlessly.",
                "__lt__ enables direct relational comparisons t1 < t2."
            ],
            [
                "Returning a non-string from `__str__` or `__repr__` (raises TypeError).",
                "Returning a non-integer or negative integer from `__len__`."
            ],
            [
                ("What is the difference between __str__ and __repr__?", "__str__ is for end-user readability; __repr__ is unambiguous and ideally evaluatable as valid Python code."),
                ("What dunder method enables using an object as a context manager with `with`?", "`__enter__` and `__exit__`."),
                ("What dunder method enables using an object as a callable function (`obj()`)?", "`__call__`.")
            ]
        ),
        format_lesson(
            "python",
            "Composition", 20,
            [
                "Model 'has-a' relationships using object composition",
                "Delegate responsibilities across collaborating component classes",
                "Prefer composition over inheritance to prevent rigid coupling"
            ],
            "Composition is the OOP design pattern where a class is composed of one or more other objects as attributes ('has-a' relationship), rather than inheriting behavior ('is-a' relationship).\n- Promotes loose coupling: components can be modified or mocked independently.\n- Avoids fragile base class problems and deep inheritance trees.",
            "class Course:\n    def __init__(self, title, instructor):\n        self.title = title\n        self.instructor = instructor # Composition (has-a)",
            "class Instructor:\n    def __init__(self, name, email):\n        self.name = name\n        self.email = email\n        \n    def get_badge(self):\n        return f\"Instructor: {self.name} <{self.email}>\"\n\nclass Course:\n    def __init__(self, title, instructor: Instructor):\n        self.title = title\n        self.instructor = instructor # Course HAS-AN instructor\n        self.modules = []\n        \n    def add_module(self, module_title):\n        self.modules.append(module_title)\n        \n    def print_syllabus(self):\n        print(f\"=== Course: {self.title} ===\")\n        print(self.instructor.get_badge())\n        print(\"Modules:\")\n        for m in self.modules:\n            print(f\"  - {m}\")\n\nlead = Instructor(\"Sarah Connor\", \"sarah@learnhub.com\")\npython_course = Course(\"Python Programming Masterclass\", lead)\npython_course.add_module(\"M1: Fundamentals\")\npython_course.add_module(\"M2: Conditions and Loops\")\npython_course.print_syllabus()",
            "=== Course: Python Programming Masterclass ===\nInstructor: Sarah Connor <sarah@learnhub.com>\nModules:\n  - M1: Fundamentals\n  - M2: Conditions and Loops",
            [
                "Course references an Instructor instance through composition.",
                "print_syllabus delegates instructor formatting to the Instructor object."
            ],
            [
                "Inheriting from a class just to reuse a single helper method (e.g. subclassing list instead of wrapping it).",
                "Tight circular dependencies where parent and child cannot be tested without each other."
            ],
            [
                ("Why is composition considered more flexible than inheritance?", "Relationships can be dynamically reconfigured at runtime by passing different component instances."),
                ("What is Dependency Injection in Python?", "Passing collaborating objects into a class via __init__ rather than creating them internally."),
                ("How does composition improve unit testing?", "Allows easily passing mock objects for collaborating components.")
            ]
        ),
        format_lesson(
            "python",
            "Dataclasses", 25,
            [
                "Use the @dataclass decorator to eliminate boilerplate code",
                "Understand auto-generated __init__, __repr__, and __eq__ methods",
                "Implement immutable (frozen=True) value objects"
            ],
            "Introduced in Python 3.7 (`dataclasses` module), the `@dataclass` decorator automatically generates special methods (`__init__`, `__repr__`, `__eq__`) for classes designed primarily to store state:\n- Declares fields using standard type annotations.\n- `frozen=True`: Makes the dataclass immutable and hashable (can be used as dictionary keys or set items).\n- Supports default values and field customization with `field(default_factory=list)`.",
            "from dataclasses import dataclass, field\n@dataclass(frozen=True)\nclass CourseSummary:\n    id: int\n    title: str\n    duration_hours: int = 50",
            "from dataclasses import dataclass\n\n@dataclass\nclass LessonItem:\n    title: str\n    duration_minutes: int\n    sequence_order: int\n    is_completed: bool = False\n\nl1 = LessonItem(\"Python Dataclasses\", 25, 9)\nl2 = LessonItem(\"Python Dataclasses\", 25, 9)\n\nprint(f\"Dataclass Auto-Repr: {l1}\")\nprint(f\"Value Equality (l1 == l2): {l1 == l2}\")",
            "Dataclass Auto-Repr: LessonItem(title='Python Dataclasses', duration_minutes=25, sequence_order=9, is_completed=False)\nValue Equality (l1 == l2): True",
            [
                "@dataclass automatically generated __init__, __repr__, and __eq__.",
                "l1 == l2 evaluates to True based on field value comparison."
            ],
            [
                "Using a mutable default value directly in a dataclass field (`items: list = []`), which raises `ValueError: mutable default <class 'list'> is not allowed; use default_factory`.",
                "Modifying an attribute on a frozen dataclass (`frozen=True`), which raises `FrozenInstanceError`."
            ],
            [
                ("How do you define a default mutable list in a dataclass?", "Use `field(default_factory=list)`."),
                ("What does `frozen=True` do on a dataclass?", "Makes all instances immutable, raising FrozenInstanceError on attribute reassignment, and generates a __hash__ method."),
                ("How does a dataclass compare to a namedtuple?", "Dataclasses support mutable or frozen states, default factory methods, inheritance, and standard class features.")
            ]
        ),
        format_lesson(
            "python",
            "OOP mini-project", 35,
            [
                "Architect a complete multi-class domain model (Course & Enrollment System)",
                "Apply encapsulation, dataclasses, properties, and validation rules",
                "Enforce duplicate enrollment rules and verify business invariants"
            ],
            "In this mini-project, we architect a complete Student Course Enrollment System in pure Python:\n- `Student`: Encapsulates student ID, name, email.\n- `Lesson`: Dataclass holding title, sequence order, and completion state.\n- `CourseEnrollment`: Manages enrolled lessons, marks topics complete, and calculates progress percentage accurately as `(completed / total) * 100.0`.",
            "class CourseEnrollment:\n    # Manages completed lesson progress\n    pass",
            "from dataclasses import dataclass\nfrom typing import List, Set\n\n@dataclass\nclass Lesson:\n    id: int\n    title: str\n    duration: int\n\nclass StudentEnrollment:\n    def __init__(self, student_name: str, course_title: str, lessons: List[Lesson]):\n        self.student_name = student_name\n        self.course_title = course_title\n        self.lessons = lessons\n        self._completed_ids: Set[int] = set()\n        \n    def complete_lesson(self, lesson_id: int):\n        if any(l.id == lesson_id for l in self.lessons):\n            self._completed_ids.add(lesson_id)\n            \n    @property\n    def progress_percentage(self) -> float:\n        if not self.lessons: return 0.0\n        return round((len(self._completed_ids) / len(self.lessons)) * 100.0, 1)\n\ncurriculum = [\n    Lesson(1, \"Python Fundamentals\", 20),\n    Lesson(2, \"Conditions & Loops\", 25),\n    Lesson(3, \"Data Structures\", 30),\n    Lesson(4, \"OOP Python\", 35)\n]\n\nenr = StudentEnrollment(\"Alex Morgan\", \"Python Masterclass\", curriculum)\nprint(f\"Initial Progress: {enr.progress_percentage}%\")\n\nenr.complete_lesson(1)\nenr.complete_lesson(2)\nprint(f\"Progress after 2 lessons: {enr.progress_percentage}% ({len(enr._completed_ids)}/{len(curriculum)})\")",
            "Initial Progress: 0.0%\nProgress after 2 lessons: 50.0% (2/4)",
            [
                "Lesson dataclass defines lightweight immutable curriculum units.",
                "StudentEnrollment encapsulates progress calculation logic.",
                "Enforces unique completed lessons and calculates 50.0% progress accurately."
            ],
            [
                "Allowing completed lessons set to count duplicate completions.",
                "Dividing by zero when curriculum lessons list is empty."
            ],
            [
                ("How does using a Set for `_completed_ids` prevent duplicate completions?", "Sets automatically enforce uniqueness; adding the same lesson ID twice has no effect."),
                ("How would you serialize this enrollment object to JSON?", "Convert to a dictionary using asdict() or a custom `.to_dict()` method and pass to `json.dumps()`."),
                ("Why is progress_percentage defined as a `@property`?", "Computes progress dynamically from current completed state without risking stale out-of-sync fields.")
            ]
        )
    ]
    return {
        "title": "Module 5 - Object-Oriented Python",
        "description": "Model real-world concepts with classes and objects.",
        "sequenceOrder": 5,
        "lessons": lessons
    }

def get_python_module_6():
    lessons = [
        format_lesson(
            "python",
            "Exception handling", 25,
            [
                "Handle exceptions using try, except, else, and finally blocks",
                "Catch specific built-in exceptions (ValueError, KeyError, TypeError, FileNotFoundError)",
                "Avoid overly broad bare except clauses"
            ],
            "Exceptions in Python represent runtime errors that disrupt execution flow:\n- `try`: Code that might fail.\n- `except SpecificError as e`: Handles the specific exception.\n- `else`: Executes ONLY if the try block succeeded without exceptions.\n- `finally`: Guaranteed to run regardless of outcome (cleanup).\nCrucial: **Never use a bare `except:` or `except Exception:` blindly**; it catches system-exiting signals (`KeyboardInterrupt`, `SystemExit`) and masks programming bugs.",
            "try:\n    value = int(user_input)\nexcept ValueError as e:\n    print(f\"Invalid number: {e}\")\nelse:\n    print(f\"Parsed: {value}\")\nfinally:\n    print(\"Cleanup complete\")",
            "def safe_divide(a, b):\n    try:\n        result = a / b\n    except ZeroDivisionError:\n        print(\"Error: Cannot divide by zero!\")\n        return None\n    except TypeError as e:\n        print(f\"Error: Invalid argument type - {e}\")\n        return None\n    else:\n        return result\n    finally:\n        pass\n\nprint(\"10 / 2 =\", safe_divide(10, 2))\nprint(\"10 / 0 =\", safe_divide(10, 0))",
            "10 / 2 = 5.0\nError: Cannot divide by zero!\n10 / 0 = None",
            [
                "safe_divide catches ZeroDivisionError and TypeError separately.",
                "else block returns result only when division succeeds."
            ],
            [
                "Using bare `except:` which catches `KeyboardInterrupt` and prevents exiting with Ctrl+C.",
                "Using exceptions for standard control flow instead of normal conditionals."
            ],
            [
                ("What built-in exception is raised when looking up a missing key in a dict?", "KeyError."),
                ("What does the else block do in a try-except structure?", "Executes only if no exceptions were raised in the try block."),
                ("What is the base class for all built-in exceptions in Python?", "BaseException (with Exception as the base for all non-system-exiting exceptions).")
            ]
        ),
        format_lesson(
            "python",
            "Raising exceptions", 20,
            [
                "Raise exceptions explicitly using the raise keyword",
                "Create custom exception classes inheriting from Exception",
                "Preserve root causes using exception chaining (raise ... from ...)"
            ],
            "You can trigger exceptions deliberately using `raise`:\n- `raise ValueError(\"Descriptive message\")`.\n- **Custom Exceptions**: Define a class inheriting from `Exception`.\n- **Exception Chaining**: `raise CustomError(\"Failed\") from original_error` links exceptions, preserving the full traceback.",
            "class CourseError(Exception):\n    \"\"\"Base exception for curriculum errors.\"\"\"\n\nraise CourseError(\"Course already published\")",
            "class DuplicateEnrollmentError(Exception):\n    def __init__(self, student, course):\n        super().__init__(f\"Student '{student}' is already enrolled in '{course}'!\")\n        self.student = student\n        self.course = course\n\ndef enroll(student, course, enrolled_students):\n    if student in enrolled_students:\n        raise DuplicateEnrollmentError(student, course)\n    enrolled_students.add(student)\n    print(f\"Enrolled {student} in {course}\")\n\nactive_roster = {\"Alex Morgan\"}\ntry:\n    enroll(\"Alex Morgan\", \"Python Masterclass\", active_roster)\nexcept DuplicateEnrollmentError as e:\n    print(f\"Domain Error: {e}\")",
            "Domain Error: Student 'Alex Morgan' is already enrolled in 'Python Masterclass'!",
            [
                "DuplicateEnrollmentError extends Exception with domain fields.",
                "enroll raises the custom exception on duplicate detection."
            ],
            [
                "Inheriting custom exceptions from `BaseException` instead of `Exception`.",
                "Raising exceptions without descriptive error messages."
            ],
            [
                ("What does `raise ... from None` do in Python 3?", "Suppresses the context of the previous exception, hiding internal tracebacks."),
                ("Why should custom exceptions inherit from Exception rather than BaseException?", "Ensures standard try-except blocks can catch them safely."),
                ("What does the assert statement do?", "Tests a condition and raises AssertionError if false (used for debugging/testing).")
            ]
        ),
        format_lesson(
            "python",
            "File handling", 25,
            [
                "Open, read, write, and append files using built-in open()",
                "Understand file access modes ('r', 'w', 'a', 'x', 'b', 't')",
                "Specify UTF-8 encoding explicitly to avoid platform-dependent corruption"
            ],
            "Python provides built-in file I/O via `open(filename, mode, encoding='utf-8')`:\n- **Modes**:\n  - `'r'`: Read (default; raises `FileNotFoundError` if missing).\n  - `'w'`: Write (truncates/creates file).\n  - `'a'`: Append (writes to end of file without truncating).\n  - `'x'`: Exclusive creation (fails if file exists).\n  - `'b'`: Binary mode (images, bytes).\n- **Reading**:\n  - `f.read()`: Reads entire file as a string.\n  - `f.readline()`: Reads a single line.\n  - `for line in f:`: Memory-efficient iteration over lines.",
            "with open(\"data.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"Hello, Python File I/O\\n\")",
            "demo_filename = \"learnhub_io_demo.tmp\"\n\n# Writing\nwith open(demo_filename, \"w\", encoding=\"utf-8\") as f:\n    f.write(\"Lesson 1: Python Files\\nLesson 2: Context Managers\\nLesson 3: JSON Data\\n\")\n\n# Reading\nwith open(demo_filename, \"r\", encoding=\"utf-8\") as f:\n    lines = [line.strip() for line in f]\n\nprint(f\"Read {len(lines)} lines from disk:\")\nfor l in lines:\n    print(f\"- {l}\")\n\nimport os\nos.remove(demo_filename) # Cleanup",
            "Read 3 lines from disk:\n- Lesson 1: Python Files\n- Lesson 2: Context Managers\n- Lesson 3: JSON Data",
            [
                "open() with 'w' creates the file with UTF-8 encoding.",
                "Memory-efficient file iteration extracts and strips lines.",
                "Temporary file is deleted cleanly."
            ],
            [
                "Omitting `encoding='utf-8'`, causing Windows systems to default to cp1252 and corrupt Unicode characters.",
                "Opening a file with `'w'` mode accidentally, which immediately wipes existing file contents."
            ],
            [
                ("What does the tell() and seek() methods do on a file object?", "tell() returns the current byte position; seek() repositions the read/write pointer."),
                ("Why should large multi-gigabyte files be iterated with `for line in f:` rather than `f.read()`?", "Lines are loaded lazily into memory one at a time, preventing Out-Of-Memory errors."),
                ("What exception is raised when opening a non-existent file in 'r' mode?", "FileNotFoundError.")
            ]
        ),
        format_lesson(
            "python",
            "Context managers", 20,
            [
                "Manage system resources automatically using the with statement",
                "Implement custom context managers using __enter__ and __exit__",
                "Utilize contextlib.contextmanager generator decorator"
            ],
            "A **Context Manager** guarantees that resources are acquired and safely released (even if an exception crashes the block):\n- Syntax: `with acquire_resource() as target: ...`.\n- Automatically calls `__enter__()` on entry and `__exit__()` on exit.\n- Standard use cases: Closing files, releasing thread locks, closing database connections, temporary configuration changes.",
            "from contextlib import contextmanager\n@contextmanager\ndef temp_resource():\n    yield\n    # Cleanup runs here",
            "class DatabaseSession:\n    def __enter__(self):\n        print(\"[Session] Connecting to database...\")\n        return \"ActiveConnection#1045\"\n        \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print(\"[Session] Rolling back/committing and closing connection cleanly.\")\n        return False # Propagate exceptions if any\n\nwith DatabaseSession() as conn:\n    print(f\"Executing queries using: {conn}\")\nprint(\"Outside with block: session fully closed.\")",
            "[Session] Connecting to database...\nExecuting queries using: ActiveConnection#1045\n[Session] Rolling back/committing and closing connection cleanly.\nOutside with block: session fully closed.",
            [
                "__enter__ sets up connection and returns target.",
                "__exit__ is guaranteed to run upon leaving the with block."
            ],
            [
                "Opening files without `with`, causing file descriptors to remain locked if an error occurs.",
                "Returning True from `__exit__` unintentionally, which swallows all exceptions silently."
            ],
            [
                ("What arguments does `__exit__` accept?", "exc_type, exc_val, exc_tb (exception type, value, and traceback)."),
                ("How does contextlib.contextmanager simplify writing context managers?", "Allows writing a generator function with a single `yield` instead of a full class with dunder methods."),
                ("Can multiple context managers be combined in a single with statement?", "Yes: `with open('a.txt') as a, open('b.txt') as b:`.")
            ]
        ),
        format_lesson(
            "python",
            "Paths and directories", 25,
            [
                "Work with filesystem paths using the object-oriented pathlib.Path module",
                "Check file/directory existence, iterate directories (iterdir, glob), and create folders",
                "Navigate paths across operating systems without slash formatting bugs"
            ],
            "The `pathlib` module (Python 3.4+) replaces legacy `os.path` with an object-oriented approach:\n- `Path`: Represents a filesystem path (`Path('dir') / 'file.txt'`).\n- The slash operator `/` joins path segments cleanly across Windows (`\\`) and Unix (`/`).\n- Methods: `p.exists()`, `p.is_file()`, `p.is_dir()`, `p.mkdir(parents=True, exist_ok=True)`, `p.glob('*.py')`, `p.read_text(encoding='utf-8')`.",
            "from pathlib import Path\np = Path(\"curriculum\") / \"java-curriculum.json\"\nif p.exists(): print(f\"Size: {p.stat().st_size} bytes\")",
            "from pathlib import Path\n\nbase = Path(\".\")\nprint(f\"Current working directory: {base.resolve()}\")\n\ntemp_dir = Path(\"learnhub_temp_dir\")\ntemp_dir.mkdir(exist_ok=True)\ntemp_file = temp_dir / \"sample.txt\"\ntemp_file.write_text(\"Pathlib I/O operation successful!\", encoding=\"utf-8\")\n\nprint(f\"File exists: {temp_file.exists()}\")\nprint(f\"File content: '{temp_file.read_text(encoding='utf-8')}'\")\n\n# Cleanup\ntemp_file.unlink()\ntemp_dir.rmdir()\nprint(\"Cleaned up temporary path.\")",
            "Current working directory: C:\\Users\\Admin\\OneDrive\\Desktop\\LearnHub\\backend\\src\\main\\resources\\curriculum\nFile exists: True\nFile content: 'Pathlib I/O operation successful!'\nCleaned up temporary path.",
            [
                "Uses / operator to concatenate path segments.",
                "write_text and read_text provide one-line file I/O.",
                "unlink and rmdir clean up file and directory."
            ],
            [
                "Hardcoding Windows backslashes in string paths (`\"dir\\file.txt\"`), which can introduce unintended escape characters (`\\n`, `\\t`).",
                "Calling `mkdir()` without `exist_ok=True`, raising `FileExistsError` if the directory already exists."
            ],
            [
                ("What does `path.glob('**/*.py')` do?", "Recursively matches all Python files in the directory and subdirectories."),
                ("How do you extract the file extension using pathlib?", "Via `path.suffix` (e.g. `'.json'`)."),
                ("What does `path.parent` return?", "The directory containing the file/path.")
            ]
        ),
        format_lesson(
            "python",
            "JSON processing", 25,
            [
                "Serialize and deserialize JSON data using the built-in json module",
                "Differentiate json.loads/dumps (strings) from json.load/dump (file streams)",
                "Customize JSON formatting using indent and sort_keys parameters"
            ],
            "**JSON (JavaScript Object Notation)** is the universal data format for REST APIs and data storage. The Python standard library `json` module translates:\n- `dict` <-> JSON Object\n- `list` <-> JSON Array\n- `str` <-> JSON String\n- `int`/`float` <-> JSON Number\n- `True`/`False` <-> `true`/`false`\n- `None` <-> `null`\n**Functions**:\n- `json.dumps(obj, indent=2)`: Serializes Python object to JSON string.\n- `json.loads(json_str)`: Deserializes JSON string to Python object.\n- `json.dump(obj, file)` / `json.load(file)`: Streams directly to/from file handles.",
            "import json\ndata = {\"course\": \"Python Masterclass\", \"lessons\": 79}\njson_str = json.dumps(data, indent=2)\nrestored = json.loads(json_str)",
            "import json\n\ncourse_record = {\n    \"id\": 102,\n    \"title\": \"Python Programming Masterclass\",\n    \"modules_count\": 8,\n    \"is_published\": True,\n    \"tags\": [\"Backend\", \"Automation\", \"Scripting\"],\n    \"prerequisites\": None\n}\n\n# Serialization\nserialized_json = json.dumps(course_record, indent=2)\nprint(\"Serialized JSON Output:\")\nprint(serialized_json)\n\n# Deserialization\nparsed = json.loads(serialized_json)\nprint(f\"\\nParsed back to dict: {parsed['title']} [Tags: {len(parsed['tags'])}]\")",
            "Serialized JSON Output:\n{\n  \"id\": 102,\n  \"title\": \"Python Programming Masterclass\",\n  \"modules_count\": 8,\n  \"is_published\": true,\n  \"tags\": [\n    \"Backend\",\n    \"Automation\",\n    \"Scripting\"\n  ],\n  \"prerequisites\": null\n}\n\nParsed back to dict: Python Programming Masterclass [Tags: 3]",
            [
                "True serialized to lowercase true; None serialized to null.",
                "loads() parses the JSON string back into a Python dictionary."
            ],
            [
                "Attempting to serialize custom class objects directly without providing a custom encoder, raising `TypeError: Object of type X is not JSON serializable`.",
                "Confusing `json.load()` (reads file) with `json.loads()` (reads string; 's' = string)."
            ],
            [
                ("How do you serialize a custom Python object to JSON?", "Provide a default function or custom JSONEncoder: `json.dumps(obj, default=lambda o: o.__dict__)`."),
                ("What does the parameter `ensure_ascii=False` do in json.dumps?", "Preserves Unicode characters directly rather than escaping them as `\\uXXXX`."),
                ("How does json.loads handle malformed JSON?", "Raises `json.JSONDecodeError`.")
            ]
        ),
        format_lesson(
            "python",
            "CSV processing", 25,
            [
                "Read and write tabular CSV files using the csv module",
                "Process records using csv.reader, csv.writer, csv.DictReader, and csv.DictWriter",
                "Handle delimiters, header rows, and newline parameters"
            ],
            "The `csv` module parses comma-separated values:\n- `csv.reader(f)`: Reads rows as lists of strings.\n- `csv.writer(f)`: Writes rows from sequences.\n- `csv.DictReader(f)`: Reads rows as dictionaries mapped to header column names.\n- `csv.DictWriter(f, fieldnames)`: Writes dictionaries to CSV.\nCrucial Windows Rule: Always open CSV files with `newline=''` to prevent extra blank lines on Windows.",
            "import csv\nwith open(\"data.csv\", \"w\", newline=\"\", encoding=\"utf-8\") as f:\n    writer = csv.writer(f)\n    writer.writerow([\"name\", \"score\"])",
            "import csv\nimport io\n\ncsv_buffer = io.StringIO()\nfieldnames = [\"id\", \"title\", \"duration\"]\nwriter = csv.DictWriter(csv_buffer, fieldnames=fieldnames)\n\nwriter.writeheader()\nwriter.writerow({\"id\": 1, \"title\": \"Python Fundamentals\", \"duration\": 20})\nwriter.writerow({\"id\": 2, \"title\": \"Conditions & Loops\", \"duration\": 25})\n\nprint(\"Generated CSV Buffer:\")\nprint(csv_buffer.getvalue())\n\n# Reading\ncsv_buffer.seek(0)\nreader = csv.DictReader(csv_buffer)\nprint(\"Parsed Rows via DictReader:\")\nfor row in reader:\n    print(f\"- Lesson #{row['id']}: {row['title']} ({row['duration']}m)\")",
            "Generated CSV Buffer:\nid,title,duration\r\n1,Python Fundamentals,20\r\n2,Conditions & Loops,25\r\n\r\nParsed Rows via DictReader:\n- Lesson #1: Python Fundamentals (20m)\n- Lesson #2: Conditions & Loops (25m)",
            [
                "DictWriter generates header and rows from dictionaries.",
                "DictReader reads columns by header name rather than index."
            ],
            [
                "Omitting `newline=''` when opening CSV files on Windows, creating duplicate blank lines between rows.",
                "Assuming CSV values are numeric; `csv.reader` returns ALL values as strings (must explicitly convert with `int()` or `float()`)."
            ],
            [
                ("How do you handle tab-separated (TSV) files using the csv module?", "Pass `delimiter='\\t'` to reader or writer."),
                ("What does csv.DictReader use for keys if the CSV has no header row?", "Pass `fieldnames=['col1', 'col2']` explicitly to DictReader."),
                ("How does the csv module escape cells that contain commas or quotation marks?", "Encloses the cell in double quotes automatically.")
            ]
        ),
        format_lesson(
            "python",
            "Iterators and generators", 30,
            [
                "Understand the Iterator and Iterable protocols (iter() and next())",
                "Create memory-efficient generator functions using yield",
                "Construct lazy data streaming pipelines using generator expressions"
            ],
            "Iterators and Generators provide memory-efficient processing of massive data sequences:\n- **Iterable**: An object that produces an iterator via `iter(obj)`.\n- **Iterator**: A stateful object with a `__next__()` method returning values until raising `StopIteration`.\n- **Generator Function**: A function containing the `yield` keyword. When called, it returns a generator object. Execution freezes at each `yield` and resumes on the next call, producing items **lazily on demand** without storing the entire sequence in memory.",
            "def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1",
            "def lesson_stream(limit):\n    for i in range(1, limit + 1):\n        yield f\"Lesson #{i}: In-Depth Video & Exercise\"\n\ngen = lesson_stream(3)\nprint(f\"Generator Object: {gen}\")\nprint(next(gen))\nprint(next(gen))\nprint(next(gen))\n\n# Generator expression (O(1) memory)\nsquares_gen = (x ** 2 for x in range(5))\nprint(\"Generator Expression Sum:\", sum(squares_gen))",
            "Generator Object: <generator object lesson_stream at 0x...>\nLesson #1: In-Depth Video & Exercise\nLesson #2: In-Depth Video & Exercise\nLesson #3: In-Depth Video & Exercise\nGenerator Expression Sum: 30",
            [
                "lesson_stream yields strings one at a time on next() calls.",
                "Generator expression (x ** 2 for x in ...) streams values lazily directly into sum()."
            ],
            [
                "Confusing `yield` with `return`: `return` terminates the function; `yield` pauses and preserves local state.",
                "Attempting to reuse or rewind a generator once exhausted; generators are one-way streams."
            ],
            [
                ("What exception is raised when calling `next()` on an exhausted generator?", "StopIteration."),
                ("How does a generator save memory compared to a list comprehension?", "Yields items one by one on-demand rather than allocating a full list in RAM."),
                ("What does `yield from iterable` do?", "Delegates sub-iteration to an inner generator or iterable.")
            ]
        ),
        format_lesson(
            "python",
            "Decorators introduction", 30,
            [
                "Understand first-class functions and closures in Python",
                "Write custom function decorators using the @decorator syntax",
                "Preserve function metadata using functools.wraps"
            ],
            "A **Decorator** is a callable that takes another function as an argument, extends or alters its behavior without modifying its source code, and returns a replacement function.\n- Relies on functions being **first-class citizens** and closures.\n- Applied using the `@decorator_name` syntax above the target function.\n- Standard pattern: use `functools.wraps` inside the decorator to preserve original function name and docstrings.",
            "import functools\ndef log_call(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        print(f\"Calling {func.__name__}\")\n        return func(*args, **kwargs)\n    return wrapper",
            "import functools\nimport time\n\ndef timer_decorator(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.perf_counter()\n        result = func(*args, **kwargs)\n        elapsed = (time.perf_counter() - start) * 1000\n        print(f\"[PERF] '{func.__name__}' executed in {elapsed:.3f} ms\")\n        return result\n    return wrapper\n\n@timer_decorator\ndef compute_data(n):\n    return sum(i * i for i in range(n))\n\nres = compute_data(50000)\nprint(f\"Result: {res}\")",
            "[PERF] 'compute_data' executed in ... ms\nResult: 41665416675000",
            [
                "timer_decorator wraps compute_data.",
                "Measures execution time transparently and logs performance diagnostics.",
                "functools.wraps preserves function name and signature."
            ],
            [
                "Omitting `@functools.wraps(func)`, which causes the decorated function's `__name__` to become `'wrapper'`.",
                "Forgetting `*args, **kwargs` in the inner wrapper, preventing the decorator from accepting arbitrary parameters."
            ],
            [
                ("How do you write a decorator that accepts arguments (e.g. `@retry(attempts=3)`)?", "Add an outer factory function that returns the decorator."),
                ("Can multiple decorators be stacked on a single function?", "Yes, they are applied from bottom to top: `@dec1 @dec2 def f():` evaluates as `dec1(dec2(f))`."),
                ("What is a class decorator?", "A decorator that wraps an entire class definition to modify or register it.")
            ]
        ),
        format_lesson(
            "python",
            "Date and time", 25,
            [
                "Work with dates and times using the standard datetime module",
                "Perform date arithmetic using timedelta",
                "Parse and format dates using strftime and strptime"
            ],
            "The `datetime` module provides classes for date and time manipulation:\n- `date`: Year, month, day.\n- `time`: Hour, minute, second, microsecond.\n- `datetime`: Combines date and time.\n- `timedelta`: Duration representing difference between dates.\n- **Formatting**: `dt.strftime(format_code)` (converts datetime to string).\n- **Parsing**: `datetime.strptime(date_string, format_code)` (converts string to datetime).\n- Timezones: Use `timezone.utc` for timezone-aware timestamps.",
            "from datetime import datetime, timedelta, timezone\nnow = datetime.now(timezone.utc)\ndeadline = now + timedelta(days=14)\nformatted = now.strftime(\"%Y-%m-%d %H:%M:%S\")",
            "from datetime import datetime, date, timedelta\n\nstart_date = date(2026, 1, 15)\nduration = timedelta(weeks=12)\nprojected_finish = start_date + duration\n\nprint(f\"Course Start    : {start_date}\")\nprint(f\"Projected Finish: {projected_finish}\")\nprint(f\"Total Days      : {duration.days} days\")\n\n# Parsing date string\ninput_str = \"2026-10-14 12:00:00\"\nparsed_dt = datetime.strptime(input_str, \"%Y-%m-%d %H:%M:%S\")\nprint(f\"Parsed Datetime : {parsed_dt.strftime('%B %d, %Y at %I:%M %p')}\")",
            "Course Start    : 2026-01-15\nProjected Finish: 2026-04-09\nTotal Days      : 84 days\nParsed Datetime : October 14, 2026 at 12:00 PM",
            [
                "timedelta computes course end date accurately.",
                "strptime parses string into structured datetime.",
                "strftime formats date in human-readable prose."
            ],
            [
                "Mixing naive datetimes (no timezone) with timezone-aware datetimes, raising `TypeError: can't compare offset-naive and offset-aware datetimes`.",
                "Confusing `%m` (month as number 01-12) with `%M` (minute 00-59)."
            ],
            [
                ("What does the 'p' in strptime stand for?", "Parse time from string (string parse time)."),
                ("What does the 'f' in strftime stand for?", "Format time to string (string format time)."),
                ("What is a timezone-aware datetime in Python?", "A datetime object with a non-null `tzinfo` attribute.")
            ]
        ),
        format_lesson(
            "python",
            "Regular expressions", 25,
            [
                "Match patterns in text using the standard re module",
                "Apply raw string literals (r'...') to avoid regex escape collisions",
                "Extract tokens using re.search, re.match, and re.findall"
            ],
            "**Regular Expressions (regex)** provide powerful pattern-matching capabilities via the `re` module:\n- **Raw Strings**: Always use raw strings `r\"pattern\"` so backslashes are not eaten by Python string escaping.\n- **Metacharacters**: `.` (any char), `^` (start), `$` (end), `*` (0+), `+` (1+), `?` (0 or 1), `\\d` (digit), `\\w` (alphanumeric).\n- **Functions**:\n  - `re.search(pat, text)`: Finds first match anywhere in string.\n  - `re.findall(pat, text)`: Returns all non-overlapping matches as a list.\n  - `re.sub(pat, repl, text)`: Replaces occurrences.",
            "import re\nmatch = re.search(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', email)\nclean = re.sub(r'\\s+', ' ', text)",
            "import re\n\nsample_text = \"Contact admin@learnhub.com or support@learnhub.org for assistance.\"\nemail_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+'\n\nfound_emails = re.findall(email_pattern, sample_text)\nprint(f\"Extracted emails: {found_emails}\")\n\nphone_input = \"User verification code: 849201\"\ncode_match = re.search(r'code:\\s*(\\d{6})', phone_input)\nif code_match:\n    print(f\"Security code extracted: {code_match.group(1)}\")",
            "Extracted emails: ['admin@learnhub.com', 'support@learnhub.org']\nSecurity code extracted: 849201",
            [
                "re.findall extracts all matching email addresses.",
                "re.search with capture group (\\d{6}) isolates the 6-digit verification code."
            ],
            [
                "Omitting the `r` prefix in regex patterns, causing backslash escape errors.",
                "Using `re.match` when `re.search` is intended (`re.match` checks strictly from the very beginning of the string)."
            ],
            [
                ("What does `re.compile(pattern)` do?", "Compiles a regex pattern into a reusable RegexObject for faster repeated matches."),
                ("What is the difference between greedy and non-greedy matching in regex?", "Greedy (`*`, `+`) matches as much as possible; non-greedy (`*?`, `+?`) matches as little as possible."),
                ("How do you perform a case-insensitive regex search in Python?", "Pass the `re.IGNORECASE` (or `re.I`) flag.")
            ]
        ),
        format_lesson(
            "python",
            "Logging and debugging", 20,
            [
                "Replace print statements with structured logging using the logging module",
                "Configure logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
                "Inspect tracebacks and debug interactively with breakpoint() and pdb"
            ],
            "Production systems use structured **logging** rather than raw print calls:\n- **Levels**: `DEBUG` (diagnostic) -> `INFO` (routine events) -> `WARNING` (unexpected event) -> `ERROR` (failure) -> `CRITICAL` (fatal crash).\n- Log messages include timestamps, module names, and severity levels.\n- **Interactive Debugging**: Python 3.7+ includes built-in `breakpoint()`, which pauses execution and drops into the interactive `pdb` debugger.",
            "import logging\nlogging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')\nlogging.info(\"Application service started\")",
            "import logging\n\n# Configure standard logger\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    datefmt=\"%H:%M:%S\"\n)\nlogger = logging.getLogger(\"LearnHubService\")\n\nlogger.info(\"Course service initialized.\")\nlogger.warning(\"Student enrollment capacity reaching 90% threshold.\")\n\ntry:\n    res = 10 / 0\nexcept ZeroDivisionError:\n    logger.error(\"Arithmetic computation failed!\", exc_info=False)",
            "12:00:00 [INFO] LearnHubService: Course service initialized.\n12:00:00 [WARNING] LearnHubService: Student enrollment capacity reaching 90% threshold.\n12:00:00 [ERROR] LearnHubService: Arithmetic computation failed!",
            [
                "Configures structured logging format with timestamp and severity.",
                "Logs messages across INFO, WARNING, and ERROR tiers."
            ],
            [
                "Using `print()` for production auditing; print cannot be redirected to rotating log files or filtered by severity levels.",
                "Passing passwords or sensitive credentials into logging statements."
            ],
            [
                ("What built-in function triggers an interactive pdb debugging session in Python 3.7+?", "`breakpoint()`."),
                ("What does `logger.exception(\"Message\")` do inside an except block?", "Logs an ERROR level message and automatically attaches the full exception traceback."),
                ("How do you configure log output to write to a rotating file on disk?", "Use `logging.handlers.RotatingFileHandler`.")
            ]
        )
    ]
    return {
        "title": "Module 6 - Exceptions, Files, and Useful Standard Libraries",
        "description": "Build robust programs that process data and recover from expected errors.",
        "sequenceOrder": 6,
        "lessons": lessons
    }

print("Python modules 5 & 6 ready.")
