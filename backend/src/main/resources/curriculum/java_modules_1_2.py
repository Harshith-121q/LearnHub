from formatter import format_lesson

def get_java_module_1():
    lessons = [
        format_lesson(
            "java",
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
                "Variables 'platform' and 'ecosystem' are allocated as String references in heap memory.",
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
        format_lesson(
            "java",
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
        format_lesson(
            "java",
            "JDK, JRE, and JVM", 25,
            [
                "Differentiate the roles of JDK, JRE, and JVM",
                "Trace execution from source code through bytecode to native instructions",
                "Distinguish development toolsets from runtime execution environments"
            ],
            "The Java execution architecture comprises three interdependent layers:\n1. JVM (Java Virtual Machine): The abstract computing machine that executes bytecode instructions on the host OS. It handles class loading, verification, and JIT compilation.\n2. JRE (Java Runtime Environment): Contains the JVM alongside standard runtime class libraries (java.base, etc.). It enables running Java programs but lacks compilation tools.\n3. JDK (Java Development Kit): The comprehensive superset required by software developers. It bundles the JRE, compiler (javac), packager (jar), archiver, and debugger (jdb).",
            "// Workflow diagram:\n// Developer writes -> App.java\n// javac compiles     -> App.class (Bytecode)\n// JVM loads/runs    -> ClassLoader -> Bytecode Verifier -> JIT / Interpreter -> Machine Code",
            "public class ArchitectureDemo {\n    public static void main(String[] args) {\n        String javaVersion = System.getProperty(\"java.version\");\n        String javaVendor = System.getProperty(\"java.vendor\");\n        String osName = System.getProperty(\"os.name\");\n        System.out.println(\"Running on JVM: \" + javaVersion + \" (\" + javaVendor + \")\");\n        System.out.println(\"Host OS: \" + osName);\n    }\n}",
            "Running on JVM: 17.0.x (Oracle Corporation)\nHost OS: Windows 11",
            [
                "System.getProperty queries properties supplied by the executing JVM runtime environment.",
                "The execution verifies that bytecode compiled on any platform executes identical logic."
            ],
            [
                "Installing only the JRE and attempting to compile code with javac.",
                "Believing the JVM is platform-independent; the JVM is platform-specific, but the bytecode it executes is platform-independent."
            ],
            [
                ("Why can a Java .class file compiled on Windows run on Linux without recompilation?", "Explain the role of the platform-specific JVM interpreting standard bytecode."),
                ("What is the primary difference between JRE and JDK?", "Compare the needs of an end-user running an app vs. a software engineer building one."),
                ("What stage in the JVM checks that bytecode does not violate memory access permissions?", "Identify the Bytecode Verifier.")
            ]
        ),
        format_lesson(
            "java",
            "Installing Java and setting up the environment", 20,
            [
                "Install a modern Long-Term Support (LTS) JDK distribution",
                "Configure system PATH and JAVA_HOME environment variables",
                "Verify developer tools from the command-line interface"
            ],
            "To develop Java applications, you need a certified OpenJDK build (such as Eclipse Temurin, Amazon Corretto, or Oracle JDK). After running the installer, your operating system must locate the executables: `JAVA_HOME` must point to the root directory of your JDK installation, and `%JAVA_HOME%\\bin` (or `$JAVA_HOME/bin` on Unix) must be added to your system `PATH`.",
            "// Terminal commands for environment verification\njava -version\njavac -version\necho %JAVA_HOME%   # On Windows\necho $JAVA_HOME    # On macOS / Linux",
            "public class EnvironmentCheck {\n    public static void main(String[] args) {\n        String javaHome = System.getenv(\"JAVA_HOME\");\n        System.out.println(\"JAVA_HOME configured: \" + (javaHome != null ? javaHome : \"Inherited from PATH\"));\n        System.out.println(\"Java Specification: \" + System.getProperty(\"java.specification.version\"));\n    }\n}",
            "JAVA_HOME configured: C:\\Program Files\\Eclipse Adoptium\\jdk-17\nJava Specification: 17",
            [
                "System.getenv inspects environment variables exported by the operating system shell.",
                "System.getProperty verifies the Java language specification version of the current process."
            ],
            [
                "Pointing JAVA_HOME to the bin folder instead of the JDK root directory.",
                "Forgetting to restart existing terminal windows after editing environment variables."
            ],
            [
                ("Why is an LTS (Long-Term Support) release like Java 17 or 21 recommended for production?", "Consider security updates, stability, and enterprise vendor support timelines."),
                ("How does your operating system use the PATH variable to resolve commands?", "Explain directory lookup order when typing commands into a shell."),
                ("What does the error 'javac: command not found' indicate?", "Identify missing PATH entry for the JDK bin directory.")
            ]
        ),
        format_lesson(
            "java",
            "First Java program", 25,
            [
                "Author, compile, and execute your inaugural Java program",
                "Deconstruct every keyword in the canonical main entry signature",
                "Understand javac compilation and JVM execution commands"
            ],
            "Every standalone Java application requires an entry point with an exact signature: `public static void main(String[] args)`. \n- `public`: Visible to the JVM runtime from outside the package.\n- `static`: Can be called without instantiating an instance of the enclosing class.\n- `void`: Does not return any value to the caller.\n- `main`: The designated method name required by the runtime specification.\n- `String[] args`: Captures command-line arguments passed during invocation.",
            "javac HelloWorld.java    // Produces HelloWorld.class\njava HelloWorld           // Executes bytecode in the JVM",
            "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, LearnHub Java Masterclass!\");\n        System.out.println(\"Compilation and execution successful.\");\n    }\n}",
            "Hello, LearnHub Java Masterclass!\nCompilation and execution successful.",
            [
                "The source file must be named HelloWorld.java matching the public class name.",
                "javac compiles the source file into HelloWorld.class.",
                "java HelloWorld starts the JVM, loads the class, and invokes the main method."
            ],
            [
                "Omitting 'static' in main, which prevents the JVM from finding the static entry point.",
                "Writing 'java HelloWorld.class' instead of 'java HelloWorld' when executing."
            ],
            [
                ("What occurs if the file is named Test.java but contains 'public class Sample'?", "Review Java's rule regarding public class names and file names."),
                ("Why does main have a void return type?", "Reflect on how Java terminates processes vs languages like C/C++ returning integer status codes."),
                ("What does System.out represent?", "Explain standard output PrintStream.")
            ]
        ),
        format_lesson(
            "java",
            "Java program structure", 20,
            [
                "Identify packages, imports, class declarations, and methods",
                "Apply Java statement termination, blocks, and brace etiquette",
                "Understand identifier naming conventions and case sensitivity"
            ],
            "A Java source file adheres to a structured organizational hierarchy:\n1. Package declaration (optional, but standard in real applications): groups related classes.\n2. Import statements: brings external classes into scope.\n3. Class definition: the structural container holding fields and methods.\n4. Curly braces `{}` delineate blocks of code, and statements end with semicolons `;`.\nJava is strictly case-sensitive: `myVariable` and `MyVariable` are entirely different identifiers.",
            "package com.learnhub.model;\n\nimport java.util.Date;\n\npublic class StudentProfile {\n    // Fields (State)\n    private String name;\n    \n    // Methods (Behavior)\n    public void display() {\n        // Statements\n    }\n}",
            "public class StructureDemo {\n    public static void main(String[] args) {\n        int classSize = 35;\n        String courseName = \"Java Core\";\n        \n        if (classSize > 0) {\n            System.out.println(\"Course: \" + courseName);\n            System.out.println(\"Enrollment: \" + classSize + \" students\");\n        }\n    }\n}",
            "Course: Java Core\nEnrollment: 35 students",
            [
                "Statements inside main execute sequentially from top to bottom.",
                "The if block introduces a local inner scope enclosed by curly braces."
            ],
            [
                "Leaving off the closing semicolon at the end of a statement.",
                "Mismatched opening and closing curly braces causing compilation syntax errors."
            ],
            [
                ("Can a single Java file contain more than one top-level public class?", "Explain the single public class per file constraint in Java."),
                ("What is the consequence of Java's case sensitivity on keyword usage (e.g. Class vs class)?", "Consider compiler keyword recognition."),
                ("Why are code blocks delineated by braces rather than indentation?", "Contrast Java's syntactic grammar with Python.")
            ]
        ),
        format_lesson(
            "java",
            "Variables and constants", 20,
            [
                "Declare, initialize, and reassign variables in Java",
                "Apply the 'final' keyword to define compile-time and runtime constants",
                "Differentiate local variables from class attributes"
            ],
            "A variable is a named storage location in memory with a designated type. In Java, local variables must be explicitly initialized before reading. The `final` keyword designates an immutable constant: once assigned a value, it cannot be rebound or reassigned. Constants conventionalize names in `UPPER_SNAKE_CASE`.",
            "dataType variableName = initialValue;\nfinal dataType CONSTANT_NAME = constantValue;",
            "public class VariablesDemo {\n    public static void main(String[] args) {\n        // Mutable local variables\n        int completedLessons = 5;\n        completedLessons = completedLessons + 1;\n        \n        // Immutable constants\n        final int TOTAL_MODULES = 8;\n        final double PASSING_SCORE = 75.0;\n        \n        System.out.println(\"Lessons completed: \" + completedLessons);\n        System.out.println(\"Total course modules: \" + TOTAL_MODULES);\n        System.out.println(\"Passing threshold: \" + PASSING_SCORE + \"%\");\n    }\n}",
            "Lessons completed: 6\nTotal course modules: 8\nPassing threshold: 75.0%",
            [
                "completedLessons is declared as an int and incremented to 6.",
                "TOTAL_MODULES and PASSING_SCORE are sealed with final; reassigning them causes javac compilation failure."
            ],
            [
                "Attempting to reassign a final variable (e.g. `PASSING_SCORE = 80.0`).",
                "Reading a local variable before giving it an initial value."
            ],
            [
                ("What error does the Java compiler produce when an uninitialized local variable is read?", "Identify variable might not have been initialized."),
                ("What is the difference between a variable and a constant?", "Discuss mutability and memory reassignment."),
                ("Why do constants follow the UPPER_SNAKE_CASE naming convention?", "Explain readability and convention standard.")
            ]
        ),
        format_lesson(
            "java",
            "Primitive data types", 25,
            [
                "Identify and utilize all 8 primitive data types in Java",
                "Select appropriate data types based on memory footprint and numerical precision",
                "Apply literal suffixes (L for long, f for float, d for double)"
            ],
            "Java provides 8 primitive types stored directly in memory (stack) rather than as heap objects:\n- Integer numbers: `byte` (8-bit), `short` (16-bit), `int` (32-bit, default), `long` (64-bit, suffix `L`)\n- Floating-point: `float` (32-bit single precision, suffix `f`), `double` (64-bit double precision, default)\n- Character: `char` (16-bit Unicode character enclosed in single quotes `'a'`)\n- Boolean: `boolean` (`true` or `false`)",
            "byte b = 127;\nshort s = 32000;\nint count = 100000;\nlong distance = 9876543210L;\nfloat price = 19.99f;\ndouble precise = 3.14159265359;\nchar grade = 'A';\nboolean active = true;",
            "public class PrimitiveDemo {\n    public static void main(String[] args) {\n        byte daysInWeek = 7;\n        int studentId = 10452;\n        long serverRequests = 8500000000L;\n        double completionRate = 94.75;\n        char performanceTier = 'S';\n        boolean certified = true;\n        \n        System.out.println(\"Student ID: \" + studentId + \" [Tier: \" + performanceTier + \"]\");\n        System.out.println(\"Total Requests: \" + serverRequests);\n        System.out.println(\"Completion: \" + completionRate + \"% | Certified: \" + certified);\n    }\n}",
            "Student ID: 10452 [Tier: S]\nTotal Requests: 8500000000\nCompletion: 94.75% | Certified: true",
            [
                "serverRequests requires the 'L' suffix because 8.5 billion exceeds the maximum 32-bit signed int range (2,147,483,647).",
                "char holds Unicode code points; double provides IEEE 754 precision."
            ],
            [
                "Omitting the 'L' suffix on large long literals, causing 'integer number too large' compiler errors.",
                "Using double or float for currency calculations where binary floating point rounding errors occur (use BigDecimal instead)."
            ],
            [
                ("What is the memory size in bits of a Java boolean, and why is it not strictly fixed by the JVM spec?", "Discuss JVM implementation details where booleans are often represented as 32-bit ints or bytes in arrays."),
                ("Why does float f = 3.14 fail to compile without an 'f' suffix?", "Explain that decimal floating literals default to 64-bit double."),
                ("What is the numeric range of a signed byte in Java?", "Identify -128 to +127.")
            ]
        ),
        format_lesson(
            "java",
            "Type conversion and casting", 20,
            [
                "Differentiate widening (implicit) from narrowing (explicit) type casting",
                "Anticipate numerical overflow and precision loss during conversion",
                "Safely convert between character codes and integers"
            ],
            "Type casting is converting a value from one primitive type to another:\n1. Widening Casting (Implicit): Moving from smaller to larger data types (`byte -> short -> int -> long -> float -> double`). Happens automatically because there is no loss of magnitude.\n2. Narrowing Casting (Explicit): Moving from larger to smaller data types (`double -> float -> long -> int -> short -> byte`). Requires explicit syntax `(type) value` and can result in truncation or data loss.",
            "// Widening (automatic)\nint num = 100;\ndouble d = num;\n\n// Narrowing (manual)\ndouble pi = 3.14159;\nint truncated = (int) pi; // 3",
            "public class CastingDemo {\n    public static void main(String[] args) {\n        // Widening\n        int lessonsCount = 45;\n        double exactRatio = lessonsCount;\n        \n        // Narrowing with precision truncation\n        double rawScore = 89.95;\n        int roundedScore = (int) rawScore;\n        \n        // Overflow during narrow casting\n        int largeVal = 130;\n        byte overflowByte = (byte) largeVal;\n        \n        System.out.println(\"Widened double: \" + exactRatio);\n        System.out.println(\"Narrowed score: \" + roundedScore + \" (fraction truncated)\");\n        System.out.println(\"130 cast to byte: \" + overflowByte + \" (overflow wrap)\");\n    }\n}",
            "Widened double: 45.0\nNarrowed score: 89 (fraction truncated)\n130 cast to byte: -126 (overflow wrap)",
            [
                "Widening converts 45 to 45.0 without precision loss.",
                "Narrowing truncates the fractional part .95 from rawScore, giving 89.",
                "Casting 130 into an 8-bit signed byte (-128 to 127) overflows and wraps around to -126 via two's complement arithmetic."
            ],
            [
                "Assuming (int) 89.95 rounds up to 90; casting truncates toward zero.",
                "Casting large numbers to smaller integer types without checking bounds, leading to negative or corrupted values."
            ],
            [
                ("How do you round a double to the nearest whole integer in Java?", "Use Math.round(double)."),
                ("Why can an int be converted to float automatically, yet precision may theoretically be lost?", "Compare 32-bit mantissa size vs 32-bit integer range."),
                ("What is the result of casting char 'A' to int?", "Explain ASCII / Unicode code point 65.")
            ]
        ),
        format_lesson(
            "java",
            "Input and output", 25,
            [
                "Output formatted data using print, println, and printf",
                "Capture terminal user input using java.util.Scanner",
                "Prevent and handle common Scanner newline consumption bugs"
            ],
            "Java handles console I/O through `System.out` (standard output) and `System.in` (standard input).\n- `print()`: Prints text without advancing to a new line.\n- `println()`: Prints text and appends a line separator.\n- `printf()`: Formats text using specifiers like `%s` (string), `%d` (integer), `%.2f` (float).\nInput is captured using `Scanner`: methods like `nextInt()`, `nextDouble()`, and `nextLine()` parse tokens. Beware: calling `nextLine()` immediately after `nextInt()` captures the residual newline character left in the buffer unless cleared with an extra `nextLine()` call.",
            "import java.util.Scanner;\nScanner scanner = new Scanner(System.in);\nint age = scanner.nextInt();\nscanner.nextLine(); // Clear buffer\nString name = scanner.nextLine();",
            "import java.util.Scanner;\n\npublic class InputOutputDemo {\n    public static void main(String[] args) {\n        String simulatedInput = \"42\\nAlex Morgan\\n\";\n        Scanner scanner = new Scanner(simulatedInput);\n        \n        int id = scanner.nextInt();\n        scanner.nextLine(); // Consume residual newline\n        String studentName = scanner.nextLine();\n        \n        System.out.printf(\"ID: %05d | Student: %-15s | Status: Active%n\", id, studentName);\n    }\n}",
            "ID: 00042 | Student: Alex Morgan     | Status: Active",
            [
                "scanner.nextInt() parses the numeric token 42.",
                "scanner.nextLine() clears the remaining newline character before reading the full name string.",
                "System.out.printf formats the output using width specifiers and zero padding (%05d)."
            ],
            [
                "Forgetting to clear the newline buffer before calling nextLine(), causing empty string reads.",
                "Forgetting to close resources or handling InputMismatchException when non-numeric input is entered."
            ],
            [
                ("What does the %n format specifier represent in System.out.printf?", "Explain platform-independent newline separator."),
                ("Why does scanner.next() differ from scanner.nextLine()?", "Explain token delimiter (whitespace) vs line delimiter (newline)."),
                ("What exception is thrown by scanner.nextInt() if the user types non-numeric text like 'abc'?", "Identify InputMismatchException.")
            ]
        ),
        format_lesson(
            "java",
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
        format_lesson(
            "java",
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
    return {
        "title": "Module 1 — Introduction to Java",
        "description": "Understand Java, set up the environment, and write simple programs.",
        "sequenceOrder": 1,
        "lessons": lessons
    }

def get_java_module_2():
    lessons = [
        format_lesson(
            "java",
            "Boolean expressions", 20,
            [
                "Evaluate truth values and relational comparisons",
                "Construct composite boolean expressions using logical operators (&&, ||, !)",
                "Apply truth tables to trace complex logical conditions"
            ],
            "A boolean expression is any expression that evaluates to either `true` or `false`. Relational operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) compare primitives. Logical operators combine boolean expressions:\n- `&&` (Logical AND): true only when BOTH operands are true.\n- `||` (Logical OR): true when AT LEAST ONE operand is true.\n- `!` (Logical NOT): inverts truth value (true becomes false, false becomes true).\nJava executes short-circuit evaluation: in `A && B`, if A is false, B is skipped.",
            "boolean isEligible = (age >= 18) && (hasPrerequisite || isExempt);",
            "public class BooleanExpressionsDemo {\n    public static void main(String[] args) {\n        int age = 22;\n        boolean hasPrerequisite = true;\n        boolean hasActiveHolds = false;\n        \n        boolean canEnroll = (age >= 18) && hasPrerequisite && !hasActiveHolds;\n        \n        System.out.println(\"Age: \" + age);\n        System.out.println(\"Has Prerequisite: \" + hasPrerequisite);\n        System.out.println(\"Account Holds: \" + hasActiveHolds);\n        System.out.println(\"Enrollment Permission Granted: \" + canEnroll);\n    }\n}",
            "Age: 22\nHas Prerequisite: true\nAccount Holds: false\nEnrollment Permission Granted: true",
            [
                "Expressions are evaluated according to operator precedence: ! highest, then &&, then ||.",
                "canEnroll evaluates to true because age >= 18 is true, hasPrerequisite is true, and !hasActiveHolds evaluates to true."
            ],
            [
                "Confusing boolean equality `==` with assignment `=` inside conditionals.",
                "Neglecting operator precedence by omitting parentheses in expressions mixing `&&` and `||`."
            ],
            [
                ("What does De Morgan's Law state regarding `!(A && B)`?", "Show that !(A && B) is equivalent to (!A || !B)."),
                ("What is the truth value of `false || true && false`?", "Consider precedence of && over || (evaluates to false)."),
                ("Why is short-circuit evaluation important when testing `ref != null && ref.isValid()`?", "Explain prevention of NullPointerException.")
            ]
        ),
        format_lesson(
            "java",
            "if statement", 20,
            [
                "Direct program flow with single-branch conditional decisions",
                "Apply standard block formatting and curly brace guidelines",
                "Evaluate numeric thresholds and boolean flag states"
            ],
            "The `if` statement executes a block of code only if a specified condition evaluates to `true`. If the condition evaluates to `false`, the code block is bypassed entirely. While single-statement if bodies can omit braces, Java conventions strictly recommend ALWAYS using braces `{}` to avoid accidental logic errors.",
            "if (condition) {\n    // Statements executed if condition is true\n}",
            "public class IfStatementDemo {\n    public static void main(String[] args) {\n        int score = 85;\n        System.out.println(\"Evaluating score: \" + score);\n        \n        if (score >= 70) {\n            System.out.println(\"Status: Passing Grade Confirmed!\");\n            System.out.println(\"Eligible for certificate issuance.\");\n        }\n        \n        System.out.println(\"Evaluation complete.\");\n    }\n}",
            "Evaluating score: 85\nStatus: Passing Grade Confirmed!\nEligible for certificate issuance.\nEvaluation complete.",
            [
                "The boolean expression `score >= 70` evaluates to true (85 >= 70).",
                "The enclosed block executes both print statements sequentially before continuing."
            ],
            [
                "Placing a semicolon immediately after the if condition (e.g. `if (score >= 70);`), which creates an empty statement and runs the subsequent block unconditionally.",
                "Omitting braces when intending to execute multiple statements inside the conditional."
            ],
            [
                ("What happens if a semicolon is placed after `if (x > 0);`?", "Explain null statement execution."),
                ("Can non-boolean types like integers (0 or 1) be used as if conditions in Java?", "Explain Java's strict boolean requirement vs C/C++ truthy values."),
                ("Write an if statement that checks if a given integer is strictly positive.", "Use `if (num > 0)`.")
            ]
        ),
        format_lesson(
            "java",
            "if-else", 20,
            [
                "Implement two-way branching logic in Java programs",
                "Validate inputs and assign binary classifications (e.g. even/odd, pass/fail)",
                "Ensure mutually exclusive execution paths"
            ],
            "The `if-else` statement provides two-way branching: if the boolean condition evaluates to `true`, the `if` block executes; otherwise, the `else` block executes. Exactly one of the two blocks is guaranteed to execute.",
            "if (condition) {\n    // Path A (true)\n} else {\n    // Path B (false)\n}",
            "public class IfElseDemo {\n    public static void main(String[] args) {\n        int number = 47;\n        \n        if (number % 2 == 0) {\n            System.out.println(number + \" is an EVEN integer.\");\n        } else {\n            System.out.println(number + \" is an ODD integer.\");\n        }\n    }\n}",
            "47 is an ODD integer.",
            [
                "The expression `47 % 2` produces remainder 1.",
                "1 == 0 evaluates to false, causing execution to jump to the `else` block."
            ],
            [
                "Using separate unlinked `if` statements instead of `if-else` when logic is mutually exclusive.",
                "Attempting to add conditions directly to an `else` keyword without an `if`."
            ],
            [
                ("How does an if-else structure guarantee exhaustive coverage for binary conditions?", "Explain mutual exclusivity."),
                ("Can an else block exist without a preceding if block?", "Explain compiler syntax requirement."),
                ("Write an if-else statement to check if a student score of 62 is passing (threshold 60).", "Provide sample code.")
            ]
        ),
        format_lesson(
            "java",
            "else-if ladder", 25,
            [
                "Evaluate multi-way conditional scenarios using else-if ladders",
                "Order condition checks logically from most specific to most general",
                "Identify and eliminate unreachable dead-code branches"
            ],
            "When dealing with more than two possible outcomes, the `else-if` ladder evaluates conditions sequentially from top to bottom. The first condition that evaluates to `true` has its block executed, and all subsequent branches are skipped. The optional final `else` catches all remaining cases. Ordering is critical: if a general condition is placed before a specific condition, the specific branch becomes unreachable.",
            "if (cond1) {\n    // branch 1\n} else if (cond2) {\n    // branch 2\n} else {\n    // fallback\n}",
            "public class ElseIfLadderDemo {\n    public static void main(String[] args) {\n        int percentage = 88;\n        char grade;\n        \n        if (percentage >= 90) {\n            grade = 'A';\n        } else if (percentage >= 80) {\n            grade = 'B';\n        } else if (percentage >= 70) {\n            grade = 'C';\n        } else if (percentage >= 60) {\n            grade = 'D';\n        } else {\n            grade = 'F';\n        }\n        \n        System.out.println(\"Percentage: \" + percentage + \"% | Letter Grade: \" + grade);\n    }\n}",
            "Percentage: 88% | Letter Grade: B",
            [
                "88 >= 90 is false, so it falls to the next check.",
                "88 >= 80 is true, setting grade = 'B' and exiting the ladder immediately."
            ],
            [
                "Ordering conditions from general to specific (e.g. checking `>= 60` before `>= 90`), causing higher grades to be misclassified.",
                "Duplicating boundary values across conditions leading to subtle off-by-one errors."
            ],
            [
                ("Why would checking `score >= 50` at the very top of a grading ladder be a fatal bug?", "Explain how all scores above 50 would match the lowest passing grade."),
                ("Is the final `else` clause mandatory in an else-if ladder?", "Explain optional default handling vs exhaustive handling."),
                ("Write an else-if ladder determining water temperature states (Freezing <= 0, Boiling >= 100, Liquid).", "Provide clear ladder.")
            ]
        ),
        format_lesson(
            "java",
            "Nested conditions", 20,
            [
                "Nest conditional logic to evaluate secondary criteria",
                "Refactor deeply nested conditions into flat expressions using logical operators",
                "Maintain code readability by avoiding excessive branching depth"
            ],
            "Nested conditions are `if` or `if-else` statements placed inside another conditional block. They are useful when a secondary decision depends strictly on a primary condition being met (e.g. user authentication succeeded, now check authorization role). However, excessive nesting ('arrow anti-pattern') degrades readability and should be flattened using guard clauses or composite boolean operators.",
            "if (isAuthenticated) {\n    if (hasAdminRole) {\n        // Perform privileged action\n    }\n}",
            "public class NestedConditionsDemo {\n    public static void main(String[] args) {\n        boolean isAuthenticated = true;\n        String userRole = \"INSTRUCTOR\";\n        boolean isCourseAssigned = true;\n        \n        if (isAuthenticated) {\n            System.out.println(\"User authenticated.\");\n            if (\"ADMIN\".equals(userRole)) {\n                System.out.println(\"Full administrative rights granted.\");\n            } else if (\"INSTRUCTOR\".equals(userRole)) {\n                if (isCourseAssigned) {\n                    System.out.println(\"Instructor authorized to review assigned course.\");\n                } else {\n                    System.out.println(\"Instructor not assigned to this course.\");\n                }\n            } else {\n                System.out.println(\"Standard student view enabled.\");\n            }\n        } else {\n            System.out.println(\"Access denied: Please log in.\");\n        }\n    }\n}",
            "User authenticated.\nInstructor authorized to review assigned course.",
            [
                "First evaluates authentication; if true, proceeds to evaluate the user's role.",
                "The nested block checks if the instructor is assigned to the course and outputs the corresponding permission."
            ],
            [
                "Nesting more than 3 levels deep, creating unreadable 'spaghetti' code.",
                "Failing to handle the else branches of inner nested conditions, causing silent failures."
            ],
            [
                ("How can guard clauses (early returns) reduce nested if complexity in methods?", "Explain returning early on invalid preconditions."),
                ("When should you replace nested conditions with a combined `&&` condition?", "Discuss when no intermediate statements are needed between checks."),
                ("Write a nested condition verifying whether a person is eligible for a driver's license (Age >= 18 and Vision test passed).", "Provide sample code.")
            ]
        ),
        format_lesson(
            "java",
            "switch statements", 25,
            [
                "Implement multi-branch selection using classic switch statements and break statements",
                "Understand supported switch data types (primitives, enums, Strings)",
                "Leverage modern Java 14+ switch expressions with arrow syntax"
            ],
            "The `switch` statement selects one of many code blocks to execute based on the value of a single selector expression. Supported types include `byte`, `short`, `char`, `int`, `String`, and `enum`.\n- Classic switch: Requires explicit `break` statements to prevent falling through into subsequent cases.\n- Modern switch expressions (Java 14+): Uses arrow syntax `case VALUE -> expression;`, eliminates accidental fall-through, and can directly return a value.",
            "// Modern switch expression (Java 14+)\nString result = switch (day) {\n    case MONDAY, FRIDAY -> \"Busy\";\n    case SATURDAY, SUNDAY -> \"Weekend\";\n    default -> \"Standard\";\n};",
            "public class SwitchDemo {\n    public static void main(String[] args) {\n        int dayOfWeek = 3;\n        String dayName;\n        \n        // Classic switch with break\n        switch (dayOfWeek) {\n            case 1: dayName = \"Monday\"; break;\n            case 2: dayName = \"Tuesday\"; break;\n            case 3: dayName = \"Wednesday\"; break;\n            case 4: dayName = \"Thursday\"; break;\n            case 5: dayName = \"Friday\"; break;\n            case 6: dayName = \"Saturday\"; break;\n            case 7: dayName = \"Sunday\"; break;\n            default: dayName = \"Invalid Day\"; break;\n        }\n        \n        // Modern switch expression\n        String dayType = switch (dayOfWeek) {\n            case 6, 7 -> \"Weekend\";\n            default -> \"Weekday\";\n        };\n        \n        System.out.println(\"Day: \" + dayName + \" (\" + dayType + \")\");\n    }\n}",
            "Day: Wednesday (Weekday)",
            [
                "The classic switch checks dayOfWeek against case 3, assigns Wednesday, and breaks.",
                "The modern switch maps dayOfWeek directly to 'Weekday' without requiring break keywords."
            ],
            [
                "Forgetting the `break` statement in classic switch, causing unintentional fall-through execution of downstream cases.",
                "Attempting to use unsupported data types like `double` or `float` in a switch expression."
            ],
            [
                ("What types are legally permitted in a Java switch expression?", "List primitives int/byte/short/char, wrapper classes, Strings, and enums."),
                ("What does the 'yield' keyword do in a multi-line modern switch expression block?", "Explain yielding a value from a block."),
                ("Why are floating-point types (float, double) disallowed in switch statements?", "Discuss imprecise binary representation and equality comparisons.")
            ]
        ),
        format_lesson(
            "java",
            "for loop", 25,
            [
                "Construct standard counting loops with initialization, condition, and update expressions",
                "Iterate over numeric sequences and calculate aggregations",
                "Identify loop control variable lifecycle and scoping"
            ],
            "The `for` loop is ideal when the number of iterations is known before entering the loop. Its header consists of three clauses separated by semicolons: `for (initialization; condition; update)`.\n1. Initialization: Executes once before the loop begins.\n2. Condition: Evaluated before each iteration; if true, the body executes; if false, loop terminates.\n3. Update: Executes at the end of each iteration (e.g. incrementing or decrementing the counter).",
            "for (int i = 0; i < count; i++) {\n    // Iteration statements\n}",
            "public class ForLoopDemo {\n    public static void main(String[] args) {\n        int totalSum = 0;\n        int limit = 5;\n        \n        System.out.print(\"Counting: \");\n        for (int i = 1; i <= limit; i++) {\n            System.out.print(i + \" \");\n            totalSum += i;\n        }\n        System.out.println();\n        System.out.println(\"Sum of 1 through \" + limit + \" = \" + totalSum);\n    }\n}",
            "Counting: 1 2 3 4 5 \nSum of 1 through 5 = 15",
            [
                "int i = 1 initializes the loop counter.",
                "The loop tests i <= 5 on each pass and increments i by 1.",
                "totalSum accumulates 1 + 2 + 3 + 4 + 5 = 15."
            ],
            [
                "Off-by-one errors (using `<` instead of `<=` or vice versa).",
                "Mutating the loop counter inside the loop body in unexpected ways, leading to skips or infinite loops."
            ],
            [
                ("What is the scope of a variable declared in the for loop initialization header?", "Explain loop-local scope."),
                ("Can any of the three parts of a for loop header be omitted?", "Explain `for (;;)` as an infinite loop construct."),
                ("Write a for loop that prints even numbers from 2 to 20 in descending order.", "Trace `for (int i = 20; i >= 2; i -= 2)`.")
            ]
        ),
        format_lesson(
            "java",
            "while loop", 20,
            [
                "Implement condition-controlled repetition using precondition while loops",
                "Safely terminate repetition using sentinel values and counter guards",
                "Diagnose and prevent infinite loop conditions"
            ],
            "A `while` loop is a precondition loop that repeats a block of code as long as a specified boolean condition remains `true`. The condition is checked BEFORE the loop body executes. If the condition is initially `false`, the body does not execute even once. To prevent an infinite loop, statements inside the loop must eventually alter the condition to `false`.",
            "while (condition) {\n    // Code to repeat\n    // Progress step\n}",
            "public class WhileLoopDemo {\n    public static void main(String[] args) {\n        int countdown = 5;\n        \n        System.out.println(\"Initiating countdown:\");\n        while (countdown > 0) {\n            System.out.println(\"T-minus: \" + countdown);\n            countdown--; // Decrement counter toward termination\n        }\n        System.out.println(\"Liftoff!\");\n    }\n}",
            "Initiating countdown:\nT-minus: 5\nT-minus: 4\nT-minus: 3\nT-minus: 2\nT-minus: 1\nLiftoff!",
            [
                "Checks condition `countdown > 0`. Since countdown is 5, enters the body.",
                "Decrements countdown on each iteration until it reaches 0, at which point the loop terminates."
            ],
            [
                "Omitting the progress/update step inside the loop body, causing the condition to remain permanently true (infinite loop).",
                "Accidentally placing a semicolon after the while header (`while (cond);`), freezing execution."
            ],
            [
                ("When is a while loop preferred over a for loop?", "Discuss scenarios where the iteration count is indeterminate or event-driven."),
                ("What happens if the condition of a while loop is false at startup?", "Explain that the loop body never executes."),
                ("How does a sentinel value assist in processing dynamic user input?", "Explain terminating a loop when a specific sentinel value like -1 or 'quit' is read.")
            ]
        ),
        format_lesson(
            "java",
            "do-while loop", 20,
            [
                "Implement postcondition loops that guarantee at least one execution",
                "Design interactive menu loops and retry mechanisms",
                "Distinguish do-while execution semantics from standard while loops"
            ],
            "The `do-while` loop is a postcondition loop: the loop body executes FIRST, and then the boolean condition is evaluated at the bottom. Consequently, the body is guaranteed to execute at least once, even if the condition is false on the first check. Syntax requires a terminating semicolon after the while condition.",
            "do {\n    // Executes at least once\n} while (condition);",
            "public class DoWhileDemo {\n    public static void main(String[] args) {\n        int attempts = 0;\n        boolean success = false;\n        \n        do {\n            attempts++;\n            System.out.println(\"Attempt #\" + attempts + \": Connecting to service...\");\n            if (attempts == 2) {\n                success = true;\n                System.out.println(\"Connection established successfully!\");\n            }\n        } while (!success && attempts < 3);\n        \n        System.out.println(\"Total attempts: \" + attempts);\n    }\n}",
            "Attempt #1: Connecting to service...\nAttempt #2: Connecting to service...\nConnection established successfully!\nTotal attempts: 2",
            [
                "The loop body executes immediately before testing `!success && attempts < 3`.",
                "On attempt 2, success becomes true, so the postcondition fails and the loop exits cleanly."
            ],
            [
                "Forgetting the required semicolon `;` after `while (condition);` at the end of the block.",
                "Using do-while where zero iterations are required on invalid initial input."
            ],
            [
                ("Why is do-while universally chosen for console-based interactive menus?", "Explain presenting choices to the user before checking their exit choice."),
                ("How many times does the body of `do { count++; } while (false);` execute?", "Identify exactly 1 time."),
                ("Write a do-while loop prompting for a number between 1 and 10 until valid.", "Provide retry validation loop.")
            ]
        ),
        format_lesson(
            "java",
            "break and continue", 20,
            [
                "Terminate loop execution early using the break statement",
                "Skip remaining statements in the current iteration using continue",
                "Understand labeled break statements for multi-level nested loop escapes"
            ],
            "Java provides jump statements to alter the natural flow of iteration:\n- `break`: Immediately exits the enclosing loop or switch block. Execution resumes at the statement following the loop.\n- `continue`: Skips the remainder of the current iteration and jumps directly to the loop's update step (in a for loop) or condition check (in a while loop).\n- Labeled break/continue: Enables breaking out of multiple nested loops by referencing an outer label.",
            "for (int i = 0; i < 10; i++) {\n    if (i == 3) continue; // skip 3\n    if (i == 7) break;    // stop loop at 7\n}",
            "public class BreakContinueDemo {\n    public static void main(String[] args) {\n        System.out.print(\"Processing items (skipping multiples of 3, halting at 8): \");\n        \n        for (int i = 1; i <= 10; i++) {\n            if (i % 3 == 0) {\n                continue; // Skip multiple of 3\n            }\n            if (i == 8) {\n                System.out.print(\"[Halt at 8] \");\n                break; // Terminate loop early\n            }\n            System.out.print(i + \" \");\n        }\n        System.out.println(\"\\nLoop concluded.\");\n    }\n}",
            "Processing items (skipping multiples of 3, halting at 8): 1 2 4 5 7 [Halt at 8] \nLoop concluded.",
            [
                "When i is 3 or 6, `i % 3 == 0` evaluates to true; `continue` skips the print statement.",
                "When i reaches 8, `break` terminates the loop completely before printing 8, 9, or 10."
            ],
            [
                "Overusing break and continue, making loop termination criteria hard to trace and test.",
                "Placing code immediately after a break or continue statement within the same block, causing 'unreachable code' compiler errors."
            ],
            [
                ("What is the difference between break and continue in a loop?", "Compare complete termination vs skipping to the next iteration."),
                ("How does a labeled break syntax appear in Java?", "Show `outer: for(...) { for(...) { break outer; } }`."),
                ("What does continue do in a while loop regarding the counter update?", "Point out that if the update is after continue, an infinite loop will occur.")
            ]
        ),
        format_lesson(
            "java",
            "Nested loops and patterns", 25,
            [
                "Design nested loop architectures with outer and inner iterators",
                "Trace execution steps across rows and columns",
                "Construct geometric patterns and mathematical matrices"
            ],
            "A nested loop is a loop inside another loop. For every single iteration of the outer loop, the inner loop executes its entire cycle from start to finish. If the outer loop runs $N$ times and the inner loop runs $M$ times, the inner loop body executes $N \\times M$ times. Nested loops are fundamental for multi-dimensional data, matrices, grids, and algorithmic pattern printing.",
            "for (int r = 1; r <= rows; r++) {\n    for (int c = 1; c <= cols; c++) {\n        // Cell processing (r, c)\n    }\n}",
            "public class NestedLoopsDemo {\n    public static void main(String[] args) {\n        int rows = 4;\n        System.out.println(\"Generating right-angled triangle pattern:\");\n        \n        for (int i = 1; i <= rows; i++) {\n            for (int j = 1; j <= i; j++) {\n                System.out.print(\"* \");\n            }\n            System.out.println(); // Move to new row\n        }\n        \n        System.out.println(\"\\nMultiplication Table Fragment (1 to 3):\");\n        for (int x = 1; x <= 3; x++) {\n            for (int y = 1; y <= 3; y++) {\n                System.out.printf(\"%d x %d = %-2d  \", x, y, (x * y));\n            }\n            System.out.println();\n        }\n    }\n}",
            "Generating right-angled triangle pattern:\n* \n* * \n* * * \n* * * * \n\nMultiplication Table Fragment (1 to 3):\n1 x 1 = 1   1 x 2 = 2   1 x 3 = 3   \n2 x 1 = 2   2 x 2 = 4   2 x 3 = 6   \n3 x 1 = 3   3 x 2 = 6   3 x 3 = 9",
            [
                "In the triangle generator, row i determines the inner loop boundary (j <= i).",
                "System.out.println() at the end of the outer loop moves cursor to the next line."
            ],
            [
                "Using the same loop counter variable name for both outer and inner loops (e.g. `i` in both).",
                "Misplacing the newline separator inside the inner loop rather than after it in the outer loop."
            ],
            [
                ("How many times does the innermost statement execute in three nested loops of 5 iterations each?", "Calculate 5 * 5 * 5 = 125."),
                ("How do you invert a triangle pattern to print 4 stars down to 1 star?", "Set inner loop or outer loop in reverse: `for (int i = rows; i >= 1; i--)`."),
                ("Why can deeply nested loops cause performance bottlenecks on large data sets?", "Discuss polynomial time complexity O(n^2), O(n^3).")
            ]
        ),
        format_lesson(
            "java",
            "Practice problems", 30,
            [
                "Solve foundational computational logic problems (Factorial, Prime Check, Fibonacci, Palindrome)",
                "Implement digit extraction algorithms using modulo and division",
                "Analyze time complexity and edge cases in loop-based solutions"
            ],
            "This comprehensive problem set consolidates Module 2 control flow mastery:\n1. Factorial ($n! = n \\times (n-1) \\times \\dots \\times 1$)\n2. Prime Number Check: Verifying divisibility up to $\\sqrt{n}$\n3. Fibonacci Sequence: Generating the series $0, 1, 1, 2, 3, 5, 8, \\dots$\n4. Palindrome Number: Reversing an integer using `% 10` and `/ 10` and checking equality\n5. Sum of Digits: Accumulating individual digits of a number.",
            "// Reverse integer algorithm:\nint rev = 0;\nwhile (n > 0) {\n    rev = rev * 10 + (n % 10);\n    n /= 10;\n}",
            "public class PracticeProblemsDemo {\n    public static long factorial(int n) {\n        long fact = 1;\n        for (int i = 2; i <= n; i++) fact *= i;\n        return fact;\n    }\n    \n    public static boolean isPrime(int n) {\n        if (n <= 1) return false;\n        for (int i = 2; i * i <= n; i++) {\n            if (n % i == 0) return false;\n        }\n        return true;\n    }\n    \n    public static boolean isPalindromeNumber(int n) {\n        int original = n, reversed = 0;\n        while (n > 0) {\n            reversed = reversed * 10 + (n % 10);\n            n /= 10;\n        }\n        return original == reversed;\n    }\n    \n    public static void main(String[] args) {\n        System.out.println(\"5! = \" + factorial(5));\n        System.out.println(\"Is 29 prime? \" + isPrime(29));\n        System.out.println(\"Is 121 a palindrome? \" + isPalindromeNumber(121));\n        System.out.println(\"Is 123 a palindrome? \" + isPalindromeNumber(123));\n    }\n}",
            "5! = 120\nIs 29 prime? true\nIs 121 a palindrome? true\nIs 123 a palindrome? false",
            [
                "factorial(5) multiplies 1 * 2 * 3 * 4 * 5 = 120.",
                "isPrime(29) checks divisibility up to sqrt(29) (~5.3), finds no divisors, and returns true.",
                "isPalindromeNumber extracts digits via modulo 10 and reconstructs the reversed number."
            ],
            [
                "Checking prime numbers up to n instead of sqrt(n), causing unnecessary computational overhead.",
                "Modifying the original number variable during digit reversal without storing a copy, losing the baseline comparison."
            ],
            [
                ("Why is checking divisors up to sqrt(n) sufficient for prime verification?", "Explain factoring symmetry."),
                ("How would you modify the digit sum algorithm to sum only even digits?", "Add an `if ((digit % 2) == 0)` check."),
                ("What is the 10th Fibonacci number starting from 0, 1?", "Calculate 34 (F0=0, F1=1, F2=1, F3=2, F4=3, F5=5, F6=8, F7=13, F8=21, F9=34).")
            ]
        )
    ]
    return {
        "title": "Module 2 — Conditional Statements and Loops",
        "description": "Control the flow of a program and solve introductory logic problems.",
        "sequenceOrder": 2,
        "lessons": lessons
    }

print("Java modules 1 & 2 ready.")
