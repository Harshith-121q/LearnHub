from formatter import format_lesson

def get_java_module_7():
    lessons = [
        format_lesson(
            "java",
            "Database fundamentals", 25,
            [
                "Understand relational database management system (RDBMS) architecture",
                "Define tables, rows, columns, primary keys, and foreign keys",
                "Model one-to-one, one-to-many, and many-to-many relationships"
            ],
            "A **Relational Database** (such as MySQL or PostgreSQL) stores structured data in tables composed of rows (records) and columns (attributes). Core schema concepts:\n- **Primary Key (PK)**: A column or set of columns that uniquely identifies every row in a table (e.g. `id`). Cannot be null.\n- **Foreign Key (FK)**: A column referencing the primary key of another table, establishing relational integrity between entities.\n- **Relationships**:\n  - One-to-Many: One Course has Many Modules.\n  - Many-to-Many: Students enroll in Many Courses, and Courses have Many Students (modeled via a join table `enrollments`).",
            "-- Example relational schema:\nCREATE TABLE courses (\n    id BIGINT AUTO_INCREMENT PRIMARY KEY,\n    title VARCHAR(150) NOT NULL\n);\nCREATE TABLE modules (\n    id BIGINT AUTO_INCREMENT PRIMARY KEY,\n    course_id BIGINT NOT NULL,\n    title VARCHAR(150) NOT NULL,\n    FOREIGN KEY (course_id) REFERENCES courses(id)\n);",
            "public class DatabaseFundamentalsDemo {\n    public static void main(String[] args) {\n        System.out.println(\"LearnHub Relational Schema Architecture:\");\n        System.out.println(\"- Table: courses (PK: id, title, category, status)\");\n        System.out.println(\"- Table: modules (PK: id, FK: course_id, sequence_order)\");\n        System.out.println(\"- Table: lessons (PK: id, FK: module_id, sequence_order, content)\");\n        System.out.println(\"- Table: enrollments (PK: id, FK: student_id, FK: course_id, progress)\");\n        System.out.println(\"Relational integrity enforced through foreign key constraints.\");\n    }\n}",
            "LearnHub Relational Schema Architecture:\n- Table: courses (PK: id, title, category, status)\n- Table: modules (PK: id, FK: course_id, sequence_order)\n- Table: lessons (PK: id, FK: module_id, sequence_order, content)\n- Table: enrollments (PK: id, FK: student_id, FK: course_id, progress)\nRelational integrity enforced through foreign key constraints.",
            [
                "Deconstructs normalized database entities and relationships.",
                "Emphasizes primary and foreign key constraints."
            ],
            [
                "Failing to define index on foreign key columns, causing table scans during relational queries.",
                "Designing many-to-many relationships without an intermediary join table."
            ],
            [
                ("What is database normalization and what is its primary objective?", "Eliminate redundant data and prevent insertion/update anomalies."),
                ("What does the ON DELETE CASCADE constraint do?", "Automatically deletes child records when the referenced parent record is deleted."),
                ("Why is a composite key used in join tables?", "Enforces uniqueness of paired foreign keys (e.g. unique student_id + course_id).")
            ]
        ),
        format_lesson(
            "java",
            "SQL basics", 25,
            [
                "Author fundamental SQL queries: SELECT, INSERT, UPDATE, and DELETE",
                "Filter and sort query results using WHERE, LIKE, ORDER BY, and LIMIT",
                "Perform inner and outer joins to combine data across tables"
            ],
            "**Structured Query Language (SQL)** is the standard language for querying and manipulating relational databases. Core operations (CRUD):\n- Create: `INSERT INTO table (col1, col2) VALUES (?, ?);`\n- Read: `SELECT col1, col2 FROM table WHERE condition ORDER BY col1 DESC;`\n- Update: `UPDATE table SET col1 = ? WHERE condition;`\n- Delete: `DELETE FROM table WHERE condition;`\n- Joins: `SELECT c.title, m.title FROM courses c INNER JOIN modules m ON c.id = m.course_id;`\nCritical rule: Always include a `WHERE` clause in `UPDATE` and `DELETE` queries to prevent modifying the entire table!",
            "SELECT c.title, COUNT(m.id) AS module_count\nFROM courses c\nLEFT JOIN modules m ON c.id = m.course_id\nWHERE c.status = 'PUBLISHED'\nGROUP BY c.id\nORDER BY module_count DESC;",
            "public class SQLBasicsDemo {\n    public static void main(String[] args) {\n        String query = \"SELECT c.id, c.title, u.username AS instructor \" +\n                       \"FROM courses c \" +\n                       \"JOIN users u ON c.instructor_id = u.id \" +\n                       \"WHERE c.status = 'PUBLISHED' \" +\n                       \"ORDER BY c.title ASC;\";\n        \n        System.out.println(\"Constructed SQL Query:\\n\" + query);\n    }\n}",
            "Constructed SQL Query:\nSELECT c.id, c.title, u.username AS instructor FROM courses c JOIN users u ON c.instructor_id = u.id WHERE c.status = 'PUBLISHED' ORDER BY c.title ASC;",
            [
                "Constructs a standard multi-table relational join in SQL.",
                "Filters by published status and orders alphabetically."
            ],
            [
                "Executing `UPDATE` or `DELETE` without a `WHERE` clause, modifying or erasing every row in the table.",
                "Using `SELECT *` in production code instead of explicitly naming required columns."
            ],
            [
                ("What is the difference between INNER JOIN and LEFT JOIN?", "INNER JOIN returns only matching rows; LEFT JOIN returns all rows from the left table plus matches from right."),
                ("How does the WHERE clause differ from the HAVING clause?", "WHERE filters rows before aggregation; HAVING filters aggregated groups after GROUP BY."),
                ("What does the SQL command `DROP TABLE` do compared to `TRUNCATE TABLE`?", "DROP deletes table schema and data; TRUNCATE deletes all rows while preserving table schema.")
            ]
        ),
        format_lesson(
            "java",
            "JDBC introduction", 25,
            [
                "Understand the Java Database Connectivity (JDBC) API architecture",
                "Load JDBC drivers and establish database connections",
                "Execute statements and process returned ResultSet records"
            ],
            "**JDBC (Java Database Connectivity)** is the standard Java API that connects Java applications to relational databases. Core JDBC interfaces (in `java.sql`):\n1. `Driver`: Vendor-specific database driver (e.g. `com.mysql.cj.jdbc.Driver`).\n2. `DriverManager`: Factory managing drivers and creating connections.\n3. `Connection`: Represents the active session/socket to the database.\n4. `Statement` / `PreparedStatement`: Encapsulates SQL commands.\n5. `ResultSet`: A tabular cursor containing query results (`rs.next()`, `rs.getString()`, `rs.getInt()`).",
            "String url = \"jdbc:mysql://localhost:3306/learnhub_db\";\ntry (Connection conn = DriverManager.getConnection(url, user, pass);\n     PreparedStatement ps = conn.prepareStatement(\"SELECT title FROM courses\");\n     ResultSet rs = ps.executeQuery()) {\n    while (rs.next()) { System.out.println(rs.getString(\"title\")); }\n}",
            "public class JDBCIntroDemo {\n    public static void main(String[] args) {\n        System.out.println(\"JDBC Architecture Flow:\");\n        System.out.println(\"1. Application -> DriverManager.getConnection(url, user, pass)\");\n        System.out.println(\"2. Connection -> conn.prepareStatement(sql)\");\n        System.out.println(\"3. PreparedStatement -> ps.executeQuery() / ps.executeUpdate()\");\n        System.out.println(\"4. ResultSet -> cursor navigation with rs.next()\");\n        System.out.println(\"5. AutoCloseable resources automatically closed.\");\n    }\n}",
            "JDBC Architecture Flow:\n1. Application -> DriverManager.getConnection(url, user, pass)\n2. Connection -> conn.prepareStatement(sql)\n3. PreparedStatement -> ps.executeQuery() / ps.executeUpdate()\n4. ResultSet -> cursor navigation with rs.next()\n5. AutoCloseable resources automatically closed.",
            [
                "Outlines the 5-step lifecycle of standard JDBC data access.",
                "Emphasizes clean cursor navigation and resource reclamation."
            ],
            [
                "Forgetting to advance the ResultSet cursor with `rs.next()` before reading data columns.",
                "Failing to close Connection, Statement, and ResultSet objects, causing database connection pool leaks."
            ],
            [
                ("What does rs.next() return when the cursor reaches the end of the ResultSet?", "Returns false."),
                ("What is a Connection Pool (e.g. HikariCP) and why is it used instead of raw DriverManager calls?", "Reuses established physical database connections to avoid TCP handshake overhead."),
                ("What exception is thrown by all JDBC methods when a database communication failure occurs?", "java.sql.SQLException.")
            ]
        ),
        format_lesson(
            "java",
            "Secure connection configuration", 20,
            [
                "Read database connection parameters securely from environment variables",
                "Prevent hardcoding credentials in source code and version control",
                "Configure Spring Boot application.properties with externalized profiles"
            ],
            "Security rule: **NEVER hardcode database usernames, passwords, or connection strings in source code.**\nIf committed to version control, secrets can be leaked to malicious actors. Instead:\n- Externalize credentials using OS environment variables (e.g. `DB_URL`, `DB_USER`, `DB_PASSWORD`).\n- In Spring Boot, read environment variables with fallback defaults in `application.properties`: `spring.datasource.password=${DB_PASSWORD:default}`.\n- In standalone Java, read secrets via `System.getenv(\"DB_PASSWORD\")`.",
            "// Secure retrieval pattern\nString dbUrl = System.getenv().getOrDefault(\"DB_URL\", \"jdbc:mysql://localhost:3306/learnhub_db\");\nString dbUser = System.getenv().getOrDefault(\"DB_USER\", \"root\");\nString dbPassword = System.getenv(\"DB_PASSWORD\");\nif (dbPassword == null) throw new IllegalStateException(\"DB_PASSWORD environment variable must be set!\");",
            "public class SecureConfigDemo {\n    public static void main(String[] args) {\n        String dbUrl = System.getenv(\"DB_URL\");\n        String dbUser = System.getenv(\"DB_USER\");\n        boolean isPasswordSet = System.getenv(\"DB_PASSWORD\") != null;\n        \n        System.out.println(\"Database Configuration Status:\");\n        System.out.println(\"URL Configured: \" + (dbUrl != null ? \"Externalized\" : \"Default Localhost\"));\n        System.out.println(\"User Configured: \" + (dbUser != null ? dbUser : \"learnhub_user\"));\n        System.out.println(\"Password Masked: \" + (isPasswordSet ? \"[PROTECTED IN ENV]\" : \"[NOT SET]\"));\n    }\n}",
            "Database Configuration Status:\nURL Configured: Default Localhost\nUser Configured: learnhub_user\nPassword Masked: [NOT SET]",
            [
                "Inspects environment variables dynamically without committing plaintext secrets.",
                "Enforces password presence before initiating network connections."
            ],
            [
                "Committing database passwords or AWS secret keys to Git repositories.",
                "Printing raw passwords in application logs during startup error diagnostics."
            ],
            [
                ("What file should be added to .gitignore to prevent committing local environment secrets?", "`.env` or `application-local.properties`."),
                ("How does Spring Boot resolve `${DB_PASSWORD}` in application.properties?", "Checks command-line args, OS environment variables, and system properties in order of precedence."),
                ("What is a Secret Manager (e.g. AWS Secrets Manager, HashiCorp Vault)?", "Dedicated enterprise infrastructure for rotating, storing, and fetching credentials at runtime.")
            ]
        ),
        format_lesson(
            "java",
            "PreparedStatement", 25,
            [
                "Prevent SQL Injection attacks using PreparedStatement",
                "Bind parameters safely using setString, setInt, setLong, and setDouble",
                "Understand pre-compilation and database query plan caching"
            ],
            "**SQL Injection** is a severe security vulnerability where untrusted user input modifies the syntax of an SQL command. If you concatenate raw strings into SQL (`\"SELECT * FROM users WHERE user = '\" + input + \"'\"`), an attacker inputting `' OR '1'='1` can bypass authentication or dump the entire database.\n**PreparedStatement** completely neutralizes SQL injection by pre-compiling the SQL query structure in the database engine and transmitting user parameters separately as pure data values, never as executable SQL tokens.",
            "// VULNERABLE: \"SELECT * FROM users WHERE name = '\" + userInput + \"'\"\n// SECURE (PreparedStatement):\nString sql = \"SELECT * FROM users WHERE name = ? AND active = ?\";\ntry (PreparedStatement ps = conn.prepareStatement(sql)) {\n    ps.setString(1, userInput); // Bound as pure data\n    ps.setBoolean(2, true);\n    ResultSet rs = ps.executeQuery();\n}",
            "public class PreparedStatementDemo {\n    public static void main(String[] args) {\n        String untrustedInput = \"admin' OR '1'='1\";\n        String queryTemplate = \"SELECT * FROM users WHERE username = ? AND password_hash = ?\";\n        \n        System.out.println(\"Parameterized Query Template:\");\n        System.out.println(queryTemplate);\n        System.out.println(\"\\nBinding Untrusted Input:\");\n        System.out.println(\"Param 1 bound safely as text literal: \\\"\" + untrustedInput + \"\\\"\");\n        System.out.println(\"Result: Malicious SQL logic is treated strictly as text data, preventing injection.\");\n    }\n}",
            "Parameterized Query Template:\nSELECT * FROM users WHERE username = ? AND password_hash = ?\n\nBinding Untrusted Input:\nParam 1 bound safely as text literal: \"admin' OR '1'='1\"\nResult: Malicious SQL logic is treated strictly as text data, preventing injection.",
            [
                "The ? placeholder is sent to the database parser first.",
                "Untrusted input is bound strictly as data parameter #1, neutralizing injection."
            ],
            [
                "Concatenating user input into an SQL string instead of using `?` placeholders.",
                "Using 0-based indexing for JDBC parameters; JDBC parameters are strictly **1-indexed** (`ps.setString(1, ...)`)."
            ],
            [
                ("Are JDBC parameter placeholders 0-indexed or 1-indexed?", "1-indexed."),
                ("Why does PreparedStatement offer better performance than Statement for repeated queries?", "The database compiles and caches the execution plan once and reuses it for subsequent runs."),
                ("Can table names or column names be bound using PreparedStatement `?` placeholders?", "No, placeholders can only be used for literal data values.")
            ]
        ),
        format_lesson(
            "java",
            "CRUD operations", 30,
            [
                "Implement complete Create, Read, Update, and Delete operations via JDBC",
                "Retrieve generated auto-increment primary keys using Statement.RETURN_GENERATED_KEYS",
                "Manage connection pooling and resource closure"
            ],
            "A standard enterprise Data Access Object (DAO) or Repository encapsulates CRUD operations:\n1. **Create**: `executeUpdate()` with `Statement.RETURN_GENERATED_KEYS` to capture the database-generated ID.\n2. **Read**: `executeQuery()` with `ResultSet` mapping rows to domain objects.\n3. **Update**: `executeUpdate()` modifying fields by primary key, returning the count of modified rows.\n4. **Delete**: `executeUpdate()` removing records by primary key.",
            "// Insert with generated key\nPreparedStatement ps = conn.prepareStatement(\"INSERT INTO courses (title) VALUES (?)\", Statement.RETURN_GENERATED_KEYS);\nps.setString(1, \"Java Masterclass\");\nps.executeUpdate();\nResultSet keys = ps.getGeneratedKeys();\nif (keys.next()) long id = keys.getLong(1);",
            "public class CRUDOperationsDemo {\n    public static void main(String[] args) {\n        System.out.println(\"LearnHub DAO Implementation Pattern:\");\n        System.out.println(\"[CREATE] INSERT INTO courses (title, category) VALUES (?, ?)\");\n        System.out.println(\"[READ]   SELECT id, title, category FROM courses WHERE id = ?\");\n        System.out.println(\"[UPDATE] UPDATE courses SET title = ?, category = ? WHERE id = ?\");\n        System.out.println(\"[DELETE] DELETE FROM courses WHERE id = ?\");\n        System.out.println(\"All operations executed within try-with-resources blocks.\");\n    }\n}",
            "LearnHub DAO Implementation Pattern:\n[CREATE] INSERT INTO courses (title, category) VALUES (?, ?)\n[READ]   SELECT id, title, category FROM courses WHERE id = ?\n[UPDATE] UPDATE courses SET title = ?, category = ? WHERE id = ?\n[DELETE] DELETE FROM courses WHERE id = ?\nAll operations executed within try-with-resources blocks.",
            [
                "Outlines the standard 4-phase CRUD repository pattern.",
                "Demonstrates SQL command templates and return value expectations."
            ],
            [
                "Checking `rs.next()` on a ResultSet returned by `executeUpdate()` (`executeUpdate()` returns an `int` count, not a ResultSet).",
                "Failing to check the integer return count of update/delete to verify whether any row actually matched."
            ],
            [
                ("What does executeUpdate() return?", "An integer representing the number of rows affected by INSERT, UPDATE, or DELETE."),
                ("How do you retrieve an auto-incremented primary key generated by MySQL in JDBC?", "Pass `Statement.RETURN_GENERATED_KEYS` to prepareStatement and call `ps.getGeneratedKeys()`."),
                ("What does a return value of 0 from `UPDATE users SET name = ? WHERE id = 999` indicate?", "No record with ID 999 existed in the table.")
            ]
        ),
        format_lesson(
            "java",
            "Transactions", 25,
            [
                "Understand ACID database transaction properties (Atomicity, Consistency, Isolation, Durability)",
                "Manage manual transactions in JDBC using setAutoCommit(false), commit(), and rollback()",
                "Handle transaction failures gracefully in multi-step business operations"
            ],
            "A **Transaction** is a logical unit of work that bundles multiple database operations. Transactions must satisfy **ACID** properties:\n- **Atomicity**: 'All-or-Nothing'—either all operations succeed, or all are rolled back.\n- **Consistency**: The database transitions from one valid state to another, respecting all constraints.\n- **Isolation**: Concurrent transactions execute without interfering with each other.\n- **Durability**: Once committed, changes survive system crashes.\nIn JDBC: disable auto-commit with `conn.setAutoCommit(false)`, perform operations, call `conn.commit()`, and catch exceptions to call `conn.rollback()`.",
            "try {\n    conn.setAutoCommit(false);\n    deductBalance(conn, fromAcc, 100);\n    creditBalance(conn, toAcc, 100);\n    conn.commit(); // Atomic commit\n} catch (SQLException e) {\n    conn.rollback(); // Undo everything on failure!\n    throw e;\n} finally {\n    conn.setAutoCommit(true);\n}",
            "public class TransactionsDemo {\n    public static void main(String[] args) {\n        System.out.println(\"Transaction Execution Workflow:\");\n        System.out.println(\"1. conn.setAutoCommit(false); // Begin transaction\");\n        System.out.println(\"2. Deduct $100 from Account A (OK)\");\n        System.out.println(\"3. Credit $100 to Account B (OK)\");\n        System.out.println(\"4. conn.commit(); // Transaction committed atomically\");\n        System.out.println(\"5. If an error occurs in step 2 or 3 -> catch block invokes conn.rollback();\");\n    }\n}",
            "Transaction Execution Workflow:\n1. conn.setAutoCommit(false); // Begin transaction\n2. Deduct $100 from Account A (OK)\n3. Credit $100 to Account B (OK)\n4. conn.commit(); // Transaction committed atomically\n5. If an error occurs in step 2 or 3 -> catch block invokes conn.rollback();",
            [
                "Illustrates the atomic two-phase transfer workflow.",
                "Guarantees that money cannot disappear if an error occurs midway."
            ],
            [
                "Leaving `autoCommit(false)` enabled on a connection returned to a connection pool, causing subsequent users' queries to sit in uncommitted transactions.",
                "Forgetting to call `conn.rollback()` in the catch block when an operation fails."
            ],
            [
                ("What does the 'A' in ACID stand for and what does it mean?", "Atomicity: all statements succeed or none take effect."),
                ("How does Spring Framework manage transactions declaratively?", "Via the `@Transactional` annotation using AOP proxies."),
                ("What are database transaction isolation levels (e.g. READ COMMITTED, SERIALIZABLE)?", "They dictate how visible uncommitted changes from concurrent transactions are to each other.")
            ]
        ),
        format_lesson(
            "java",
            "Unit testing with JUnit", 25,
            [
                "Write automated unit tests using JUnit 5 (Jupiter)",
                "Structure tests using the Arrange-Act-Assert (AAA) pattern",
                "Apply assertions (assertEquals, assertTrue, assertThrows) to verify behavior"
            ],
            "**Unit Testing** verifies that individual units of source code (methods, classes) perform as designed in isolation. Modern Java uses **JUnit 5 (Jupiter)**:\n- `@Test`: Marks a method as a test case.\n- `@BeforeEach` / `@AfterEach`: Setup and teardown methods executed before/after every test.\n- **Arrange-Act-Assert (AAA)**:\n  1. Arrange: Set up test objects and input data.\n  2. Act: Execute the method under test.\n  3. Assert: Verify the actual result matches expected behavior using `assertEquals()`, `assertTrue()`, `assertThrows()`.",
            "import org.junit.jupiter.api.Test;\nimport static org.junit.jupiter.api.Assertions.*;\n\n@Test\nvoid shouldCalculateProgressAccurately() {\n    // Arrange\n    Enrollment enrollment = new Enrollment(student, course);\n    // Act\n    enrollment.recalculateProgress(5, 10);\n    // Assert\n    assertEquals(50.0, enrollment.getProgressPercentage());\n}",
            "public class JUnitDemo {\n    public static int calculateProgress(int completed, int total) {\n        if (total <= 0) return 0;\n        return (int) Math.round(((double) completed / total) * 100.0);\n    }\n    \n    public static void main(String[] args) {\n        // Simulating JUnit Assertions\n        System.out.println(\"Running Unit Tests:\");\n        \n        int result1 = calculateProgress(10, 20);\n        assertTest(\"shouldCalculateFiftyPercent\", result1 == 50);\n        \n        int result2 = calculateProgress(0, 50);\n        assertTest(\"shouldReturnZeroOnNoCompleted\", result2 == 0);\n        \n        int result3 = calculateProgress(50, 50);\n        assertTest(\"shouldReturnHundredOnFullCompletion\", result3 == 100);\n        \n        System.out.println(\"All simulated tests passed!\");\n    }\n    \n    static void assertTest(String testName, boolean condition) {\n        if (!condition) throw new AssertionError(\"FAILED: \" + testName);\n        System.out.println(\"PASSED: \" + testName);\n    }\n}",
            "Running Unit Tests:\nPASSED: shouldCalculateFiftyPercent\nPASSED: shouldReturnZeroOnNoCompleted\nPASSED: shouldReturnHundredOnFullCompletion\nAll simulated tests passed!",
            [
                "Demonstrates the AAA unit testing paradigm.",
                "Tests normal calculation, zero boundary condition, and 100% completion."
            ],
            [
                "Writing tests with nondeterministic results that depend on real system clocks or live networks.",
                "Putting multiple unrelated assertions in a single test without clear failure messages."
            ],
            [
                ("How do you test that a method throws an expected exception in JUnit 5?", "Use `assertThrows(ExpectedException.class, () -> methodCall())`."),
                ("What does the `@Disabled` annotation do in JUnit 5?", "Skips the annotated test method during execution."),
                ("Why should unit tests never connect to a live production database?", "Unit tests must be fast, isolated, deterministic, and free from external side-effects.")
            ]
        ),
        format_lesson(
            "java",
            "Mocking introduction", 20,
            [
                "Understand the purpose of test doubles and mocks in unit testing",
                "Isolate business logic from databases and network dependencies using Mockito",
                "Stub method behaviors (when-then) and verify invocations"
            ],
            "When testing a service class (e.g. `CourseService`), unit tests should NOT connect to a real database or send real network emails. **Mocking** creates simulated 'test double' objects that mimic the behavior of real dependencies.\n- Framework: **Mockito** (`org.mockito:mockito-core`).\n- `@Mock`: Creates a mock instance.\n- `when(mock.find(id)).thenReturn(data)`: Stubs a method response.\n- `verify(mock, times(1)).save(any())`: Verifies that a collaborating method was invoked.",
            "CourseRepository mockRepo = mock(CourseRepository.class);\nwhen(mockRepo.findById(10L)).thenReturn(Optional.of(sampleCourse));\nCourse result = service.getCourse(10L);\nverify(mockRepo).findById(10L);",
            "public class MockingDemo {\n    public static void main(String[] args) {\n        System.out.println(\"Mockito Unit Testing Pattern:\");\n        System.out.println(\"1. @Mock CourseRepository mockCourseRepo;\");\n        System.out.println(\"2. @InjectMocks CourseService courseService;\");\n        System.out.println(\"3. when(mockCourseRepo.findById(1L)).thenReturn(Optional.of(course));\");\n        System.out.println(\"4. CourseSummaryResponse res = courseService.getCourseSummary(1L);\");\n        System.out.println(\"5. assertEquals(\\\"Java Masterclass\\\", res.getTitle());\");\n        System.out.println(\"6. verify(mockCourseRepo, times(1)).findById(1L);\");\n    }\n}",
            "Mockito Unit Testing Pattern:\n1. @Mock CourseRepository mockCourseRepo;\n2. @InjectMocks CourseService courseService;\n3. when(mockCourseRepo.findById(1L)).thenReturn(Optional.of(course));\n4. CourseSummaryResponse res = courseService.getCourseSummary(1L);\n5. assertEquals(\"Java Masterclass\", res.getTitle());\n6. verify(mockCourseRepo, times(1)).findById(1L);",
            [
                "Outlines standard Spring Boot + Mockito unit testing workflow.",
                "Demonstrates stubbing and behavioral verification."
            ],
            [
                "Mocking data transfer objects (DTOs) or simple domain models; only mock external services, repositories, and interfaces.",
                "Over-mocking to the point where tests verify mock implementation details rather than actual business logic."
            ],
            [
                ("What is the difference between a Mock and a Spy in Mockito?", "A Mock is a complete dummy object; a Spy wraps a real object while allowing stubbing specific methods."),
                ("What does Mockito's `any()` matcher do?", "Matches any incoming argument of the specified type in stubbing or verification."),
                ("Why does mocking accelerate test suite execution?", "Eliminates I/O disk waits, network latency, and database connection overhead.")
            ]
        ),
        format_lesson(
            "java",
            "Debugging and diagnosis", 20,
            [
                "Diagnose production database connection and SQL syntax errors",
                "Trace root causes through chained SQLExceptions",
                "Create minimal reproducible examples to isolate complex bugs"
            ],
            "When diagnosing database and system failures:\n1. Inspect SQL State and Error Codes: `SQLException.getSQLState()` and `getErrorCode()` provide vendor-specific failure reasons.\n2. Chained Exceptions: `SQLException.getNextException()` iterates through nested server errors.\n3. Minimal Reproduction: Strip away extraneous code and isolate the failing query with hardcoded sample data to determine whether the issue is network, permissions, schema, or Java code.",
            "try {\n    // DB operation\n} catch (SQLException e) {\n    System.err.println(\"SQLState: \" + e.getSQLState());\n    System.err.println(\"ErrorCode: \" + e.getErrorCode());\n    for (Throwable t : e) { t.printStackTrace(); }\n}",
            "public class DiagnosisDemo {\n    public static void main(String[] args) {\n        System.out.println(\"Diagnostic Checklist for Database Failures:\");\n        System.out.println(\"1. Network: Is MySQL running on port 3306? Test with ping / telnet.\");\n        System.out.println(\"2. Authentication: Are username and password correct?\");\n        System.out.println(\"3. Schema: Does table and column name match exact case?\");\n        System.out.println(\"4. Constraint: Did foreign key or unique constraint fail?\");\n        System.out.println(\"5. Connection Pool: Are connections leaking without close()?\");\n    }\n}",
            "Diagnostic Checklist for Database Failures:\n1. Network: Is MySQL running on port 3306? Test with ping / telnet.\n2. Authentication: Are username and password correct?\n3. Schema: Does table and column name match exact case?\n4. Constraint: Did foreign key or unique constraint fail?\n5. Connection Pool: Are connections leaking without close()?",
            [
                "Provides structured diagnostic checklist for enterprise system engineers.",
                "Covers networking, authentication, schema, and connection pool diagnosis."
            ],
            [
                "Assuming database query failure is a Java code bug when database tables or columns haven't been migrated.",
                "Restarting database servers repeatedly without inspecting the server error log."
            ],
            [
                ("What does MySQL error code 1062 signify?", "Duplicate entry for a key (Unique constraint violation)."),
                ("What does MySQL error code 1452 signify?", "Cannot add or update a child row: a foreign key constraint fails."),
                ("How does connection pool exhaustion manifest in Spring Boot?", "HikariCP throws `ConnectionTimeoutException: Connection is not available, request timed out after 30000ms`.")
            ]
        )
    ]
    return {
        "title": "Module 7 — SQL, JDBC, and Testing",
        "description": "Connect Java programs to databases and verify behavior.",
        "sequenceOrder": 7,
        "lessons": lessons
    }

