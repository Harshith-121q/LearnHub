from formatter import format_lesson

def get_python_module_7():
    lessons = [
        format_lesson(
            "python",
            "HTTP and REST introduction", 25,
            [
                "Understand the HTTP request/response architecture",
                "Differentiate HTTP methods: GET, POST, PUT, PATCH, and DELETE",
                "Interpret standard HTTP status codes (200, 201, 400, 401, 403, 404, 500)"
            ],
            "Web APIs connect distributed services over the **HTTP protocol** using **REST (Representational State Transfer)** principles:\n- **Client/Server**: Client sends an HTTP Request; server evaluates it and sends back an HTTP Response.\n- **HTTP Methods**:\n  - `GET`: Retrieve resources (safe and idempotent).\n  - `POST`: Create a new resource.\n  - `PUT`: Replace an entire existing resource.\n  - `PATCH`: Partially update an existing resource.\n  - `DELETE`: Remove a resource.\n- **Status Codes**:\n  - `2xx Success`: 200 OK, 201 Created.\n  - `4xx Client Error`: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found.\n  - `5xx Server Error`: 500 Internal Server Error.",
            "# Canonical REST endpoints:\n# GET    /api/courses        -> List published courses\n# POST   /api/courses        -> Create course (Admin only)\n# GET    /api/courses/{id}   -> Fetch course details\n# DELETE /api/courses/{id}   -> Archive/Delete course",
            "class MockHTTPResponse:\n    def __init__(self, status_code, body):\n        self.status_code = status_code\n        self.body = body\n\nresponse = MockHTTPResponse(200, {\"status\": \"success\", \"course\": \"Python Masterclass\"})\nprint(f\"HTTP Status Code: {response.status_code} OK\")\nprint(f\"Response Payload: {response.body}\")",
            "HTTP Status Code: 200 OK\nResponse Payload: {'status': 'success', 'course': 'Python Masterclass'}",
            [
                "Deconstructs REST client-server protocol.",
                "Maps HTTP status codes to standard client responses."
            ],
            [
                "Using GET requests for operations that modify server state (violates REST idempotency).",
                "Returning 200 OK when an error actually occurred."
            ],
            [
                ("What does the HTTP 401 status code mean compared to 403?", "401 means unauthenticated (must log in); 403 means authenticated but unauthorized (forbidden role)."),
                ("What is an idempotent HTTP method?", "A method where making multiple identical requests has the same effect as a single request (GET, PUT, DELETE)."),
                ("What HTTP header specifies that the request or response payload is JSON?", "`Content-Type: application/json`.")
            ]
        ),
        format_lesson(
            "python",
            "Calling APIs", 25,
            [
                "Make HTTP requests using urllib.request and the third-party requests library",
                "Configure query parameters and custom request headers",
                "Enforce network timeouts to prevent hanging connections"
            ],
            "Python communicates with web services via HTTP:\n- Standard library: `urllib.request` (built-in, no installation needed).\n- Industry Standard: The `requests` library (`pip install requests`):\n  `import requests`\n  `response = requests.get('https://api.example.com/courses', timeout=5)`\n- Crucial Rule: Always specify `timeout=seconds` to ensure network delays do not hang application threads indefinitely.",
            "import urllib.request\nimport json\n\n# Standard library HTTP GET\ntry:\n    with urllib.request.urlopen(\"http://localhost:8080/api/courses\", timeout=3) as res:\n        data = json.loads(res.read().decode())\nexcept Exception as e:\n    pass",
            "import json\nimport urllib.parse\n\n# Simulating API request parameters\nbase_url = \"https://api.learnhub.com/v1/courses\"\nparams = {\"category\": \"Programming\", \"tier\": \"Beginner\", \"limit\": 10}\nquery_string = urllib.parse.urlencode(params)\nfull_endpoint = f\"{base_url}?{query_string}\"\n\nprint(\"Constructed REST API Endpoint:\")\nprint(full_endpoint)\nprint(\"Timeout guard configured: 5.0 seconds\")",
            "Constructed REST API Endpoint:\nhttps://api.learnhub.com/v1/courses?category=Programming&tier=Beginner&limit=10\nTimeout guard configured: 5.0 seconds",
            [
                "urllib.parse.urlencode constructs URL query parameters safely.",
                "Demonstrates timeout parameter guarding."
            ],
            [
                "Making requests without specifying a `timeout`, risking frozen threads if the remote server stalls.",
                "Concatenating query string values manually without URL encoding special characters like spaces."
            ],
            [
                ("Why is `timeout` mandatory in production HTTP requests?", "Prevents slow or dead remote servers from consuming all worker threads."),
                ("How do you inspect the parsed JSON body using the requests library?", "Call `response.json()`."),
                ("What does `response.raise_for_status()` do in requests?", "Raises an HTTPError if the response status code was 4xx or 5xx.")
            ]
        ),
        format_lesson(
            "python",
            "API error handling", 20,
            [
                "Handle network connection timeouts and DNS failures",
                "Validate HTTP status codes using response.raise_for_status()",
                "Gracefully parse malformed JSON payloads"
            ],
            "When calling external APIs, failure is normal (network down, rate limited, 500 error, malformed JSON). Robust API clients implement three layers of error defense:\n1. Network/Connection Exceptions (`requests.exceptions.ConnectionError`, `Timeout`).\n2. HTTP Status Verification (`response.raise_for_status()`).\n3. JSON Parsing Exceptions (`json.JSONDecodeError`).",
            "try:\n    response = requests.get(url, timeout=5)\n    response.raise_for_status() # Raises on 4xx/5xx\n    data = response.json()\nexcept requests.exceptions.Timeout:\n    logger.error(\"Request timed out\")\nexcept requests.exceptions.HTTPError as e:\n    logger.error(f\"HTTP error: {e.response.status_code}\")\nexcept json.JSONDecodeError:\n    logger.error(\"Invalid JSON payload returned\")",
            "def simulate_api_fetch(status_code, raw_body):\n    if status_code == 404:\n        raise ValueError(\"Resource not found (HTTP 404)\")\n    if status_code >= 500:\n        raise RuntimeError(\"Upstream server error (HTTP 500)\")\n    try:\n        import json\n        return json.loads(raw_body)\n    except Exception as e:\n        raise ValueError(f\"Malformed JSON response: {e}\")\n\ntry:\n    simulate_api_fetch(404, \"\")\nexcept ValueError as err:\n    print(f\"Captured API client error: {err}\")",
            "Captured API client error: Resource not found (HTTP 404)",
            [
                "Demonstrates multi-tiered error interception.",
                "Translates HTTP protocol errors into meaningful domain exceptions."
            ],
            [
                "Assuming every 200 response contains valid JSON.",
                "Retrying non-idempotent failed requests (like POST payments) without checking idempotency keys."
            ],
            [
                ("What HTTP status code represents Rate Limiting (Too Many Requests)?", "HTTP 429 Too Many Requests."),
                ("What is an exponential backoff retry strategy?", "Retrying failed requests with exponentially increasing wait times (e.g. 1s, 2s, 4s, 8s)."),
                ("What does the Retry-After HTTP header indicate?", "The number of seconds the client must wait before making another request.")
            ]
        ),
        format_lesson(
            "python",
            "Database fundamentals", 20,
            [
                "Understand relational database models and schema design",
                "Identify primary keys, foreign keys, and indexes",
                "Model relational constraints for courses, users, and enrollments"
            ],
            "A **Relational Database** organizes data into tables consisting of rows and columns:\n- **Primary Key**: Unique identifier for each record (`id`).\n- **Foreign Key**: Establishes links between tables (e.g. `module.course_id -> course.id`).\n- **Constraints**: `NOT NULL`, `UNIQUE`, `CHECK`, and relational integrity rules (`ON DELETE CASCADE`).",
            "-- Python SQLite / MySQL Schema\nCREATE TABLE students (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    username TEXT UNIQUE NOT NULL,\n    email TEXT NOT NULL\n);",
            "print(\"Relational Database Table Architecture:\")\nprint(\"- Table 'courses'     : PK(id), title, description, duration\")\nprint(\"- Table 'modules'     : PK(id), FK(course_id), sequence_order\")\nprint(\"- Table 'lessons'     : PK(id), FK(module_id), sequence_order, content\")\nprint(\"- Table 'enrollments' : PK(id), FK(user_id), FK(course_id), progress\")",
            "Relational Database Table Architecture:\n- Table 'courses'     : PK(id), title, description, duration\n- Table 'modules'     : PK(id), FK(course_id), sequence_order\n- Table 'lessons'     : PK(id), FK(module_id), sequence_order, content\n- Table 'enrollments' : PK(id), FK(user_id), FK(course_id), progress",
            [
                "Deconstructs normalized database schema matching LearnHub.",
                "Emphasizes foreign keys and relational integrity."
            ],
            [
                "Failing to add indexes to foreign key columns used in WHERE and JOIN clauses.",
                "Storing comma-separated IDs in a single text column instead of a proper normalized join table."
            ],
            [
                ("What is the difference between SQLite and MySQL?", "SQLite is a serverless, embedded single-file database; MySQL is a client-server multi-user enterprise RDBMS."),
                ("What does a UNIQUE constraint enforce?", "Guarantees that all values in a column or set of columns are distinct."),
                ("What is database index indexing (B-Tree)?", "A data structure that accelerates search queries from O(n) table scans to O(log n).")
            ]
        ),
        format_lesson(
            "python",
            "Database connectivity", 25,
            [
                "Connect to SQLite using Python's built-in sqlite3 module",
                "Manage connection and cursor lifecycles using context managers",
                "Externalize database credentials securely using os.environ"
            ],
            "Python connects to databases using the standard **Python Database API Specification v2.0 (DB-API 2.0)**:\n- Built-in: `sqlite3` (zero-configuration embedded database).\n- MySQL / PostgreSQL: `mysql-connector-python`, `pymysql`, `psycopg2`.\n- Standard components:\n  - `Connection`: The database session (`sqlite3.connect(\":memory:\")`).\n  - `Cursor`: Object used to execute SQL queries and fetch results (`cursor.execute()`, `cursor.fetchall()`).",
            "import sqlite3\nwith sqlite3.connect(\"app.db\") as conn:\n    cursor = conn.cursor()\n    cursor.execute(\"SELECT * FROM courses\")",
            "import sqlite3\n\n# In-memory database for testing\nconn = sqlite3.connect(\":memory:\")\ncursor = conn.cursor()\n\ncursor.execute(\"CREATE TABLE status_check (id INT, message TEXT);\")\ncursor.execute(\"INSERT INTO status_check VALUES (1, 'Database connected successfully');\")\nconn.commit()\n\ncursor.execute(\"SELECT message FROM status_check WHERE id = 1;\")\nresult = cursor.fetchone()\nprint(f\"DB Query Result: '{result[0]}'\")\nconn.close()",
            "DB Query Result: 'Database connected successfully'",
            [
                "Connects to an in-memory SQLite database.",
                "Creates table, inserts record, commits, queries, and closes cleanly."
            ],
            [
                "Forgetting to call `conn.commit()`, causing INSERT and UPDATE statements to be discarded when connection closes.",
                "Leaving database connections open without closing, leaking connection pool slots."
            ],
            [
                ("What does cursor.fetchone() return if no rows match the query?", "None."),
                ("What does cursor.fetchall() return?", "A list of row tuples."),
                ("Why is an in-memory SQLite database (`:memory:`) ideal for automated testing?", "Ultra-fast execution, zero disk I/O, and completely destroyed on teardown.")
            ]
        ),
        format_lesson(
            "python",
            "SQL CRUD operations", 30,
            [
                "Execute INSERT, SELECT, UPDATE, and DELETE operations in Python",
                "Retrieve auto-generated primary keys using cursor.lastrowid",
                "Apply transactional commit and rollback"
            ],
            "Python DB-API enables complete CRUD operations:\n1. **Create**: `cursor.execute(\"INSERT INTO ... VALUES (?, ?)\", (val1, val2))`. Key retrieved via `cursor.lastrowid`.\n2. **Read**: `cursor.execute(\"SELECT ... WHERE ...\", (param,))`. Read with `cursor.fetchall()`.\n3. **Update**: `cursor.execute(\"UPDATE ... SET col = ? WHERE id = ?\", (val, id))`.\n4. **Delete**: `cursor.execute(\"DELETE FROM ... WHERE id = ?\", (id,))`.\nAlways commit changes via `conn.commit()`.",
            "cursor.execute(\"INSERT INTO courses (title) VALUES (?)\", (\"Python\",))\ncourse_id = cursor.lastrowid\nconn.commit()",
            "import sqlite3\n\nconn = sqlite3.connect(\":memory:\")\ncursor = conn.cursor()\ncursor.execute(\"\"\"CREATE TABLE courses (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    title TEXT,\n    duration INT\n);\"\"\")\n\n# Create\ncursor.execute(\"INSERT INTO courses (title, duration) VALUES (?, ?);\", (\"Python Masterclass\", 50))\ncourse_id = cursor.lastrowid\n\n# Read\ncursor.execute(\"SELECT id, title, duration FROM courses WHERE id = ?;\", (course_id,))\nrecord = cursor.fetchone()\nprint(f\"[READ]   Fetched Course: #{record[0]} - {record[1]} ({record[2]}h)\")\n\n# Update\ncursor.execute(\"UPDATE courses SET duration = ? WHERE id = ?;\", (55, course_id))\n\n# Delete\ncursor.execute(\"DELETE FROM courses WHERE id = ?;\", (course_id,))\nprint(f\"[DELETE] Rows deleted: {cursor.rowcount}\")\nconn.close()",
            "[READ]   Fetched Course: #1 - Python Masterclass (50h)\n[DELETE] Rows deleted: 1",
            [
                "Demonstrates complete CRUD cycle.",
                "Captures lastrowid and inspects rowcount on deletion."
            ],
            [
                "Passing parameters to cursor.execute as a raw variable rather than a tuple (`cursor.execute(sql, 'single_val')` treats string as sequence of chars; must pass `('single_val',)`).",
                "Forgetting to call `conn.commit()` after insert/update/delete."
            ],
            [
                ("What does cursor.rowcount represent after an UPDATE or DELETE statement?", "The number of rows modified or deleted."),
                ("Why is a comma required when passing a single parameter tuple: `(val,)`?", "Without the trailing comma, `(val)` is just parentheses around a value, not a tuple."),
                ("How do you configure sqlite3 to return rows as dictionaries instead of tuples?", "Set `conn.row_factory = sqlite3.Row`.")
            ]
        ),
        format_lesson(
            "python",
            "SQL injection prevention", 25,
            [
                "Understand the mechanics and catastrophic impact of SQL Injection attacks",
                "Use parameterized queries exclusively with ? or %s placeholders",
                "Identify vulnerable string formatting and f-string patterns in database queries"
            ],
            "**SQL Injection** occurs when untrusted user input is directly concatenated or formatted into an SQL query string.\n- **VULNERABLE (NEVER DO THIS)**:\n  `query = f\"SELECT * FROM users WHERE user = '{username}'\"`\n  If an attacker inputs `' OR '1'='1`, the query becomes `WHERE user = '' OR '1'='1'`, returning all users.\n- **SECURE (Parameterized Queries)**:\n  `cursor.execute(\"SELECT * FROM users WHERE user = ?\", (username,))`\n  The database engine pre-compiles query logic and treats parameter inputs strictly as literal data.",
            "# Vulnerable: f\"SELECT * FROM users WHERE name = '{user_input}'\"\n# Secure: cursor.execute(\"SELECT * FROM users WHERE name = ?\", (user_input,))",
            "import sqlite3\n\nconn = sqlite3.connect(\":memory:\")\ncursor = conn.cursor()\ncursor.execute(\"CREATE TABLE accounts (username TEXT, role TEXT);\")\ncursor.execute(\"INSERT INTO accounts VALUES ('admin', 'ADMIN');\")\ncursor.execute(\"INSERT INTO accounts VALUES ('alex', 'STUDENT');\")\n\nmalicious_input = \"admin' OR '1'='1\"\n\n# Parameterized query blocks injection\ncursor.execute(\"SELECT * FROM accounts WHERE username = ?;\", (malicious_input,))\nresult = cursor.fetchall()\nprint(f\"Parameterized Search with payload: '{malicious_input}'\")\nprint(f\"Matches found: {len(result)} (Safe: no injection occurred!)\")\nconn.close()",
            "Parameterized Search with payload: 'admin' OR '1'='1'\nMatches found: 0 (Safe: no injection occurred!)",
            [
                "The malicious payload is treated as a literal search string.",
                "Zero records matched, demonstrating complete protection."
            ],
            [
                "Using Python f-strings or `.format()` to construct SQL queries (`cursor.execute(f\"SELECT ... {val}\")`).",
                "Attempting to parameterize table or column names using `?` (table and column names cannot be parameterized; use strict whitelisting instead)."
            ],
            [
                ("Can table names be passed as parameterized query placeholders?", "No, placeholders only substitute data values; table/column names must be validated against a whitelist."),
                ("What placeholder syntax is used by sqlite3 vs MySQL connector?", "sqlite3 uses `?`; mysql-connector-python uses `%s`."),
                ("What tool can automatically audit Python code for SQL injection vulnerabilities?", "Bandit (security linter for Python).")
            ]
        ),
        format_lesson(
            "python",
            "Unit testing with unittest or pytest", 25,
            [
                "Write automated unit tests using Python's built-in unittest module and pytest",
                "Structure test cases using the Arrange-Act-Assert (AAA) pattern",
                "Apply assertions (assertEqual, assertTrue, assertRaises) to verify correctness"
            ],
            "Automated testing verifies that your code behaves as expected and prevents regressions:\n- **Built-in `unittest`**: Class-based testing (`class TestFoo(unittest.TestCase)`).\n- **Modern `pytest`**: Function-based testing with plain `assert` statements (`assert result == expected`).\n- Test methods MUST begin with `test_` to be discovered automatically by test runners.\n- Test exceptions: `with self.assertRaises(ValueError): func()`.",
            "import unittest\nclass TestCourse(unittest.TestCase):\n    def test_progress(self):\n        self.assertEqual(calculate_progress(5, 10), 50.0)",
            "import unittest\n\ndef calculate_progress(completed: int, total: int) -> float:\n    if total <= 0: return 0.0\n    return round((completed / total) * 100.0, 1)\n\nclass TestProgressCalculation(unittest.TestCase):\n    def test_halfway_progress(self):\n        self.assertEqual(calculate_progress(5, 10), 50.0)\n        \n    def test_zero_total_guard(self):\n        self.assertEqual(calculate_progress(0, 0), 0.0)\n        \n    def test_full_completion(self):\n        self.assertEqual(calculate_progress(79, 79), 100.0)\n\n# Run tests programmatically\nsuite = unittest.TestLoader().loadTestsFromTestCase(TestProgressCalculation)\nrunner = unittest.TextTestRunner(verbosity=1)\nrunner.run(suite)",
            "...\n----------------------------------------------------------------------\nRan 3 tests in 0.001s\n\nOK",
            [
                "Test methods inherit from unittest.TestCase.",
                "Tests verify normal calculation, zero total guard, and 100% completion.",
                "TextTestRunner executes tests cleanly."
            ],
            [
                "Naming test methods without the `test_` prefix, causing test runners to skip them entirely.",
                "Writing tests that depend on execution order of other tests (tests must be completely isolated)."
            ],
            [
                ("What does pytest provide over unittest?", "Plain assert statements, powerful fixture system, detailed failure introspection, and less boilerplate."),
                ("What is a test fixture?", "A setup function providing standardized baseline data or environment state to tests."),
                ("What command runs all discovered tests in a project with pytest?", "`pytest`.")
            ]
        ),
        format_lesson(
            "python",
            "Mocking introduction", 20,
            [
                "Understand the purpose of test doubles using unittest.mock",
                "Isolate unit tests from external HTTP APIs, databases, and filesystem access",
                "Use MagicMock, Mock, and patch to stub functions and verify calls"
            ],
            "Unit tests must be fast, reliable, and decoupled from external services. **Mocking** (`unittest.mock`) replaces real dependencies with simulated objects:\n- `MagicMock`: Mock object that dynamically responds to all method calls and attributes.\n- `@patch('module.target_func')`: Decorator that temporarily patches a function during test execution.\n- Assertions: `mock.assert_called_once()`, `mock.assert_called_with(expected_arg)`.",
            "from unittest.mock import patch, MagicMock\n@patch('requests.get')\ndef test_api(mock_get):\n    mock_get.return_value.json.return_value = {'status': 'ok'}",
            "from unittest.mock import MagicMock\n\nclass CourseService:\n    def __init__(self, db_conn):\n        self.db = db_conn\n        \n    def get_course_title(self, course_id):\n        cursor = self.db.cursor()\n        cursor.execute(\"SELECT title FROM courses WHERE id = ?\", (course_id,))\n        row = cursor.fetchone()\n        return row[0] if row else \"Not Found\"\n\n# Unit test with mock database\nmock_conn = MagicMock()\nmock_cursor = MagicMock()\nmock_conn.cursor.return_value = mock_cursor\nmock_cursor.fetchone.return_value = (\"Python Programming Masterclass\",)\n\nservice = CourseService(mock_conn)\ntitle = service.get_course_title(101)\n\nprint(f\"Service retrieved title: '{title}'\")\nmock_cursor.execute.assert_called_once_with(\"SELECT title FROM courses WHERE id = ?\", (101,))\nprint(\"Verified mock database query execution!\")",
            "Service retrieved title: 'Python Programming Masterclass'\nVerified mock database query execution!",
            [
                "MagicMock simulates database connection and cursor without touching real databases.",
                "assert_called_once_with verifies exact query parameter binding."
            ],
            [
                "Patching where an object is defined instead of **where it is looked up/used**.",
                "Over-mocking to the point where tests verify mock setup rather than real business logic."
            ],
            [
                ("What is the golden rule of Python patching?", "Patch where the object is looked up (used), not where it is defined."),
                ("What does `mock.side_effect` allow you to do?", "Raise an exception when the mock is called or return different values sequentially."),
                ("What does the spec parameter do on a Mock?", "Restricts the mock to the attribute and method names of the real class, preventing typos.")
            ]
        ),
        format_lesson(
            "python",
            "Code quality", 20,
            [
                "Adhere to PEP 8 Python coding conventions",
                "Apply static analysis tools: flake8, ruff, black, and mypy",
                "Structure maintainable, modular Python software architectures"
            ],
            "Writing high-quality Python code requires adherence to established conventions and tooling:\n- **PEP 8**: 4 spaces, snake_case functions/variables, PascalCase classes, max line length (88-100 chars).\n- **Linters**: `flake8` or `ruff` (catches syntax errors and style violations).\n- **Formatters**: `black` (uncompromising, deterministic code formatter).\n- **Type Checking**: `mypy` (verifies type annotations statically).",
            "# PEP 8 standard formatting\nclass CourseManager:\n    def fetch_published(self, limit: int = 10) -> list[str]:\n        return [\"Python\", \"Java\"][:limit]",
            "import sys\n\nprint(\"Python Code Quality Checklist:\")\nprint(\"1. PEP 8 Compliance: 4 spaces, snake_case variables, UPPERCASE constants\")\nprint(\"2. Automated Formatting: 'ruff format .' or 'black .'\")\nprint(\"3. Static Linting: 'ruff check .' to catch bugs and unused imports\")\nprint(\"4. Type Checking: 'mypy .' for static typing validation\")\nprint(\"5. Security Auditing: 'bandit -r .' to detect vulnerabilities\")",
            "Python Code Quality Checklist:\n1. PEP 8 Compliance: 4 spaces, snake_case variables, UPPERCASE constants\n2. Automated Formatting: 'ruff format .' or 'black .'\n3. Static Linting: 'ruff check .' to catch bugs and unused imports\n4. Type Checking: 'mypy .' for static typing validation\n5. Security Auditing: 'bandit -r .' to detect vulnerabilities",
            [
                "Summarizes professional Python developer tooling stack.",
                "Emphasizes clean formatting, linting, and static typing."
            ],
            [
                "Ignoring unused imports and undefined variables.",
                "Writing massive 500-line functions instead of modular single-responsibility units."
            ],
            [
                ("Why has Ruff become the dominant Python linter in modern development?", "Written in Rust; executes 10-100x faster than legacy Python linters."),
                ("What is the purpose of a pre-commit hook in Git?", "Runs formatters and linters automatically before committing code."),
                ("How does explicit typing improve IDE autocompletion and maintainability?", "Enables IDEs and static analyzers to infer valid attributes and catch type mismatches before runtime.")
            ]
        )
    ]
    return {
        "title": "Module 7 - APIs, Databases, and Testing",
        "description": "Connect Python applications to external services and verify behavior.",
        "sequenceOrder": 7,
        "lessons": lessons
    }

