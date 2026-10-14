import json
import os

def fmt(title, objectives, explanation, syntax, code_example, expected_output, walkthrough, common_mistakes, questions):
    md = []
    md.append("### 🎯 Learning Objectives")
    for obj in objectives:
        md.append(f"- {obj}")
    md.append("")
    md.append("### 📖 Concept Explanation")
    md.append(explanation.strip())
    md.append("")
    if syntax:
        md.append("### 💻 Syntax & Key Concepts")
        md.append(f"```java\n{syntax.strip()}\n```")
        md.append("")
    if code_example:
        md.append("### 🚀 Working Example")
        md.append(f"```java\n{code_example.strip()}\n```")
        md.append("")
    if expected_output:
        md.append("**Expected Output:**")
        md.append(f"```text\n{expected_output.strip()}\n```")
        md.append("")
    if walkthrough:
        md.append("### 🔍 Step-by-Step Walkthrough")
        for i, step in enumerate(walkthrough, 1):
            md.append(f"{i}. {step}")
        md.append("")
    if common_mistakes:
        md.append("### ⚠️ Common Mistakes & Pitfalls")
        for mistake in common_mistakes:
            md.append(f"- {mistake}")
        md.append("")
    if questions:
        md.append("### 📝 Practice Questions")
        for i, q in enumerate(questions, 1):
            md.append(f"{i}. **{q[0]}**\n   *Hint:* {q[1]}")
        md.append("")
    return "\n".join(md)

# Build Java Modules & Lessons
modules = []

