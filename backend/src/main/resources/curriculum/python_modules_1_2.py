from formatter import format_lesson

def get_python_module_1():
    lessons = [
        format_lesson(
            "python",
            "Introduction to Python", 20,
            [
                "Understand the design philosophy, origin, and high readability of Python",
                "Identify primary application domains (automation, data science, web development, AI)",
                "Evaluate interpreted execution versus compiled binaries"
            ],
            "Python is a high-level, interpreted, general-purpose programming language conceived by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability through significant whitespace and clear, expressive syntax ('Executable Pseudocode'). Today, Python powers backend web services (Django, FastAPI), data analysis (pandas, NumPy), machine learning (PyTorch, TensorFlow), system automation, and cloud infrastructure scripting. Its extensive standard library ('Batteries Included') makes it accessible yet immensely powerful.",
            "# Canonical Python structure\ndef main():\n    print(\"Hello, Python Ecosystem!\")\n\nif __name__ == '__main__':\n    main()",
            "def main():\n    platform_name = \"Python 3.12\"\n    primary_use = \"Web APIs, Automation, and Artificial Intelligence\"\n    print(f\"Platform: {platform_name}\")\n    print(f\"Deployment Focus: {primary_use}\")\n\nif __name__ == '__main__':\n    main()",
            "Platform: Python 3.12\nDeployment Focus: Web APIs, Automation, and Artificial Intelligence",
            [
                "The Python interpreter executes top-level script statements sequentially.",
                "f-strings (formatted string literals) provide elegant expression interpolation.",
                "The main function encapsulates execution logic cleanly."
            ],
            [
                "Mixing tabs and spaces for indentation, which causes TabError.",
                "Assuming Python is completely untyped; Python is dynamically typed but strongly typed (it will not automatically convert '5' + 5)."
            ],
            [
                ("What does the 'Zen of Python' (import this) advocate regarding code readability?", "Readability counts, simple is better than complex, explicit is better than implicit."),
                ("How does Python's interpreted nature differ from ahead-of-time compilation in Java or C++?", "Bytecode is compiled into .pyc files on-the-fly and interpreted by the CPython virtual machine."),
                ("Name three global enterprise frameworks built using Python.", "Django, FastAPI, Flask, PyTorch.")
            ]
        ),
        format_lesson(
            "python",
            "Installing Python", 20,
            [
                "Install a modern Python 3 interpreter on Windows, macOS, or Linux",
                "Verify terminal access via python --version and python3 --version",
                "Configure modern code editors (VS Code) and interactive REPL environments"
            ],
            "To write and execute Python programs, you need the Python 3 interpreter (CPython). During installation on Windows, ensure you check 'Add python.exe to PATH' so the interpreter is accessible from any terminal window. Python includes an interactive Read-Eval-Print Loop (REPL), where you can type code expressions and receive immediate evaluation.",
            "# Verify command-line installation\npython --version\n# or on macOS/Linux\npython3 --version\n\n# Launch interactive REPL\npython",
            "import sys\nimport platform\n\nprint(f\"Python Version: {platform.python_version()}\")\nprint(f\"Interpreter System: {platform.system()} ({platform.architecture()[0]})\")\nprint(f\"Executable Location: {sys.executable}\")",
            "Python Version: 3.12.0\nInterpreter System: Windows (64bit)\nExecutable Location: C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe",
            [
                "platform.python_version() queries the active runtime interpreter version.",
                "sys.executable confirms the exact filesystem path of the running Python binary."
            ],
            [
                "Forgetting to check 'Add python.exe to PATH' on Windows, resulting in 'python is not recognized' errors.",
                "Confusing legacy Python 2 (deprecated in 2020) with Python 3; always use Python 3."
            ],
            [
                ("How do you exit an interactive Python REPL session?", "Type `exit()` or press Ctrl+Z followed by Enter on Windows (Ctrl+D on Unix)."),
                ("What is CPython?", "The default, standard reference implementation of Python written in C."),
                ("What does the command `python -m pip install <package>` do?", "Executes the pip package manager module using the specific Python interpreter.")
            ]
        ),
        format_lesson(
            "python",
            "First Python program", 20,
            [
                "Create, save, and execute your first script (app.py)",
                "Understand the print() built-in function",
                "Trace how the Python interpreter reads and evaluates script files"
            ],
            "In Python, writing a first program requires none of the class boilerplate or static typing required by Java or C++. A single line of code is a fully valid, executable Python program:\n`print('Hello, World!')`\nWhen you run `python hello.py`, the interpreter reads the file top-to-bottom, compiles it into bytecode in memory, and executes each statement sequentially.",
            "# Save as hello.py and run via terminal: python hello.py\nprint('Hello, LearnHub Python Track!')",
            "greeting = \"Welcome to LearnHub Python Masterclass!\"\nversion = 3\nstatus = \"Ready\"\n\nprint(greeting)\nprint(f\"Tracking track version: {version} | Environment: {status}\")",
            "Welcome to LearnHub Python Masterclass!\nTracking track version: 3 | Environment: Ready",
            [
                "The variables are assigned dynamically without explicit type keywords.",
                "print() sends characters to standard output and automatically appends a newline."
            ],
            [
                "Using Python 2 print syntax (`print 'text'`) which is a syntax error in Python 3; Python 3 requires parentheses (`print('text')`).",
                "Running `python hello` without the `.py` extension in the terminal."
            ],
            [
                ("Why does Python not require a public class or main() method just to print a greeting?", "Python is a scripting language capable of top-level procedural execution."),
                ("What file extension is used for standard Python source files?", ".py"),
                ("What does the shebang line `#!/usr/bin/env python3` do in Unix scripts?", "Tells the shell which interpreter to use when executing the file directly as a script.")
            ]
        ),
        format_lesson(
            "python",
            "Python syntax and indentation", 20,
            [
                "Master indentation-based code blocks (off-side rule)",
                "Apply PEP 8 style conventions (4 spaces, snake_case)",
                "Use single-line and docstring comments effectively"
            ],
            "Unlike C, Java, or JavaScript which use curly braces `{}` to define blocks, Python uses **indentation** (the off-side rule). All statements within the same logical block MUST be indented by the exact same amount.\n- PEP 8 Standard: Use **4 spaces per indentation level** (never tabs).\n- Statements typically end at the end of the line (no semicolons required).\n- Comments begin with `#`.\n- Multi-line docstrings are enclosed in triple quotes `\"\"\"`.",
            "if condition:\n    # Indented by 4 spaces\n    statement_1\n    statement_2\n# Unindented statement (outside block)",
            "def evaluate_student(name, score):\n    \"\"\"Evaluates student score and prints status.\"\"\"\n    # 4 spaces indentation block\n    if score >= 70:\n        status = \"Passing\"\n        remark = \"Great progress!\"\n    else:\n        status = \"Needs Review\"\n        remark = \"Schedule tutoring.\"\n        \n    print(f\"Student: {name} | Status: {status} ({remark})\")\n\nevaluate_student(\"Alex Morgan\", 88)",
            "Student: Alex Morgan | Status: Passing (Great progress!)",
            [
                "Function body is indented 4 spaces.",
                "The if-else blocks introduce nested 8-space indentation levels.",
                "evaluate_student call is placed at the top-level 0-indentation baseline."
            ],
            [
                "Mixing tabs and spaces, triggering `IndentationError: unexpected indent` or `TabError`.",
                "Forgetting the colon `:` at the end of `if`, `else`, `for`, `def`, or `class` headers."
            ],
            [
                ("What is PEP 8?", "The official Style Guide for Python Code defining formatting and naming rules."),
                ("Why does Python enforce indentation syntactically rather than optionally?", "Ensures all Python code is uniform, readable, and visually clean across teams."),
                ("How do you continue a long Python statement across multiple lines?", "Use parentheses `(...)` for implicit line continuation or a backslash `\\`.")
            ]
        ),
        format_lesson(
            "python",
            "Variables", 20,
            [
                "Declare, assign, and reassign variables dynamically",
                "Understand Python's object reference model and memory identity (id)",
                "Apply naming conventions (snake_case, uppercase constants)"
            ],
            "In Python, variables are **labels (names) that reference objects in memory**, rather than fixed memory boxes. Key characteristics:\n- **Dynamic Typing**: You do not declare variable types; the interpreter associates the type with the object in memory, not the variable name.\n- Reassignment: A variable can reference an integer at one moment and later reference a string.\n- Naming rules: Must begin with a letter or underscore, contain alphanumeric characters and underscores, and are case-sensitive (`count` vs `Count`).",
            "score = 95           # Integer object\nscore = \"Ninety-Five\" # Now points to a String object\nTOTAL_MAX = 100       # Constant convention (UPPER_SNAKE_CASE)",
            "x = 42\ny = x\n\nprint(f\"Value x: {x} (ID: {id(x)})\")\nprint(f\"Value y: {y} (ID: {id(y)})\")\nprint(f\"x and y reference the same object: {x is y}\")\n\nx = 100 # Rebinds x to a new integer object\nprint(f\"After rebinding x: x={x}, y={y}\")",
            "Value x: 42 (ID: ...)\nValue y: 42 (ID: ...)\nx and y reference the same object: True\nAfter rebinding x: x=100, y=42",
            [
                "Initially, both x and y reference the integer object 42 in memory.",
                "Reassigning x creates a new integer object 100; y continues referencing 42."
            ],
            [
                "Assuming variables are fixed memory locations; assigning `y = x` copies the reference, not the underlying object.",
                "Using reserved Python keywords (e.g. `class`, `def`, `for`, `import`) as variable names."
            ],
            [
                ("What does the built-in id() function return?", "The unique integer identity (memory address) of an object."),
                ("How does Python garbage collection clean up unreferenced objects?", "Via reference counting supplemented by a cyclic garbage collector."),
                ("What is multiple assignment in Python (e.g. a, b = 1, 2)?", "Tuple unpacking assigning multiple variables concurrently.")
            ]
        ),
        format_lesson(
            "python",
            "Basic data types", 20,
            [
                "Identify Python's core primitive data types: int, float, str, bool, and None",
                "Inspect object types at runtime using type() and isinstance()",
                "Understand arbitrary-precision integers and floating-point representations"
            ],
            "Python provides rich built-in scalar data types:\n1. `int`: Integers with **arbitrary precision** (no overflow or 32/64-bit limits; can grow as large as host memory allows).\n2. `float`: IEEE 754 double-precision 64-bit floating point numbers.\n3. `str`: Immutable sequences of Unicode characters enclosed in single `'...'` or double `\"...\"` quotes.\n4. `bool`: Boolean truth values: `True` or `False` (subclass of int).\n5. `NoneType`: Represents the absence of a value (`None`), analogous to null in other languages.",
            "age = 25              # int\ngpa = 3.85            # float\nname = \"Alex\"         # str\nis_enrolled = True    # bool\ngraduation_date = None # NoneType",
            "val_int = 987654321012345678901234567890\nval_float = 3.14159\nval_str = \"LearnHub Platform\"\nval_bool = True\nval_none = None\n\nfor item in [val_int, val_float, val_str, val_bool, val_none]:\n    print(f\"Value: {item} | Type: {type(item).__name__}\")",
            "Value: 987654321012345678901234567890 | Type: int\nValue: 3.14159 | Type: float\nValue: LearnHub Platform | Type: str\nValue: True | Type: bool\nValue: None | Type: NoneType",
            [
                "val_int demonstrates Python's automatic arbitrary-precision integers without overflow.",
                "type(item).__name__ inspects runtime data types dynamically."
            ],
            [
                "Capitalizing booleans incorrectly (writing `true` or `false` with lowercase; Python requires `True` and `False`).",
                "Using `== None` instead of the idiomatic identity check `is None`."
            ],
            [
                ("Why is `is None` preferred over `== None`?", "is tests identity against the singleton NoneType instance, avoiding overridden __eq__ side-effects."),
                ("Can Python integers suffer from integer overflow like 32-bit ints in C or Java?", "No, Python 3 integers automatically allocate additional bytes as needed."),
                ("What is the difference between `type(obj) is int` and `isinstance(obj, int)`?", "isinstance supports inheritance hierarchies; type() checks exact type.")
            ]
        ),
        format_lesson(
            "python",
            "Type conversion", 20,
            [
                "Convert values between types using int(), float(), str(), and bool()",
                "Anticipate and handle ValueError on invalid conversions",
                "Understand Python truthiness (falsy vs truthy values)"
            ],
            "Type conversion (typecasting) transforms data from one type to another:\n- `int(x)`: Converts to integer (truncates float decimals; raises `ValueError` on malformed strings).\n- `float(x)`: Converts to float.\n- `str(x)`: Converts any object into its string representation.\n- `bool(x)`: Converts to boolean according to **truthiness** rules.\n**Falsy Values**: `0`, `0.0`, `\"\"` (empty string), `[]` (empty list), `{}`, `set()`, `None`, and `False`. Everything else in Python is **truthy**.",
            "# Explicit conversions\nnum = int(\"42\")\nratio = float(\"3.75\")\nflag = bool(\"\") # False (empty string is falsy)",
            "raw_input_score = \"85\"\nraw_input_decimal = \"92.7\"\n\nparsed_score = int(raw_input_score)\nparsed_decimal = float(raw_input_decimal)\n\nprint(f\"Parsed int: {parsed_score} + 5 = {parsed_score + 5}\")\nprint(f\"Parsed float: {parsed_decimal}\")\n\n# Truthiness demonstration\nprint(f\"bool(0): {bool(0)}\")\nprint(f\"bool('Hello'): {bool('Hello')}\")\nprint(f\"bool([]): {bool([])}\")",
            "Parsed int: 85 + 5 = 90\nParsed float: 92.7\nbool(0): False\nbool('Hello'): True\nbool([]): False",
            [
                "int() parses the numeric string and allows arithmetic.",
                "bool() evaluates truthiness: empty containers and zero evaluate to False."
            ],
            [
                "Calling `int(\"3.14\")` directly, which raises `ValueError` (must convert to float first: `int(float(\"3.14\"))`).",
                "Concatenating numbers and strings without converting (`\"Score: \" + 95` fails with TypeError; use f-strings instead)."
            ],
            [
                ("What exception is raised when calling `int('abc')`?", "ValueError: invalid literal for int() with base 10."),
                ("Is an empty list `[]` considered truthy or falsy in Python conditionals?", "Falsy."),
                ("How does `str(obj)` differ from `repr(obj)`?", "str is for human-readable output; repr is an unambiguous representation often matching valid Python code.")
            ]
        ),
        format_lesson(
            "python",
            "Input and output", 25,
            [
                "Capture terminal user input using the built-in input() function",
                "Format output using f-strings, sep, and end parameters in print()",
                "Format numbers with precision specifiers (e.g. .2f, commas, percentages)"
            ],
            "Python handles console I/O seamlessly:\n- `input(prompt)`: Displays prompt and waits for user input. **Always returns a string** (must be cast with `int()` or `float()` for numeric calculations).\n- `print(*objects, sep=' ', end='\\n')`:\n  - `sep`: String inserted between items (default space).\n  - `end`: String appended at the very end (default newline).\n- **f-strings** (Python 3.6+): Prefix string with `f\"...\"` and place variables or expressions directly inside curly braces `{expr:format}`.",
            "# f-string formatting options\nprice = 1450.5\nprint(f\"Formatted: ${price:,.2f}\") # $1,450.50",
            "# Simulated I/O\nstudent_name = \"Alex Morgan\"\ncompleted_lessons = 18\ntotal_lessons = 25\nprogress_rate = completed_lessons / total_lessons\n\n# Custom separator and end\nprint(\"LearnHub\", \"Python\", \"Masterclass\", sep=\" -> \")\n\n# Formatted f-string output\nprint(f\"Student : {student_name}\")\nprint(f\"Progress: {completed_lessons}/{total_lessons} ({progress_rate:.1%})\")",
            "LearnHub -> Python -> Masterclass\nStudent : Alex Morgan\nProgress: 18/25 (72.0%)",
            [
                "sep=' -> ' replaces default spaces between print arguments.",
                "progress_rate:.1% automatically multiplies by 100 and formats as percentage."
            ],
            [
                "Forgetting that `input()` returns a string, causing `age + 5` to raise a `TypeError`.",
                "Using legacy `%` formatting or `.format()` where f-strings are much clearer and faster."
            ],
            [
                ("How do you prevent print() from starting a new line?", "Pass `end=' '` or `end=''`."),
                ("What does the format specifier `{val:05d}` do?", "Pads an integer with leading zeros to 5 total digits."),
                ("Can arbitrary Python expressions and method calls be placed inside f-strings?", "Yes: `{name.upper()}` or `{a + b}` are fully valid.")
            ]
        ),
        format_lesson(
            "python",
            "Operators", 25,
            [
                "Apply arithmetic, comparison, logical, assignment, membership, and identity operators",
                "Understand short-circuit evaluation in logical 'and' / 'or'",
                "Differentiate value equality (==) from object identity (is)"
            ],
            "Python operators cover standard and unique computational operations:\n1. Arithmetic: `+`, `-`, `*`, `/` (true float division), `//` (floor/integer division), `%` (modulo), `**` (exponentiation).\n2. Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=` (supports chaining: `10 <= x <= 20`).\n3. Logical: `and`, `or`, `not` (short-circuiting).\n4. Membership: `in`, `not in` (tests membership in sequences, sets, dicts).\n5. Identity: `is`, `is not` (tests whether two references point to the exact same object in memory).",
            "# Chained comparisons\nif 0 <= score <= 100: ...\n# Exponentiation and floor division\npower = 2 ** 8    # 256\nfloor = 7 // 2     # 3",
            "a = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n\nprint(f\"a == b (content equality): {a == b}\")\nprint(f\"a is b (memory identity): {a is b}\")\nprint(f\"a is c (same reference): {a is c}\")\n\n# Floor division vs float division\nprint(f\"7 / 2 = {7 / 2} | 7 // 2 = {7 // 2} | 2 ** 5 = {2 ** 5}\")\n\n# Membership operator\nprint(f\"2 in a: {2 in a} | 9 not in a: {9 not in a}\")",
            "a == b (content equality): True\na is b (memory identity): False\na is c (same reference): True\n7 / 2 = 3.5 | 7 // 2 = 3 | 2 ** 5 = 32\n2 in a: True | 9 not in a: True",
            [
                "a == b is True because list elements match.",
                "a is b is False because they are two distinct list instances in memory.",
                "7 / 2 produces float 3.5; 7 // 2 produces integer floor 3."
            ],
            [
                "Using `is` instead of `==` to compare numbers or strings.",
                "Confusing single slash `/` (float division) with double slash `//` (floor division)."
            ],
            [
                ("What does the expression `x = a or b` return if a is truthy?", "Returns a without evaluating b (short-circuit)."),
                ("What is the result of `2 ** 3 ** 2`?", "512 (exponentiation is right-associative: 3**2=9, then 2**9=512)."),
                ("How do chained comparisons like `1 < x < 10` work in Python?", "Evaluated as `1 < x and x < 10` with x evaluated only once.")
            ]
        ),
        format_lesson(
            "python",
            "Strings and string methods", 25,
            [
                "Navigate strings using 0-based and negative indexing",
                "Slice strings using start:stop:step notation",
                "Apply built-in string methods (strip, split, join, replace, find, upper, lower)"
            ],
            "In Python, `str` is an **immutable sequence of Unicode characters**:\n- **Indexing**: `s[0]` gets first character; negative indexing `s[-1]` accesses from the end.\n- **Slicing**: `s[start:stop:step]` extracts a substring (start inclusive, stop exclusive).\n- **Key Methods**:\n  - `strip()`: Removes leading and trailing whitespace.\n  - `split(sep)`: Splits string into a list of strings.\n  - `join(iterable)`: Joins elements of an iterable into a string separated by delimiter.\n  - `replace(old, new)`: Returns copy with replacements.\n  - `find(sub)`: Returns index of substring, or -1 if not found.",
            "text = \"  Python Programming  \"\nclean = text.strip().lower() # \"python programming\"\ntokens = clean.split()        # [\"python\", \"programming\"]\njoined = \"-\".join(tokens)     # \"python-programming\"",
            "message = \"LearnHub Python Masterclass\"\n\n# Indexing & Slicing\nprint(f\"First char: '{message[0]}' | Last char: '{message[-1]}'\")\nprint(f\"Slice (0:8): '{message[0:8]}'\")\nprint(f\"Reverse slice: '{message[::-1]}'\")\n\n# Methods\nwords = message.split(\" \")\nslug = \"_\".join(words).lower()\nprint(f\"URL Slug: {slug}\")\nprint(f\"Contains 'Python': {'Python' in message}\")",
            "First char: 'L' | Last char: 's'\nSlice (0:8): 'LearnHub'\nReverse slice: 'ssalcretsaM nohtyP buHnraeL'\nURL Slug: learnhub_python_masterclass\nContains 'Python': True",
            [
                "message[0:8] extracts 'LearnHub' without mutating the original string.",
                "message[::-1] reverses the string using step -1.",
                "split and join transform text into a URL slug."
            ],
            [
                "Attempting to modify a character in-place (`s[0] = 'X'`), which raises `TypeError: 'str' object does not support item assignment`.",
                "Calling `join()` on a list containing non-string elements without converting them first (`','.join(map(str, nums))`)."
            ],
            [
                ("Why are Python strings immutable?", "Hash stability (use as dict keys/sets), memory sharing, and thread-safety."),
                ("What does `''.join(reversed(text))` do?", "Reverses a string efficiently."),
                ("What does the find() method return if the target substring does not exist in the string?", "Returns -1.")
            ]
        )
    ]
    return {
        "title": "Module 1 - Python Fundamentals",
        "description": "Install Python and understand the language's core syntax and data types.",
        "sequenceOrder": 1,
        "lessons": lessons
    }