def get_python_module_8():
    lessons = [
        format_lesson(
            "python",
            "Calculator and unit converter", 30,
            [
                "Build an interactive terminal calculator and unit converter",
                "Validate user numerical inputs and operation choices",
                "Structure reusable calculation functions"
            ],
            "In this project, we develop an interactive Calculator and Unit Converter in Python:\n- Arithmetic: Addition, subtraction, multiplication, true division, power.\n- Unit conversions: Temperature (Celsius <-> Fahrenheit), distance (Miles <-> Kilometers), memory (Bytes <-> MB/GB).\n- Input validation: Guarding against non-numeric entries and zero-division.",
            "def convert_celsius_to_fahrenheit(c: float) -> float:\n    return (c * 9/5) + 32",
            "class UnitConverter:\n    @staticmethod\n    def celsius_to_fahrenheit(c: float) -> float:\n        return (c * 9/5) + 32\n        \n    @staticmethod\n    def km_to_miles(km: float) -> float:\n        return km * 0.621371\n        \n    @staticmethod\n    def bytes_to_mb(b: int) -> float:\n        return b / (1024 * 1024)\n\nprint(\"Unit Converter Test Suite:\")\nprint(f\"100°C in Fahrenheit: {UnitConverter.celsius_to_fahrenheit(100):.1f}°F\")\nprint(f\"10 Kilometers in Miles: {UnitConverter.km_to_miles(10):.2f} miles\")\nprint(f\"10,485,760 Bytes in MB: {UnitConverter.bytes_to_mb(10485760):.2f} MB\")",
            "Unit Converter Test Suite:\n100°C in Fahrenheit: 212.0°F\n10 Kilometers in Miles: 6.21 miles\n10,485,760 Bytes in MB: 10.00 MB",
            [
                "Encapsulates conversion calculations as clean static methods.",
                "Computes conversions accurately with formatted output."
            ],
            [
                "Using integer division in temperature conversion (e.g. `9 // 5` which produces 1 instead of 1.8).",
                "Allowing negative values for absolute quantities (like Kelvin or file sizes)."
            ],
            [
                ("How would you adapt this to read interactive CLI commands in a loop?", "Use `while True:` with `input()` and a break condition on 'quit'."),
                ("How do you handle ValueError when user inputs non-numeric characters?", "Wrap `float(input())` in a try-except block."),
                ("What module in Python provides comprehensive unit conversions?", "Pint or custom conversion tables.")
            ]
        ),
        format_lesson(
            "python",
            "Expense tracker", 30,
            [
                "Build an expense tracker storing records in lists and dictionaries",
                "Filter and aggregate expenses by category and date",
                "Persist financial records to local JSON storage"
            ],
            "This project implements an Expense Tracker:\n- Record structure: ID, date, category (Food, Travel, Books, Tech), amount, description.\n- Operations: Add expense, list all expenses, calculate total and category summaries.\n- Persistence: Reads and writes records to a local JSON file.",
            "class ExpenseTracker:\n    def add_expense(self, category, amount, description): ...\n    def get_summary(self): ...",
            "from collections import defaultdict\n\nclass ExpenseTracker:\n    def __init__(self):\n        self.expenses = []\n        \n    def add_expense(self, category: str, amount: float, description: str):\n        self.expenses.append({\"category\": category, \"amount\": amount, \"desc\": description})\n        \n    def get_summary(self):\n        summary = defaultdict(float)\n        for e in self.expenses:\n            summary[e[\"category\"]] += e[\"amount\"]\n        return dict(summary)\n\ntracker = ExpenseTracker()\ntracker.add_expense(\"Education\", 49.99, \"LearnHub Python Masterclass Subscription\")\ntracker.add_expense(\"Books\", 35.50, \"Fluent Python 2nd Edition\")\ntracker.add_expense(\"Tech\", 120.00, \"Mechanical Keyboard\")\ntracker.add_expense(\"Books\", 24.00, \"Clean Code\")\n\nsummary = tracker.get_summary()\nprint(\"Expense Summary by Category:\")\nfor cat, total in summary.items():\n    print(f\"- {cat:12}: ${total:.2f}\")\nprint(f\"Total Expenses : ${sum(summary.values()):.2f}\")",
            "Expense Summary by Category:\n- Education   : $49.99\n- Books       : $59.50\n- Tech        : $120.00\nTotal Expenses : $229.49",
            [
                "Records categorized expense dictionaries.",
                "defaultdict aggregates spending by category in O(n) time.",
                "Computes total overall expenditure."
            ],
            [
                "Using float for enterprise currency transactions (use Decimal for strict accounting).",
                "Failing to handle empty expense lists in aggregation methods."
            ],
            [
                ("Why should Python's decimal.Decimal be used for financial accounting apps?", "Eliminates floating-point rounding inaccuracies."),
                ("How do you sort expenses by amount descending?", "`sorted(expenses, key=lambda e: e['amount'], reverse=True)`."),
                ("How do you export the expense report to CSV?", "Use `csv.DictWriter`.")
            ]
        ),
        format_lesson(
            "python",
            "Contact book", 30,
            [
                "Implement a full CRUD Contact Book application",
                "Search contacts by name, email, or phone number",
                "Persist contacts to disk using structured JSON"
            ],
            "The Contact Book application manages personal and professional contacts:\n- Attributes: Name, email, phone, tags.\n- Capabilities: Add contact, search by substring, update phone/email, delete by name.\n- File persistence with automatic loading on startup.",
            "class ContactBook:\n    def add_contact(self, name, phone, email): ...\n    def search(self, query): ...",
            "class ContactBook:\n    def __init__(self):\n        self.contacts = {}\n        \n    def add(self, name, phone, email):\n        self.contacts[name.lower()] = {\"name\": name, \"phone\": phone, \"email\": email}\n        \n    def search(self, term):\n        term = term.lower()\n        return [c for c in self.contacts.values() if term in c[\"name\"].lower() or term in c[\"email\"].lower()]\n\nbook = ContactBook()\nbook.add(\"Alex Morgan\", \"555-0192\", \"alex@learnhub.com\")\nbook.add(\"Sarah Connor\", \"555-0482\", \"sarah@learnhub.com\")\n\nmatches = book.search(\"learnhub.com\")\nprint(f\"Found {len(matches)} contacts matching 'learnhub.com':\")\nfor m in matches:\n    print(f\"- {m['name']} ({m['phone']}) <{m['email']}>\")",
            "Found 2 contacts matching 'learnhub.com':\n- Alex Morgan (555-0192) <alex@learnhub.com>\n- Sarah Connor (555-0482) <sarah@learnhub.com>",
            [
                "Maintains normalized lowercase lookup keys in dictionary.",
                "Substrings search matches against both name and email.",
                "Formats clean contact directory."
            ],
            [
                "Overwriting existing contacts with identical names without confirmation.",
                "Failing to validate phone number format using regex."
            ],
            [
                ("How do you validate email format before adding to the contact book?", "Use regular expressions via `re.match`."),
                ("How do you safely persist the contact book to disk?", "Use `json.dump(self.contacts, file, indent=2)` inside a context manager."),
                ("What data structure would allow fuzzy searching for misspelled contact names?", "Levenshtein distance algorithm or difflib.get_close_matches.")
            ]
        ),
        format_lesson(
            "python",
            "Quiz application", 30,
            [
                "Model interactive multiple-choice quiz questions",
                "Track student answers, compute final score percentage, and provide answer keys",
                "Manage state across multi-question assessments"
            ],
            "In this project, we create an Interactive Quiz Application:\n- Question data: Prompt text, list of options, correct option index, explanation.\n- Engine: Presents questions, captures user choices, calculates score, displays performance feedback.",
            "class QuizEngine:\n    def submit_answer(self, q_idx, chosen_option): ...",
            "class QuizApp:\n    def __init__(self, questions):\n        self.questions = questions\n        self.score = 0\n        \n    def evaluate(self, user_answers):\n        self.score = 0\n        for q, ans in zip(self.questions, user_answers):\n            if ans == q[\"answer\"]:\n                self.score += 1\n        return round((self.score / len(self.questions)) * 100.0, 1)\n\nquiz_questions = [\n    {\"prompt\": \"What is the keyword for defining a function in Python?\", \"answer\": 1, \"options\": [\"func\", \"def\", \"function\"]},\n    {\"prompt\": \"Which built-in type is immutable in Python?\", \"answer\": 2, \"options\": [\"list\", \"dict\", \"tuple\"]},\n    {\"prompt\": \"What does len() return?\", \"answer\": 0, \"options\": [\"Length\", \"Last item\", \"Capacity\"]}\n]\n\napp = QuizApp(quiz_questions)\nstudent_answers = [1, 2, 0] # All correct\nfinal_score = app.evaluate(student_answers)\nprint(f\"Quiz Results: {app.score}/{len(quiz_questions)} Correct ({final_score}%)\")\nprint(\"Status: PASSED WITH DISTINCTION!\")",
            "Quiz Results: 3/3 Correct (100.0%)\nStatus: PASSED WITH DISTINCTION!",
            [
                "Models quiz questions as structured data.",
                "Evaluates student answers against answer keys and computes percentage."
            ],
            [
                "Hardcoding answer indices without validating that they exist in the options list.",
                "Crashing on invalid user choices outside valid range."
            ],
            [
                ("How would you shuffle question order and option order without altering answer keys?", "Use `random.shuffle()` and update answer index accordingly."),
                ("How can quiz questions be loaded dynamically from an external JSON file?", "Use `json.load()` to parse question bank from disk."),
                ("How would you adapt this for timed quizzes?", "Use time.time() to record start time and enforce duration limits.")
            ]
        ),
        format_lesson(
            "python",
            "File analyzer", 30,
            [
                "Read arbitrary text files and compute linguistic statistics",
                "Count total lines, words, characters, and unique vocabulary size",
                "Report top-10 most frequent words using collections.Counter"
            ],
            "The File Analyzer reads any text file and generates a comprehensive content report:\n- Metrics: Line count, word count, character count.\n- Vocabulary: Count of unique words.\n- Word Frequency: Top 10 most frequent words (excluding common stop words).",
            "from collections import Counter\ndef analyze_text(content: str): ...",
            "from collections import Counter\nimport re\n\nsample_text = \"\"\"Python is an interpreted, high-level, general-purpose programming language.\nPython's design philosophy emphasizes code readability.\nPython provides rich standard libraries and clean syntax.\"\"\"\n\nlines = sample_text.splitlines()\nwords = re.findall(r'\\b[a-zA-Z]+\\b', sample_text.lower())\nword_counts = Counter(words)\n\nprint(\"File Analysis Report:\")\nprint(f\"- Total Lines       : {len(lines)}\")\nprint(f\"- Total Words       : {len(words)}\")\nprint(f\"- Unique Words      : {len(word_counts)}\")\nprint(f\"- Top 3 Frequent    : {word_counts.most_common(3)}\")",
            "File Analysis Report:\n- Total Lines       : 3\n- Total Words       : 21\n- Unique Words      : 18\n- Top 3 Frequent    : [('python', 2), ('is', 1), ('an', 1)]",
            [
                "re.findall tokenizes words ignoring punctuation.",
                "Counter computes frequency statistics.",
                "Reports line, word, and top frequency metrics."
            ],
            [
                "Splitting on spaces alone (`text.split(' ')`), which leaves attached punctuation on words.",
                "Loading giant multi-gigabyte files entirely into a single string (stream line by line instead)."
            ],
            [
                ("How do you filter out stop words (like 'the', 'is', 'at') from the report?", "Maintain a set of stop words and filter: `[w for w in words if w not in stop_words]`."),
                ("How do you calculate average word length?", "`sum(len(w) for w in words) / len(words)`."),
                ("How would you export this report to an HTML summary?", "Use string templates or Jinja2 to format the report into an HTML page.")
            ]
        ),
        format_lesson(
            "python",
            "API data viewer", 30,
            [
                "Consume external REST API endpoints",
                "Filter, format, and display structured JSON records",
                "Implement graceful fallback on connectivity timeouts"
            ],
            "The API Data Viewer connects to an external HTTP API, validates response data, filters records based on query parameters, and presents a clean, formatted terminal dashboard.",
            "def fetch_and_display(endpoint: str): ...",
            "import json\n\n# Simulated REST API payload\nmock_api_response = \"\"\"[\n    {\"id\": 101, \"title\": \"Java Programming Masterclass\", \"category\": \"Programming\", \"duration\": 60},\n    {\"id\": 102, \"title\": \"Python Programming Masterclass\", \"category\": \"Programming\", \"duration\": 50},\n    {\"id\": 103, \"title\": \"Modern React & Vite UI\", \"category\": \"Frontend\", \"duration\": 35}\n]\"\"\"\n\ncourses = json.loads(mock_api_response)\nprint(\"=== LearnHub Active Course Catalog ===\")\nprint(f\"{'ID':<5} {'Course Title':<35} {'Category':<15} {'Duration':<10}\")\nprint(\"-\" * 70)\nfor c in courses:\n    print(f\"{c['id']:<5} {c['title']:<35} {c['category']:<15} {c['duration']:>2} hours\")",
            "=== LearnHub Active Course Catalog ===\nID    Course Title                        Category        Duration  \n----------------------------------------------------------------------\n101   Java Programming Masterclass        Programming     60 hours\n102   Python Programming Masterclass      Programming     50 hours\n103   Modern React & Vite UI              Frontend        35 hours",
            [
                "Parses structured JSON response.",
                "Formats output into an aligned terminal table."
            ],
            [
                "Printing raw JSON dictionaries directly to users instead of formatted tables.",
                "Failing to handle missing attributes in API response objects."
            ],
            [
                ("How do you format table output automatically in Python?", "Use the `tabulate` third-party library or f-string alignment specifiers."),
                ("How do you cache API responses locally to avoid redundant network calls?", "Store response JSON to disk with a timestamp or use `requests_cache`."),
                ("How do you handle API pagination (e.g. `?page=1&limit=50`)?", "Iterate through pages in a while loop until the `next_page` URL or results array is empty.")
            ]
        ),
        format_lesson(
            "python",
            "Database-backed record manager", 35,
            [
                "Build a persistent database-backed Student Course Record Manager",
                "Implement secure CRUD database operations using parameterized SQL",
                "Manage relational integrity across students, courses, and progress records"
            ],
            "This project develops a complete Database-Backed Record Manager in Python using SQLite:\n- Schema: `students`, `courses`, `enrollments`.\n- Functions: Add student, enroll in course, record lesson completion, display student transcripts.\n- Fully protected against SQL injection using parameterized queries.",
            "class DatabaseRecordManager:\n    def enroll_student(self, student_id, course_id): ...",
            "import sqlite3\n\nconn = sqlite3.connect(\":memory:\")\ncursor = conn.cursor()\n\ncursor.execute(\"CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT UNIQUE);\")\ncursor.execute(\"CREATE TABLE enrollments (student_id INT, course_title TEXT, completed_lessons INT, total INT);\")\n\ncursor.execute(\"INSERT INTO students (name) VALUES (?);\", (\"Alex Morgan\",))\ns_id = cursor.lastrowid\ncursor.execute(\"INSERT INTO enrollments VALUES (?, ?, ?, ?);\", (s_id, \"Python Programming Masterclass\", 40, 79))\nconn.commit()\n\ncursor.execute(\"\"\"SELECT s.name, e.course_title, e.completed_lessons, e.total \n                  FROM students s JOIN enrollments e ON s.id = e.student_id;\"\"\")\nrow = cursor.fetchone()\nprogress = (row[2] / row[3]) * 100.0\nprint(f\"Student: {row[0]}\")\nprint(f\"Course : {row[1]}\")\nprint(f\"Progress: {row[2]}/{row[3]} lessons ({progress:.1f}%)\")\nconn.close()",
            "Student: Alex Morgan\nCourse : Python Programming Masterclass\nProgress: 40/79 lessons (50.6%)",
            [
                "Creates relational database schema.",
                "Executes relational join query and calculates progress percentage accurately."
            ],
            [
                "Not committing transactions before querying.",
                "Using raw string concatenation instead of parameterized tuples."
            ],
            [
                ("How would you add foreign key constraint enforcement in SQLite?", "Execute `PRAGMA foreign_keys = ON;` on connection creation."),
                ("What is an Object-Relational Mapper (ORM) like SQLAlchemy?", "A library that maps database tables directly to Python classes and objects."),
                ("How do you handle database migrations when table schemas evolve?", "Use tools like Alembic or Flyway.")
            ]
        ),
        format_lesson(
            "python",
            "Final revision and challenge set", 40,
            [
                "Consolidate all 8 modules of the Python Programming Masterclass",
                "Solve multi-concept software engineering challenges",
                "Review data structures, OOP design, file handling, and database integration"
            ],
            "This final review capstone provides a comprehensive review of all core Python domains:\n1. Python Fundamentals & Data Types\n2. Conditions & Loops\n3. Built-in Data Structures & Comprehensions\n4. Functions, Modules, and Environments\n5. Object-Oriented Programming & Dataclasses\n6. Exceptions, Files, and Standard Libraries\n7. APIs, Databases, and Unit Testing\n8. Full-Stack Python Projects.",
            "# Python Masterclass Complete Certification Review\nclass MasterclassFinalReview: ...",
            "print(\"====================================================\")\nprint(\"  CONGRATULATIONS: PYTHON PROGRAMMING MASTERCLASS   \")\nprint(\"====================================================\")\nprint(\"Curriculum Coverage Summary:\")\nprint(\"- Module 1: Python Fundamentals (10 lessons)\")\nprint(\"- Module 2: Conditions and Loops (9 lessons)\")\nprint(\"- Module 3: Python Data Structures (10 lessons)\")\nprint(\"- Module 4: Functions, Modules, and Environments (10 lessons)\")\nprint(\"- Module 5: Object-Oriented Python (10 lessons)\")\nprint(\"- Module 6: Exceptions, Files, and Standard Libraries (12 lessons)\")\nprint(\"- Module 7: APIs, Databases, and Testing (10 lessons)\")\nprint(\"- Module 8: Python Projects and Revision (8 lessons)\")\nprint(\"Total: 79 comprehensive lessons mastered!\")\nprint(\"====================================================\")",
            "====================================================\n  CONGRATULATIONS: PYTHON PROGRAMMING MASTERCLASS   \n====================================================\nCurriculum Coverage Summary:\n- Module 1: Python Fundamentals (10 lessons)\n- Module 2: Conditions and Loops (9 lessons)\n- Module 3: Python Data Structures (10 lessons)\n- Module 4: Functions, Modules, and Environments (10 lessons)\n- Module 5: Object-Oriented Python (10 lessons)\n- Module 6: Exceptions, Files, and Standard Libraries (12 lessons)\n- Module 7: APIs, Databases, and Testing (10 lessons)\n- Module 8: Python Projects and Revision (8 lessons)\nTotal: 79 comprehensive lessons mastered!\n====================================================",
            [
                "Summarizes all 8 modules and 79 required curriculum lessons.",
                "Validates comprehensive Python software engineering mastery."
            ],
            [
                "Relying on basic scripting habits without adopting modular OOP architecture.",
                "Neglecting automated unit tests and typing annotations in production code."
            ],
            [
                ("What are the key advantages of Python in modern cloud and AI backends?", "Expressive syntax, rapid development velocity, immense library ecosystem, and high interoperability with C/C++ runtimes."),
                ("How does the Global Interpreter Lock (GIL) affect Python multithreading?", "Prevents multiple native threads from executing Python bytecodes simultaneously in CPython; bypassed using multiprocessing or asyncio."),
                ("What command builds a distributable Python wheel package?", "`python -m build`.")
            ]
        )
    ]
    return {
        "title": "Module 8 - Python Projects and Revision",
        "description": "Apply Python concepts in practical applications.",
        "sequenceOrder": 8,
        "lessons": lessons
    }

print("Python modules 7 & 8 ready.")