# Module 1
m1_lessons = [
    (
        "Introduction to Java", 20,
        [
            "Understand the origin, background, and evolution of Java",
            "Identify common enterprise, cloud, and tooling applications of Java",
            "Evaluate Java's architectural strengths and inherent trade-offs"
        ],
        "Java is a high-level, class-based, object-oriented programming language released by Sun Microsystems in 1995. Originally designed by James Gosling, Java was engineered with the philosophy of 'Write Once, Run Anywhere' (WORA). Today, Java is the bedrock of global financial transaction systems, enterprise backends (Spring Boot, Quarkus), Android ecosystem runtime, and big data infrastructure (Apache Spark, Kafka). Its key strength lies in long-term backward compatibility, predictable memory management, and a massive ecosystem of libraries.",
        "// Canonical Java source structure\npublic class SystemProfile {\n    public static void main(String[] args) {\n        // Statements executed sequentially\n    }\n}",
        "public class IntroDemo {\n    public static void main(String[] args) {\n        String platform = \"Java SE 17 LTS\";\n        String ecosystem = \"Enterprise & Cloud Infrastructure\";\n        System.out.println(\"Platform: \" + platform);\n        System.out.println(\"Primary Deployment: \" + ecosystem);\n    }\n}",
        "Platform: Java SE 17 LTS\nPrimary Deployment: Enterprise & Cloud Infrastructure",
        [
            "The JVM looks for the canonical entry point: 'public static void main(String[] args)'.",
            "Variables 'platform' and 'ecosystem' are allocated as String references.",
            "System.out.println outputs characters to the standard output stream with a newline."
        ],
        [
            "Confusing Java with JavaScript; they are completely distinct languages with different type systems and runtimes.",
            "Naming the public class differently than the underlying .java file name on disk."
        ],
        [
            ("Why is backward compatibility considered one of Java's greatest enterprise assets?", "Think about enterprises maintaining multi-decade codebases that need to upgrade JVM versions without rewriting."),
            ("Name three global distributed platforms powered by the JVM ecosystem.", "Consider search, stream processing, or big data tools like Kafka, ElasticSearch, and Hadoop."),
            ("What does the 'WORA' acronym stand for and how is it technically achieved?", "Reference compiled bytecode and the platform-specific JVM.")
        ]
    ),
    (
        "Features of Java", 20,
        [
            "Explain platform independence via intermediate bytecode",
            "Understand automatic memory management through Garbage Collection",
            "Analyze Java's built-in type safety and security model"
        ],
        "Java distinguishes itself through several foundational architectural features:\n1. Platform Independence: Compiles to intermediate bytecode (.class) rather than machine-specific binaries.\n2. Object-Oriented: Everything belongs to classes, promoting modularity, encapsulation, and reuse.\n3. Robust & Strongly Typed: Strict compile-time and runtime type checking reduces memory corruption.\n4. Automatic Garbage Collection: Memory reclamation is handled by the JVM, preventing dangling pointers and manual deallocation bugs.\n5. Multithreaded & Concurrent: Core language primitives allow executing concurrent tasks natively.",
        "// Bytecode execution model\n// Source (.java) -> javac -> Bytecode (.class) -> JVM (JIT compiler) -> Native Machine Code",
        "public class FeaturesDemo {\n    public static void main(String[] args) {\n        boolean platformIndependent = true;\n        boolean automaticGC = true;\n        System.out.println(\"Bytecode portability active: \" + platformIndependent);\n        System.out.println(\"JVM Automatic GC active: \" + automaticGC);\n    }\n}",
        "Bytecode portability active: true\nJVM Automatic GC active: true",
        [
            "The compiler 'javac' verifies types and creates bytecode instructions.",
            "The JVM loads the class file, interprets bytecode, and compiles hot paths to native instructions using the JIT compiler."
        ],
        [
            "Assuming Java does not have memory leaks; unreferenced objects in static collections can still cause memory retention.",
            "Thinking Garbage Collection occurs at predictable, scheduled moments; GC runs asynchronously according to JVM heuristics."
        ],
        [
            ("What role does the Just-In-Time (JIT) compiler play in runtime performance?", "Consider how frequently executed bytecode blocks are converted directly into machine instructions."),
            ("How does Java's elimination of explicit pointer arithmetic enhance application security?", "Think about buffer overflows and arbitrary memory access prevention."),
            ("Can an application manually force the JVM to run garbage collection?", "Investigate System.gc() and why it is merely a recommendation to the runtime.")
        ]
    ),
    (
        "JDK, JRE, and JVM", 25,
        [
            "Define the responsibilities of JDK, JRE, and the JVM",
            "Trace execution from source code through javac into bytecode and runtime",
            "Distinguish development utilities from production runtime environments"
        ],
        "Understanding Java's architecture requires distinguishing three layers:\n- JVM (Java Virtual Machine): The abstract computing machine that executes compiled Java bytecode. Each OS has its own JVM implementation.\n- JRE (Java Runtime Environment): The bundle containing the JVM plus the core standard class libraries (java.base, java.sql, etc.) required to execute Java apps.\n- JDK (Java Development Kit): The complete superset containing the JRE plus developer tools such as the compiler (javac), packager (jar), documentation tool (javadoc), and debugger (jdb).",
        "// Compilation & Execution Pipeline:\n// MyClass.java ---[ javac ]---> MyClass.class (bytecode) ---[ java (JVM) ]---> CPU Execution",
        "public class ArchDemo {\n    public static void main(String[] args) {\n        System.out.println(\"Java Version: \" + System.getProperty(\"java.version\"));\n        System.out.println(\"JVM Vendor: \" + System.getProperty(\"java.vm.vendor\"));\n        System.out.println(\"OS Architecture: \" + System.getProperty(\"os.arch\"));\n    }\n}",
        "Java Version: 17.0.1\nJVM Vendor: Eclipse Adoptium\nOS Architecture: amd64",
        [
            "The program queries standard system properties from the java.lang.System class.",
            "These properties reflect the host runtime environment provisioned by the underlying JVM."
        ],
        [
            "Deploying a heavyweight full JDK to a container where only a minimal runtime JRE/JVM image is needed.",
            "Attempting to compile .java source code using only a JRE installation where 'javac' is not present."
        ],
        [
            ("Why is the JVM platform-dependent while Java bytecode is platform-independent?", "Consider how Windows, Linux, and macOS have distinct CPU instruction sets."),
            ("What command-line tool in the JDK is used to inspect compiled bytecode instructions?", "Look up the javap disassembler tool."),
            ("Which modern JDK tool creates optimized, customized minimal runtime images?", "Investigate the jlink utility introduced in Java 9.")
        ]
    ),
    (
        "Installing Java and setting up the environment", 20,
        [
            "Install and verify a supported Long-Term Support (LTS) JDK",
            "Configure JAVA_HOME and PATH operating system environment variables",
            "Validate compiler and interpreter availability via command terminal"
        ],
        "To develop with Java, install a modern OpenJDK distribution (such as Eclipse Temurin, Amazon Corretto, or Oracle JDK 17/21 LTS). After installation, two environment variables are crucial:\n- JAVA_HOME: Points to the root directory of your installed JDK (e.g., C:\\Program Files\\Eclipse Adoptium\\jdk-17).\n- PATH: Appends %JAVA_HOME%\\bin (or $JAVA_HOME/bin on Linux/macOS) so commands like javac and java are recognized globally in any terminal.",
        "// Verification commands in terminal:\n// java -version\n// javac -version\n// echo %JAVA_HOME%  (Windows) or echo $JAVA_HOME (Linux/macOS)",
        "public class EnvironmentCheck {\n    public static void main(String[] args) {\n        String javaHome = System.getenv(\"JAVA_HOME\");\n        System.out.println(\"Environment Ready: true\");\n        System.out.println(\"Runtime Classpath: \" + System.getProperty(\"java.class.path\"));\n    }\n}",
        "Environment Ready: true\nRuntime Classpath: .",
        [
            "System.getenv inspects process environment variables configured in the operating system.",
            "System.getProperty exposes active classpath search paths loaded by the Application ClassLoader."
        ],
        [
            "Setting JAVA_HOME to point to the 'bin' subdirectory instead of the root JDK directory.",
            "Installing a 32-bit JDK on a 64-bit operating system causing memory constraint issues."
        ],
        [
            ("How do you verify whether 'javac' and 'java' point to the exact same JDK version?", "Check output of both commands in the terminal."),
            ("Why is an LTS (Long-Term Support) release preferred in production environments?", "Consider stability, security patch support lifecycles, and third-party vendor guarantees."),
            ("What error occurs if your operating system cannot find javac in PATH?", "Identify 'javac is not recognized as an internal or external command'.")
        ]
    ),
    (
        "First Java program", 20,
        [
            "Author, compile, and execute the canonical HelloWorld program",
            "Deconstruct each keyword in the main method signature",
            "Understand terminal commands 'javac' and 'java'"
        ],
        "Every executable Java program requires a class containing an entry point method. The signature is strictly defined as:\n`public static void main(String[] args)`\n- public: Access modifier allowing the JVM runtime to invoke this method from outside the class package.\n- static: Enables the JVM to call the method without instantiating an object of the enclosing class.\n- void: Specifies that the method does not return any value to the caller.\n- main: The exact identifier recognized by the JVM launcher as the application starting point.\n- String[] args: Parameter array storing command-line arguments passed at launch.",
        "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
        "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, LearnHub World!\");\n        System.out.println(\"Welcome to Enterprise Java Mastery.\");\n    }\n}",
        "Hello, LearnHub World!\nWelcome to Enterprise Java Mastery.",
        [
            "The class 'HelloWorld' is loaded into JVM memory.",
            "The JVM calls HelloWorld.main with an empty String array.",
            "System.out.println transmits string characters to the console standard output stream."
        ],
        [
            "Omitting the 'String[] args' argument in main, causing 'Main method not found' error at runtime.",
            "Adding a semicolon after class declaration like 'public class HelloWorld; {}'."
        ],
        [
            ("Can you change 'String[] args' to 'String args[]' or 'String... args'?", "Test alternative parameter syntax in Java."),
            ("What happens if you run 'java HelloWorld.class' instead of 'java HelloWorld'?", "Observe the ClassNotFoundException caused by treating .class as a package."),
            ("Is a program permitted to have multiple main methods with different signatures?", "Consider method overloading rules.")
        ]
    ),
    (
        "Java program structure", 20,
        [
            "Organize Java source files with package, imports, and class declarations",
            "Apply brace matching, statement semicolons, and whitespace conventions",
            "Comply with file naming requirements for public classes"
        ],
        "A Java source file (.java) follows an explicit architectural hierarchy:\n1. Package declaration (optional, but standard for production): defines the namespace.\n2. Import statements: brings external classes and packages into scope.\n3. Class declaration: contains fields, constructors, and methods.\nRule: A source file can contain multiple classes, but only ONE public class. The file name must match that public class exactly, including capitalization.",
        "// Structure outline:\npackage com.learnhub.foundation;\nimport java.util.Date;\n\npublic class ProgramStructure {\n    // Fields\n    // Methods\n}",
        "public class StructureDemo {\n    public static void main(String[] args) {\n        // Statement termination with semicolon\n        int moduleCount = 8;\n        String platformName = \"LearnHub\";\n        \n        // Block delimited with curly braces\n        {\n            int localScope = 42;\n            System.out.println(\"Platform: \" + platformName + \" | Modules: \" + moduleCount);\n        }\n    }\n}",
        "Platform: LearnHub | Modules: 8",
        [
            "The compiler verifies package and import paths.",
            "Class definition opens a class-level block with curly braces.",
            "Method main contains executable statements, each terminated with a semicolon."
        ],
        [
            "Mismatched capitalization between the public class name and the physical .java filename.",
            "Declaring more than one public class in a single source file."
        ],
        [
            ("Can a Java file contain zero public classes? If so, how must it be named?", "Think about package-private classes."),
            ("What is the consequence of placing code outside a class body in Java?", "Understand why all executable code must reside within a class."),
            ("What does the semicolon signify to the Java compiler?", "Identify statement termination vs block delimiters.")
        ]
    ),
    (
        "Variables and constants", 20,
        [
            "Declare, initialize, and reassign typed variables",
            "Enforce immutability using the 'final' keyword",
            "Apply camelCase naming conventions and legal identifier rules"
        ],
        "A variable is a named memory location that stores a typed value. Java is strictly typed: every variable must have a declared type.\n- Declaration: `int studentCount;`\n- Initialization: `studentCount = 25;`\n- Combined: `int studentCount = 25;`\nConstants: When a variable is prepended with the `final` keyword, its value cannot be reassigned once initialized. By convention, compile-time constants are written in UPPERCASE_WITH_UNDERSCORES.",
        "// Variable:\ntype identifier = initialValue;\n\n// Constant:\nfinal type CONSTANT_NAME = immutableValue;",
        "public class VariablesDemo {\n    public static void main(String[] args) {\n        // Mutable variable\n        int enrolledStudents = 120;\n        enrolledStudents = enrolledStudents + 5;\n        \n        // Immutable constant\n        final double PASSING_GRADE = 70.0;\n        final int MAX_CLASS_CAPACITY = 200;\n        \n        System.out.println(\"Enrolled: \" + enrolledStudents + \"/\" + MAX_CLASS_CAPACITY);\n        System.out.println(\"Passing Threshold: \" + PASSING_GRADE + \"%\");\n    }\n}",
        "Enrolled: 125/200\nPassing Threshold: 70.0%",
        [
            "Variable enrolledStudents is allocated in local stack memory with value 120, then updated to 125.",
            "PASSING_GRADE is declared as final double; any subsequent attempt to mutate it yields a compile error."
        ],
        [
            "Attempting to reassign a final variable after initial assignment.",
            "Using uninitialized local variables in expressions; Java does not assign default values to local variables."
        ],
        [
            ("What are the naming rules for legal Java identifiers regarding numbers and special characters?", "Identify rules on leading digits, $, and _."),
            ("Why does Java enforce that local variables must be explicitly initialized before reading?", "Compare stack frame allocation with heap object zero-initialization."),
            ("Can a final object reference have its internal fields mutated?", "Distinguish reference immutability from object state mutability.")
        ]
    ),
    (
        "Primitive data types", 25,
        [
            "Identify all 8 primitive data types, their bit widths, and ranges",
            "Select appropriate numeric, character, and boolean types for domain data",
            "Use literal suffixes such as L for long and F for float"
        ],
        "Java defines 8 primitive data types stored directly in memory (stack frames or object fields):\n1. byte: 8-bit signed (-128 to 127)\n2. short: 16-bit signed (-32,768 to 32,767)\n3. int: 32-bit signed (default for integers, ~-2.14B to 2.14B)\n4. long: 64-bit signed (requires 'L' suffix for large literals, e.g., 5000000000L)\n5. float: 32-bit IEEE 754 floating point (requires 'F' suffix, e.g., 3.14F)\n6. double: 64-bit IEEE 754 floating point (default for decimals, 15 decimal precision)\n7. char: 16-bit unsigned Unicode character ('A', '\\u0041')\n8. boolean: true or false (1 bit logical value)",
        "byte b = 100;\nshort s = 1000;\nint i = 50000;\nlong l = 10000000000L;\nfloat f = 19.99F;\ndouble d = 19.9999;\nchar c = 'J';\nboolean active = true;",
        "public class PrimitivesDemo {\n    public static void main(String[] args) {\n        byte coreId = 4;\n        int requestCount = 1_450_000;\n        long epochMillis = 1_697_000_000_000L;\n        double serverLoad = 84.75;\n        char gradeTier = 'A';\n        boolean isHealthy = true;\n        \n        System.out.println(\"Core: \" + coreId + \" | Requests: \" + requestCount);\n        System.out.println(\"Timestamp: \" + epochMillis + \" | Load: \" + serverLoad + \"%\");\n        System.out.println(\"Tier: \" + gradeTier + \" | Healthy: \" + isHealthy);\n    }\n}",
        "Core: 4 | Requests: 1450000\nTimestamp: 1697000000000 | Load: 84.75%\nTier: A | Healthy: true",
        [
            "Underscores in numeric literals (1_450_000) are purely for developer readability and ignored by the compiler.",
            "Variables are assigned exact bit widths according to specification regardless of underlying OS."
        ],
        [
            "Forgetting the 'L' suffix when assigning numbers greater than 2,147,483,647 to a long variable.",
            "Forgetting the 'F' suffix on float literals, causing 'incompatible types: possible lossy conversion from double to float'."
        ],
        [
            ("Why should double or float never be used for precise financial currency calculations?", "Investigate IEEE 754 binary floating point rounding errors and BigDecimal."),
            ("What is the default value of primitive instance variables in a class?", "Recall 0 for numbers, false for boolean, '\\u0000' for char."),
            ("What is the memory size difference between primitive int and wrapper Integer?", "Account for object headers and pointer overhead in heap memory.")
        ]
    ),
    (
        "Type conversion and casting", 20,
        [
            "Distinguish implicit widening from explicit narrowing conversions",
            "Perform safe explicit casts between numeric types",
            "Identify and prevent numeric overflow and precision loss"
        ],
        "Type conversion happens when a value of one type is assigned to a variable of another type:\n- Widening Conversion (Implicit): Converting smaller type to larger type (e.g., int -> long -> double). Safe with zero data loss, handled automatically by the compiler.\n- Narrowing Conversion (Explicit): Converting larger type to smaller type (e.g., double -> int, long -> short). Potential data truncation or precision loss; requires explicit casting syntax `(targetType) expression`.",
        "// Widening (Implicit):\nint num = 100;\ndouble dec = num;\n\n// Narrowing (Explicit Cast):\ndouble price = 99.95;\nint rounded = (int) price; // Truncates decimal to 99",
        "public class CastingDemo {\n    public static void main(String[] args) {\n        // Widening\n        int originalScore = 85;\n        double preciseScore = originalScore;\n        \n        // Narrowing\n        double rawCompletionRate = 78.89;\n        int displayRate = (int) rawCompletionRate; // Fractional part dropped\n        \n        // Overflow demonstration\n        int largeNum = 130;\n        byte overflowedByte = (byte) largeNum; // byte range is -128 to 127\n        \n        System.out.println(\"Widened score: \" + preciseScore);\n        System.out.println(\"Truncated rate: \" + displayRate + \"%\");\n        System.out.println(\"Overflowed byte (130 -> byte): \" + overflowedByte);\n    }\n}",
        "Widened score: 85.0\nTruncated rate: 78%\nOverflowed byte (130 -> byte): -126",
        [
            "originalScore is implicitly widened from 32-bit int to 64-bit double (85 -> 85.0).",
            "rawCompletionRate is explicitly cast to int, truncating .89 rather than rounding.",
            "130 in binary wraps around the 8-bit two's complement boundary yielding -126."
        ],
        [
            "Expecting `(int) 9.99` to round up to 10; casting simply truncates towards zero.",
            "Casting non-primitive incompatible types like String to int using cast operator `(int) \"123\"` instead of Integer.parseInt()."
        ],
        [
            ("How does Java handle integer division when assigning to a double variable (e.g., double res = 5 / 2;)?", "Analyze why the division occurs as int first yielding 2, then widened to 2.0."),
            ("What occurs during byte overflow when 127 is incremented by 1 in a cast expression?", "Understand two's complement binary representation."),
            ("Which utility method should be used to round a double to the nearest whole integer?", "Look up Math.round().")
        ]
    ),
    (
        "Input and output", 25,
        [
            "Output formatted text using print, println, and printf",
            "Read interactive console input using java.util.Scanner",
            "Handle Scanner newline pitfalls when alternating nextInt and nextLine"
        ],
        "Console communication in Java:\n- Standard Output: `System.out.print` (no newline), `System.out.println` (appends newline), and `System.out.printf` (formatted output with specifiers like `%s`, `%d`, `%.2f`).\n- Standard Input: `java.util.Scanner` wraps `System.in` to parse tokens.\nCommon Trap: Calling `scanner.nextInt()` or `scanner.nextDouble()` reads only the number, leaving the newline character `\\n` in the buffer. A subsequent `scanner.nextLine()` will immediately consume that leftover newline and return an empty string. Solution: call an extra `scanner.nextLine()` to flush the buffer.",
        "import java.util.Scanner;\nScanner scanner = new Scanner(System.in);\nint id = scanner.nextInt();\nscanner.nextLine(); // flush buffer\nString name = scanner.nextLine();",
        "import java.util.Scanner;\n\npublic class InputOutputDemo {\n    public static void main(String[] args) {\n        String courseName = \"Java Masterclass\";\n        int moduleCount = 8;\n        double cost = 0.00;\n        \n        // Formatted printing\n        System.out.printf(\"Course: %-20s | Modules: %02d | Tuition: $%.2f%n\",\n                courseName, moduleCount, cost);\n                \n        // Simulated reading from string scanner\n        String sampleInput = \"Alex\\n24\\nSoftware Engineer\";\n        Scanner sc = new Scanner(sampleInput);\n        \n        String name = sc.nextLine();\n        int age = sc.nextInt();\n        sc.nextLine(); // consume trailing newline\n        String role = sc.nextLine();\n        \n        System.out.println(\"Parsed: \" + name + \" (\" + age + \") - \" + role);\n    }\n}",
        "Course: Java Masterclass     | Modules: 08 | Tuition: $0.00\nParsed: Alex (24) - Software Engineer",
        [
            "printf formats columns with left-alignment (%-20s) and zero-padded integer (%02d).",
            "sc.nextLine reads up to the line delimiter.",
            "sc.nextInt parses the integer token 24.",
            "sc.nextLine flushes the remaining newline character before reading 'Software Engineer'."
        ],
        [
            "Forgetting to flush the scanner buffer after nextInt() before calling nextLine().",
            "Using mismatched printf format specifiers (e.g. %d for a floating point double)."
        ],
        [
            ("What format specifier outputs a floating-point number with exactly 3 decimal places?", "Answer: %.3f"),
            ("Why should Scanner instances connected to System.in generally not be closed in modular helper methods?", "Think about closing System.in for the remainder of the JVM process."),
            ("What exception is thrown by scanner.nextInt() if the user types non-numeric text like 'abc'?", "Identify InputMismatchException.")
        ]
    ),
    (
        "Operators", 25,
        [
            "Utilize arithmetic, relational, logical, assignment, and unary operators",
            "Understand operator precedence and associativity rules",
            "Leverage short-circuit evaluation in boolean expressions"
        ],
        "Operators perform operations on variables and values:\n1. Arithmetic: `+`, `-`, `*`, `/`, `%` (modulo remainder)\n2. Relational: `==`, `!=`, `>`, `<`, `>=`, `<=` (yields boolean)\n3. Logical: `&&` (AND), `||` (OR), `!` (NOT)\n4. Assignment & Compound: `=`, `+=`, `-=`, `*=`, `/=`, `%=`\n5. Unary & Increment: `++var` (pre-increment), `var++` (post-increment), `--`\nShort-Circuiting: In `A && B`, if A is false, B is NEVER evaluated. In `A || B`, if A is true, B is NEVER evaluated. This allows guarding against null pointer checks safely (e.g., `str != null && str.length() > 0`).",
        "// Ternary Operator:\nresult = (condition) ? valueIfTrue : valueIfFalse;\n\n// Compound assignment with automatic casting:\nint x = 10;\nx += 5; // x = 15",
        "public class OperatorsDemo {\n    public static void main(String[] args) {\n        int count = 5;\n        int post = count++; // post=5, count=6\n        int pre = ++count;  // count=7, pre=7\n        \n        int a = 17, b = 5;\n        int quotient = a / b; // 3\n        int remainder = a % b; // 2\n        \n        // Short-circuit guard\n        String label = null;\n        boolean isValid = (label != null) && (label.length() > 0); // Safely returns false without NPE\n        \n        // Ternary operator\n        int score = 82;\n        String status = (score >= 70) ? \"PASSED\" : \"NEEDS_REVIEW\";\n        \n        System.out.println(\"Post: \" + post + \" | Pre: \" + pre + \" | Current: \" + count);\n        System.out.println(\"17 / 5 = \" + quotient + \" with remainder \" + remainder);\n        System.out.println(\"Guard check: \" + isValid + \" | Status: \" + status);\n    }\n}",
        "Post: 5 | Pre: 7 | Current: 7\n17 / 5 = 3 with remainder 2\nGuard check: false | Status: PASSED",
        [
            "Post-increment evaluates the existing value first before incrementing.",
            "Pre-increment updates the variable before producing the expression value.",
            "The short-circuit AND stops execution at (label != null) because it is false, protecting against NullPointerException."
        ],
        [
            "Confusing assignment `=` with equality comparison `==`.",
            "Using bitwise `&` instead of short-circuit `&&`, causing expressions with null checks to throw NullPointerException."
        ],
        [
            ("What is the difference between post-increment (i++) and pre-increment (++i)?", "Trace order of assignment versus mutation."),
            ("How does the ternary operator compare to a traditional if-else block?", "Understand expressions returning values versus control flow statements."),
            ("What is the result of `10 + 20 + \"Java\"` versus `\"Java\" + 10 + 20`?", "Trace left-to-right evaluation and string concatenation precedence.")
        ]
    ),
    (
        "Comments and coding conventions", 15,
        [
            "Apply single-line, multi-line, and Javadoc comment styles",
            "Adhere to standard Java naming conventions (PascalCase, camelCase, UPPER_CASE)",
            "Structure clean, maintainable, self-documenting code"
        ],
        "Code readability is as vital as correctness:\n1. Comments:\n   - Single-line: `// comment`\n   - Multi-line: `/* block */`\n   - Javadoc: `/** Documentation tags @param, @return, @throws */` parsed by javadoc tool to generate HTML docs.\n2. Naming Conventions:\n   - Classes and Interfaces: PascalCase (e.g., `CourseService`, `StudentEnrollment`)\n   - Methods and Variables: camelCase (e.g., `calculateProgressPercentage()`, `lessonCount`)\n   - Constants: UPPER_SNAKE_CASE (e.g., `MAX_RETRY_ATTEMPTS`, `DEFAULT_TIMEOUT_MS`)\n   - Packages: lowercase words (e.g., `com.learnhub.service`)",
        "/**\n * Represents a student course enrollment.\n * @author LearnHub Faculty\n * @version 1.0\n */\npublic class Enrollment {\n    // Implementation\n}",
        "public class ConventionsDemo {\n    public static final int MAX_BUFFER_SIZE = 1024;\n\n    /**\n     * Calculates the completion percentage for a course track.\n     * @param completed count of finished lessons\n     * @param total total lessons count\n     * @return completion percentage from 0.0 to 100.0\n     */\n    public static double computeProgress(int completed, int total) {\n        if (total <= 0) return 0.0;\n        return ((double) completed / total) * 100.0;\n    }\n\n    public static void main(String[] args) {\n        double rate = computeProgress(14, 20);\n        System.out.printf(\"Calculated Rate: %.1f%%%n\", rate);\n    }\n}",
        "Calculated Rate: 70.0%",
        [
            "Javadoc block precedes computeProgress with standard @param and @return tags.",
            "Naming follows PascalCase for class, camelCase for method, and UPPERCASE for constant."
        ],
        [
            "Writing redundant comments that state the obvious rather than explaining 'why' the logic exists.",
            "Violating case conventions such as naming classes with a lowercase letter."
        ],
        [
            ("Which tag in Javadoc documents exceptions thrown by a method?", "Look up @throws or @exception."),
            ("Why should constant names be written in UPPER_SNAKE_CASE?", "Consider visual distinction between mutable variables and compile-time constants."),
            ("How does clean formatting and indentation assist code review and debugging?", "Reflect on code readability and bug prevention.")
        ]
    )
]

print(f"Module 1 ready: {len(m1_lessons)} lessons.")