def get_python_module_2():
    lessons = [
        format_lesson(
            "python",
            "Boolean expressions", 20,
            [
                "Evaluate boolean expressions and comparison operators",
                "Combine conditions using logical keywords: and, or, and not",
                "Leverage Python's truthiness rules for clean conditional expressions"
            ],
            "A boolean expression evaluates to either `True` or `False`. Logical keywords in Python are plain English words rather than symbols:\n- `and`: True if both conditions are truthy.\n- `or`: True if at least one condition is truthy.\n- `not`: Inverts truth value.\nShort-circuiting: `A and B` returns A if A is falsy, otherwise B. `A or B` returns A if A is truthy, otherwise B.",
            "is_authorized = is_logged_in and (is_admin or has_permission)",
            "user_role = \"INSTRUCTOR\"\nis_active = True\nhas_warnings = False\n\ncan_access_roster = is_active and (user_role in (\"ADMIN\", \"INSTRUCTOR\")) and not has_warnings\nprint(f\"Instructor Roster Access: {can_access_roster}\")",
            "Instructor Roster Access: True",
            [
                "Evaluates composite condition using readable logical keywords.",
                "Short-circuits immediately if is_active is False."
            ],
            [
                "Using bitwise operators `&` and `|` instead of logical `and` and `or` for boolean conditions.",
                "Writing redundant checks like `if condition == True:` instead of simply `if condition:`."
            ],
            [
                ("What is the result of `'hello' and 0 or 'fallback'`?", "'fallback' ('hello' and 0 is 0; 0 or 'fallback' is 'fallback')."),
                ("What values in Python evaluate to False in a boolean context?", "0, 0.0, '', [], {}, set(), None, False."),
                ("Why is `if items:` considered better Python style than `if len(items) > 0:`?", "Follows Pythonic truthiness conventions.")
            ]
        ),
        format_lesson(
            "python",
            "if, elif, and else", 20,
            [
                "Implement conditional branching using if, elif, and else statements",
                "Order conditions logically to avoid unreachable branches",
                "Use conditional expressions (ternary operator: x if cond else y)"
            ],
            "Python uses `if`, `elif` (short for else if), and `else` to control branching. Blocks are defined strictly by indentation:\n- First condition evaluating to truthy executes its block; all downstream elif/else blocks are skipped.\n- **Conditional Expression (Ternary)**: `value_if_true if condition else value_if_false`.",
            "# Ternary expression\nstatus = \"PASSED\" if score >= 70 else \"NEEDS_REVIEW\"",
            "score = 84\n\nif score >= 90:\n    tier = \"Advanced Distinction\"\nelif score >= 80:\n    tier = \"Proficient\"\nelif score >= 70:\n    tier = \"Passing\"\nelse:\n    tier = \"Needs Improvement\"\n    \nstatus_badge = \"CERTIFIED\" if score >= 70 else \"PENDING\"\nprint(f\"Score: {score} | Tier: {tier} | Badge: {status_badge}\")",
            "Score: 84 | Tier: Proficient | Badge: CERTIFIED",
            [
                "Evaluates score >= 90 (False), falls through to score >= 80 (True).",
                "Assigns 'Proficient' and exits branch immediately.",
                "Ternary operator assigns 'CERTIFIED' cleanly."
            ],
            [
                "Forgetting the colon `:` at the end of `if` or `elif` lines.",
                "Using multiple unlinked `if` statements instead of `elif`, causing multiple branches to trigger unintentionally."
            ],
            [
                ("How does Python's elif compare to else if in Java or C++?", "Syntactically cleaner and prevents deep indentation drift."),
                ("Can an if statement have multiple elif clauses?", "Yes, any number of elif clauses can be chained."),
                ("What does the pass statement do inside an empty if block?", "Acts as a no-op placeholder to satisfy indentation syntax.")
            ]
        ),
        format_lesson(
            "python",
            "for loops", 25,
            [
                "Iterate over sequences (strings, lists, tuples, ranges) using for loops",
                "Apply the for-in syntax cleanly without manual index tracking",
                "Accumulate calculations and process iterable elements"
            ],
            "In Python, a `for` loop is a **for-each loop**: it iterates directly over the items of any iterable sequence (such as a string, list, dictionary, or range) in sequential order. You do not need to manage manual counters or index bounds.",
            "for item in collection:\n    # Process item directly",
            "languages = [\"Python\", \"Java\", \"JavaScript\", \"Go\"]\nprint(\"Core Curriculum Tracks:\")\nfor lang in languages:\n    print(f\"- {lang} Masterclass (Duration: 50h)\")\n\n# Summing numbers in a range\ntotal = 0\nfor n in range(1, 6):\n    total += n\nprint(f\"Sum of 1 through 5: {total}\")",
            "Core Curriculum Tracks:\n- Python Masterclass (Duration: 50h)\n- Java Masterclass (Duration: 50h)\n- JavaScript Masterclass (Duration: 50h)\n- Go Masterclass (Duration: 50h)\nSum of 1 through 5: 15",
            [
                "Directly iterates through strings in the languages list.",
                "range(1, 6) generates numbers 1, 2, 3, 4, 5 and accumulates sum = 15."
            ],
            [
                "Modifying the list (adding/removing items) while iterating over it, causing skipped elements.",
                "Writing C-style loops (`for i in range(len(items)): print(items[i])`) when `for item in items:` is cleaner and idiomatic."
            ],
            [
                ("What types of objects can be iterated over with a for loop in Python?", "Any object implementing the iterable protocol (__iter__ returning an iterator)."),
                ("What does the optional `else` block on a for loop do?", "Executes when the loop terminates normally (without hitting a break)."),
                ("How do you iterate over key-value pairs of a dictionary in a for loop?", "Use `for k, v in my_dict.items():`.")
            ]
        ),
        format_lesson(
            "python",
            "while loops", 20,
            [
                "Implement condition-controlled loops using while",
                "Manage loop state progression to prevent infinite loops",
                "Implement interactive prompt loops and sentinel termination"
            ],
            "A `while` loop repeatedly executes its block as long as a specified condition evaluates to truthy. The condition is tested before each iteration. The loop body must eventually update variables such that the condition becomes falsy; otherwise, an **infinite loop** occurs.",
            "while condition:\n    # Repeat until condition becomes False",
            "counter = 5\nprint(\"Launching interactive countdown:\")\nwhile counter > 0:\n    print(f\"T-minus {counter}...\")\n    counter -= 1\nprint(\"Ignition! Python script executed successfully.\")",
            "Launching interactive countdown:\nT-minus 5...\nT-minus 4...\nT-minus 3...\nT-minus 2...\nT-minus 1...\nIgnition! Python script executed successfully.",
            [
                "Evaluates counter > 0.",
                "Decrements counter on each step until 0 is reached, terminating the loop."
            ],
            [
                "Omitting the decrement/update step, resulting in an infinite loop that freezes CPU execution.",
                "Using floating point numbers in equality loop termination conditions (`while x != 1.0:`), which may miss due to rounding."
            ],
            [
                ("How do you stop an accidental infinite loop in a terminal?", "Press Ctrl+C to send SIGINT (KeyboardInterrupt)."),
                ("Does Python have a native `do-while` loop construct?", "No, emulate using `while True:` with an `if condition: break` at the bottom."),
                ("What does a while-else clause do in Python?", "Executes when the while condition becomes false, provided the loop was not broken by a break statement.")
            ]
        ),
        format_lesson(
            "python",
            "range()", 20,
            [
                "Generate integer sequences using range(stop), range(start, stop), and range(start, stop, step)",
                "Avoid common off-by-one errors with stop boundaries",
                "Understand lazy generation and memory efficiency of range objects"
            ],
            "The `range()` function returns an immutable sequence of integers. It is lazy: it produces numbers on demand using $O(1)$ memory regardless of how large the range is.\nSignatures:\n- `range(stop)`: 0 up to stop (exclusive).\n- `range(start, stop)`: start (inclusive) up to stop (exclusive).\n- `range(start, stop, step)`: increments by step (can be negative for counting downwards).",
            "# range signatures\nfor i in range(5): ...         # 0, 1, 2, 3, 4\nfor i in range(2, 6): ...      # 2, 3, 4, 5\nfor i in range(10, 0, -2): ... # 10, 8, 6, 4, 2",
            "print(\"Counting 1 to 5:\", list(range(1, 6)))\nprint(\"Even numbers 2 to 10:\", list(range(2, 11, 2)))\nprint(\"Countdown 5 to 1:\", list(range(5, 0, -1)))",
            "Counting 1 to 5: [1, 2, 3, 4, 5]\nEven numbers 2 to 10: [2, 4, 6, 8, 10]\nCountdown 5 to 1: [5, 4, 3, 2, 1]",
            [
                "range(1, 6) stops at 5 (stop index 6 is exclusive).",
                "range(2, 11, 2) skips by 2.",
                "range(5, 0, -1) steps backwards down to 1."
            ],
            [
                "Off-by-one error: expecting `range(1, 10)` to include 10 (it stops at 9).",
                "Passing a step of 0, which raises `ValueError: range() arg 3 must not be zero`."
            ],
            [
                ("Does `range(1_000_000_000)` allocate an array of one billion integers in RAM?", "No, range generates numbers on the fly in O(1) memory."),
                ("How do you generate numbers from 10 down to 0 including 0?", "`range(10, -1, -1)`."),
                ("Can range accept floating-point numbers?", "No, only integers (use numpy.arange or itertools for floats).")
            ]
        ),
        format_lesson(
            "python",
            "break and continue", 20,
            [
                "Terminate loop repetition early using break",
                "Skip the rest of the current iteration using continue",
                "Utilize loop else blocks that execute only when break is not encountered"
            ],
            "Python provides jump statements to redirect loop flow:\n- `break`: Immediately terminates the innermost enclosing loop.\n- `continue`: Skips the remainder of the current iteration and jumps to the next cycle.\n- **for-else / while-else**: The `else` block attached to a loop executes **only if the loop finished naturally without encountering a break**. Ideal for search loops.",
            "for item in items:\n    if item == target:\n        print(\"Found!\")\n        break\nelse:\n    print(\"Target not found in collection.\")",
            "print(\"Processing batch (skipping odds, halting at 8):\")\nfor num in range(1, 11):\n    if num % 2 != 0:\n        continue # Skip odd numbers\n    if num == 8:\n        print(f\"[Halt at {num}]\")\n        break\n    print(f\"Processed even: {num}\")",
            "Processing batch (skipping odds, halting at 8):\nProcessed even: 2\nProcessed even: 4\nProcessed even: 6\n[Halt at 8]",
            [
                "Odd numbers are skipped by continue.",
                "Even numbers 2, 4, 6 are processed.",
                "When num == 8, break terminates the loop."
            ],
            [
                "Putting statements after break or continue within the same block, creating unreachable code.",
                "Misunderstanding the loop `else` clause as executing on every iteration; it only runs once upon complete loop conclusion."
            ],
            [
                ("How does the `else` clause on a Python loop differ from an `if-else` clause?", "Runs only if the loop completes without hitting a break."),
                ("Does break exit only the innermost loop in nested loops?", "Yes, break exits only the immediate enclosing loop."),
                ("How do you terminate multiple nested loops in Python?", "Use boolean flags, refactor into a function and return early, or raise an exception.")
            ]
        ),
        format_lesson(
            "python",
            "Nested loops", 25,
            [
                "Implement nested loops for multi-dimensional data and grids",
                "Trace iteration counts across outer and inner variables",
                "Construct geometric patterns and matrix coordinate pairs"
            ],
            "A nested loop is a loop located inside another loop. For every iteration of the outer loop, the inner loop executes its full cycle. If outer runs $N$ times and inner runs $M$ times, the body executes $N \\times M$ times.",
            "for r in range(rows):\n    for c in range(cols):\n        grid[r][c] = ...",
            "print(\"Generating star triangle pattern:\")\nfor i in range(1, 5):\n    for j in range(i):\n        print(\"* \", end=\"\")\n    print() # Newline\n\nprint(\"\\nMatrix Coordinate Pairs (2x3):\")\nfor r in range(2):\n    for c in range(3):\n        print(f\"({r}, {c}) \", end=\"\")\n    print()",
            "Generating star triangle pattern:\n* \n* * \n* * * \n* * * * \n\nMatrix Coordinate Pairs (2x3):\n(0, 0) (0, 1) (0, 2) \n(1, 0) (1, 1) (1, 2)",
            [
                "Outer loop controls rows; inner loop controls column stars.",
                "end='' keeps output on same line until print() emits newline."
            ],
            [
                "Accidentally reusing the same loop variable name for both outer and inner loops (`for i in ...: for i in ...:`).",
                "Unnecessary nested loops leading to quadratic $O(n^2)$ time complexity on large datasets."
            ],
            [
                ("How many times does the inner statement execute for `for i in range(4): for j in range(5):`?", "20 times (4 * 5)."),
                ("How do you print a multiplication table from 1 to 5 using nested loops?", "Outer loop from 1 to 5, inner loop from 1 to 5 printing i * j."),
                ("How can itertools.product replace nested loops cleanly?", "Allows `for r, c in itertools.product(range(2), range(3)):`.")
            ]
        ),
        format_lesson(
            "python",
            "Looping with enumerate and zip", 25,
            [
                "Iterate with index tracking using the built-in enumerate() function",
                "Pair multiple sequences concurrently using zip() and zip(strict=True)",
                "Unpack tuples cleanly inside loop headers"
            ],
            "Python provides two essential iteration helpers:\n1. `enumerate(iterable, start=0)`: Yields pairs of `(index, item)` during iteration, eliminating manual counter variables.\n2. `zip(*iterables)`: Aggregates elements from multiple iterables element-wise, terminating when the shortest sequence is exhausted. Python 3.10+ adds `zip(a, b, strict=True)` to raise a `ValueError` if lengths mismatch.",
            "# enumerate and zip patterns\nfor idx, item in enumerate(items, start=1): ...\nfor name, score in zip(names, scores): ...",
            "students = [\"Alex Morgan\", \"Sarah Connor\", \"David Miller\"]\nscores = [92, 88, 95]\n\nprint(\"Student Roster via enumerate:\")\nfor rank, name in enumerate(students, start=1):\n    print(f\"{rank}. {name}\")\n\nprint(\"\\nPaired Records via zip:\")\nfor name, score in zip(students, scores):\n    print(f\"- {name:15}: {score}%\")",
            "Student Roster via enumerate:\n1. Alex Morgan\n2. Sarah Connor\n3. David Miller\n\nPaired Records via zip:\n- Alex Morgan    : 92%\n- Sarah Connor   : 88%\n- David Miller   : 95%",
            [
                "enumerate provides 1-based ranking without maintaining a separate counter.",
                "zip pairs students and scores cleanly in parallel."
            ],
            [
                "Using `range(len(items))` just to get an index (use `enumerate(items)` instead).",
                "Forgetting that standard `zip()` silently drops remaining items if one sequence is longer than another."
            ],
            [
                ("What does itertools.zip_longest() do?", "Zips sequences up to the longest, filling missing values with a designated fillvalue (default None)."),
                ("Can enumerate accept a custom starting index?", "Yes, pass `start=1` or any integer as second argument."),
                ("How do you convert a zipped collection into a dictionary?", "Call `dict(zip(keys, values))`.")
            ]
        ),
        format_lesson(
            "python",
            "Practice problems", 30,
            [
                "Solve classic algorithmic logic problems (Factorial, Prime Check, Fibonacci, Palindrome)",
                "Extract digits using modulo and integer division",
                "Benchmark and optimize iterative loops for mathematical challenges"
            ],
            "This problem set consolidates Module 2 mastery:\n1. Factorial ($n!$)\n2. Prime Number Check (trial division up to $\\sqrt{n}$)\n3. Fibonacci Series ($F_n = F_{n-1} + F_{n-2}$)\n4. Palindrome Check (integer and string)\n5. Sum of Digits.",
            "# Palindrome number check via integer math:\norig, rev = n, 0\nwhile n > 0:\n    rev = rev * 10 + (n % 10)\n    n //= 10\nreturn orig == rev",
            "def factorial(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result\n\ndef is_prime(n):\n    if n <= 1: return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0: return False\n    return True\n\ndef fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a\n\nprint(f\"5! = {factorial(5)}\")\nprint(f\"Is 29 prime? {is_prime(29)}\")\nprint(f\"7th Fibonacci number: {fibonacci(7)}\")",
            "5! = 120\nIs 29 prime? True\n7th Fibonacci number: 13",
            [
                "factorial(5) evaluates 1 * 2 * 3 * 4 * 5 = 120.",
                "is_prime checks divisors up to sqrt(29) (~5.3) and returns True.",
                "fibonacci calculates the series iteratively in O(n) time and O(1) space."
            ],
            [
                "Checking prime divisors up to n instead of sqrt(n).",
                "Using naive recursion for Fibonacci which causes exponential $O(2^n)$ slowdown."
            ],
            [
                ("How do you check if an integer is a palindrome using string conversion?", "Compare `str(n) == str(n)[::-1]`."),
                ("What is the sum of digits of 12345?", "1 + 2 + 3 + 4 + 5 = 15."),
                ("Why does `a, b = b, a + b` work correctly in Python?", "The right-hand side tuple (b, a + b) is evaluated first before assignment.")
            ]
        )
    ]
    return {
        "title": "Module 2 - Conditions and Loops",
        "description": "Use Boolean logic and iteration to solve problems.",
        "sequenceOrder": 2,
        "lessons": lessons
    }

print("Python modules 1 & 2 ready.")