def get_java_module_8():
    lessons = [
        format_lesson(
            "java",
            "Student Grade Calculator", 30,
            [
                "Build a complete terminal grade calculation and classification application",
                "Validate user inputs, range boundaries, and weightings",
                "Apply structured methods, conditionals, and formatted output"
            ],
            "In this project, we create a complete Student Grade Calculator that captures subject marks, enforces [0, 100] bounds, calculates weighted averages, assigns GPA tiers, and displays a formatted academic report card.",
            "public static double calculateWeightedAverage(int[] marks, double[] weights) { ... }",
            "public class StudentGradeCalculatorProject {\n    public static char determineLetterGrade(double average) {\n        if (average >= 90) return 'A';\n        if (average >= 80) return 'B';\n        if (average >= 70) return 'C';\n        if (average >= 60) return 'D';\n        return 'F';\n    }\n    \n    public static void main(String[] args) {\n        String student = \"Alex Morgan\";\n        String[] subjects = {\"Java Core\", \"Data Structures\", \"SQL Databases\"};\n        int[] scores = {92, 88, 95};\n        \n        int sum = 0;\n        System.out.println(\"=== Academic Report Card: \" + student + \" ===\");\n        for (int i = 0; i < subjects.length; i++) {\n            System.out.printf(\"%-18s: %3d%%%n\", subjects[i], scores[i]);\n            sum += scores[i];\n        }\n        \n        double average = (double) sum / subjects.length;\n        char grade = determineLetterGrade(average);\n        System.out.println(\"------------------------------------\");\n        System.out.printf(\"Overall Average   : %6.2f%%%n\", average);\n        System.out.println(\"Final Grade Awarded: \" + grade);\n        System.out.println(\"Status            : \" + (grade != 'F' ? \"PASSED\" : \"PROBATION\"));\n    }\n}",
            "=== Academic Report Card: Alex Morgan ===\nJava Core         :  92%\nData Structures   :  88%\nSQL Databases     :  95%\n------------------------------------\nOverall Average   :  91.67%\nFinal Grade Awarded: A\nStatus            : PASSED",
            [
                "Iterates through subjects and accumulates total score.",
                "Computes floating-point average and passes into determineLetterGrade.",
                "Outputs formatted report card cleanly."
            ],
            [
                "Performing integer division (e.g. `sum / count`) which loses fractional grade percentages.",
                "Allowing negative marks or marks above 100 to enter calculations without validation."
            ],
            [
                ("How would you adapt this program to support course credit weightings?", "Multiply each grade by credit hours and divide by total credit hours."),
                ("How can you add file persistence to export the report card to disk?", "Use `Files.writeString(Path.of(\"report.txt\"), reportContent)`."),
                ("How would you test determineLetterGrade with JUnit 5?", "Write parameterized tests for boundaries 89, 90, 79, 80, etc.")
            ]
        ),
        format_lesson(
            "java",
            "Number Utility Toolkit", 30,
            [
                "Architect a reusable mathematical number toolkit",
                "Implement prime checking, greatest common divisor (GCD), and Armstrong numbers",
                "Develop comprehensive automated unit tests for all toolkit methods"
            ],
            "The Number Utility Toolkit bundles reusable computational algorithms into a clean static utility class:\n- `isPrime(n)`: Fast $O(\\sqrt{n})$ prime check.\n- `gcd(a, b)`: Euclidean algorithm for Greatest Common Divisor.\n- `lcm(a, b)`: Least Common Multiple via $(a \\times b) / \\text{gcd}(a, b)$.\n- `isArmstrong(n)`: Checks if the sum of digits raised to the power of number of digits equals the number.",
            "public final class NumberToolkit {\n    public static int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }\n}",
            "public class NumberUtilityToolkitProject {\n    public static boolean isPrime(int n) {\n        if (n <= 1) return false;\n        for (int i = 2; i * i <= n; i++) {\n            if (n % i == 0) return false;\n        }\n        return true;\n    }\n    \n    public static int gcd(int a, int b) {\n        return b == 0 ? a : gcd(b, a % b);\n    }\n    \n    public static int lcm(int a, int b) {\n        if (a == 0 || b == 0) return 0;\n        return Math.abs(a * b) / gcd(a, b);\n    }\n    \n    public static void main(String[] args) {\n        System.out.println(\"Number Utility Toolkit Test Bench:\");\n        System.out.println(\"Is 37 prime? \" + isPrime(37));\n        System.out.println(\"GCD of 48 and 18: \" + gcd(48, 18));\n        System.out.println(\"LCM of 12 and 18: \" + lcm(12, 18));\n    }\n}",
            "Number Utility Toolkit Test Bench:\nIs 37 prime? true\nGCD of 48 and 18: 6\nLCM of 12 and 18: 36",
            [
                "isPrime validates prime numbers efficiently up to square root of n.",
                "gcd applies the recursive Euclidean algorithm.",
                "lcm computes the lowest common multiple safely."
            ],
            [
                "Handling negative numbers in GCD without calling Math.abs().",
                "Division by zero in LCM when either input is 0."
            ],
            [
                ("What is the time complexity of the Euclidean algorithm for GCD?", "O(log(min(a, b)))."),
                ("Why should a utility class have a private constructor?", "To prevent instantiation of static-only classes."),
                ("What is an Armstrong number (e.g. 153)?", "1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.")
            ]
        ),
        format_lesson(
            "java",
            "Library Management System", 35,
            [
                "Model books, members, and loans using OOP classes and collections",
                "Manage state transitions (available, borrowed, reserved)",
                "Enforce borrowing rules and handle custom domain exceptions"
            ],
            "In this project, we implement an Object-Oriented Library Management System:\n- `Book`: Encapsulates ISBN, title, author, and checkout status.\n- `Member`: Encapsulates member ID, name, and list of borrowed books.\n- `Library`: Manages collections of books and members, handles checkouts, returns, and inventory queries.\n- Custom exceptions: `BookNotAvailableException`, `MemberNotFoundException`.",
            "public class Library {\n    private Map<String, Book> catalog = new HashMap<>();\n    public void checkoutBook(String isbn, String memberId) { ... }\n}",
            "import java.util.*;\n\npublic class LibraryProjectDemo {\n    static class Book {\n        private final String isbn;\n        private final String title;\n        private boolean isBorrowed = false;\n        \n        Book(String isbn, String title) { this.isbn = isbn; this.title = title; }\n        public String getIsbn() { return isbn; }\n        public String getTitle() { return title; }\n        public boolean isBorrowed() { return isBorrowed; }\n        public void setBorrowed(boolean borrowed) { isBorrowed = borrowed; }\n    }\n    \n    static class Library {\n        private final Map<String, Book> catalog = new HashMap<>();\n        \n        public void addBook(Book b) { catalog.put(b.getIsbn(), b); }\n        \n        public void borrowBook(String isbn, String student) {\n            Book b = catalog.get(isbn);\n            if (b == null) throw new IllegalArgumentException(\"Book not found: \" + isbn);\n            if (b.isBorrowed()) throw new IllegalStateException(\"Book is currently on loan!\");\n            b.setBorrowed(true);\n            System.out.println(\"Book '\" + b.getTitle() + \"' successfully checked out to \" + student);\n        }\n    }\n    \n    public static void main(String[] args) {\n        Library lib = new Library();\n        lib.addBook(new Book(\"978-0134685991\", \"Effective Java\"));\n        \n        lib.borrowBook(\"978-0134685991\", \"Alex Morgan\");\n        \n        try {\n            lib.borrowBook(\"978-0134685991\", \"Sarah Connor\"); // Expect loan error\n        } catch (IllegalStateException e) {\n            System.out.println(\"Checkout rejected: \" + e.getMessage());\n        }\n    }\n}",
            "Book 'Effective Java' successfully checked out to Alex Morgan\nCheckout rejected: Book is currently on loan!",
            [
                "Encapsulates Book state and maintains catalog in HashMap.",
                "borrowBook validates book existence and loan availability before updating state.",
                "Rejects concurrent borrow attempts cleanly."
            ],
            [
                "Allowing a book to be checked out multiple times simultaneously.",
                "Failing to handle null when looking up non-existent ISBNs in the catalog map."
            ],
            [
                ("How would you add overdue fine calculations to this design?", "Add checkout timestamp and compute elapsed days vs borrowing limit."),
                ("How would you search books by author using Java 8 Streams?", "Filter catalog.values().stream() matching author name."),
                ("What collection would you use to maintain a waitlist for a popular book?", "Queue<Member> / ArrayDeque<Member>.")
            ]
        ),
        format_lesson(
            "java",
            "Bank Account Manager", 35,
            [
                "Implement an enterprise-grade financial account manager",
                "Support deposits, withdrawals, and account-to-account funds transfers",
                "Apply transactional rollback and audit logging for audit compliance"
            ],
            "This project develops an enterprise Bank Account Manager featuring:\n- Accounts with strict validation and immutable audit identifiers.\n- Funds transfer between accounts with atomic safety: if credit fails, debit must be rolled back.\n- Custom domain exceptions (`InsufficientFundsException`, `AccountLockedException`).\n- Transaction logging history tracking every credit and debit.",
            "public boolean transfer(Account from, Account to, double amount) throws InsufficientFundsException { ... }",
            "import java.util.ArrayList;\nimport java.util.List;\n\npublic class BankAccountManagerProject {\n    static class InsufficientFundsException extends Exception {\n        public InsufficientFundsException(String msg) { super(msg); }\n    }\n    \n    static class BankAccount {\n        private final String id;\n        private double balance;\n        private final List<String> auditLog = new ArrayList<>();\n        \n        BankAccount(String id, double initial) {\n            this.id = id;\n            this.balance = initial;\n            auditLog.add(\"Account opened with initial balance: $\" + initial);\n        }\n        \n        public synchronized void deposit(double amt) {\n            balance += amt;\n            auditLog.add(\"Deposited: +$\" + amt + \" | Balance: $\" + balance);\n        }\n        \n        public synchronized void withdraw(double amt) throws InsufficientFundsException {\n            if (amt > balance) throw new InsufficientFundsException(\"Insufficient funds for $\" + amt);\n            balance -= amt;\n            auditLog.add(\"Withdrew: -$\" + amt + \" | Balance: $\" + balance);\n        }\n        \n        public double getBalance() { return balance; }\n        public void printStatement() {\n            System.out.println(\"--- Account Statement: \" + id + \" ---\");\n            auditLog.forEach(System.out::println);\n        }\n    }\n    \n    public static void main(String[] args) throws Exception {\n        BankAccount acc = new BankAccount(\"BA-4401\", 500.0);\n        acc.deposit(200.0);\n        acc.withdraw(150.0);\n        acc.printStatement();\n    }\n}",
            "--- Account Statement: BA-4401 ---\nAccount opened with initial balance: $500.0\nDeposited: +$200.0 | Balance: $700.0\nWithdrew: -$150.0 | Balance: $550.0",
            [
                "Encapsulates balance with synchronized deposit and withdraw methods.",
                "Maintains complete internal audit trail for compliance.",
                "Guarantees data integrity and accurate balance state."
            ],
            [
                "Allowing double rounding errors in currency (in production, always use `BigDecimal` or store integer cents).",
                "Neglecting synchronization on balance mutations in multi-threaded banking environments."
            ],
            [
                ("Why is BigDecimal mandatory for financial calculations in production Java?", "Prevents binary floating-point rounding inaccuracies inherent to double and float."),
                ("How do you ensure deadlock-free transfers when locking two accounts?", "Always acquire locks in a deterministic order (e.g. by comparing account IDs)."),
                ("What is an Event Sourcing pattern in banking?", "Storing every state change as an immutable transaction event rather than just overwriting balance.")
            ]
        ),
        format_lesson(
            "java",
            "Student Record System", 35,
            [
                "Build a persistent Student Record System reading and writing to disk",
                "Implement searching, sorting, and filtering of records",
                "Serialize records as structured CSV/JSON data using modern NIO"
            ],
            "This project implements a complete Student Record System that stores student profiles, persists them to local files, searches by name or student ID, and sorts by GPA.\n- Formats: CSV or JSON persistence.\n- Operations: Add student, search by ID, list all sorted by GPA, and export summary.",
            "public void saveToFile(Path path) throws IOException { ... }\npublic static StudentRecordSystem loadFromFile(Path path) throws IOException { ... }",
            "import java.nio.file.*;\nimport java.io.IOException;\nimport java.util.*;\n\npublic class StudentRecordSystemProject {\n    static class Record {\n        int id;\n        String name;\n        double gpa;\n        Record(int id, String name, double gpa) { this.id = id; this.name = name; this.gpa = gpa; }\n        public String toCsv() { return id + \",\" + name + \",\" + gpa; }\n    }\n    \n    public static void main(String[] args) throws IOException {\n        Path dbFile = Path.of(\"students_demo.csv\");\n        List<Record> students = List.of(\n            new Record(101, \"Alex Morgan\", 3.85),\n            new Record(102, \"Sarah Connor\", 3.95),\n            new Record(103, \"David Miller\", 3.60)\n        );\n        \n        List<String> lines = new ArrayList<>();\n        lines.add(\"id,name,gpa\");\n        students.forEach(s -> lines.add(s.toCsv()));\n        Files.write(dbFile, lines);\n        \n        System.out.println(\"Student records written to: \" + dbFile.toAbsolutePath());\n        \n        // Read and display\n        List<String> readLines = Files.readAllLines(dbFile);\n        System.out.println(\"Read \" + (readLines.size() - 1) + \" student records successfully.\");\n        \n        Files.deleteIfExists(dbFile); // Cleanup\n    }\n}",
            "Student records written to: c:\\Users\\Admin\\OneDrive\\Desktop\\LearnHub\\students_demo.csv\nRead 3 student records successfully.",
            [
                "Constructs CSV representations of student objects.",
                "Persists data to disk using NIO Files.write.",
                "Reads back records and cleans up temporary file."
            ],
            [
                "Failing to handle file parsing exceptions when CSV rows are malformed.",
                "Hardcoding Windows-specific file path separators (`\\`) instead of using `Path.of()` or `/`."
            ],
            [
                ("How do you handle commas inside student names when saving CSV data?", "Enclose fields in double quotes or escape them."),
                ("How does Files.lines() improve memory efficiency when reading massive files?", "Streams lines lazily on-demand rather than loading the entire file into heap."),
                ("Why should persistent database operations use atomic temp file renaming?", "Guarantees file integrity even if the system crashes midway through writing.")
            ]
        ),
        format_lesson(
            "java",
            "JDBC Student Management System", 35,
            [
                "Connect the Student Record System to an active MySQL database via JDBC",
                "Implement secure CRUD repository operations using PreparedStatement",
                "Integrate connection pooling, transactional integrity, and resource management"
            ],
            "In this project, we transition our domain model to a live database using **JDBC**:\n- Database table: `students (id BIGINT AUTO_INCREMENT PK, name VARCHAR(100), email VARCHAR(100) UNIQUE, gpa DOUBLE)`.\n- Repository methods: `save()`, `findById()`, `findAllSortedByGpa()`, `update()`, `deleteById()`.\n- Fully protected against SQL injection using parameterized queries.",
            "public class StudentJdbcRepository {\n    public void save(Student s) throws SQLException { ... }\n}",
            "public class JDBCStudentProjectDemo {\n    public static void main(String[] args) {\n        System.out.println(\"JDBC Student Management System Architecture:\");\n        System.out.println(\"1. Connection: HikariDataSource pooled connection\");\n        System.out.println(\"2. PreparedStatement: INSERT INTO students (name, email, gpa) VALUES (?, ?, ?)\");\n        System.out.println(\"3. Key Retrieval: Statement.RETURN_GENERATED_KEYS sets student.id\");\n        System.out.println(\"4. Query: SELECT id, name, email, gpa FROM students ORDER BY gpa DESC\");\n        System.out.println(\"5. Verified zero connection leaks using try-with-resources.\");\n    }\n}",
            "JDBC Student Management System Architecture:\n1. Connection: HikariDataSource pooled connection\n2. PreparedStatement: INSERT INTO students (name, email, gpa) VALUES (?, ?, ?)\n3. Key Retrieval: Statement.RETURN_GENERATED_KEYS sets student.id\n4. Query: SELECT id, name, email, gpa FROM students ORDER BY gpa DESC\n5. Verified zero connection leaks using try-with-resources.",
            [
                "Outlines complete end-to-end JDBC persistence flow.",
                "Demonstrates enterprise patterns matching LearnHub's backend architecture."
            ],
            [
                "Failing to handle unique constraint violation on email column.",
                "Leaving open ResultSets or Connections inside loops."
            ],
            [
                ("How do you catch a duplicate email error in JDBC?", "Catch SQLException and check if getErrorCode() == 1062."),
                ("What does HikariCP do when a connection is closed with conn.close()?", "Returns the physical connection to the active pool rather than terminating the socket."),
                ("Why should database operations be encapsulated inside a DAO or Repository class?", "Separates data persistence logic from core business services.")
            ]
        ),
        format_lesson(
            "java",
            "Final Course Enrollment Manager", 40,
            [
                "Model courses, modules, lessons, students, and enrollments",
                "Enforce duplicate enrollment constraints and track progress accurately",
                "Persist state across sessions and calculate percentage completion"
            ],
            "This capstone project brings together all elements of the LearnHub platform:\n- Entities: `User` (Student/Instructor/Admin), `Course`, `Module`, `Lesson`, `Enrollment`, `LessonProgress`.\n- Business Rules:\n  - Enforce that a student cannot enroll twice in the same course.\n  - Enforce that completing a lesson increments completed count and recalculates progress accurately as `(completed / total) * 100.0`.\n  - Transitioning between lessons updates progress in real time.",
            "public class EnrollmentManager {\n    public void completeLesson(Long enrollmentId, Long lessonId) { ... }\n}",
            "import java.util.*;\n\npublic class FinalEnrollmentManagerProject {\n    static class Enrollment {\n        String student;\n        String course;\n        Set<Integer> completedLessonIds = new HashSet<>();\n        int totalLessons;\n        \n        Enrollment(String student, String course, int totalLessons) {\n            this.student = student;\n            this.course = course;\n            this.totalLessons = totalLessons;\n        }\n        \n        public void completeLesson(int lessonId) {\n            completedLessonIds.add(lessonId);\n        }\n        \n        public double getProgressPercentage() {\n            if (totalLessons == 0) return 0.0;\n            return ((double) completedLessonIds.size() / totalLessons) * 100.0;\n        }\n    }\n    \n    public static void main(String[] args) {\n        Enrollment enr = new Enrollment(\"Alex Morgan\", \"Java Programming Masterclass\", 98);\n        System.out.printf(\"Initial Progress: %.1f%%%n\", enr.getProgressPercentage());\n        \n        // Complete first 5 lessons\n        for (int i = 1; i <= 5; i++) enr.completeLesson(i);\n        System.out.printf(\"Progress after 5 lessons: %.1f%% (%d of %d lessons)%n\", \n            enr.getProgressPercentage(), enr.completedLessonIds.size(), enr.totalLessons);\n            \n        // Complete 44 more lessons\n        for (int i = 6; i <= 49; i++) enr.completeLesson(i);\n        System.out.printf(\"Midway Progress: %.1f%% (%d of %d lessons)%n\", \n            enr.getProgressPercentage(), enr.completedLessonIds.size(), enr.totalLessons);\n    }\n}",
            "Initial Progress: 0.0%\nProgress after 5 lessons: 5.1% (5 of 98 lessons)\nMidway Progress: 50.0% (49 of 98 lessons)",
            [
                "Enforces unique completed lessons via HashSet.",
                "Recalculates progress percentage dynamically and accurately across all 98 curriculum lessons."
            ],
            [
                "Counting duplicate lesson completions multiple times, causing progress to exceed 100%.",
                "Division by zero when total lessons count is 0."
            ],
            [
                ("How does LearnHub prevent duplicate lesson completion entries in MySQL?", "Unique composite constraint on `(enrollment_id, lesson_id)` in `lesson_progress` table."),
                ("How does the frontend LearningPage synchronize completed lessons with the backend?", "Via REST API call to `/api/student/lessons/{id}/complete`."),
                ("Why is progress stored on the Enrollment entity in addition to individual LessonProgress rows?", "Provides O(1) instant summary reads for dashboards without aggregating 98 rows every time.")
            ]
        ),
        format_lesson(
            "java",
            "Final revision and challenge set", 40,
            [
                "Consolidate all 8 modules of the Java Programming Masterclass",
                "Solve comprehensive multi-paradigm interview challenges",
                "Review JVM memory, concurrency, collections, and database persistence"
            ],
            "This final review capstone provides a comprehensive review of all core Java domains:\n1. Core Syntax & Data Types\n2. Control Flow & Looping\n3. Methods, Arrays & Strings\n4. Object-Oriented Design & Encapsulation\n5. Exceptions & Collections Framework\n6. Modern Java (Streams, Lambdas, Optional) & Concurrency\n7. Relational Databases & JDBC\n8. Full Enterprise Software Engineering.",
            "// Java Masterclass Complete Certification Review\npublic class MasterclassFinalReview { ... }",
            "public class FinalRevisionProject {\n    public static void main(String[] args) {\n        System.out.println(\"====================================================\");\n        System.out.println(\"  CONGRATULATIONS: JAVA PROGRAMMING MASTERCLASS     \");\n        System.out.println(\"====================================================\");\n        System.out.println(\"Curriculum Coverage Summary:\");\n        System.out.println(\"- Module 1: Introduction to Java (12 lessons)\");\n        System.out.println(\"- Module 2: Conditional Statements and Loops (12 lessons)\");\n        System.out.println(\"- Module 3: Methods, Arrays, and Strings (12 lessons)\");\n        System.out.println(\"- Module 4: Object-Oriented Programming (15 lessons)\");\n        System.out.println(\"- Module 5: Exceptions, Collections, and Generics (15 lessons)\");\n        System.out.println(\"- Module 6: Files, Modern Java, and Concurrency (14 lessons)\");\n        System.out.println(\"- Module 7: SQL, JDBC, and Testing (10 lessons)\");\n        System.out.println(\"- Module 8: Java Projects and Revision (8 lessons)\");\n        System.out.println(\"Total: 98 comprehensive lessons mastered!\");\n        System.out.println(\"====================================================\");\n    }\n}",
            "====================================================\n  CONGRATULATIONS: JAVA PROGRAMMING MASTERCLASS     \n====================================================\nCurriculum Coverage Summary:\n- Module 1: Introduction to Java (12 lessons)\n- Module 2: Conditional Statements and Loops (12 lessons)\n- Module 3: Methods, Arrays, and Strings (12 lessons)\n- Module 4: Object-Oriented Programming (15 lessons)\n- Module 5: Exceptions, Collections, and Generics (15 lessons)\n- Module 6: Files, Modern Java, and Concurrency (14 lessons)\n- Module 7: SQL, JDBC, and Testing (10 lessons)\n- Module 8: Java Projects and Revision (8 lessons)\nTotal: 98 comprehensive lessons mastered!\n====================================================",
            [
                "Summarizes all 8 modules and 98 required curriculum lessons.",
                "Reinforces mastery across OOP, collections, streams, concurrency, and persistence."
            ],
            [
                "Stopping at basic syntax without mastering object-oriented design and memory management.",
                "Neglecting automated unit testing and defensive input validation."
            ],
            [
                ("What are the key differences between Java 8 and Java 17 LTS?", "Records, sealed classes, switch expressions, text blocks, and modern GC algorithms (ZGC)."),
                ("What architectural pattern separates presentation, business logic, and database access?", "Model-View-Controller (MVC) and Layered Architecture."),
                ("How does continuous integration (CI) verify Java code quality?", "Runs automated Maven/Gradle test suites and code coverage gates on every commit.")
            ]
        )
    ]
    return {
        "title": "Module 8 — Java Projects and Revision",
        "description": "Combine the course concepts into complete small applications.",
        "sequenceOrder": 8,
        "lessons": lessons
    }

print("Java modules 7 & 8 ready.")
