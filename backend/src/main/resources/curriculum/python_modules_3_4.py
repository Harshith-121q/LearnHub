from formatter import format_lesson

def get_python_module_3():
    lessons = [
        format_lesson(
            "python",
            "Lists", 25,
            [
                "Create, index, and slice dynamically sized mutable lists",
                "Manipulate elements using append, extend, insert, remove, pop, and sort",
                "Understand list memory representation and O(1) amortized appending"
            ],
            "A **List** in Python is an ordered, mutable sequence of heterogeneous objects (`[item1, item2, ...]`).\n- Indexed from `0` to `len - 1` with negative indexing `-1` from the end.\n- **Methods**:\n  - `append(x)`: Adds item x to the end ($O(1)$ amortized).\n  - `extend(iterable)`: Appends all items from iterable.\n  - `insert(i, x)`: Inserts item x at index i ($O(n)$).\n  - `remove(x)`: Removes first occurrence of value x.\n  - `pop(i)`: Removes and returns item at index i (defaults to end).\n  - `sort()`: In-place Timsort ($O(n \\log n)$).",
            "fruits = [\"apple\", \"banana\"]\nfruits.append(\"cherry\")\nfruits.insert(1, \"blueberry\")\nlast = fruits.pop() # Removes \"cherry\"",
            "courses = [\"Java\", \"Python\", \"React\"]\ncourses.append(\"Spring Boot\")\ncourses.insert(1, \"Data Structures\")\n\nprint(f\"Courses after insertion: {courses}\")\nremoved = courses.pop(2) # Removes item at index 2\nprint(f\"Popped course: {removed}\")\n\ncourses.sort()\nprint(f\"Alphabetically sorted: {courses}\")",
            "Courses after insertion: ['Java', 'Data Structures', 'Python', 'React', 'Spring Boot']\nPopped course: Python\nAlphabetically sorted: ['Data Structures', 'Java', 'React', 'Spring Boot']",
            [
                "courses list is dynamically resized.",
                "insert(1, ...) shifts subsequent elements right.",
                "pop(2) extracts and returns the element at index 2.",
                "sort() arranges elements alphabetically in-place."
            ],
            [
                "Confusing `append()` with `extend()`: `list.append([1, 2])` nests a list inside a list, whereas `extend([1, 2])` adds elements individually.",
                "Calling `courses = courses.sort()`: `sort()` modifies in-place and returns `None`, so reassigning overwrites your list with `None`."
            ],
            [
                ("What does list.sort() return?", "None (modifies in-place)."),
                ("What is the difference between `del list[0]` and `list.remove(val)`?", "del deletes by index; remove searches and deletes by value."),
                ("How does Python list implement dynamic growth under the hood?", "CPython over-allocates internal arrays to provide O(1) amortized append.")
            ]
        ),
        format_lesson(
            "python",
            "Tuples", 20,
            [
                "Create and unpack immutable tuples",
                "Define single-element tuples using the trailing comma syntax",
                "Select tuples for fixed records, dictionary keys, and performance gains"
            ],
            "A **Tuple** is an ordered, **immutable** sequence of objects (`(item1, item2)`).\n- Once created, elements cannot be added, removed, or replaced.\n- **Tuple Unpacking**: `name, score = (\"Alex\", 95)`.\n- Single-element tuple syntax requires a trailing comma: `single = (42,)` (without the comma, `(42)` is just parenthesized integer 42).\n- Tuples have less memory overhead than lists and can be used as dictionary keys because they are hashable (provided their contents are hashable).",
            "point = (10, 20)\nx, y = point # Unpacking\nsingle_item = (100,) # Trailing comma required!",
            "student_record = (\"Alex Morgan\", 10452, \"Computer Science\")\nname, student_id, major = student_record # Unpacking\n\nprint(f\"Student : {name}\")\nprint(f\"ID      : {student_id}\")\nprint(f\"Major   : {major}\")\n\n# Tuples as dict keys\ngrid_scores = {(0, 0): 100, (0, 1): 85}\nprint(f\"Coordinate (0, 0) score: {grid_scores[(0, 0)]}\")",
            "Student : Alex Morgan\nID      : 10452\nMajor   : Computer Science\nCoordinate (0, 0) score: 100",
            [
                "student_record encapsulates a multi-field record immutably.",
                "Tuple unpacking assigns elements to distinct variables.",
                "Demonstrates immutable tuple used as a hashable dictionary key."
            ],
            [
                "Attempting to modify a tuple (`point[0] = 5`), raising `TypeError: 'tuple' object does not support item assignment`.",
                "Writing `t = (5)` and wondering why `type(t)` is `int` rather than `tuple` (forgot comma)."
            ],
            [
                ("Why can a tuple be used as a dictionary key while a list cannot?", "Tuples are immutable and hashable; lists are mutable and unhashable."),
                ("What is extended tuple unpacking using `*`?", "`first, *middle, last = [1, 2, 3, 4, 5]`."),
                ("What is a namedtuple in Python?", "A tuple subclass in collections where fields can be accessed by attribute name as well as index.")
            ]
        ),
        format_lesson(
            "python",
            "Sets", 20,
            [
                "Enforce uniqueness using mutable sets and frozensets",
                "Perform set operations: union (|), intersection (&), difference (-), and symmetric difference (^)",
                "Execute O(1) membership lookups (item in my_set)"
            ],
            "A **Set** is an unordered collection of unique, hashable objects (`{item1, item2}`).\n- Duplicates are automatically discarded.\n- **Membership Testing**: `x in my_set` runs in **$O(1)$ constant time** using a hash table (unlike lists which require $O(n)$).\n- **Mathematical Set Operations**:\n  - Union `A | B`: Elements in either A or B.\n  - Intersection `A & B`: Elements in both A and B.\n  - Difference `A - B`: Elements in A but not B.\n  - Symmetric Difference `A ^ B`: Elements in A or B, but not both.",
            "enrolled = {\"Alex\", \"Sarah\"}\nenrolled.add(\"David\")\nenrolled.add(\"Alex\") # Duplicate ignored",
            "java_students = {\"Alex\", \"Sarah\", \"John\", \"Emily\"}\npython_students = {\"Sarah\", \"David\", \"Alex\", \"Michael\"}\n\nboth_tracks = java_students & python_students       # Intersection\neither_track = java_students | python_students      # Union\nonly_java = java_students - python_students         # Difference\n\nprint(f\"Enrolled in both: {both_tracks}\")\nprint(f\"Total unique students: {len(either_track)}\")\nprint(f\"Exclusively in Java: {only_java}\")",
            "Enrolled in both: {'Alex', 'Sarah'}\nTotal unique students: 6\nExclusively in Java: {'Emily', 'John'}",
            [
                "Sets discard duplicate names automatically.",
                "& extracts common students {'Alex', 'Sarah'}.",
                "- isolates students taking only the Java track."
            ],
            [
                "Creating an empty set with `{}`: `{}` creates an empty dictionary; use `set()` to create an empty set.",
                "Attempting to add unhashable mutable objects (like lists or dicts) into a set."
            ],
            [
                ("How do you create an empty set in Python?", "`empty_set = set()` (not `{}`)."),
                ("What is a frozenset?", "An immutable, hashable version of a set that can be used as a dictionary key or placed inside other sets."),
                ("What is the time complexity of testing `item in my_set`?", "O(1) average time.")
            ]
        ),
        format_lesson(
            "python",
            "Dictionaries", 25,
            [
                "Store key-value mappings using dictionaries (dict)",
                "Access and update data safely using get(), setdefault(), and update()",
                "Iterate over keys(), values(), and items() cleanly"
            ],
            "A **Dictionary** (`dict`) is an associative mapping of unique keys to values (`{key: value}`). In modern Python (3.7+), dictionaries preserve insertion order.\n- Keys must be hashable and immutable (strings, numbers, tuples).\n- **Access**:\n  - `d[key]`: Raises `KeyError` if key is missing.\n  - `d.get(key, default)`: Safely returns `default` (or `None`) if key is absent.\n- **Iteration**: `for k, v in d.items(): ...`.",
            "user = {\"username\": \"alex_m\", \"role\": \"STUDENT\"}\nrole = user.get(\"role\", \"GUEST\") # Safe lookup\nuser[\"active\"] = True             # Add/update key",
            "course_info = {\n    \"title\": \"Python Programming Masterclass\",\n    \"modules\": 8,\n    \"duration_hours\": 50,\n    \"published\": True\n}\n\n# Safe access with fallback\ninstructor = course_info.get(\"instructor\", \"Sarah Connor (Assigned)\")\nprint(f\"Course: {course_info['title']}\")\nprint(f\"Lead Faculty: {instructor}\")\n\nprint(\"\\nFull Specification Attributes:\")\nfor key, val in course_info.items():\n    print(f\"- {key:15}: {val}\")",
            "Course: Python Programming Masterclass\nLead Faculty: Sarah Connor (Assigned)\n\nFull Specification Attributes:\n- title          : Python Programming Masterclass\n- modules        : 8\n- duration_hours : 50\n- published      : True",
            [
                "course_info stores structured metadata.",
                "get() provides safe fallback without throwing KeyError.",
                "items() unpacks keys and values in iteration."
            ],
            [
                "Accessing `d[missing_key]` directly, crashing with `KeyError`.",
                "Using mutable types (like lists) as dictionary keys."
            ],
            [
                ("How does dict.setdefault(key, default) work?", "Returns the value if key exists; if not, inserts key with default and returns it."),
                ("How do you merge two dictionaries in Python 3.9+?", "Using the union operator: `merged = dict1 | dict2`."),
                ("What is a defaultdict in the collections module?", "A dictionary that automatically initializes missing keys with a default factory function.")
            ]
        ),
        format_lesson(
            "python",
            "Slicing", 20,
            [
                "Apply sequence slicing: [start:stop:step]",
                "Extract sublists and substrings using positive and negative indices",
                "Reverse sequences and create shallow copies using slice idioms"
            ],
            "Slicing extracts portions of any sequence (strings, lists, tuples) using the syntax `sequence[start:stop:step]`:\n- `start`: Index to begin (inclusive, defaults to 0).\n- `stop`: Index to end (exclusive, defaults to len).\n- `step`: Stride interval (defaults to 1; negative step reverses traversal).\n- Slicing never raises `IndexOutOfBoundsException`; out-of-range bounds are automatically clamped to the sequence boundaries.",
            "# Slicing idioms\nfirst_three = items[:3]\nlast_two = items[-2:]\nshallow_copy = items[:]\nreversed_seq = items[::-1]",
            "modules = [\"M1\", \"M2\", \"M3\", \"M4\", \"M5\", \"M6\", \"M7\", \"M8\"]\n\nprint(\"First 3 modules  :\", modules[:3])\nprint(\"Middle (M3 to M5):\", modules[2:5])\nprint(\"Last 2 modules   :\", modules[-2:])\nprint(\"Every second one :\", modules[::2])\nprint(\"Reversed sequence:\", modules[::-1])",
            "First 3 modules  : ['M1', 'M2', 'M3']\nMiddle (M3 to M5): ['M3', 'M4', 'M5']\nLast 2 modules   : ['M7', 'M8']\nEvery second one : ['M1', 'M3', 'M5', 'M7']\nReversed sequence: ['M8', 'M7', 'M6', 'M5', 'M4', 'M3', 'M2', 'M1']",
            [
                "modules[:3] takes elements from index 0 to 2.",
                "modules[2:5] extracts indices 2, 3, 4.",
                "modules[::-1] cleanly reverses the entire list."
            ],
            [
                "Thinking `modules[2:5]` includes index 5; the stop index is always exclusive.",
                "Modifying elements in a shallow copy slice (`items[:]`) expecting nested mutable objects to be isolated."
            ],
            [
                ("How do you slice the last 3 items of any sequence?", "`seq[-3:]`."),
                ("What does the slice step `[::-1]` do?", "Reverses the sequence from end to beginning."),
                ("Does list slicing create a copy or a view in Python?", "Standard list slicing creates a new shallow copy of the sublist.")
            ]
        ),
        format_lesson(
            "python",
            "List comprehensions", 25,
            [
                "Transform and filter data concisely using list comprehensions",
                "Compare readability and performance against traditional for loops",
                "Avoid overly complex nested comprehensions"
            ],
            "A **List Comprehension** provides a concise, declarative syntax to generate a new list from an existing iterable:\n`[expression for item in iterable if condition]`\n- Combines mapping (transformation) and filtering into a single expressive line.\n- Executed in C speed in CPython, making it faster than manual `.append()` inside a standard for loop.",
            "# Traditional loop:\nsquares = []\nfor x in range(10):\n    if x % 2 == 0: squares.append(x ** 2)\n\n# List comprehension:\nsquares = [x ** 2 for x in range(10) if x % 2 == 0]",
            "raw_scores = [45, 88, 92, 59, 73, 95]\n\n# Filter passing scores and format\npassing_scores = [s for s in raw_scores if s >= 70]\ncurved_scores = [min(100, s + 5) for s in raw_scores]\n\nprint(f\"Raw Scores    : {raw_scores}\")\nprint(f\"Passing (>=70): {passing_scores}\")\nprint(f\"Curved (+5)   : {curved_scores}\")",
            "Raw Scores    : [45, 88, 92, 59, 73, 95]\nPassing (>=70): [88, 92, 73, 95]\nCurved (+5)   : [50, 93, 97, 64, 78, 100]",
            [
                "passing_scores filters out scores < 70.",
                "curved_scores transforms every score by adding 5, clamped at 100."
            ],
            [
                "Writing multi-line nested comprehensions that sacrifice readability (if it exceeds 1-2 lines, write a regular loop).",
                "Using list comprehension solely for side-effects (e.g. `[print(x) for x in items]`); use a standard for loop instead."
            ],
            [
                ("How does an if-else expression work inside a list comprehension?", "Placed before the for: `[x if cond else y for x in items]`."),
                ("Why are list comprehensions faster than equivalent for loops with append()?", "They avoid bytecode method lookup overhead for the `.append` function in every cycle."),
                ("What is the difference between a list comprehension and a generator expression?", "List comprehension uses `[...]` and produces entire list in memory; generator uses `(...)` and yields lazily.")
            ]
        ),
        format_lesson(
            "python",
            "Dictionary and set comprehensions", 20,
            [
                "Construct dictionaries concisely using {k_expr: v_expr for item in iterable}",
                "Create unique filtered sets using {expr for item in iterable}",
                "Invert key-value mappings and filter dictionaries"
            ],
            "Similar to list comprehensions, Python provides comprehensions for sets and dictionaries:\n- **Set Comprehension**: `{expression for item in iterable if condition}` (automatically deduplicates).\n- **Dictionary Comprehension**: `{key_expr: value_expr for item in iterable if condition}` (creates key-value associations).",
            "# Inverting a dictionary\noriginal = {\"Alex\": 101, \"Sarah\": 102}\ninverted = {val: key for key, val in original.items()}",
            "students = [\"alex\", \"sarah\", \"david\", \"alex\", \"emily\"]\n\n# Set comprehension (unique title-cased names)\nunique_names = {s.title() for s in students}\nprint(f\"Unique Names: {unique_names}\")\n\n# Dict comprehension (name -> length)\nname_lengths = {name: len(name) for name in unique_names}\nprint(f\"Name Lengths Mapping: {name_lengths}\")",
            "Unique Names: {'David', 'Emily', 'Sarah', 'Alex'}\nName Lengths Mapping: {'David': 5, 'Emily': 5, 'Sarah': 5, 'Alex': 4}",
            [
                "Set comprehension eliminates duplicate 'alex' and title-cases values.",
                "Dict comprehension maps each unique name to its character length."
            ],
            [
                "Inverting a dictionary with duplicate values, which silently overwrites collision keys.",
                "Confusing set comprehensions `{x for x in ...}` with dict comprehensions `{k: v for ...}`."
            ],
            [
                ("How do you filter keys from a dictionary using a comprehension?", "`{k: v for k, v in d.items() if k.startswith('A')}`."),
                ("What happens if a dict comprehension produces duplicate keys?", "Subsequent assignments overwrite previous values for that key."),
                ("Can dictionary comprehensions iterate over multiple iterables simultaneously?", "Yes, using nested `for` clauses or `zip()`.")
            ]
        ),
        format_lesson(
            "python",
            "Built-in functions", 25,
            [
                "Master core Python built-ins: len, sum, min, max, and sorted",
                "Evaluate iterables using any() and all() predicates",
                "Apply key functions for custom sorting criteria"
            ],
            "Python includes powerful built-in functions that operate across all iterable types:\n- `len(seq)`: Length ($O(1)$ on built-in sequences).\n- `sum(iterable, start=0)`: Sums elements.\n- `min(iterable, key=...)` / `max(iterable, key=...)`: Finds extrema.\n- `sorted(iterable, key=..., reverse=...)`: Returns a new sorted list without mutating the original.\n- `all(iterable)`: True if ALL elements are truthy.\n- `any(iterable)`: True if AT LEAST ONE element is truthy.",
            "# Sorting by custom criteria\ncourses = [\"Go\", \"Python\", \"Java\"]\nsorted_by_len = sorted(courses, key=len) # ['Go', 'Java', 'Python']",
            "scores = [85, 92, 78, 95, 62]\n\nprint(f\"Total items : {len(scores)}\")\nprint(f\"Sum of marks: {sum(scores)}\")\nprint(f\"Class Range : Min={min(scores)}, Max={max(scores)}\")\n\nall_passed = all(s >= 60 for s in scores)\nany_distinction = any(s >= 90 for s in scores)\n\nprint(f\"All students passed (>=60)? {all_passed}\")\nprint(f\"Any distinctions (>=90)?   {any_distinction}\")",
            "Total items : 5\nSum of marks: 412\nClass Range : Min=62, Max=95\nAll students passed (>=60)? True\nAny distinctions (>=90)?   True",
            [
                "min and max compute extrema.",
                "all() short-circuits to verify that every student met the passing threshold.",
                "any() checks if distinction was achieved by at least one student."
            ],
            [
                "Calling `sum()` on non-numeric collections (e.g. attempting to sum strings; use `''.join()` instead).",
                "Shadowing built-in function names by creating variables named `min`, `max`, `sum`, or `list`."
            ],
            [
                ("How does sorted(items) differ from items.sort()?", "sorted() works on any iterable and returns a new list; .sort() is a method exclusively on lists modifying in-place."),
                ("What does all([]) return on an empty iterable?", "True (vacuous truth)."),
                ("What does any([]) return on an empty iterable?", "False.")
            ]
        ),
        format_lesson(
            "python",
            "Mutability and copying", 25,
            [
                "Distinguish mutable objects (list, dict, set) from immutable objects (int, str, tuple)",
                "Identify reference aliasing bugs and unintended side-effects",
                "Perform shallow copies (copy) and deep copies (deepcopy)"
            ],
            "Understanding Python's memory model is essential:\n- **Immutable Objects**: `int`, `float`, `str`, `tuple`, `frozenset`, `bool`. Once created, their contents cannot change. Operations return new objects.\n- **Mutable Objects**: `list`, `dict`, `set`, custom classes. Can be mutated in-place.\n- **Aliasing**: `b = a` does NOT create a copy; both variables point to the same object in memory.\n- **Shallow Copy (`copy.copy`)**: Copies the outer container, but child elements remain references to original objects.\n- **Deep Copy (`copy.deepcopy`)**: Recursively copies the container and all nested objects.",
            "import copy\nshallow = original.copy()        # Shallow copy\ndeep = copy.deepcopy(original)   # Fully isolated deep copy",
            "import copy\n\noriginal = [[1, 2], [3, 4]]\nshallow = list(original)         # Shallow copy\ndeep = copy.deepcopy(original)   # Deep copy\n\noriginal[0][0] = 999\n\nprint(f\"Original : {original}\")\nprint(f\"Shallow  : {shallow} (Inner list altered!)\")\nprint(f\"Deep Copy: {deep} (Completely isolated)\")",
            "Original : [[999, 2], [3, 4]]\nShallow  : [[999, 2], [3, 4]] (Inner list altered!)\nDeep Copy: [[1, 2], [3, 4]] (Completely isolated)",
            [
                "original[0][0] = 999 mutates the shared nested list.",
                "shallow reflects the mutation because it references the same inner list.",
                "deep is unaffected because deepcopy duplicated the inner objects recursively."
            ],
            [
                "Creating multi-dimensional lists via `[[0] * 3] * 3`, which creates 3 references to the EXACT SAME row list.",
                "Using mutable objects (e.g. `def func(items=[]):`) as default argument values in functions."
            ],
            [
                ("Why is `def func(data=[])` considered a famous Python trap?", "The default list is instantiated once at function definition, retaining mutations across subsequent calls."),
                ("How do you correctly define an optional list parameter in a function?", "Use `def func(data=None): if data is None: data = []`."),
                ("What does the `is` operator test compared to `==`?", "`is` tests whether two references point to the exact same object in memory; `==` tests value equality.")
            ]
        ),
        format_lesson(
            "python",
            "Data structure practice", 30,
            [
                "Solve real-world aggregation and frequency counting problems",
                "Group and partition student course records",
                "Select optimal data structures for speed and clarity"
            ],
            "This capstone lesson applies Module 3 data structures to realistic engineering problems:\n1. Frequency Counting with `collections.Counter` and standard dicts.\n2. Deduplicating while maintaining order using `dict.fromkeys()`.\n3. Grouping items by category using `collections.defaultdict`.\n4. Finding common elements across sets.",
            "from collections import Counter, defaultdict\ncounts = Counter(words)\ngroups = defaultdict(list)",
            "from collections import Counter, defaultdict\n\n# 1. Frequency counting\nenrollment_events = [\"Python\", \"Java\", \"Python\", \"Go\", \"Python\", \"Java\", \"React\"]\ncounter = Counter(enrollment_events)\nprint(f\"Track Frequencies: {dict(counter)}\")\nprint(f\"Top Course: {counter.most_common(1)}\")\n\n# 2. Grouping by difficulty\ncourses = [\n    (\"Python Basics\", \"Beginner\"),\n    (\"Java Core\", \"Beginner\"),\n    (\"Data Structures\", \"Intermediate\"),\n    (\"Concurrency in Python\", \"Intermediate\"),\n    (\"Distributed Systems\", \"Advanced\")\n]\n\ncurriculum_by_tier = defaultdict(list)\nfor title, tier in courses:\n    curriculum_by_tier[tier].append(title)\n\nprint(\"\\nCurriculum Grouped by Difficulty:\")\nfor tier, titles in curriculum_by_tier.items():\n    print(f\"{tier:12}: {titles}\")",
            "Track Frequencies: {'Python': 3, 'Java': 2, 'Go': 1, 'React': 1}\nTop Course: [('Python', 3)]\n\nCurriculum Grouped by Difficulty:\nBeginner    : ['Python Basics', 'Java Core']\nIntermediate: ['Data Structures', 'Concurrency in Python']\nAdvanced    : ['Distributed Systems']",
            [
                "Counter computes frequency counts in O(n) time.",
                "defaultdict(list) groups courses by difficulty tier cleanly without manual key checks."
            ],
            [
                "Manually writing boilerplate `if key not in d: d[key] = []` when `defaultdict(list)` handles it cleanly.",
                "Using lists for repeated lookups (`if item in my_list:`) instead of converting to a `set` for O(1) performance."
            ],
            [
                ("How does Counter.most_common(n) find top elements efficiently?", "Uses a heap queue (heapq.nlargest) running in O(N log k) time."),
                ("How do you deduplicate a list while preserving original order in Python 3.7+?", "`list(dict.fromkeys(my_list))`."),
                ("What is the time complexity of set intersection across sets of size N and M?", "O(min(N, M)).")
            ]
        )
    ]
    return {
        "title": "Module 3 - Python Data Structures",
        "description": "Choose and use the correct built-in data structure.",
        "sequenceOrder": 3,
        "lessons": lessons
    }

