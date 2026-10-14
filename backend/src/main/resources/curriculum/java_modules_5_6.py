from formatter import format_lesson

def get_java_module_5():
    lessons = [
        format_lesson(
            "java",
            "Exception fundamentals", 20,
            [
                "Understand the Throwable, Exception, and Error hierarchy",
                "Differentiate checked from unchecked (runtime) exceptions",
                "Analyze runtime errors (NullPointerException, ArithmeticException)"
            ],
            "An **Exception** is an abnormal event occurring during program execution that disrupts the normal flow of instructions. The JVM represents errors and exceptions as objects inheriting from `java.lang.Throwable`:\n- `Throwable`\n  - `Error`: Serious problems that a reasonable application should not try to catch (e.g. `OutOfMemoryError`, `StackOverflowError`).\n  - `Exception`: Conditions that a reasonable application might want to catch.\n    - `RuntimeException` (Unchecked): Bugs, programming errors (e.g. `NullPointerException`, `IndexOutOfBoundsException`, `IllegalArgumentException`). Compiler does not force handling.\n    - Checked Exceptions: External conditions like I/O and SQL (`IOException`, `SQLException`). Compiler forces handling.",
            "// Hierarchy: Throwable -> Exception -> RuntimeException (Unchecked)\n//                                  -> IOException, SQLException (Checked)",
            "public class ExceptionFundamentalsDemo {\n    public static void main(String[] args) {\n        System.out.println(\"Demonstrating controlled runtime exception handling:\");\n        try {\n            int result = 100 / 0; // Throws ArithmeticException\n        } catch (ArithmeticException e) {\n            System.out.println(\"Caught expected exception: \" + e.getMessage());\n            System.out.println(\"Exception Type: \" + e.getClass().getSimpleName());\n        }\n        System.out.println(\"Application recovered gracefully.\");\n    }\n}",
            "Demonstrating controlled runtime exception handling:\nCaught expected exception: / by zero\nException Type: ArithmeticException\nApplication recovered gracefully.",
            [
                "The division by zero raises an ArithmeticException instance at runtime.",
                "The catch block intercepts the exception, prints diagnostic info, and allows normal execution to continue."
            ],
            [
                "Catching `Error` or `Throwable` indiscriminately, which can prevent JVM shutdown on fatal out-of-memory states.",
                "Using exceptions for standard control flow instead of proper conditional checks."
            ],
            [
                ("Why does the compiler not force handling of RuntimeException subtypes?", "Explain unchecked programming bugs that can occur virtually anywhere."),
                ("What is the difference between Error and Exception in Java?", "Explain fatal system-level problems vs recoverable application states."),
                ("What happens if an unhandled exception reaches the main method?", "Explain thread termination and printing of stack trace to stderr.")
            ]
        ),
        format_lesson(
            "java",
            "try-catch-finally", 25,
            [
                "Handle exceptions using structured try-catch-finally blocks",
                "Order multiple catch blocks from most specific to most general",
                "Ensure reliable cleanup in the finally block regardless of exception occurrence"
            ],
            "The `try-catch-finally` block is Java's core mechanism for handling exceptions:\n- `try`: Encloses code that might throw an exception.\n- `catch`: Intercepts and handles a specific exception type. Multiple catch blocks can be chained (ordered from specific subclass to generic superclass).\n- `finally`: A block that is **always guaranteed to execute**, whether an exception was thrown, caught, or not thrown at all (and even if the try block contains a `return` statement). Ideal for releasing external resources.",
            "try {\n    // Code that might fail\n} catch (NumberFormatException e) {\n    // Specific handler\n} catch (Exception e) {\n    // Generic fallback\n} finally {\n    // Always runs (cleanup)\n}",
            "public class TryCatchFinallyDemo {\n    public static int parseStudentScore(String input) {\n        System.out.println(\"Parsing input: '\" + input + \"'\");\n        try {\n            return Integer.parseInt(input);\n        } catch (NumberFormatException e) {\n            System.out.println(\"Parsing error: Defaulting to 0\");\n            return 0;\n        } finally {\n            System.out.println(\"Finally block executed (cleanup/audit).\");\n        }\n    }\n    \n    public static void main(String[] args) {\n        int s1 = parseStudentScore(\"95\");\n        System.out.println(\"Score 1: \" + s1 + \"\\n\");\n        \n        int s2 = parseStudentScore(\"invalid\");\n        System.out.println(\"Score 2: \" + s2);\n    }\n}",
            "Parsing input: '95'\nFinally block executed (cleanup/audit).\nScore 1: 95\n\nParsing input: 'invalid'\nParsing error: Defaulting to 0\nFinally block executed (cleanup/audit).\nScore 2: 0",
            [
                "For '95', parsing succeeds, finally executes, and 95 is returned.",
                "For 'invalid', NumberFormatException is caught, the catch block sets return 0, finally executes, and 0 is returned."
            ],
            [
                "Placing a general `catch (Exception e)` BEFORE a specific `catch (IOException e)`, causing a compilation error.",
                "Suppressing exceptions completely with an empty catch block (`catch (Exception e) {}`), hiding bugs silently."
            ],
            [
                ("Under what rare circumstance will a finally block NOT execute?", "Identify System.exit(0) or JVM crash/power loss."),
                ("What does multi-catch syntax look like in Java 7+?", "Show `catch (IOException | SQLException e)`."),
                ("What happens if both try and finally blocks contain return statements?", "Explain finally return overriding try return (anti-pattern).")
            ]
        ),
        format_lesson(
            "java",
            "throw and throws", 20,
            [
                "Explicitly instantiate and throw exceptions using throw",
                "Declare checked exceptions in method signatures using throws",
                "Propagate exceptions up the call stack to appropriate handlers"
            ],
            "Java distinguishes between signaling an exception and declaring it:\n- `throw`: Keyword used inside a method body to explicitly throw an exception object (e.g. `throw new IllegalArgumentException(\"Invalid age\");`).\n- `throws`: Keyword used in the method signature to declare that this method may throw one or more checked exceptions. This alerts callers that they must either catch the exception or declare it in their own signature.",
            "public void process(int age) throws InvalidAgeException {\n    if (age < 0) throw new InvalidAgeException(\"Negative age not allowed\");\n}",
            "public class ThrowThrowsDemo {\n    public static void validateEnrollmentEligibility(int age) {\n        if (age < 16) {\n            throw new IllegalArgumentException(\"Minimum enrollment age is 16. Provided: \" + age);\n        }\n        System.out.println(\"Eligibility verified for age: \" + age);\n    }\n    \n    public static void main(String[] args) {\n        try {\n            validateEnrollmentEligibility(20);\n            validateEnrollmentEligibility(14); // Throws exception\n        } catch (IllegalArgumentException e) {\n            System.out.println(\"Caught expected exception: \" + e.getMessage());\n        }\n    }\n}",
            "Eligibility verified for age: 20\nCaught expected exception: Minimum enrollment age is 16. Provided: 14",
            [
                "validateEnrollmentEligibility verifies the age invariant and throws IllegalArgumentException.",
                "main catches the exception and prints the informative error message."
            ],
            [
                "Confusing `throw` (action statement) with `throws` (method signature clause).",
                "Throwing generic `new Exception()` instead of descriptive standard exceptions."
            ],
            [
                ("Can a method declare unchecked exceptions in its throws clause?", "Explain yes, but it is optional and serves only as documentation."),
                ("What happens if a checked exception is thrown inside a method that does not declare it with throws?", "Explain javac compile failure."),
                ("What information is captured in an exception object when instantiated with new?", "Discuss the stack trace capturing execution call hierarchy.")
            ]
        ),
        format_lesson(
            "java",
            "Checked and unchecked exceptions", 25,
            [
                "Differentiate checked from unchecked exceptions by class hierarchy",
                "Choose between checked and unchecked exceptions when designing APIs",
                "Design sensible, resilient error handling paths"
            ],
            "The division between checked and unchecked exceptions is a core Java design decision:\n- **Checked Exceptions**: Subclasses of `Exception` excluding `RuntimeException`. They represent recoverable environmental errors (e.g. file missing, network unavailable). The compiler enforces 'Catch or Declare'—the code will NOT compile unless handled.\n- **Unchecked Exceptions**: Subclasses of `RuntimeException`. They represent programming bugs or invariant violations (e.g. null pointer, illegal argument). Modern frameworks (like Spring Boot) heavily favor unchecked exceptions to avoid cluttered method signatures.",
            "// Checked (compiler enforced): IOException, SQLException\n// Unchecked (runtime bugs): NullPointerException, IllegalArgumentException, IllegalStateException",
            "import java.io.IOException;\n\npublic class CheckedUncheckedDemo {\n    // Checked: caller MUST handle or declare\n    public static void loadCurriculumFile(String path) throws IOException {\n        if (!path.endsWith(\".json\")) {\n            throw new IOException(\"File format must be JSON. Given: \" + path);\n        }\n        System.out.println(\"Curriculum loaded: \" + path);\n    }\n    \n    public static void main(String[] args) {\n        try {\n            loadCurriculumFile(\"curriculum.txt\");\n        } catch (IOException e) {\n            System.out.println(\"Handled checked exception: \" + e.getMessage());\n        }\n    }\n}",
            "Handled checked exception: File format must be JSON. Given: curriculum.txt",
            [
                "loadCurriculumFile declares throws IOException in its signature.",
                "main safely handles the checked exception inside a try-catch block."
            ],
            [
                "Catching a checked exception and doing nothing, swallowing the error without logging.",
                "Declaring checked exceptions on internal helper methods unnecessarily, creating boilerplate."
            ],
            [
                ("Why did modern Java frameworks (e.g. Spring) migrate to unchecked exceptions?", "Discuss boilerplate reduction and cleaner decoupled architectures."),
                ("How do you convert a checked exception into an unchecked exception?", "Wrap it inside `new RuntimeException(checkedException)` (exception chaining)."),
                ("Is ClassNotFoundException checked or unchecked?", "Identify checked.")
            ]
        ),
        format_lesson(
            "java",
            "Custom exceptions", 25,
            [
                "Create domain-specific custom exception classes",
                "Extend RuntimeException or Exception with descriptive constructors",
                "Preserve root-cause stack traces using exception chaining"
            ],
            "In enterprise applications, standard Java exceptions (like `IllegalArgumentException`) are often too generic to represent specific business domain errors. Creating **Custom Exceptions** provides clarity:\n- Extend `RuntimeException` for business rule violations (e.g. `CourseNotFoundException`, `EnrollmentLimitExceededException`).\n- Provide constructors accepting a message string and a `Throwable cause` for exception chaining, preserving the original root cause.",
            "public class CourseNotFoundException extends RuntimeException {\n    public CourseNotFoundException(String message) { super(message); }\n    public CourseNotFoundException(String message, Throwable cause) { super(message, cause); }\n}",
            "public class CustomExceptionsDemo {\n    static class DuplicateEnrollmentException extends RuntimeException {\n        private final Long studentId;\n        private final Long courseId;\n        \n        public DuplicateEnrollmentException(Long studentId, Long courseId) {\n            super(\"Student \" + studentId + \" is already actively enrolled in course \" + courseId);\n            this.studentId = studentId;\n            this.courseId = courseId;\n        }\n    }\n    \n    public static void enroll(Long studentId, Long courseId, boolean isEnrolled) {\n        if (isEnrolled) {\n            throw new DuplicateEnrollmentException(studentId, courseId);\n        }\n        System.out.println(\"Enrollment created for student \" + studentId);\n    }\n    \n    public static void main(String[] args) {\n        try {\n            enroll(101L, 202L, true);\n        } catch (DuplicateEnrollmentException e) {\n            System.out.println(\"Domain Error Caught: \" + e.getMessage());\n        }\n    }\n}",
            "Domain Error Caught: Student 101 is already actively enrolled in course 202",
            [
                "DuplicateEnrollmentException encapsulates specific business error context.",
                "Custom fields studentId and courseId facilitate programmatic handling and auditing."
            ],
            [
                "Extending `Throwable` or `Error` instead of `Exception` or `RuntimeException`.",
                "Forgetting to call `super(message, cause)`, losing root-cause exception chaining."
            ],
            [
                ("When should a custom exception extend RuntimeException vs Exception?", "Use RuntimeException for unrecoverable business errors and Exception for recoverable situations."),
                ("What is Exception Chaining in Java?", "Passing the original cause to super(cause) to maintain the full stack trace."),
                ("Why are custom exceptions valuable in REST APIs?", "They map cleanly to HTTP status codes (e.g. 404 Not Found, 409 Conflict).")
            ]
        ),
        format_lesson(
            "java",
            "Collections Framework", 25,
            [
                "Navigate the Java Collections Framework interface hierarchy",
                "Differentiate List, Set, Queue, and Map contracts",
                "Select optimal collection implementations based on access patterns and Big-O complexity"
            ],
            "The **Java Collections Framework (JCF)** provides standardized interfaces and high-performance data structure implementations:\n- `Iterable` -> `Collection`\n  - `List`: Ordered, index-accessible, permits duplicates (`ArrayList`, `LinkedList`).\n  - `Set`: Unordered collection of unique elements; no duplicates allowed (`HashSet`, `TreeSet`).\n  - `Queue`: First-In-First-Out (FIFO) processing order (`ArrayDeque`, `PriorityQueue`).\n- `Map` (separate hierarchy): Key-value pair associations with unique keys (`HashMap`, `TreeMap`).",
            "// Choosing data structures:\n// Need ordered sequence with fast random lookup? -> ArrayList\n// Need uniqueness and O(1) membership check? -> HashSet\n// Need key-value mapping? -> HashMap\n// Need FIFO processing? -> ArrayDeque",
            "import java.util.*;\n\npublic class CollectionsFrameworkDemo {\n    public static void main(String[] args) {\n        List<String> list = new ArrayList<>(List.of(\"Java\", \"Python\", \"Java\"));\n        Set<String> set = new HashSet<>(list); // Eliminates duplicates\n        Map<String, Integer> map = new HashMap<>();\n        map.put(\"Java\", 98);\n        map.put(\"Python\", 79);\n        \n        System.out.println(\"List (permits duplicates): \" + list);\n        System.out.println(\"Set (enforces uniqueness): \" + set);\n        System.out.println(\"Map (key-value counts): \" + map);\n    }\n}",
            "List (permits duplicates): [Java, Python, Java]\nSet (enforces uniqueness): [Java, Python]\nMap (key-value counts): {Java=98, Python=79}",
            [
                "List preserves insertion order and allows 'Java' twice.",
                "Set automatically filters duplicate entries.",
                "Map associates courses with their respective lesson counts."
            ],
            [
                "Using raw types without generics (e.g. `List list = new ArrayList()`), causing loss of type safety.",
                "Choosing LinkedList over ArrayList for general lookups; ArrayList is almost always faster due to CPU cache locality."
            ],
            [
                ("Why does Map not inherit from the Collection interface?", "Because Map operates on key-value pairs rather than individual elements."),
                ("What is the time complexity of HashSet.contains(element)?", "O(1) average time."),
                ("What is the difference between fail-fast and fail-safe iterators?", "Fail-fast throws ConcurrentModificationException if modified during iteration.")
            ]
        ),
        format_lesson(
            "java",
            "List", 25,
            [
                "Implement ordered sequences using ArrayList and LinkedList",
                "Perform element additions, positional retrieval, removals, and replacements",
                "Analyze memory footprint and algorithmic complexity (O(1) vs O(n))"
            ],
            "A `List` is an ordered collection (sequence). Key implementations:\n1. `ArrayList`: Backed by a dynamically resizing array. Fast random access $O(1)$ by index. Appending at end is amortized $O(1)$. Inserting/removing in the middle requires shifting elements ($O(n)$).\n2. `LinkedList`: Backed by a doubly-linked list. Fast insertions/deletions at both ends ($O(1)$), but index lookup requires traversal ($O(n)$) and incurs significant pointer memory overhead.",
            "List<String> courses = new ArrayList<>();\ncourses.add(\"Java Masterclass\");\nString first = courses.get(0);\ncourses.remove(\"Java Masterclass\");",
            "import java.util.ArrayList;\nimport java.util.List;\n\npublic class ListDemo {\n    public static void main(String[] args) {\n        List<String> modules = new ArrayList<>();\n        modules.add(\"M1: Fundamentals\");\n        modules.add(\"M2: Control Flow\");\n        modules.add(\"M3: Methods & Arrays\");\n        \n        // Positional operations\n        modules.add(1, \"M1.5: Tooling Setup\"); // Insert at index 1\n        \n        System.out.println(\"Module Count: \" + modules.size());\n        System.out.println(\"Module at Index 2: \" + modules.get(2));\n        \n        modules.remove(\"M1.5: Tooling Setup\");\n        System.out.println(\"Final Module Sequence: \" + modules);\n    }\n}",
            "Module Count: 4\nModule at Index 2: M2: Control Flow\nFinal Module Sequence: [M1: Fundamentals, M2: Control Flow, M3: Methods & Arrays]",
            [
                "modules.add(1, ...) inserts at index 1 and shifts subsequent elements right.",
                "modules.get(2) retrieves M2: Control Flow in O(1) time.",
                "modules.remove() removes by value and shifts remaining elements left."
            ],
            [
                "Calling `list.remove(1)` when meaning to remove the integer value 1; with `List<Integer>`, it removes at index 1 instead of value 1.",
                "Using LinkedList assuming it is faster for general use cases; modern CPUs favor contiguous ArrayList memory layout."
            ],
            [
                ("How does an ArrayList resize when its capacity is exceeded?", "It allocates a new array typically 1.5x larger and copies elements over."),
                ("How do you convert a List to an array in Java?", "Use `list.toArray(new String[0])`."),
                ("What does `List.of(...)` return in Java 9+?", "An unmodifiable (immutable) list.")
            ]
        ),
        format_lesson(
            "java",
            "Set", 25,
            [
                "Enforce mathematical uniqueness using HashSet, LinkedHashSet, and TreeSet",
                "Understand hash bucket distribution and O(1) average lookup",
                "Implement the equals() and hashCode() contract for custom set elements"
            ],
            "A `Set` is a collection that cannot contain duplicate elements:\n- `HashSet`: Elements stored in an internal hash table. Offers $O(1)$ constant-time add, remove, and contains operations. Makes NO ordering guarantees.\n- `LinkedHashSet`: Maintains a doubly-linked list running through its hash table; preserves insertion order.\n- `TreeSet`: Backed by a Red-Black tree; sorts elements in natural ascending order or custom comparator ($O(\\log n)$ operations).\nCrucial: Custom objects stored in a HashSet **MUST override both equals() and hashCode()** consistently.",
            "Set<String> uniqueTags = new HashSet<>();\nuniqueTags.add(\"Java\");\nuniqueTags.add(\"Java\"); // Ignored, returns false",
            "import java.util.*;\n\npublic class SetDemo {\n    public static void main(String[] args) {\n        Set<String> enrolledStudents = new HashSet<>();\n        enrolledStudents.add(\"Alex\");\n        enrolledStudents.add(\"Sarah\");\n        enrolledStudents.add(\"Alex\"); // Duplicate attempt\n        \n        System.out.println(\"HashSet (unique): \" + enrolledStudents);\n        System.out.println(\"Contains 'Sarah'? \" + enrolledStudents.contains(\"Sarah\"));\n        \n        Set<Integer> sortedScores = new TreeSet<>(List.of(88, 45, 92, 73, 92));\n        System.out.println(\"TreeSet (unique and sorted): \" + sortedScores);\n    }\n}",
            "HashSet (unique): [Alex, Sarah]\nContains 'Sarah'? true\nTreeSet (unique and sorted): [45, 73, 88, 92]",
            [
                "The duplicate 'Alex' is rejected automatically by HashSet.",
                "TreeSet deduplicates and sorts the integer scores in ascending order."
            ],
            [
                "Failing to override `hashCode()` when overriding `equals()`, causing distinct hash buckets for logically equal objects.",
                "Mutating an object's fields after placing it in a HashSet, which corrupts its hash code and makes it unfindable."
            ],
            [
                ("What is the equals() and hashCode() contract in Java?", "If `a.equals(b)` is true, then `a.hashCode() == b.hashCode()` MUST be true."),
                ("Why should fields used in hashCode() be immutable?", "To prevent hash bucket misalignment after insertion."),
                ("How does TreeSet determine element ordering?", "Via Comparable.compareTo() or a custom Comparator.")
            ]
        ),
        format_lesson(
            "java",
            "Map", 25,
            [
                "Associate unique keys with values using HashMap and TreeMap",
                "Execute key lookups, updates, removals, and containsKey checks",
                "Iterate through Map entries using entrySet(), keySet(), and values()"
            ],
            "A `Map` maps unique keys to values. A Map cannot contain duplicate keys; each key maps to at most one value.\n- `HashMap`: Implemented using a hash table. Provides average $O(1)$ operations for `put()`, `get()`, and `containsKey()`. Allows one `null` key.\n- `TreeMap`: Red-Black tree implementation with keys sorted in ascending order ($O(\\log n)$).\n- Modern methods: `getOrDefault(key, defaultVal)`, `putIfAbsent(key, val)`, `computeIfAbsent(key, mappingFunc)`.",
            "Map<String, Integer> map = new HashMap<>();\nmap.put(\"Java\", 98);\nint count = map.getOrDefault(\"Python\", 0);",
            "import java.util.HashMap;\nimport java.util.Map;\n\npublic class MapDemo {\n    public static void main(String[] args) {\n        Map<String, String> instructorCourses = new HashMap<>();\n        instructorCourses.put(\"sarah@learnhub.com\", \"Java Masterclass\");\n        instructorCourses.put(\"david@learnhub.com\", \"Python Masterclass\");\n        \n        // Safe lookup\n        String course = instructorCourses.getOrDefault(\"alex@learnhub.com\", \"Unassigned\");\n        System.out.println(\"Alex's Course: \" + course);\n        \n        System.out.println(\"\\nAll Course Assignments:\");\n        for (Map.Entry<String, String> entry : instructorCourses.entrySet()) {\n            System.out.println(\"Instructor: \" + entry.getKey() + \" -> \" + entry.getValue());\n        }\n    }\n}",
            "Alex's Course: Unassigned\n\nAll Course Assignments:\nInstructor: sarah@learnhub.com -> Java Masterclass\nInstructor: david@learnhub.com -> Python Masterclass",
            [
                "getOrDefault returns fallback 'Unassigned' when key is absent without throwing exception.",
                "entrySet() provides key-value pair iteration in O(n) time."
            ],
            [
                "Iterating through keySet() and calling `map.get(key)` inside the loop (inefficient double-lookup; use entrySet instead).",
                "Assuming HashMap preserves insertion order (use LinkedHashMap if insertion order is needed)."
            ],
            [
                ("What happens when put(key, newValue) is called with a key that already exists?", "The old value is overwritten and returned."),
                ("How does Java 8 handle hash collisions inside HashMap buckets?", "Buckets exceeding 8 elements transform from linked lists into balanced red-black trees ($O(\\log n)$)."),
                ("Can a HashMap hold null keys or null values?", "Yes, HashMap permits one null key and multiple null values.")
            ]
        ),
        format_lesson(
            "java",
            "Queue and Deque", 20,
            [
                "Implement FIFO queues and double-ended queues using ArrayDeque",
                "Apply offer, poll, and peek operations safely without throwing exceptions",
                "Select appropriate queue structures for task scheduling and breadth-first search"
            ],
            "A `Queue` models a First-In-First-Out (FIFO) waiting line where elements are added at the tail and removed from the head.\nA `Deque` (Double-Ended Queue) allows insertions and deletions at BOTH ends, serving as both a Queue and a Stack (LIFO).\nBest practice: Use `ArrayDeque` instead of the legacy `Stack` class or `LinkedList`; `ArrayDeque` has zero node allocation overhead and faster cache locality.",
            "Deque<String> queue = new ArrayDeque<>();\nqueue.offer(\"First\"); // Enqueue\nString item = queue.poll(); // Dequeue (returns null if empty)\nString head = queue.peek(); // Inspect head",
            "import java.util.ArrayDeque;\nimport java.util.Deque;\n\npublic class QueueDequeDemo {\n    public static void main(String[] args) {\n        Deque<String> supportTickets = new ArrayDeque<>();\n        \n        // Enqueue tasks\n        supportTickets.offer(\"Ticket #1: Password Reset\");\n        supportTickets.offer(\"Ticket #2: Course Enrollment Error\");\n        supportTickets.offer(\"Ticket #3: Certificate Verification\");\n        \n        System.out.println(\"Next in line: \" + supportTickets.peek());\n        \n        // Process queue FIFO\n        while (!supportTickets.isEmpty()) {\n            System.out.println(\"Processing: \" + supportTickets.poll());\n        }\n    }\n}",
            "Next in line: Ticket #1: Password Reset\nProcessing: Ticket #1: Password Reset\nProcessing: Ticket #2: Course Enrollment Error\nProcessing: Ticket #3: Certificate Verification",
            [
                "offer() enqueues tickets at the tail.",
                "peek() inspects the front ticket without removing it.",
                "poll() retrieves and removes each ticket in original arrival order."
            ],
            [
                "Using `remove()` or `element()` on an empty queue, which throws `NoSuchElementException` (use `poll()` and `peek()` which return null).",
                "Using the legacy `java.util.Stack` class, which extends Vector and has synchronized performance overhead."
            ],
            [
                ("Why is ArrayDeque preferred over LinkedList for standard Queue/Stack operations?", "ArrayDeque does not allocate node objects and has better cache locality."),
                ("What does PriorityQueue do?", "Orders elements according to priority using a binary heap rather than FIFO."),
                ("How do you use ArrayDeque as a LIFO stack?", "Use `push()`, `pop()`, and `peek()`.")
            ]
        ),
        format_lesson(
            "java",
            "Iterators", 20,
            [
                "Traverse collections using java.util.Iterator",
                "Safely remove elements during iteration using iterator.remove()",
                "Diagnose and eliminate ConcurrentModificationException"
            ],
            "An `Iterator` is an object that enables traversing through a collection regardless of its underlying data structure. Core methods:\n- `hasNext()`: Returns true if more elements remain.\n- `next()`: Returns the next element.\n- `remove()`: Removes the last element returned by `next()` from the underlying collection.\nCrucial rule: If you modify a collection (add/remove) directly while iterating over it with an enhanced for-loop, Java throws `ConcurrentModificationException`. To safely remove elements during iteration, use `iterator.remove()` or `collection.removeIf()`.",
            "Iterator<String> it = list.iterator();\nwhile (it.hasNext()) {\n    if (it.next().equals(\"Drop\")) it.remove(); // Safe removal\n}",
            "import java.util.ArrayList;\nimport java.util.Iterator;\nimport java.util.List;\n\npublic class IteratorDemo {\n    public static void main(String[] args) {\n        List<Integer> scores = new ArrayList<>(List.of(85, 42, 90, 58, 77));\n        \n        System.out.println(\"Initial scores: \" + scores);\n        \n        // Safely remove failing scores (< 60) via Iterator\n        Iterator<Integer> it = scores.iterator();\n        while (it.hasNext()) {\n            int score = it.next();\n            if (score < 60) {\n                it.remove(); // Safe removal\n            }\n        }\n        \n        System.out.println(\"Passing scores after filter: \" + scores);\n    }\n}",
            "Initial scores: [85, 42, 90, 58, 77]\nPassing scores after filter: [85, 90, 77]",
            [
                "Iterator traverses scores safely.",
                "it.remove() deletes 42 and 58 without throwing ConcurrentModificationException.",
                "Passing scores remain intact."
            ],
            [
                "Calling `list.remove(item)` inside an enhanced `for (Item i : list)` loop, triggering `ConcurrentModificationException`.",
                "Calling `it.remove()` without a preceding call to `it.next()`, throwing `IllegalStateException`."
            ],
            [
                ("What modern Collection method replaces the iterator while-loop for removals?", "Explain `collection.removeIf(predicate)`."),
                ("What causes ConcurrentModificationException?", "Mismatch between modCount and expectedModCount in collection iterators."),
                ("How does ListIterator differ from standard Iterator?", "Supports bidirectional traversal (`hasPrevious()`, `previous()`) and element addition/replacement.")
            ]
        ),
        format_lesson(
            "java",
            "Generics", 25,
            [
                "Write type-safe generic classes and parameterized methods",
                "Apply bounded type parameters (<T extends Comparable<T>>)",
                "Understand compile-time type safety and type erasure"
            ],
            "Generics enable types (classes and interfaces) to be parameters when defining classes, interfaces, and methods. Generics provide:\n1. Compile-Time Type Safety: Catches type mismatches at compilation rather than crashing with `ClassCastException` at runtime.\n2. Elimination of Casts: No explicit casting is needed when retrieving elements.\n3. Type Erasure: Java implements generics using type erasure: compiler verifies types and inserts casts, then erases type parameters to bytecode (`Object` or bound).",
            "public class Box<T> {\n    private T item;\n    public void set(T item) { this.item = item; }\n    public T get() { return item; }\n}",
            "public class GenericsDemo {\n    // Generic method\n    public static <T> void printSummary(String label, T value) {\n        System.out.println(\"[\" + label + \"] Value: \" + value + \" (Type: \" + value.getClass().getSimpleName() + \")\");\n    }\n    \n    // Bounded generic method\n    public static <T extends Comparable<T>> T findMax(T a, T b) {\n        return a.compareTo(b) >= 0 ? a : b;\n    }\n    \n    public static void main(String[] args) {\n        printSummary(\"Course ID\", 1045);\n        printSummary(\"Course Title\", \"Java Masterclass\");\n        \n        System.out.println(\"Max of 45 and 89: \" + findMax(45, 89));\n        System.out.println(\"Max of 'Apple' and 'Zebra': \" + findMax(\"Apple\", \"Zebra\"));\n    }\n}",
            "[Course ID] Value: 1045 (Type: Integer)\n[Course Title] Value: Java Masterclass (Type: String)\nMax of 45 and 89: 89\nMax of 'Apple' and 'Zebra': Zebra",
            [
                "printSummary is a generic method handling both Integer and String inputs safely.",
                "findMax is bounded by Comparable, guaranteeing that compareTo is available."
            ],
            [
                "Attempting to instantiate a generic type directly (`new T()`), which fails due to type erasure.",
                "Using primitive types as generic type arguments (`List<int>`); must use wrapper types (`List<Integer>`)."
            ],
            [
                ("What is Type Erasure in Java?", "Process where the compiler removes generic type parameters after verification to ensure backwards compatibility with older JVMs."),
                ("What does the wildcard `<? extends Number>` mean?", "Upper-bounded wildcard accepting Number or any subclass of Number (read-only safe)."),
                ("What is the PECS mnemonic in Java generics?", "Producer Extends, Consumer Super.")
            ]
        ),
        format_lesson(
            "java",
            "Wrapper classes", 20,
            [
                "Map primitive data types to their corresponding object wrapper classes",
                "Understand Autoboxing and Unboxing mechanics",
                "Prevent NullPointerException during unboxing of null wrapper references"
            ],
            "Java provides Wrapper classes in `java.lang` to wrap primitive data types in objects:\n- `byte` -> `Byte`, `int` -> `Integer`, `long` -> `Long`, `double` -> `Double`, `boolean` -> `Boolean`, `char` -> `Character`.\nMechanics:\n- **Autoboxing**: Automatic conversion of a primitive to its corresponding wrapper object (`Integer obj = 10;`).\n- **Unboxing**: Automatic conversion of a wrapper object to its corresponding primitive (`int x = obj;`).\nDanger: Unboxing an `Integer` reference that is `null` throws a `NullPointerException`.",
            "Integer boxed = 42; // Autoboxing\nint unboxed = boxed; // Unboxing\n// If boxed is null -> NullPointerException during unboxing!",
            "public class WrapperClassesDemo {\n    public static void main(String[] args) {\n        Integer a = 127;\n        Integer b = 127;\n        System.out.println(\"127 cached equality (a == b): \" + (a == b)); // true (Integer Cache -128 to 127)\n        \n        Integer c = 128;\n        Integer d = 128;\n        System.out.println(\"128 cached equality (c == d): \" + (c == d)); // false (different heap instances!)\n        System.out.println(\"128 content equality (.equals): \" + c.equals(d)); // true\n        \n        // Parsing helpers\n        int parsed = Integer.parseInt(\"2048\");\n        System.out.println(\"Parsed string: \" + parsed);\n    }\n}",
            "127 cached equality (a == b): true\n128 cached equality (c == d): false\n128 content equality (.equals): true\nParsed string: 2048",
            [
                "Integer caches instances between -128 and 127; values beyond that create new heap objects, making == return false.",
                ".equals() correctly verifies value equality across all ranges.",
                "Integer.parseInt converts string input to primitive int."
            ],
            [
                "Using `==` to compare wrapper objects; always use `.equals()` to avoid integer cache trap bugs.",
                "Allowing null wrapper references in arithmetic expressions, causing silent unboxing NullPointerExceptions."
            ],
            [
                ("What range of values does the Java Integer Cache support by default?", "Identify -128 to 127."),
                ("What happens when unboxing an Integer variable that holds null?", "Throws NullPointerException."),
                ("How does Integer.valueOf() differ from Integer.parseInt()?", "valueOf returns an Integer wrapper object; parseInt returns a primitive int.")
            ]
        ),
        format_lesson(
            "java",
            "Comparable and Comparator", 25,
            [
                "Implement natural sorting using java.lang.Comparable",
                "Define custom, decoupled sorting strategies using java.util.Comparator",
                "Leverage modern Comparator factory methods (comparing, thenComparing)"
            ],
            "Java provides two interfaces for ordering objects:\n1. `Comparable<T>`: Defines natural ordering inside the class itself via `compareTo(T other)`. A class can only have ONE natural ordering.\n2. `Comparator<T>`: Defines external, alternative sorting logic decoupled from the class via `compare(T o1, T o2)`. You can define multiple Comparators (by name, by score, descending).\nModern Java 8 provides fluent factories: `Comparator.comparing(Student::getName).thenComparing(Student::getScore)`.",
            "// Comparable:\npublic int compareTo(Student o) { return Integer.compare(this.id, o.id); }\n\n// Comparator:\nComparator<Student> byScore = (s1, s2) -> Double.compare(s2.getScore(), s1.getScore());",
            "import java.util.*;\n\npublic class ComparableComparatorDemo {\n    static class Student implements Comparable<Student> {\n        private String name;\n        private int score;\n        \n        Student(String name, int score) { this.name = name; this.score = score; }\n        public String getName() { return name; }\n        public int getScore() { return score; }\n        \n        @Override\n        public int compareTo(Student other) {\n            return this.name.compareTo(other.name); // Natural order: Alphabetical\n        }\n        \n        @Override\n        public String toString() { return name + \" (\" + score + \")\"; }\n    }\n    \n    public static void main(String[] args) {\n        List<Student> roster = new ArrayList<>(List.of(\n            new Student(\"Sarah\", 92),\n            new Student(\"Alex\", 85),\n            new Student(\"David\", 95)\n        ));\n        \n        Collections.sort(roster); // Natural order (name)\n        System.out.println(\"Sorted by Name (Comparable): \" + roster);\n        \n        // Custom order: descending score\n        roster.sort(Comparator.comparingInt(Student::getScore).reversed());\n        System.out.println(\"Sorted by Score Descending (Comparator): \" + roster);\n    }\n}",
            "Sorted by Name (Comparable): [Alex (85), David (95), Sarah (92)]\nSorted by Score Descending (Comparator): [David (95), Sarah (92), Alex (85)]",
            [
                "Collections.sort(roster) uses Student.compareTo() to sort alphabetically.",
                "Comparator.comparingInt(Student::getScore).reversed() sorts students by highest score first."
            ],
            [
                "Using integer subtraction `(o1.score - o2.score)` in compareTo, which can cause integer overflow errors (use `Integer.compare` instead).",
                "Inconsistent compareTo and equals: if `compareTo` returns 0, `equals` should return true."
            ],
            [
                ("Why is `Integer.compare(a, b)` safer than `a - b` in a Comparator?", "Avoids numeric overflow wrapping around to opposite sign."),
                ("Can a class implement both Comparable and have multiple external Comparators?", "Yes, Comparable defines default ordering while Comparators provide alternatives."),
                ("How do you sort a list of strings by length descending?", "Use `list.sort(Comparator.comparingInt(String::length).reversed())`.")
            ]
        ),
        format_lesson(
            "java",
            "Collection practice", 30,
            [
                "Build practical data aggregation pipelines using Collections",
                "Deduplicate records, count frequencies, and sort multidimensional data",
                "Group and partition student course records"
            ],
            "This capstone lesson consolidates Module 5 concepts into realistic data processing tasks:\n1. Frequency Counting: Counting occurrences of tokens using `HashMap` and `getOrDefault()`.\n2. Deduplication: Converting lists to `LinkedHashSet` to preserve original order while removing duplicates.\n3. Grouping: Grouping records by department or status using a `Map<Category, List<Item>>`.",
            "Map<String, Integer> freq = new HashMap<>();\nfor (String word : words) {\n    freq.put(word, freq.getOrDefault(word, 0) + 1);\n}",
            "import java.util.*;\n\npublic class CollectionPracticeDemo {\n    public static void main(String[] args) {\n        List<String> rawCourseFeed = List.of(\"Java\", \"Python\", \"Java\", \"React\", \"Python\", \"Java\", \"Spring\");\n        \n        // 1. Frequency counting\n        Map<String, Integer> counts = new HashMap<>();\n        for (String c : rawCourseFeed) {\n            counts.put(c, counts.getOrDefault(c, 0) + 1);\n        }\n        System.out.println(\"Course Enrollments Count: \" + counts);\n        \n        // 2. Order-preserving deduplication\n        Set<String> uniqueOrdered = new LinkedHashSet<>(rawCourseFeed);\n        System.out.println(\"Unique Courses (Preserved Order): \" + uniqueOrdered);\n        \n        // 3. Find top course\n        String topCourse = Collections.max(counts.entrySet(), Map.Entry.comparingByValue()).getKey();\n        System.out.println(\"Most Popular Track: \" + topCourse + \" (\" + counts.get(topCourse) + \" enrollments)\");\n    }\n}",
            "Course Enrollments Count: {Java=3, Spring=1, React=1, Python=2}\nUnique Courses (Preserved Order): [Java, Python, React, Spring]\nMost Popular Track: Java (3 enrollments)",
            [
                "getOrDefault aggregates counts in a single pass.",
                "LinkedHashSet removes duplicates while maintaining discovery order.",
                "Collections.max with Map.Entry.comparingByValue finds the highest enrollment track."
            ],
            [
                "Manually checking containsKey and then doing get and put, requiring 2-3 lookups instead of using getOrDefault or merge.",
                "Using standard HashSet when order preservation is required by the product specifications."
            ],
            [
                ("How does Map.merge() simplify frequency counting in Java 8+?", "Explain `map.merge(key, 1, Integer::sum)`."),
                ("How do you invert a Map<K, V> into a Map<V, List<K>>?", "Iterate entries and group keys by their value."),
                ("What is the time complexity of building a frequency map of N tokens?", "O(N) linear time.")
            ]
        )
    ]
    return {
        "title": "Module 5 — Exceptions, Collections, and Generics",
        "description": "Handle errors and choose appropriate data structures.",
        "sequenceOrder": 5,
        "lessons": lessons
    }

def get_java_module_6():
    lessons = [
        format_lesson(
            "java",
            "File handling with Path and Files", 25,
            [
                "Work with the modern java.nio.file API (Path and Files)",
                "Read, write, and append text files with UTF-8 encoding",
                "Verify file existence and inspect directory attributes safely"
            ],
            "Modern Java file I/O is built around `java.nio.file` (NIO.2 introduced in Java 7):\n- `Path`: Represents a file or directory path in a platform-independent manner (`Path.of(\"dir\", \"file.txt\")`).\n- `Files`: Utility class providing static methods to read, write, copy, move, and query files.\n- High-convenience methods: `Files.readString(path)`, `Files.writeString(path, content)`, `Files.lines(path)`, and `Files.exists(path)`.",
            "Path path = Path.of(\"logs\", \"app.log\");\nFiles.writeString(path, \"Audit log entry\\n\", StandardOpenOption.CREATE, StandardOpenOption.APPEND);\nString content = Files.readString(path);",
            "import java.nio.file.Files;\nimport java.nio.file.Path;\nimport java.io.IOException;\n\npublic class NIOFilesDemo {\n    public static void main(String[] args) {\n        Path tempFile = Path.of(\"learnhub_demo.tmp\");\n        try {\n            Files.writeString(tempFile, \"LearnHub Platform: Java Module 6\\nStatus: Operational\");\n            System.out.println(\"File created: \" + tempFile.toAbsolutePath());\n            System.out.println(\"File exists: \" + Files.exists(tempFile));\n            System.out.println(\"File size: \" + Files.size(tempFile) + \" bytes\");\n            \n            String content = Files.readString(tempFile);\n            System.out.println(\"Read content:\\n\" + content);\n            \n            Files.deleteIfExists(tempFile); // Cleanup\n            System.out.println(\"Temporary file cleaned up.\");\n        } catch (IOException e) {\n            System.out.println(\"I/O Error: \" + e.getMessage());\n        }\n    }\n}",
            "File created: c:\\Users\\Admin\\OneDrive\\Desktop\\LearnHub\\learnhub_demo.tmp\nFile exists: true\nFile size: 55 bytes\nRead content:\nLearnHub Platform: Java Module 6\nStatus: Operational\nTemporary file cleaned up.",
            [
                "Path.of creates a platform-independent file path reference.",
                "Files.writeString writes textual UTF-8 content to disk.",
                "Files.deleteIfExists ensures clean temporary file cleanup."
            ],
            [
                "Using legacy `java.io.File` which lacks modern exception reporting and atomic operations.",
                "Reading giant files (gigabytes) into memory at once using `readString()` instead of streaming via `Files.lines()`."
            ],
            [
                ("Why is `java.nio.file.Path` preferred over `java.io.File`?", "NIO.2 provides better exception handling, symbolic link support, and atomic operations."),
                ("What charset does `Files.readString(Path)` use by default?", "StandardCharsets.UTF_8."),
                ("How does `Files.lines(Path)` handle large files efficiently?", "Lazily streams lines on-demand using Stream<String> without buffering entire file in RAM.")
            ]
        ),
        format_lesson(
            "java",
            "Byte and character streams", 25,
            [
                "Distinguish byte streams (InputStream/OutputStream) from character streams (Reader/Writer)",
                "Apply buffering (BufferedReader/BufferedWriter) for efficient high-volume I/O",
                "Select proper streams based on data payload (binary vs Unicode text)"
            ],
            "Java I/O streams are categorized by data format:\n1. Byte Streams (`InputStream` / `OutputStream`): Process raw 8-bit bytes (images, compiled classes, audio, network packets). Examples: `FileInputStream`, `FileOutputStream`.\n2. Character Streams (`Reader` / `Writer`): Process 16-bit Unicode characters with automatic encoding translation. Examples: `FileReader`, `FileWriter`.\n3. Buffered Streams: Wrap underlying streams with an internal memory buffer (`BufferedReader`, `BufferedWriter`) to drastically reduce costly disk/network round-trips.",
            "// BufferedReader pattern\ntry (BufferedReader reader = new BufferedReader(new FileReader(\"data.txt\"))) {\n    String line;\n    while ((line = reader.readLine()) != null) { ... }\n}",
            "import java.io.BufferedReader;\nimport java.io.StringReader;\nimport java.io.IOException;\n\npublic class StreamsDemo {\n    public static void main(String[] args) {\n        String sampleData = \"Lesson 1: Java Streams\\nLesson 2: Try-With-Resources\\nLesson 3: Concurrency\";\n        \n        try (BufferedReader reader = new BufferedReader(new StringReader(sampleData))) {\n            String line;\n            int lineNumber = 1;\n            while ((line = reader.readLine()) != null) {\n                System.out.println(\"Line \" + lineNumber++ + \": \" + line);\n            }\n        } catch (IOException e) {\n            System.out.println(\"Stream error: \" + e.getMessage());\n        }\n    }\n}",
            "Line 1: Lesson 1: Java Streams\nLine 2: Lesson 2: Try-With-Resources\nLine 3: Lesson 3: Concurrency",
            [
                "BufferedReader wraps character source, buffering reads into memory.",
                "readLine() extracts entire lines cleanly until null indicates end of stream."
            ],
            [
                "Reading character text using raw InputStream, causing multi-byte Unicode characters to corrupt.",
                "Failing to flush buffered writers before closing, leading to truncated files."
            ],
            [
                ("What is the default buffer size of a BufferedReader in Java?", "8192 characters (8 KB)."),
                ("Why do character streams require an explicit Charset?", "To translate between raw disk bytes and Unicode chars."),
                ("What does flush() do on an OutputStream or Writer?", "Forces all buffered bytes/chars out to the destination disk or socket immediately.")
            ]
        ),
        format_lesson(
            "java",
            "Try-with-resources", 20,
            [
                "Manage system resources automatically using try-with-resources",
                "Implement the java.lang.AutoCloseable interface",
                "Prevent resource leaks in file handles, database connections, and network sockets"
            ],
            "Before Java 7, closing resources (files, database connections) required messy nested try-catch-finally blocks. Java 7 introduced **try-with-resources**: any resource that implements `java.lang.AutoCloseable` can be declared in parentheses after `try (...)`. The JVM automatically invokes `close()` on all declared resources when leaving the try block, even if an exception occurs.",
            "try (FileReader fr = new FileReader(\"file.txt\");\n     BufferedReader br = new BufferedReader(fr)) {\n    // br and fr are closed automatically in reverse order of creation\n}",
            "public class TryWithResourcesDemo {\n    static class DatabaseConnection implements AutoCloseable {\n        public void query(String sql) {\n            System.out.println(\"Executing query: \" + sql);\n        }\n        \n        @Override\n        public void close() {\n            System.out.println(\"DatabaseConnection closed automatically and cleanly.\");\n        }\n    }\n    \n    public static void main(String[] args) {\n        try (DatabaseConnection conn = new DatabaseConnection()) {\n            conn.query(\"SELECT * FROM courses\");\n        }\n        System.out.println(\"Scope exited successfully.\");\n    }\n}",
            "Executing query: SELECT * FROM courses\nDatabaseConnection closed automatically and cleanly.\nScope exited successfully.",
            [
                "DatabaseConnection implements AutoCloseable.",
                "conn is automatically closed upon leaving the try scope, preventing socket leaks."
            ],
            [
                "Declaring resources outside the try-with-resources header, forfeiting automatic management.",
                "Confusing suppressed exceptions: try-with-resources attaches secondary exceptions to the primary exception using `addSuppressed()`."
            ],
            [
                ("What interface must a class implement to participate in try-with-resources?", "java.lang.AutoCloseable."),
                ("In what order are multiple resources closed in a try-with-resources block?", "In reverse order of their declaration."),
                ("What happens if both the try block and close() throw an exception?", "The close() exception is suppressed and attached to the main exception.")
            ]
        ),
        format_lesson(
            "java",
            "Serialization concepts", 20,
            [
                "Understand object serialization and deserialization concepts",
                "Evaluate security vulnerabilities and deprecation of native Java serialization",
                "Adopt modern JSON/XML serialization alternatives (Jackson, Gson)"
            ],
            "**Serialization** is the process of converting an in-memory object graph into a persistent stream of bytes. **Deserialization** reconstructs the object from the byte stream.\n- Native Java Serialization: Requires implementing `Serializable` and defining `serialVersionUID`. However, native Java serialization has severe security risks (arbitrary code execution vulnerabilities).\n- Industry Best Practice: Modern applications avoid native serialization and use **JSON** (via Jackson or Gson) for persistence and cross-platform network exchange.",
            "// Native (discouraged in modern systems): implements Serializable\n// Modern alternative: ObjectMapper.writeValueAsString(object) -> JSON",
            "public class SerializationConceptsDemo {\n    public static void main(String[] args) {\n        System.out.println(\"LearnHub Architecture Note:\");\n        System.out.println(\"- Native Java Serialization is prone to gadget-chain security vulnerabilities.\");\n        System.out.println(\"- Industry standard: Structured JSON / Protocol Buffers.\");\n        System.out.println(\"- Using Jackson ObjectMapper for REST and cache persistence.\");\n    }\n}",
            "LearnHub Architecture Note:\n- Native Java Serialization is prone to gadget-chain security vulnerabilities.\n- Industry standard: Structured JSON / Protocol Buffers.\n- Using Jackson ObjectMapper for REST and cache persistence.",
            [
                "Discusses trade-offs between legacy binary serialization and modern structured JSON.",
                "Emphasizes secure enterprise design patterns."
            ],
            [
                "Deserializing untrusted binary streams, which can allow attackers to execute arbitrary code via gadget chains.",
                "Forgetting to declare `serialVersionUID`, causing deserialization failure when class fields evolve."
            ],
            [
                ("What does the transient keyword do on a class field in Java?", "Prevents that field from being included in serialization."),
                ("Why is JSON preferred over native Java serialization?", "Language-neutral, human-readable, and free from remote execution deserialization exploits."),
                ("What is the purpose of serialVersionUID?", "Verifies that the sender and receiver of a serialized object maintain compatible versions.")
            ]
        ),
        format_lesson(
            "java",
            "Lambda expressions", 25,
            [
                "Write concise lambda expressions using arrow syntax (->)",
                "Replace verbose anonymous inner classes with lambda expressions",
                "Understand variable capture and effectively final constraints"
            ],
            "A **Lambda Expression** (introduced in Java 8) is a short block of code that takes in parameters and returns a value. Lambdas provide a clear and concise way to represent an instance of a **Functional Interface** (an interface with a single abstract method, SAM).\nSyntax: `(parameters) -> expression` or `(parameters) -> { statements; }`.\nLambdas can capture variables from their enclosing scope, provided those variables are `final` or **effectively final** (never modified after initialization).",
            "// Before Java 8:\nRunnable r = new Runnable() { public void run() { System.out.println(\"Hello\"); } };\n\n// With Lambda:\nRunnable r = () -> System.out.println(\"Hello\");",
            "import java.util.ArrayList;\nimport java.util.List;\n\npublic class LambdaDemo {\n    public static void main(String[] args) {\n        List<String> tracks = new ArrayList<>(List.of(\"Java\", \"Python\", \"Go\", \"TypeScript\"));\n        \n        // Lambda filter with Predicate\n        tracks.removeIf(track -> track.startsWith(\"T\"));\n        \n        // Lambda iteration with Consumer\n        tracks.forEach(track -> System.out.println(\"Course track: \" + track));\n    }\n}",
            "Course track: Java\nCourse track: Python\nCourse track: Go",
            [
                "track -> track.startsWith(\"T\") is a Predicate lambda returning boolean.",
                "track -> System.out.println(...) is a Consumer lambda executing an action.",
                "Removes TypeScript and prints remaining tracks."
            ],
            [
                "Attempting to mutate a local variable declared outside the lambda body (variable must be effectively final).",
                "Writing complex 20-line lambda expressions; refactor large lambdas into dedicated methods."
            ],
            [
                ("What is a Functional Interface?", "An interface that declares exactly one abstract method."),
                ("What does 'effectively final' mean in Java?", "A local variable whose value is never changed after initialization, even if not explicitly declared final."),
                ("Can a lambda expression have multiple parameters and a block body?", "Yes: `(a, b) -> { int sum = a + b; return sum; }`.")
            ]
        ),
        format_lesson(
            "java",
            "Functional interfaces", 25,
            [
                "Utilize core standard functional interfaces in java.util.function",
                "Apply Predicate, Function, Consumer, and Supplier in business pipelines",
                "Annotate custom interfaces with @FunctionalInterface"
            ],
            "Java 8 provides standard functional interfaces in `java.util.function`:\n1. `Predicate<T>`: Evaluates `boolean test(T t)` (testing, filtering).\n2. `Function<T, R>`: Transforms `R apply(T t)` (mapping from type T to R).\n3. `Consumer<T>`: Executes `void accept(T t)` (consuming input with side-effects, printing, saving).\n4. `Supplier<T>`: Generates `T get()` (lazy generation, factory creation).\n5. `BiFunction<T, U, R>`, `UnaryOperator<T>`, `BinaryOperator<T>`.",
            "Predicate<Integer> isPassing = score -> score >= 70;\nFunction<String, Integer> stringLength = String::length;\nConsumer<String> logger = System.out::println;\nSupplier<Double> randomValue = Math::random;",
            "import java.util.function.*;\n\npublic class FunctionalInterfacesDemo {\n    public static void main(String[] args) {\n        Predicate<Integer> isEligible = age -> age >= 18;\n        Function<String, Integer> wordCounter = str -> str.split(\"\\\\s+\").length;\n        Consumer<String> alert = msg -> System.out.println(\"[SYSTEM ALERT]: \" + msg);\n        Supplier<String> tokenGenerator = () -> \"TOKEN_\" + System.currentTimeMillis();\n        \n        System.out.println(\"Age 20 eligible? \" + isEligible.test(20));\n        System.out.println(\"Word count in 'LearnHub Core': \" + wordCounter.apply(\"LearnHub Core\"));\n        alert.accept(\"Database synchronization active\");\n        System.out.println(\"Generated: \" + tokenGenerator.get());\n    }\n}",
            "Age 20 eligible? true\nWord count in 'LearnHub Core': 2\n[SYSTEM ALERT]: Database synchronization active\nGenerated: TOKEN_1791953000000",
            [
                "Predicate evaluates boolean condition.",
                "Function converts String to Integer word count.",
                "Consumer performs logging side-effect; Supplier produces fresh token."
            ],
            [
                "Adding a second abstract method to an interface annotated with `@FunctionalInterface`, causing compile failure.",
                "Confusing Function (transforms T to R) with Consumer (takes T and returns void)."
            ],
            [
                ("Can a functional interface have default or static methods?", "Yes, it can have any number of default/static methods as long as it has exactly one abstract method."),
                ("What does the andThen() method do on a Consumer or Function?", "Chains multiple operations sequentially."),
                ("What is the difference between Predicate<T> and BiPredicate<T, U>?", "Predicate accepts one argument; BiPredicate accepts two arguments.")
            ]
        ),
        format_lesson(
            "java",
            "Stream API", 30,
            [
                "Construct functional processing pipelines using the Java Stream API",
                "Differentiate intermediate operations (filter, map, sorted) from terminal operations (collect, reduce)",
                "Understand lazy evaluation and pipeline execution mechanics"
            ],
            "The **Stream API** (Java 8) enables declarative, functional-style operations on sequences of elements:\n- A stream does NOT store elements; it carries values from a source (collection, array) through a computational pipeline.\n- **Intermediate Operations**: Return a new stream and are **lazy** (not executed until a terminal operation is invoked). Examples: `filter()`, `map()`, `sorted()`, `distinct()`, `limit()`.\n- **Terminal Operations**: Trigger pipeline execution and produce a result or side-effect. Examples: `collect()`, `forEach()`, `reduce()`, `count()`, `findFirst()`.",
            "List<String> result = list.stream()\n    .filter(s -> s.length() > 3)\n    .map(String::toUpperCase)\n    .sorted()\n    .collect(Collectors.toList());",
            "import java.util.List;\nimport java.util.stream.Collectors;\n\npublic class StreamAPIDemo {\n    public static void main(String[] args) {\n        List<String> courses = List.of(\"Java\", \"Python\", \"JavaScript\", \"Go\", \"Java\", \"Rust\");\n        \n        List<String> filtered = courses.stream()\n            .distinct()                           // Remove duplicates\n            .filter(name -> name.length() > 3)    // Keep length > 3\n            .map(String::toUpperCase)             // Transform to uppercase\n            .sorted()                             // Alphabetical sort\n            .collect(Collectors.toList());        // Terminal collection\n            \n        System.out.println(\"Processed Courses: \" + filtered);\n        \n        long count = courses.stream().filter(c -> c.startsWith(\"J\")).count();\n        System.out.println(\"Courses starting with 'J': \" + count);\n    }\n}",
            "Processed Courses: [JAVA, JAVASCRIPT, PYTHON, RUST]\nCourses starting with 'J': 3",
            [
                "distinct() removes the duplicate 'Java'.",
                "filter() eliminates 'Go' because length <= 3.",
                "map() transforms remaining strings to uppercase, sorted() orders them, and collect() returns a new List."
            ],
            [
                "Attempting to reuse a Stream after a terminal operation has already executed (`IllegalStateException: stream has already been operated upon or closed`).",
                "Performing stateful or blocking operations inside stream lambdas."
            ],
            [
                ("Why are intermediate stream operations described as lazy?", "They do not execute until a terminal operation triggers evaluation."),
                ("How does parallelStream() work internally?", "Uses the common ForkJoinPool to process chunks across CPU cores."),
                ("What does reduce() do in a stream pipeline?", "Combines stream elements into a single summary value (e.g. sum, max).")
            ]
        ),
        format_lesson(
            "java",
            "Optional", 20,
            [
                "Eliminate NullPointerException using java.util.Optional<T>",
                "Safely unwrap values using orElse, orElseGet, and orElseThrow",
                "Adopt Optional best practices in method return types"
            ],
            "Introduced in Java 8, `Optional<T>` is a container object that may or may not contain a non-null value. It was created to provide a type-level solution for representing 'no result' without using `null`, directly eliminating unexpected `NullPointerException`s.\nKey operations:\n- `Optional.of(val)` / `Optional.ofNullable(val)` / `Optional.empty()`\n- `isPresent()` / `isEmpty()`\n- `orElse(defaultVal)`: Returns value or fallback immediately.\n- `orElseGet(supplier)`: Lazily evaluates fallback supplier if empty.\n- `orElseThrow()`: Throws exception if value is absent.",
            "Optional<Course> findCourse(Long id) {\n    return Optional.ofNullable(repository.findById(id));\n}\nCourse c = findCourse(42).orElseThrow(() -> new CourseNotFoundException(\"Missing course\"));",
            "import java.util.Optional;\n\npublic class OptionalDemo {\n    public static Optional<String> findInstructor(String courseTitle) {\n        if (\"Java Masterclass\".equalsIgnoreCase(courseTitle)) {\n            return Optional.of(\"Sarah Connor\");\n        }\n        return Optional.empty();\n    }\n    \n    public static void main(String[] args) {\n        Optional<String> instructor1 = findInstructor(\"Java Masterclass\");\n        System.out.println(\"Java Instructor: \" + instructor1.orElse(\"Unassigned\"));\n        \n        Optional<String> instructor2 = findInstructor(\"Rust Track\");\n        System.out.println(\"Rust Instructor: \" + instructor2.orElse(\"Staff Faculty\"));\n    }\n}",
            "Java Instructor: Sarah Connor\nRust Instructor: Staff Faculty",
            [
                "findInstructor returns an Optional<String> clearly communicating that an instructor might not exist.",
                "orElse provides safe fallback defaults without checking for null."
            ],
            [
                "Calling `optional.get()` without checking `isPresent()`, which throws `NoSuchElementException` when empty.",
                "Using Optional as class field types or method parameter types; Optional is designed primarily as a method return type."
            ],
            [
                ("What is the difference between orElse(val) and orElseGet(supplier)?", "orElse evaluates the default value eagerly; orElseGet evaluates lazily only when empty."),
                ("Why should Optional NOT be used as a method parameter type?", "It forces callers to wrap values unnecessarily and can itself be passed as null."),
                ("What does Optional.map() do?", "Transforms the enclosed value if present, returning a new Optional.")
            ]
        ),
        format_lesson(
            "java",
            "Date and time API", 25,
            [
                "Utilize the modern java.time package (LocalDate, LocalTime, LocalDateTime)",
                "Calculate elapsed time and intervals using Duration and Period",
                "Format and parse timestamps using DateTimeFormatter"
            ],
            "Java 8 completely replaced the buggy, mutable legacy `java.util.Date` and `Calendar` with the immutable, thread-safe `java.time` API (JSR-310):\n- `LocalDate`: Date without time (year, month, day).\n- `LocalTime`: Time without date (hour, minute, second, nanosecond).\n- `LocalDateTime`: Combines date and time without timezone offset.\n- `ZonedDateTime`: Date and time with explicit timezone rules (e.g. `ZoneId.of(\"UTC\")`).\n- `Period`: Date-based amount of time (years, months, days).\n- `Duration`: Time-based amount of time (seconds, nanoseconds).",
            "LocalDate today = LocalDate.now();\nLocalDate deadline = today.plusDays(14);\nDateTimeFormatter fmt = DateTimeFormatter.ofPattern(\"yyyy-MM-dd HH:mm\");",
            "import java.time.LocalDate;\nimport java.time.LocalDateTime;\nimport java.time.format.DateTimeFormatter;\nimport java.time.Period;\n\npublic class DateTimeDemo {\n    public static void main(String[] args) {\n        LocalDate startDate = LocalDate.of(2026, 1, 15);\n        LocalDate completionDate = startDate.plusMonths(3);\n        \n        Period courseDuration = Period.between(startDate, completionDate);\n        System.out.println(\"Course Start: \" + startDate);\n        System.out.println(\"Projected Finish: \" + completionDate);\n        System.out.println(\"Duration: \" + courseDuration.getMonths() + \" months\");\n        \n        LocalDateTime now = LocalDateTime.now();\n        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(\"MMMM dd, yyyy - HH:mm:ss\");\n        System.out.println(\"Formatted System Time: \" + now.format(formatter));\n    }\n}",
            "Course Start: 2026-01-15\nProjected Finish: 2026-04-15\nDuration: 3 months\nFormatted System Time: October 14, 2026 - 11:45:00",
            [
                "LocalDate.of creates an immutable calendar date.",
                "plusMonths(3) produces a new date object without modifying the original.",
                "DateTimeFormatter formats timestamps cleanly."
            ],
            [
                "Using legacy `java.util.Date` and `SimpleDateFormat` which are not thread-safe and have 0-indexed months.",
                "Confusing `Duration` (for times/seconds) with `Period` (for calendar days/months/years)."
            ],
            [
                ("Why is SimpleDateFormat notorious in multi-threaded Java applications?", "It is mutable and not thread-safe, corrupting dates under concurrent access."),
                ("How do you convert a LocalDateTime to UTC Instant?", "Use `dateTime.toInstant(ZoneOffset.UTC)`."),
                ("Are classes in the java.time package mutable or immutable?", "All classes in java.time are strictly immutable and thread-safe.")
            ]
        ),
        format_lesson(
            "java",
            "Multithreading basics", 25,
            [
                "Understand thread concurrency and JVM execution models",
                "Create threads by extending Thread or implementing Runnable",
                "Manage thread lifecycle states (NEW, RUNNABLE, BLOCKED, WAITING, TERMINATED)"
            ],
            "A **Thread** is the smallest unit of execution within a process. Multithreading allows concurrent execution of two or more parts of a program to maximize CPU core utilization. In Java:\n1. Implementing `Runnable`: Preferred approach (`() -> { ... }`). Separates the task from the thread runner mechanism.\n2. Extending `Thread`: Overrides `run()`, but consumes the class's single inheritance slot.\nLifecycle states: `NEW -> RUNNABLE -> (BLOCKED / WAITING / TIMED_WAITING) -> TERMINATED`.\nCrucial: Call `thread.start()` to spawn a new OS thread. Calling `thread.run()` directly runs synchronously on the current thread without concurrency!",
            "Thread t = new Thread(() -> {\n    System.out.println(\"Running in thread: \" + Thread.currentThread().getName());\n});\nt.start();",
            "public class MultithreadingDemo {\n    public static void main(String[] args) throws InterruptedException {\n        Thread backgroundWorker = new Thread(() -> {\n            System.out.println(\"Worker thread started: \" + Thread.currentThread().getName());\n            try {\n                Thread.sleep(50);\n            } catch (InterruptedException e) {\n                Thread.currentThread().interrupt();\n            }\n            System.out.println(\"Worker task finished.\");\n        });\n        \n        backgroundWorker.start();\n        backgroundWorker.join(); // Wait for worker to finish\n        System.out.println(\"Main thread resumed and concluding.\");\n    }\n}",
            "Worker thread started: Thread-0\nWorker task finished.\nMain thread resumed and concluding.",
            [
                "backgroundWorker is started with start(), creating a separate thread.",
                "thread.join() causes the main thread to wait until backgroundWorker completes."
            ],
            [
                "Calling `thread.run()` instead of `thread.start()`, which executes synchronously on the caller's thread.",
                "Ignoring InterruptedException without restoring the thread's interrupt status (`Thread.currentThread().interrupt()`)."
            ],
            [
                ("Why is implementing Runnable preferred over extending Thread?", "Keeps task logic decoupled and preserves class inheritance."),
                ("What does Thread.sleep() do?", "Suspends current thread execution for specified milliseconds without giving up locks."),
                ("What is a daemon thread in Java?", "A background thread that does not prevent the JVM from exiting when all user threads finish.")
            ]
        ),
        format_lesson(
            "java",
            "Synchronization", 25,
            [
                "Identify race conditions in shared mutable multithreaded states",
                "Synchronize access using the synchronized keyword (methods and blocks)",
                "Understand intrinsic locks (monitors) and atomic variables"
            ],
            "When multiple threads concurrently read and write **shared mutable state** without coordination, **Race Conditions** occur, corrupting data integrity. Java provides:\n- `synchronized` methods/blocks: Uses an object's intrinsic monitor lock to ensure **mutual exclusion**—only one thread can execute the protected critical section at a time.\n- `volatile`: Ensures memory visibility across CPU caches (every read comes from main memory).\n- `AtomicInteger` / `AtomicLong`: Lock-free thread-safe primitives using low-level hardware Compare-And-Swap (CAS).",
            "private int count = 0;\npublic synchronized void increment() {\n    count++; // Protected from race conditions\n}",
            "public class SynchronizationDemo {\n    static class Counter {\n        private int value = 0;\n        \n        public synchronized void increment() {\n            value++;\n        }\n        \n        public synchronized int getValue() {\n            return value;\n        }\n    }\n    \n    public static void main(String[] args) throws InterruptedException {\n        Counter counter = new Counter();\n        \n        Thread t1 = new Thread(() -> { for (int i = 0; i < 1000; i++) counter.increment(); });\n        Thread t2 = new Thread(() -> { for (int i = 0; i < 1000; i++) counter.increment(); });\n        \n        t1.start();\n        t2.start();\n        t1.join();\n        t2.join();\n        \n        System.out.println(\"Synchronized Count (Expected 2000): \" + counter.getValue());\n    }\n}",
            "Synchronized Count (Expected 2000): 2000",
            [
                "t1 and t2 concurrently increment the counter 1000 times each.",
                "synchronized keyword on increment() guarantees mutual exclusion, producing exact count of 2000."
            ],
            [
                "Synchronizing on different lock objects across threads, failing to provide mutual exclusion.",
                "Creating Deadlocks by acquiring multiple locks in different orders across threads."
            ],
            [
                ("What is a Deadlock in multithreading?", "A state where two or more threads are permanently blocked, each waiting for a lock held by the other."),
                ("How does AtomicInteger achieve thread safety without using synchronized locks?", "Uses CPU hardware-level Compare-And-Swap (CAS) instructions."),
                ("What is the difference between a synchronized method and a synchronized block?", "Synchronized blocks allow fine-grained locking on specific objects rather than locking the entire method/this.")
            ]
        ),
        format_lesson(
            "java",
            "Executor framework", 25,
            [
                "Manage thread lifecycles using java.util.concurrent.ExecutorService",
                "Submit asynchronous tasks using Callable and Future",
                "Prevent resource exhaustion by utilizing managed thread pools"
            ],
            "Creating raw `new Thread()` instances for every incoming request causes severe CPU and memory exhaustion under load. The **Executor Framework** decouples task submission from execution mechanics using thread pools:\n- `Executors.newFixedThreadPool(n)`: Pool with a fixed number of reusable threads.\n- `Executors.newCachedThreadPool()`: Dynamically creates threads as needed.\n- `Callable<V>`: Like Runnable, but returns a computed result and can throw checked exceptions.\n- `Future<V>`: Represents the pending result of an asynchronous task (`get()` blocks until done).\n- Always call `executor.shutdown()` to release threads cleanly.",
            "ExecutorService executor = Executors.newFixedThreadPool(4);\nFuture<Integer> future = executor.submit(() -> 42 * 2);\nint result = future.get();\nexecutor.shutdown();",
            "import java.util.concurrent.*;\n\npublic class ExecutorFrameworkDemo {\n    public static void main(String[] args) throws Exception {\n        ExecutorService pool = Executors.newFixedThreadPool(2);\n        \n        Callable<String> task = () -> {\n            Thread.sleep(50);\n            return \"Report generated by: \" + Thread.currentThread().getName();\n        };\n        \n        Future<String> futureResult = pool.submit(task);\n        System.out.println(\"Task submitted asynchronously, performing other work...\");\n        \n        String result = futureResult.get(1, TimeUnit.SECONDS);\n        System.out.println(\"Result received: \" + result);\n        \n        pool.shutdown();\n    }\n}",
            "Task submitted asynchronously, performing other work...\nResult received: Report generated by: pool-1-thread-1",
            [
                "newFixedThreadPool allocates 2 reusable worker threads.",
                "Callable executes in the background and returns a Future.",
                "futureResult.get() retrieves the computed result with a timeout guard."
            ],
            [
                "Forgetting to call `executor.shutdown()`, preventing the JVM from terminating because pool threads remain active.",
                "Calling `future.get()` without a timeout, causing infinite hangs if the task stalls."
            ],
            [
                ("What is the difference between execute() and submit() on an ExecutorService?", "execute() takes Runnable and returns void; submit() takes Callable/Runnable and returns Future."),
                ("What happens to tasks submitted to a thread pool when all threads are currently busy?", "They wait in an internal blocking task queue (e.g. LinkedBlockingQueue)."),
                ("What is CompletableFuture in Java 8+?", "An asynchronous reactive pipeline supporting non-blocking composition and chaining.")
            ]
        ),
        format_lesson(
            "java",
            "JVM memory basics", 25,
            [
                "Differentiate JVM Stack memory from Heap memory",
                "Trace object allocation, references, and Garbage Collection mechanics",
                "Diagnose OutOfMemoryError and StackOverflowError causes"
            ],
            "The JVM divides runtime memory into distinct regions:\n1. **Stack Memory**: Fast, per-thread memory storing local primitive variables and object reference pointers. Stack frames are created on method invocation and destroyed immediately on method return.\n2. **Heap Memory**: Shared memory region where all objects (`new Object()`) and class instances are allocated. Reclaimed automatically by the Garbage Collector.\n3. **Metaspace**: Stores loaded class metadata, bytecode, and static variables.\nMemory Errors:\n- `StackOverflowError`: Call stack depth exceeded (e.g. infinite recursion).\n- `OutOfMemoryError: Java heap space`: Heap is exhausted because active references prevent GC.",
            "// Stack: int count = 5; Student ref = [Address 0x7F2A]\n// Heap: [Address 0x7F2A] -> Student { name=\"Alex\", id=101 }",
            "public class JVMMemoryDemo {\n    public static void main(String[] args) {\n        long totalHeap = Runtime.getRuntime().totalMemory() / (1024 * 1024);\n        long maxHeap = Runtime.getRuntime().maxMemory() / (1024 * 1024);\n        long freeHeap = Runtime.getRuntime().freeMemory() / (1024 * 1024);\n        \n        System.out.println(\"JVM Heap Configuration:\");\n        System.out.println(\"Current Allocated Heap: \" + totalHeap + \" MB\");\n        System.out.println(\"Max Allowable Heap (-Xmx): \" + maxHeap + \" MB\");\n        System.out.println(\"Free Heap in Allocated: \" + freeHeap + \" MB\");\n    }\n}",
            "JVM Heap Configuration:\nCurrent Allocated Heap: 256 MB\nMax Allowable Heap (-Xmx): 4096 MB\nFree Heap in Allocated: 240 MB",
            [
                "Queries the JVM Runtime instance for active memory pool stats.",
                "Demonstrates how the JVM dynamically sizes heap memory within -Xmx limits."
            ],
            [
                "Assuming Java cannot have memory leaks; holding obsolete references in static collections prevents GC reclamation and causes OutOfMemoryError.",
                "Creating millions of short-lived temporary objects inside tight loops instead of reusing buffers."
            ],
            [
                ("What command-line flags set initial and maximum heap sizes in the JVM?", "`-Xms` for initial heap, `-Xmx` for maximum heap."),
                ("How does generational garbage collection (Young vs Old generation) optimize GC cycles?", "Weak Generational Hypothesis: most objects die young, so Young Gen is collected frequently and quickly."),
                ("What is a memory leak in a garbage-collected language like Java?", "An object that is no longer needed by application logic but remains reachable via an active reference chain.")
            ]
        ),
        format_lesson(
            "java",
            "Debugging", 20,
            [
                "Apply IDE debugging workflows (Breakpoints, Step Over, Step Into, Step Out)",
                "Inspect variables, watches, and stack frames during execution pauses",
                "Analyze stack traces to pinpoint root-cause source file and line numbers"
            ],
            "Debugging is the systematic process of finding and resolving bugs in software:\n- **Breakpoint**: Pauses execution at a specific line before it runs.\n- **Step Over (F8)**: Executes the current line and pauses at the next line in the current method.\n- **Step Into (F7)**: Jumps inside the method called on the current line.\n- **Step Out (Shift+F8)**: Executes the remainder of the current method and pauses at caller.\n- **Watch**: Expression evaluated dynamically in real time.\n- **Stack Trace**: Traceback printed when an exception crashes, showing the exact file, class, method, and line number where the failure originated.",
            "// Interpreting a stack trace:\n// Exception in thread \"main\" java.lang.NullPointerException\n//     at com.learnhub.service.CourseService.enroll(CourseService.java:42) <- Root cause line!",
            "public class DebuggingDemo {\n    public static int calculateAverage(int[] values) {\n        if (values == null || values.length == 0) return 0;\n        int sum = 0;\n        for (int v : values) sum += v;\n        return sum / values.length;\n    }\n    \n    public static void main(String[] args) {\n        int[] sample = {80, 90, 100};\n        int avg = calculateAverage(sample);\n        System.out.println(\"Diagnostic check: Calculated average is \" + avg);\n    }\n}",
            "Diagnostic check: Calculated average is 90",
            [
                "calculateAverage guards against null and empty array edge cases.",
                "Demonstrates trace analysis and defensive validation patterns."
            ],
            [
                "Relying solely on `System.out.println` statements instead of using an interactive IDE debugger.",
                "Ignoring the bottom-most cause in a chained exception stack trace."
            ],
            [
                ("What is a conditional breakpoint in an IDE?", "A breakpoint that only pauses execution when a specified boolean condition evaluates to true (e.g. `i == 950`)."),
                ("How do you read a stack trace from top to bottom?", "Top line indicates exception type; immediate following lines show call stack frames leading to the error."),
                ("What is the difference between Step Over and Step Into?", "Step Over treats method calls as a single step; Step Into steps inside the method's code.")
            ]
        )
    ]
    return {
        "title": "Module 6 — Files, Modern Java, and Concurrency",
        "description": "Use modern language features, work with files, and understand basic concurrency.",
        "sequenceOrder": 6,
        "lessons": lessons
    }

print("Java modules 5 & 6 ready.")