def get_python_module_4():
    lessons = [
        format_lesson(
            "python",
            "Defining functions", 20,
            [
                "Define modular functions using the def keyword",
                "Document function behavior and arguments using docstrings",
                "Understand execution flow and parameter passing"
            ],
            "Functions are reusable blocks of code that take inputs, perform operations, and return results. In Python:\n- Declared using the `def` keyword.\n- Indented body executes when the function is invoked.\n- Documentation strings (**docstrings**) directly follow the function header inside triple quotes `\"\"\"` and are accessible via `help(func)` or `func.__doc__`.\n- If a function finishes without an explicit `return` statement, it implicitly returns `None`.",
            "def calculate_area(width: float, height: float) -> float:\n    \"\"\"Calculates rectangle area.\"\"\"\n    return width * height",
            "def calculate_completion(completed: int, total: int) -> float:\n    \"\"\"Calculates progress percentage accurately from 0.0 to 100.0.\"\"\"\n    if total <= 0:\n        return 0.0\n    return round((completed / total) * 100.0, 1)\n\nprog = calculate_completion(15, 20)\nprint(f\"Computed Progress: {prog}%\")\nprint(f\"Function Docstring: {calculate_completion.__doc__}\")",
            "Computed Progress: 75.0%\nFunction Docstring: Calculates progress percentage accurately from 0.0 to 100.0.",
            [
                "calculate_completion validates zero total before division.",
                "Type hints clarify expected parameter and return types.",
                "docstring provides inline documentation."
            ],
            [
                "Forgetting the colon `:` at the end of the `def` line.",
                "Assuming a function without a return statement returns 0; it returns `None`."
            ],
            [
                ("What do Python type annotations (e.g. def foo(x: int) -> str) do at runtime?", "They are metadata stored in __annotations__ and not enforced at runtime without static checkers like mypy."),
                ("How do you access the docstring of a function programmatically?", "Via `func.__doc__`."),
                ("Can functions in Python be passed as arguments to other functions?", "Yes, functions are first-class citizens in Python.")
            ]
        ),
        format_lesson(
            "python",
            "Parameters and arguments", 25,
            [
                "Differentiate positional arguments from keyword (named) arguments",
                "Define default parameter values safely",
                "Understand Python's pass-by-object-reference evaluation model"
            ],
            "Python supports flexible argument passing:\n- **Positional Arguments**: Bound according to position.\n- **Keyword Arguments**: Specified by name (`func(width=10, height=20)`), enabling calls in any order.\n- **Default Parameters**: Specified in definition (`def enroll(name, tier=\"Beginner\"):`). Callers can omit them.\nCrucial Rule: Positional arguments MUST appear before keyword arguments, and default parameters MUST appear after non-default parameters.",
            "def create_course(title, duration=50, published=True): ...\ncreate_course(\"Python\", published=False)",
            "def register_student(name, email, role=\"STUDENT\", send_welcome=True):\n    print(f\"Registering: {name} <{email}> [Role: {role}] (Email Notification: {send_welcome})\")\n\n# Positional\nregister_student(\"Alex Morgan\", \"alex@learnhub.com\")\n# Keyword\nregister_student(email=\"sarah@learnhub.com\", name=\"Sarah Connor\", role=\"INSTRUCTOR\")",
            "Registering: Alex Morgan <alex@learnhub.com> [Role: STUDENT] (Email Notification: True)\nRegistering: Sarah Connor <sarah@learnhub.com> [Role: INSTRUCTOR] (Email Notification: True)",
            [
                "register_student uses default role='STUDENT' and send_welcome=True.",
                "Keyword arguments allow passing parameters in any order."
            ],
            [
                "Using a mutable object (like a list or dict) as a default parameter value (`def add(item, items=[]):`).",
                "Placing a positional argument after a keyword argument in a function call."
            ],
            [
                ("What are positional-only parameters in Python 3.8+?", "Parameters before `/` in function signature that cannot be passed by keyword name."),
                ("What are keyword-only parameters in Python?", "Parameters after `*` in function signature that must be passed by keyword name."),
                ("Why should default parameter values always be immutable (e.g. None)?", "To prevent state persistence across calls.")
            ]
        ),
        format_lesson(
            "python",
            "Return values", 20,
            [
                "Return single or multiple values from functions using tuple packing",
                "Leverage early returns (guard clauses) to reduce nesting",
                "Handle None return states gracefully"
            ],
            "In Python, functions terminate and pass data back to caller using the `return` statement:\n- Multiple return values: `return x, y, z` packs values into a tuple, which caller can unpack directly (`a, b, c = func()`).\n- Early Returns: Returning immediately when invalid inputs or edge cases are met flattens code and eliminates deeply nested `if-else` blocks.",
            "def get_min_max(numbers):\n    return min(numbers), max(numbers) # Returns tuple\nlow, high = get_min_max([10, 45, 2, 88])",
            "def analyze_scores(scores):\n    # Guard clause\n    if not scores:\n        return 0, 0.0, 0\n    return len(scores), sum(scores) / len(scores), max(scores)\n\ncount, avg, top = analyze_scores([88, 92, 79, 95])\nprint(f\"Processed {count} scores | Average: {avg:.1f} | Top: {top}\")",
            "Processed 4 scores | Average: 88.5 | Top: 95",
            [
                "analyze_scores guards against empty lists.",
                "Returns 3 values packed into a tuple and unpacked at caller."
            ],
            [
                "Expecting code after a `return` statement to execute (unreachable).",
                "Forgetting to capture multiple return values, ending up with a tuple instead of unpacked variables."
            ],
            [
                ("What data structure is actually returned when a function returns multiple comma-separated values?", "A tuple."),
                ("What does a function return if it executes to the end without hitting a return statement?", "None."),
                ("How do guard clauses enhance code readability?", "Handle edge cases at the top of the function and return early, keeping happy path code at zero indentation.")
            ]
        ),
        format_lesson(
            "python",
            "Variable-length arguments", 25,
            [
                "Accept arbitrary positional arguments using *args",
                "Accept arbitrary keyword arguments using **kwargs",
                "Unpack lists (*args) and dictionaries (**kwargs) into function calls"
            ],
            "Python enables functions to accept variable numbers of arguments:\n- `*args`: Collects extra positional arguments into a **tuple**.\n- `**kwargs`: Collects extra keyword arguments into a **dictionary**.\n- Argument Unpacking: Callers can unpack an existing list into positional arguments using `*list`, or unpack a dictionary into keyword arguments using `**dict`.",
            "def log_event(level, *args, **kwargs):\n    # args is a tuple, kwargs is a dict\n    pass",
            "def build_course_profile(title, *instructors, **metadata):\n    print(f\"Course: {title}\")\n    print(f\"Instructors: {list(instructors)}\")\n    print(\"Metadata Attributes:\")\n    for k, v in metadata.items():\n        print(f\"  {k}: {v}\")\n\nbuild_course_profile(\n    \"Python Masterclass\",\n    \"Sarah Connor\", \"Alex Morgan\",\n    difficulty=\"Beginner to Advanced\",\n    duration_hours=50,\n    status=\"PUBLISHED\"\n)",
            "Course: Python Masterclass\nInstructors: ['Sarah Connor', 'Alex Morgan']\nMetadata Attributes:\n  difficulty: Beginner to Advanced\n  duration_hours: 50\n  status: PUBLISHED",
            [
                "*instructors captures all positional names after title into a tuple.",
                "**metadata captures named flags into a dictionary."
            ],
            [
                "Putting `*args` after `**kwargs`; the order must strictly be: positional, `*args`, keyword, `**kwargs`.",
                "Passing arguments that collide with named parameters when unpacking dictionaries."
            ],
            [
                ("What data type is `args` inside a function defined with `*args`?", "Tuple."),
                ("What data type is `kwargs` inside a function defined with `**kwargs`?", "Dictionary."),
                ("How do you forward all incoming arguments from a wrapper function to an inner target?", "`target(*args, **kwargs)`.")
            ]
        ),
        format_lesson(
            "python",
            "Variable scope", 25,
            [
                "Understand Python's LEGB scope lookup rule (Local, Enclosing, Global, Built-in)",
                "Identify variable shadowing and UnboundLocalError",
                "Manage global and nonlocal keywords appropriately"
            ],
            "Python resolves variable names using the **LEGB Rule** in order:\n1. **L**ocal: Inside the current function.\n2. **E**nclosing: In any enclosing nested functions (closures).\n3. **G**lobal: At the top level of the current module file.\n4. **B**uilt-in: In Python's built-in namespace (`len`, `range`).\nRule: Modifying a global variable inside a function requires the `global` keyword. Modifying an enclosing variable requires `nonlocal`. Avoid global mutable state.",
            "# LEGB resolution demonstration\nglobal_counter = 0\ndef increment():\n    global global_counter\n    global_counter += 1",
            "platform_name = \"LearnHub Core\" # Global\n\ndef outer_service():\n    service_version = \"v2.1\" # Enclosing\n    \n    def inner_worker():\n        request_id = 1045 # Local\n        print(f\"Local     : {request_id}\")\n        print(f\"Enclosing : {service_version}\")\n        print(f\"Global    : {platform_name}\")\n        print(f\"Built-in  : {len('LearnHub')}\")\n        \n    inner_worker()\n\nouter_service()",
            "Local     : 1045\nEnclosing : v2.1\nGlobal    : LearnHub Core\nBuilt-in  : 8",
            [
                "Demonstrates the 4 tiers of the LEGB lookup hierarchy.",
                "inner_worker accesses local, enclosing, global, and built-in names seamlessly."
            ],
            [
                "Reading a global variable, and then assigning to it later in the same function without `global`, triggering `UnboundLocalError: local variable referenced before assignment`.",
                "Overusing the `global` keyword, creating hidden couplings between functions."
            ],
            [
                ("What causes UnboundLocalError in Python?", "Assigning to a variable inside a function marks it as local, so referencing it before that assignment fails."),
                ("What does the nonlocal keyword do?", "Declares that a variable refers to a previously bound variable in the nearest enclosing scope (excluding globals)."),
                ("Why should global mutable state be minimized in software architecture?", "Makes unit testing difficult and causes race conditions in multithreaded apps.")
            ]
        ),
        format_lesson(
            "python",
            "Lambda functions", 20,
            [
                "Write small, anonymous lambda functions",
                "Apply lambdas in higher-order functions (sorted, filter, map)",
                "Understand lambda limitations (single expression, no statements)"
            ],
            "A **Lambda Function** is a small, anonymous inline function defined with the `lambda` keyword:\n`lambda parameters: expression`\n- Can take any number of arguments, but can only have **one single expression**.\n- The expression is evaluated and automatically returned.\n- Best used as short transformation callbacks in functions like `sorted()`, `min()`, `max()`, and GUI callbacks.",
            "# Lambda syntax\nsquare = lambda x: x ** 2\n# Common use with sorting\nstudents.sort(key=lambda s: s['score'])",
            "courses = [\n    {\"title\": \"Python Masterclass\", \"hours\": 50, \"students\": 1200},\n    {\"title\": \"Java Masterclass\", \"hours\": 60, \"students\": 950},\n    {\"title\": \"React Fullstack\", \"hours\": 35, \"students\": 1500}\n]\n\n# Sort by popularity (students descending)\ncourses.sort(key=lambda c: c[\"students\"], reverse=True)\nprint(\"Courses Sorted by Students Descending:\")\nfor c in courses:\n    print(f\"- {c['title']:20}: {c['students']} students\")",
            "Courses Sorted by Students Descending:\n- React Fullstack     : 1500 students\n- Python Masterclass  : 1200 students\n- Java Masterclass    : 950 students",
            [
                "lambda c: c['students'] extracts the key for comparison.",
                "reverse=True orders from highest to lowest."
            ],
            [
                "Assigning lambda to a variable name (`my_func = lambda x: ...`); PEP 8 recommends using standard `def my_func(x):` instead.",
                "Attempting to put statements (like `return`, `assert`, or `pass`) inside a lambda."
            ],
            [
                ("Why can a lambda expression not contain statements like assignments or loops?", "Python syntax grammar restricts lambdas to a single syntactic expression."),
                ("How does operator.itemgetter compare to a lambda for dict key sorting?", "`itemgetter('students')` is faster and more readable than `lambda c: c['students']`."),
                ("Can a lambda function take multiple arguments?", "Yes: `lambda a, b: a + b`.")
            ]
        ),
        format_lesson(
            "python",
            "Modules and imports", 25,
            [
                "Import modules from Python's standard library and custom files",
                "Use import, from ... import, and import aliases (as)",
                "Understand module search path (sys.path) and avoid circular imports"
            ],
            "A **Module** is simply a Python file (`.py`) containing code, functions, and classes that can be reused across projects.\n- **Import Styles**:\n  - `import math`: Namespaced access (`math.sqrt(16)`).\n  - `from math import sqrt, pi`: Direct function access.\n  - `import numpy as np`: Module aliasing.\n- When importing, Python searches directories in `sys.path` (current directory, standard library, site-packages).\n- Modules are executed once when first imported and cached in `sys.modules`.",
            "import os\nfrom datetime import datetime, timezone\nimport json as serializer",
            "import math\nfrom datetime import date\n\nprint(f\"Pi value from math module: {math.pi:.5f}\")\nprint(f\"Square root of 144: {math.sqrt(144)}\")\n\ntoday = date.today()\nprint(f\"Current Date via datetime module: {today.isoformat()}\")",
            "Pi value from math module: 3.14159\nSquare root of 144: 12.0\nCurrent Date via datetime module: 2026-10-14",
            [
                "Imports standard library modules math and datetime.",
                "Accesses constants, functions, and classes cleanly."
            ],
            [
                "Using wildcard imports (`from math import *`), polluting the namespace and causing name collisions.",
                "Naming your local script the same as a standard library module (e.g. naming your file `math.py` or `random.py`), shadowing the standard module."
            ],
            [
                ("What is a circular import in Python and how do you resolve it?", "Two modules importing each other at top-level; resolve by refactoring shared code into a third module or importing inside functions."),
                ("What does `sys.path` contain?", "A list of directory strings where the Python interpreter searches for imported modules."),
                ("Why should wildcard `from module import *` be avoided?", "Makes it impossible for static analyzers and human reviewers to determine where names originate.")
            ]
        ),
        format_lesson(
            "python",
            "Packages", 20,
            [
                "Organize related modules into directories forming packages",
                "Understand the role of __init__.py in package initialization",
                "Apply relative imports (from . import sibling) within packages"
            ],
            "A **Package** is a directory holding multiple Python modules along with an `__init__.py` file.\n- In Python 3.3+, regular packages use `__init__.py` to mark package boundaries and specify exported symbols via `__all__`.\n- Enables clean hierarchical organization:\n  `learnhub/`\n  `  __init__.py`\n  `  auth/`\n  `  curriculum/`\n  `    course_service.py`\n- Relative imports: `from .models import Course` (within the same package).",
            "# Package structure:\n# learnhub/\n#   __init__.py\n#   services/\n#     __init__.py\n#     course_service.py",
            "import os\n\npackage_structure = \"\"\"learnhub_pkg/\n├── __init__.py          # Package initialization & public API exports\n├── curriculum/\n│   ├── __init__.py\n│   ├── java_track.py    # Java module and lesson definitions\n│   └── python_track.py  # Python module and lesson definitions\n└── analytics/\n    ├── __init__.py\n    └── progress.py      # Student progress calculation engine\"\"\"\n\nprint(\"Canonical Python Enterprise Package Layout:\")\nprint(package_structure)",
            "Canonical Python Enterprise Package Layout:\nlearnhub_pkg/\n├── __init__.py          # Package initialization & public API exports\n├── curriculum/\n│   ├── __init__.py\n│   ├── java_track.py    # Java module and lesson definitions\n│   └── python_track.py  # Python module and lesson definitions\n└── analytics/\n    ├── __init__.py\n    └── progress.py      # Student progress calculation engine",
            [
                "Deconstructs enterprise package structure matching LearnHub requirements.",
                "Highlights __init__.py initialization boundaries."
            ],
            [
                "Running relative imports (`from . import ...`) directly as standalone scripts instead of executing as a package (`python -m pkg.module`).",
                "Putting heavy, slow initialization code inside `__init__.py`."
            ],
            [
                ("What does `__all__` define inside an `__init__.py` file?", "A list of public string module names exported when `from package import *` is executed."),
                ("What is a Namespace Package in Python 3.3+?", "A package without an __init__.py that can span across multiple disconnected directory paths."),
                ("How do you run a module inside a package from the terminal?", "`python -m package_name.module_name`.")
            ]
        ),
        format_lesson(
            "python",
            "Virtual environments and pip", 20,
            [
                "Create isolated virtual environments using python -m venv .venv",
                "Activate and deactivate virtual environments across OS shells",
                "Install, freeze, and manage third-party dependencies using pip and requirements.txt"
            ],
            "A **Virtual Environment** is an isolated Python directory tree containing its own Python interpreter and independent set of third-party libraries.\n- Solves dependency conflicts (e.g. Project A requires Django 4.2; Project B requires Django 5.0).\n- **Workflow**:\n  1. Create: `python -m venv .venv`\n  2. Activate:\n     - Windows: `.venv\\Scripts\\activate`\n     - macOS/Linux: `source .venv/bin/activate`\n  3. Install: `pip install requests pytest`\n  4. Freeze: `pip freeze > requirements.txt`\n  5. Restore: `pip install -r requirements.txt`",
            "# Terminal commands:\npython -m venv .venv\n.venv\\Scripts\\activate\npip install requests\npip freeze > requirements.txt",
            "import sys\n\nis_in_venv = sys.prefix != sys.base_prefix\nprint(f\"Running inside Virtual Environment: {is_in_venv}\")\nprint(f\"Active Python Prefix: {sys.prefix}\")\nprint(f\"Base System Python  : {sys.base_prefix}\")",
            "Running inside Virtual Environment: False\nActive Python Prefix: C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\nBase System Python  : C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312",
            [
                "sys.prefix != sys.base_prefix programmatically verifies virtual environment isolation.",
                "Demonstrates environment inspection mechanics."
            ],
            [
                "Installing packages globally without activating a virtual environment, cluttering system Python.",
                "Committing the `.venv` directory to Git (always add `.venv/` to `.gitignore`)."
            ],
            [
                ("What should be placed in .gitignore regarding virtual environments?", "`.venv/`, `env/`, `__pycache__/`, `*.pyc`."),
                ("What does `pip freeze` do?", "Outputs installed packages and their exact pinned versions (e.g. `requests==2.31.0`)."),
                ("What is pyproject.toml in modern Python packaging?", "The modern PEP 518/621 standard file for configuring project build systems, dependencies, and tools.")
            ]
        ),
        format_lesson(
            "python",
            "Main guard", 20,
            [
                "Understand the special __name__ variable in Python modules",
                "Implement the if __name__ == '__main__': idiom",
                "Separate reusable library code from executable script entry points"
            ],
            "When the Python interpreter runs a source file:\n- If executed directly (e.g. `python app.py`), Python assigns the string `'__main__'` to the special variable `__name__`.\n- If the file is imported by another module (`import app`), Python assigns the module's actual file name (e.g. `'app'`) to `__name__`.\nThe **Main Guard** idiom `if __name__ == '__main__':` ensures that script execution code (CLI prompts, tests) only runs when the file is run directly, and NOT when imported by other modules.",
            "def calculate(x): return x * 2\n\nif __name__ == '__main__':\n    # Only executes when run directly!\n    print(calculate(10))",
            "def compute_track_hours(modules_count, hours_per_module=6):\n    \"\"\"Reusable calculation function.\"\"\"\n    return modules_count * hours_per_module\n\n# Main Guard\nif __name__ == '__main__':\n    print(\"File executed directly as a script.\")\n    print(f\"__name__ value: '{__name__}'\")\n    total = compute_track_hours(8)\n    print(f\"Total projected hours for 8 modules: {total}h\")",
            "File executed directly as a script.\n__name__ value: '__main__'\nTotal projected hours for 8 modules: 48h",
            [
                "compute_track_hours is available for import without triggering script execution.",
                "The main guard runs test output strictly when invoked directly."
            ],
            [
                "Placing top-level executable code without a main guard, causing tests or print statements to run whenever another module imports it.",
                "Misspelling `__name__` or `'__main__'` (e.g. single underscores `_name_`)."
            ],
            [
                ("What is the value of `__name__` inside a module named `utils.py` when imported by another file?", "'utils'."),
                ("Why is the main guard considered a universal Python best practice?", "Enables modules to serve dual roles as importable libraries and executable scripts."),
                ("How does the main guard facilitate unit testing?", "Allows test frameworks to import functions without running the script's main loop.")
            ]
        )
    ]
    return {
        "title": "Module 4 - Functions, Modules, and Environments",
        "description": "Write reusable code and organize it into maintainable projects.",
        "sequenceOrder": 4,
        "lessons": lessons
    }

print("Python modules 3 & 4 ready.")
