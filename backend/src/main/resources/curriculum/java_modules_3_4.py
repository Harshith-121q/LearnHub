from formatter import format_lesson

def get_java_module_3():
    lessons = [
        format_lesson(
            "java",
            "Methods and method signatures", 20,
            [
                "Define modular methods with clear access modifiers, return types, and identifiers",
                "Understand method signatures and how the JVM distinguishes call targets",
                "Apply variable scoping rules between local method scopes and class fields"
            ],
            "A method is a block of code designed to perform a specific task, promoting reusability and maintainability. A method declaration consists of:\n1. Modifiers: `public`, `private`, `static`.\n2. Return Type: Data type returned (`int`, `String`, etc.), or `void` if nothing is returned.\n3. Method Name: Verb-based identifier following camelCase conventions.\n4. Parameter List: Comma-separated list of typed inputs enclosed in parentheses.\n5. Method Body: Statements inside curly braces.\nA method signature consists strictly of the **method name and the parameter type list** (return types and access modifiers are NOT part of the signature).",
            "public returnType methodName(ParamType p1, ParamType p2) {\n    // Method body\n    return value;\n}",
            "public class MethodsDemo {\n    public static int calculateRectangleArea(int width, int height) {\n        return width * height;\n    }\n    \n    public static void printReport(String title, int value) {\n        System.out.println(\"Report: \" + title + \" | Computed Area: \" + value);\n    }\n    \n    public static void main(String[] args) {\n        int area = calculateRectangleArea(12, 8);\n        printReport(\"Classroom Grid\", area);\n    }\n}",
            "Report: Classroom Grid | Computed Area: 96",
            [
                "calculateRectangleArea takes two int parameters, computes their product, and returns an int.",
                "printReport takes a String and int, executes printing logic, and returns void.",
                "main coordinates invocation and passes return values into downstream calls."
            ],
            [
                "Declaring a return type other than void but omitting a `return` statement on all code paths.",
                "Assuming the return type differentiates a method signature; two methods with identical names and parameters but different return types will fail compilation."
            ],
            [
                ("What two components strictly comprise a Java method signature?", "Identify method name and parameter types list."),
                ("Can a method with a void return type contain a return statement?", "Explain `return;` as an early exit mechanism."),
                ("What error occurs if a return statement is unreachable?", "Explain compile-time unreachable statement error.")
            ]
        ),
        format_lesson(
            "java",
            "Parameters and return values", 20,
            [
                "Distinguish formal parameters from actual arguments",
                "Understand Java's strictly 'Pass-by-Value' parameter passing model",
                "Evaluate reference manipulation vs primitive copying in method calls"
            ],
            "Java is strictly **Pass-by-Value** in all situations:\n- When a primitive value is passed as an argument, a copy of the primitive value is created. Modifying that parameter inside the method does NOT affect the caller's original variable.\n- When an object reference is passed, a copy of the reference address is passed by value. The method can modify the internal state of the referenced object, but reassigning the reference itself inside the method does NOT rebind the caller's reference.",
            "// Value demonstration:\npublic static void modify(int x) { x = 99; } // Original remains unchanged\npublic static void mutate(StringBuilder sb) { sb.append(\" altered\"); } // Mutates referenced object",
            "public class PassByValueDemo {\n    public static void incrementPrimitive(int val) {\n        val += 10;\n    }\n    \n    public static void modifyArray(int[] arr) {\n        arr[0] = 999; // Mutates referenced array in heap\n    }\n    \n    public static void main(String[] args) {\n        int score = 50;\n        incrementPrimitive(score);\n        System.out.println(\"Primitive after method call: \" + score);\n        \n        int[] numbers = {10, 20, 30};\n        modifyArray(numbers);\n        System.out.println(\"Array element 0 after call: \" + numbers[0]);\n    }\n}",
            "Primitive after method call: 50\nArray element 0 after call: 999",
            [
                "score passed to incrementPrimitive is copied; the original score remains 50.",
                "modifyArray receives a copy of the reference to the heap array; altering arr[0] updates the heap object directly."
            ],
            [
                "Believing Java is 'pass-by-reference' for objects; reassigning `arr = new int[5]` inside the method has no effect on caller.",
                "Expecting primitive parameters to be updated without capturing a return value."
            ],
            [
                ("Why does swapping two integers via `swap(int a, int b)` fail to alter variables in the caller?", "Explain pass-by-value copying."),
                ("How can a method return multiple values in Java?", "Discuss returning custom class objects, arrays, or records."),
                ("What is the consequence of reassigning an object parameter inside a method?", "Explain reference local shadow reassignment.")
            ]
        ),
        format_lesson(
            "java",
            "Method overloading", 20,
            [
                "Implement method overloading within the same class",
                "Vary parameter counts, types, and sequence orders",
                "Identify ambiguous invocations and invalid overload declarations"
            ],
            "Method Overloading allows multiple methods in the same class to share the same name, provided they have different parameter lists (different number of parameters, different types, or different ordering of types). Overloading improves API consistency (e.g. `System.out.println` has overloads for `int`, `String`, `boolean`, `char`, etc.). Method overloading is resolved at **compile-time** (static polymorphism).",
            "public int add(int a, int b) { return a + b; }\npublic double add(double a, double b) { return a + b; }\npublic int add(int a, int b, int c) { return a + b + c; }",
            "public class OverloadingDemo {\n    public static int multiply(int a, int b) {\n        return a * b;\n    }\n    \n    public static double multiply(double a, double b) {\n        return a * b;\n    }\n    \n    public static String multiply(String text, int times) {\n        return text.repeat(times);\n    }\n    \n    public static void main(String[] args) {\n        System.out.println(\"Int multiply: \" + multiply(4, 5));\n        System.out.println(\"Double multiply: \" + multiply(2.5, 4.0));\n        System.out.println(\"String repeat: \" + multiply(\"Java! \", 3));\n    }\n}",
            "Int multiply: 20\nDouble multiply: 10.0\nString repeat: Java! Java! Java! ",
            [
                "The compiler examines arguments at call site: multiply(4, 5) matches the (int, int) signature.",
                "multiply(2.5, 4.0) matches (double, double); multiply(\"Java! \", 3) matches (String, int)."
            ],
            [
                "Attempting to overload a method solely by changing its return type (results in compile error).",
                "Creating ambiguous overloads (e.g. `foo(int, double)` and `foo(double, int)` called with `foo(5, 5)`)."
            ],
            [
                ("Can two methods be overloaded if only their access modifiers differ?", "Explain no, because signatures are identical."),
                ("How does automatic type promotion affect overloaded method resolution?", "Explain widening search from int to long/float/double."),
                ("Why is method overloading referred to as compile-time polymorphism?", "Explain compiler binding based on reference types.")
            ]
        ),
        format_lesson(
            "java",
            "Recursion", 25,
            [
                "Deconstruct recursive algorithms into base cases and recursive steps",
                "Trace JVM call stack activation frames and unwinding",
                "Compare recursive time/memory trade-offs with iterative loops"
            ],
            "Recursion occurs when a method calls itself to solve a smaller subproblem of the original problem. Every well-designed recursive algorithm requires two components:\n1. Base Case: A terminating condition where the answer is known directly without further recursive calls.\n2. Recursive Case: The reduction step where the method calls itself with a strictly smaller or simpler input.\nWithout a valid base case, calls accumulate indefinitely until the JVM runs out of call stack memory and throws `StackOverflowError`.",
            "public static int factorial(int n) {\n    if (n <= 1) return 1; // Base case\n    return n * factorial(n - 1); // Recursive case\n}",
            "public class RecursionDemo {\n    public static long factorial(int n) {\n        if (n <= 1) return 1;\n        return n * factorial(n - 1);\n    }\n    \n    public static int fibonacci(int n) {\n        if (n <= 0) return 0;\n        if (n == 1) return 1;\n        return fibonacci(n - 1) + fibonacci(n - 2);\n    }\n    \n    public static void main(String[] args) {\n        System.out.println(\"Factorial of 6: \" + factorial(6));\n        System.out.println(\"7th Fibonacci number: \" + fibonacci(7));\n    }\n}",
            "Factorial of 6: 720\n7th Fibonacci number: 13",
            [
                "factorial(6) creates stack frames down to factorial(1) = 1, then unwinds: 1*2*3*4*5*6 = 720.",
                "fibonacci branches into a recursive tree, evaluating subproblems down to base cases 0 and 1."
            ],
            [
                "Missing base case or incorrect termination condition, triggering a `StackOverflowError`.",
                "Using naive recursion for Fibonacci without memoization, leading to exponential $O(2^n)$ time complexity."
            ],
            [
                ("What error occurs when a recursive function never hits a base case?", "Identify java.lang.StackOverflowError."),
                ("How does the JVM call stack maintain state across recursive invocations?", "Explain stack frames storing local variables and return addresses."),
                ("When is an iterative loop preferable to a recursive method?", "Discuss memory overhead and stack depth limits.")
            ]
        ),
        format_lesson(
            "java",
            "One-dimensional arrays", 25,
            [
                "Declare, instantiate, and initialize one-dimensional arrays",
                "Access array elements via 0-based indexing and inspect length property",
                "Safely iterate through arrays using standard for and enhanced for-each loops"
            ],
            "An array in Java is a fixed-size, homogeneous container object allocated in heap memory holding elements of a single specified type.\n- Elements are indexed from `0` to `length - 1`.\n- The size of an array is immutable once created.\n- Uninitialized elements receive default values: `0` for numbers, `false` for booleans, `null` for object references.\n- Accessing an index outside valid bounds throws `ArrayIndexOutOfBoundsException`.",
            "// Declaration and instantiation\nint[] scores = new int[5]; // Elements default to 0\nString[] names = {\"Alice\", \"Bob\", \"Charlie\"}; // Array literal",
            "public class ArrayDemo {\n    public static void main(String[] args) {\n        int[] grades = {88, 92, 79, 95, 84};\n        \n        System.out.println(\"Total students: \" + grades.length);\n        System.out.println(\"First grade: \" + grades[0]);\n        System.out.println(\"Last grade: \" + grades[grades.length - 1]);\n        \n        int sum = 0;\n        System.out.print(\"Grades: \");\n        for (int g : grades) { // Enhanced for-each loop\n            System.out.print(g + \" \");\n            sum += g;\n        }\n        System.out.println();\n        \n        double average = (double) sum / grades.length;\n        System.out.printf(\"Class Average: %.2f%n\", average);\n    }\n}",
            "Total students: 5\nFirst grade: 88\nLast grade: 84\nGrades: 88 92 79 95 84 \nClass Average: 87.60",
            [
                "grades.length returns 5.",
                "Enhanced for-each loop cleanly traverses each integer element in order without managing indices.",
                "Average casts sum to double to ensure floating-point precision."
            ],
            [
                "Attempting to access `array[array.length]`, triggering `ArrayIndexOutOfBoundsException`.",
                "Treating `length` as a method (e.g. `array.length()`) instead of a public final field."
            ],
            [
                ("What is the default value of elements in a new boolean[10] array?", "Identify false."),
                ("Can you resize an existing Java array after it has been instantiated?", "Explain immutability of array size in Java."),
                ("How does an enhanced for-each loop prevent indexing bugs?", "Explain abstraction of index boundary checks.")
            ]
        ),
        format_lesson(
            "java",
            "Multidimensional arrays", 25,
            [
                "Construct and traverse two-dimensional rectangular arrays and grids",
                "Understand Java's 'array-of-arrays' representation and jagged arrays",
                "Implement nested row and column traversal algorithms"
            ],
            "In Java, multidimensional arrays are actually **arrays of arrays**. A 2D array `int[][] matrix` is an array whose elements are themselves references to 1D integer arrays. Because of this architecture, Java supports **ragged (jagged) arrays**, where each row can have a completely different length.",
            "// Rectangular 2D array:\nint[][] grid = new int[3][4]; // 3 rows, 4 columns\n\n// Jagged array:\nint[][] jagged = new int[3][];\njagged[0] = new int[2];\njagged[1] = new int[4];",
            "public class MultiArrayDemo {\n    public static void main(String[] args) {\n        int[][] matrix = {\n            {1, 2, 3},\n            {4, 5, 6},\n            {7, 8, 9}\n        };\n        \n        System.out.println(\"Matrix Rows: \" + matrix.length);\n        System.out.println(\"Row 0 Columns: \" + matrix[0].length);\n        \n        int diagonalSum = 0;\n        for (int r = 0; r < matrix.length; r++) {\n            for (int c = 0; c < matrix[r].length; c++) {\n                if (r == c) diagonalSum += matrix[r][c];\n            }\n        }\n        System.out.println(\"Primary Diagonal Sum (1+5+9): \" + diagonalSum);\n    }\n}",
            "Matrix Rows: 3\nRow 0 Columns: 3\nPrimary Diagonal Sum (1+5+9): 15",
            [
                "matrix is an array of 3 row arrays.",
                "Outer loop iterates through rows with matrix.length; inner loop iterates across columns with matrix[r].length.",
                "Sum accumulates elements where row index equals column index (1 + 5 + 9 = 15)."
            ],
            [
                "Confusing row and column index order (`matrix[row][col]`).",
                "Assuming all rows have the same length when dealing with jagged arrays, leading to index out of bounds errors."
            ],
            [
                ("What is a jagged array in Java?", "Explain an array where inner arrays have varying lengths."),
                ("How do you find the number of columns in row 2 of a 2D array named grid?", "Use grid[2].length."),
                ("Write code to instantiate a 3x3 identity matrix.", "Initialize 2D array and set `matrix[i][i] = 1`.")
            ]
        ),
        format_lesson(
            "java",
            "Array algorithms", 30,
            [
                "Implement linear search and find extrema (minimum and maximum)",
                "Reverse array contents in-place using two-pointer swap",
                "Perform array duplication using System.arraycopy and Arrays.copyOf"
            ],
            "Working with arrays involves fundamental algorithms:\n1. Search: Linear search checks each element sequentially ($O(n)$).\n2. Extrema: Iterating through the collection tracking current min/max values.\n3. In-Place Reversal: Two pointers (start and end) swapping elements until meeting in the middle ($O(n)$ time, $O(1)$ auxiliary space).\n4. Copying: `System.arraycopy(src, srcPos, dest, destPos, length)` offers high-performance native memory copying.",
            "int[] copy = Arrays.copyOf(original, original.length);\nSystem.arraycopy(src, 0, dest, 0, len);",
            "import java.util.Arrays;\n\npublic class ArrayAlgorithmsDemo {\n    public static int findMax(int[] arr) {\n        int max = arr[0];\n        for (int v : arr) if (v > max) max = v;\n        return max;\n    }\n    \n    public static void reverseInPlace(int[] arr) {\n        int left = 0, right = arr.length - 1;\n        while (left < right) {\n            int temp = arr[left];\n            arr[left] = arr[right];\n            arr[right] = temp;\n            left++;\n            right--;\n        }\n    }\n    \n    public static void main(String[] args) {\n        int[] numbers = {45, 12, 89, 34, 71};\n        System.out.println(\"Original: \" + Arrays.toString(numbers));\n        System.out.println(\"Maximum element: \" + findMax(numbers));\n        \n        reverseInPlace(numbers);\n        System.out.println(\"Reversed: \" + Arrays.toString(numbers));\n    }\n}",
            "Original: [45, 12, 89, 34, 71]\nMaximum element: 89\nReversed: [71, 34, 89, 12, 45]",
            [
                "findMax iterates over elements and returns 89.",
                "reverseInPlace swaps indices (0,4) and (1,3), leaving middle index 2 untouched.",
                "Arrays.toString() formats array contents as a comma-separated readable string."
            ],
            [
                "Initializing min/max to 0 instead of `arr[0]`, which fails if all array values are negative.",
                "Reversing an array by running a loop all the way from `0` to `length - 1`, which inadvertently swaps items twice and returns original order."
            ],
            [
                ("What is the time complexity of linear search across an unsorted array of size N?", "Explain O(N)."),
                ("Why is `System.arraycopy` preferred over manual for-loop element assignment?", "Explain native JVM memory block transfer optimizations."),
                ("How does the two-pointer reversal algorithm achieve O(1) auxiliary space?", "Explain in-place swapping without allocating a secondary buffer.")
            ]
        ),
        format_lesson(
            "java",
            "Strings", 25,
            [
                "Understand String immutability and the JVM String Constant Pool",
                "Apply core inspection methods (length, charAt, indexOf, contains)",
                "Transform and parse text using substring, replace, split, and trim"
            ],
            "In Java, `String` is an immutable reference object: once created, its internal character sequence cannot be altered. Any method that appears to modify a String (e.g. `toUpperCase()`, `replace()`) actually creates and returns a brand-new `String` object in memory.\nString literals are stored in the **String Constant Pool** inside heap memory to conserve memory and optimize reuse.",
            "String s = \"LearnHub\";\ns = s.substring(0, 5); // s is now \"Learn\"",
            "public class StringDemo {\n    public static void main(String[] args) {\n        String course = \"  LearnHub Fullstack Java Track  \";\n        \n        // Inspection\n        System.out.println(\"Original length: \" + course.length());\n        \n        // Transformations\n        String clean = course.trim();\n        System.out.println(\"Trimmed: '\" + clean + \"' (Length: \" + clean.length() + \")\");\n        System.out.println(\"Uppercase: \" + clean.toUpperCase());\n        System.out.println(\"Contains 'Java'? \" + clean.contains(\"Java\"));\n        System.out.println(\"Substring (0, 8): \" + clean.substring(0, 8));\n        \n        // Splitting\n        String[] tokens = clean.split(\" \");\n        System.out.println(\"Word count: \" + tokens.length);\n    }\n}",
            "Original length: 33\nTrimmed: 'LearnHub Fullstack Java Track' (Length: 29)\nUppercase: LEARNHUB FULLSTACK JAVA TRACK\nContains 'Java'? true\nSubstring (0, 8): LearnHub\nWord count: 4",
            [
                "course.trim() removes leading and trailing whitespace without modifying the original string.",
                "clean.substring(0, 8) extracts characters from index 0 up to (but not including) index 8.",
                "clean.split(\" \") breaks text into an array of 4 individual word strings."
            ],
            [
                "Calling string manipulation methods without storing the returned new string (e.g. `str.toUpperCase();` alone does not modify `str`).",
                "Assuming `substring(startIndex, endIndex)` includes the character at `endIndex`; the end index is exclusive."
            ],
            [
                ("Why are Strings made immutable in the Java language specification?", "Discuss security, caching, thread-safety, and String Constant Pool integrity."),
                ("What does the split() method accept as its delimiter parameter?", "Explain regular expression (regex)."),
                ("What exception is thrown if substring index bounds are negative or exceed string length?", "Identify StringIndexOutOfBoundsException.")
            ]
        ),
        format_lesson(
            "java",
            "String comparison", 20,
            [
                "Contrast reference equality (==) with content equality (.equals)",
                "Perform case-insensitive comparisons using equalsIgnoreCase",
                "Prevent NullPointerException during string comparisons using safe idiom patterns"
            ],
            "Understanding string comparison is critical in Java:\n- The `==` operator tests **reference equality**: whether both variables point to the exact same memory address in heap/pool.\n- The `.equals(Object obj)` method tests **logical content equality**: whether both strings contain the exact same sequence of characters.\nTo avoid `NullPointerException`, invoke `.equals()` from a known non-null literal (e.g. `\"ADMIN\".equals(role)` instead of `role.equals(\"ADMIN\")`).",
            "// Wrong: str1 == str2 (checks memory address!)\n// Right: str1.equals(str2) (checks character contents)\n// Safe: \"CONSTANT\".equals(variable)",
            "public class StringComparisonDemo {\n    public static void main(String[] args) {\n        String literal1 = \"LearnHub\";\n        String literal2 = \"LearnHub\"; // Reuses object from String Pool\n        String objectString = new String(\"LearnHub\"); // Forced new heap object\n        \n        System.out.println(\"literal1 == literal2: \" + (literal1 == literal2)); // true (same pool object)\n        System.out.println(\"literal1 == objectString: \" + (literal1 == objectString)); // false (distinct addresses)\n        System.out.println(\"literal1.equals(objectString): \" + literal1.equals(objectString)); // true (same content)\n        \n        // Case-insensitive\n        System.out.println(\"IgnoreCase check: \" + literal1.equalsIgnoreCase(\"learnhub\"));\n    }\n}",
            "literal1 == literal2: true\nliteral1 == objectString: false\nliteral1.equals(objectString): true\nIgnoreCase check: true",
            [
                "literal1 and literal2 share the same pooled instance, so == evaluates to true.",
                "objectString is explicitly allocated as a new heap instance, so == returns false.",
                ".equals() compares characters and returns true for both."
            ],
            [
                "Using `==` to compare user input strings or database results, leading to erratic false negatives.",
                "Calling `str.equals(\"value\")` when `str` is null, causing `NullPointerException`."
            ],
            [
                ("What does String.intern() do?", "Explain adding a string to the String Constant Pool or returning its pooled reference."),
                ("How does compareTo() differ from equals()?", "Explain lexicographical ordering returning negative, zero, or positive integer."),
                ("Why is `\"ADMIN\".equals(role)` considered a safer coding idiom than `role.equals(\"ADMIN\")`?", "Explain null-safety without extra conditionals.")
            ]
        ),
        format_lesson(
            "java",
            "StringBuilder", 20,
            [
                "Identify performance degradation from repeated immutable String concatenations",
                "Utilize StringBuilder for high-throughput mutable string manipulation",
                "Apply append, insert, delete, replace, and reverse operations"
            ],
            "Because `String` is immutable, repeatedly appending strings in a loop (using `+` or `+=`) creates thousands of intermediate string objects in memory, resulting in $O(n^2)$ time complexity and excessive Garbage Collection pressure.\n`StringBuilder` represents a **mutable sequence of characters** backed by a dynamically growing internal char array. It provides $O(1)$ amortized append operations without reallocating intermediate objects.",
            "StringBuilder sb = new StringBuilder();\nsb.append(\"Item: \").append(42).append(\"\\n\");\nString result = sb.toString();",
            "public class StringBuilderDemo {\n    public static void main(String[] args) {\n        StringBuilder sb = new StringBuilder(\"Java\");\n        \n        sb.append(\" Programming\");\n        System.out.println(\"Appended: \" + sb);\n        \n        sb.insert(4, \" Masterclass\");\n        System.out.println(\"Inserted: \" + sb);\n        \n        sb.replace(0, 4, \"Modern Java\");\n        System.out.println(\"Replaced: \" + sb);\n        \n        sb.reverse();\n        System.out.println(\"Reversed: \" + sb);\n    }\n}",
            "Appended: Java Programming\nInserted: Java Masterclass Programming\nReplaced: Modern Java Masterclass Programming\nReversed: gnimmargorP ssalcretsaM avaJ nredoM",
            [
                "append() modifies the internal character buffer in-place.",
                "insert() shifts characters to place text at a specific index.",
                "reverse() reverses the character buffer in-place."
            ],
            [
                "Using StringBuffer instead of StringBuilder in single-threaded code; StringBuffer has synchronized methods that introduce unnecessary locking overhead.",
                "Calling `.toString()` inside every iteration of a loop instead of once at the very end."
            ],
            [
                ("What is the primary difference between StringBuilder and StringBuffer?", "Explain thread-safety synchronization overhead."),
                ("What is the default initial character capacity of a new StringBuilder()?", "Identify 16 characters."),
                ("Why is concatenating 10,000 strings with `+` in a loop inefficient?", "Explain generation of $O(n)$ intermediate objects and quadratic runtime.")
            ]
        ),
        format_lesson(
            "java",
            "Command-line arguments", 20,
            [
                "Inspect and parse command-line arguments via String[] args",
                "Convert textual string arguments into typed primitives",
                "Validate argument array length to prevent indexing exceptions"
            ],
            "When a Java program starts, the JVM packages all arguments passed in the terminal into a `String[] args` array passed to the `main` method. Arguments are separated by whitespace unless enclosed in quotes. Before accessing elements, always verify `args.length` to guard against `ArrayIndexOutOfBoundsException`.",
            "// Terminal invocation:\n// java App 1024 production\nint port = Integer.parseInt(args[0]);\nString env = args[1];",
            "public class CommandLineArgsDemo {\n    public static void main(String[] args) {\n        // Simulated args check\n        String[] sampleArgs = {\"--mode=production\", \"--port=8080\"};\n        \n        System.out.println(\"Total arguments provided: \" + sampleArgs.length);\n        for (int i = 0; i < sampleArgs.length; i++) {\n            System.out.println(\"Arg[\" + i + \"]: \" + sampleArgs[i]);\n        }\n    }\n}",
            "Total arguments provided: 2\nArg[0]: --mode=production\nArg[1]: --port=8080",
            [
                "sampleArgs mimics command-line arguments passed to the JVM.",
                "Iterating through sampleArgs inspects flags and option strings."
            ],
            [
                "Accessing `args[0]` without first verifying `if (args.length > 0)`, throwing `ArrayIndexOutOfBoundsException`.",
                "Calling `Integer.parseInt(args[0])` without handling `NumberFormatException` when the user inputs non-numeric characters."
            ],
            [
                ("How do you pass arguments containing spaces on the command line?", "Enclose the argument in double quotes (e.g. \"LearnHub Course\")."),
                ("What exception is thrown if Integer.parseInt() fails to parse an argument?", "Identify NumberFormatException."),
                ("Are command-line arguments in Java 0-indexed or 1-indexed?", "Explain 0-indexed.")
            ]
        ),
        format_lesson(
            "java",
            "Practice problems", 30,
            [
                "Solve classic string and array challenges (Anagrams, Palindromes, Word Frequency)",
                "Implement array rotation and second-largest element discovery in linear time",
                "Apply StringBuilder and array manipulation for clean algorithmic solutions"
            ],
            "This problem set covers essential technical interview challenges on strings and arrays:\n1. Palindrome String: Checking if string reads same forward and backward.\n2. Anagram Check: Verifying if two strings contain identical character counts.\n3. Word Count: Splitting sentences and counting tokens.\n4. Second Largest Element: Finding second maximum value in an array in a single $O(n)$ pass.\n5. Array Rotation: Shifting elements cyclically by $k$ positions.",
            "// Anagram check via character frequency array:\nint[] freq = new int[26];\nfor (char c : s1.toCharArray()) freq[c - 'a']++;\nfor (char c : s2.toCharArray()) freq[c - 'a']--;",
            "import java.util.Arrays;\n\npublic class StringArrayProblemsDemo {\n    public static boolean isAnagram(String s1, String s2) {\n        char[] c1 = s1.replaceAll(\"\\\\s+\", \"\").toLowerCase().toCharArray();\n        char[] c2 = s2.replaceAll(\"\\\\s+\", \"\").toLowerCase().toCharArray();\n        if (c1.length != c2.length) return false;\n        Arrays.sort(c1);\n        Arrays.sort(c2);\n        return Arrays.equals(c1, c2);\n    }\n    \n    public static int findSecondLargest(int[] arr) {\n        int largest = Integer.MIN_VALUE;\n        int second = Integer.MIN_VALUE;\n        for (int num : arr) {\n            if (num > largest) {\n                second = largest;\n                largest = num;\n            } else if (num > second && num != largest) {\n                second = num;\n            }\n        }\n        return second;\n    }\n    \n    public static void main(String[] args) {\n        System.out.println(\"Is 'listen' and 'silent' anagram? \" + isAnagram(\"listen\", \"silent\"));\n        System.out.println(\"Is 'triangle' and 'integral' anagram? \" + isAnagram(\"triangle\", \"integral\"));\n        \n        int[] numbers = {23, 85, 12, 99, 44, 99, 67};\n        System.out.println(\"Second largest in [23, 85, 12, 99, 44, 99, 67]: \" + findSecondLargest(numbers));\n    }\n}",
            "Is 'listen' and 'silent' anagram? true\nIs 'triangle' and 'integral' anagram? true\nSecond largest in [23, 85, 12, 99, 44, 99, 67]: 85",
            [
                "isAnagram strips whitespace, converts to lowercase, sorts char arrays, and checks equality.",
                "findSecondLargest maintains two running pointers, finding 85 in a single O(n) pass while ignoring duplicate maximums (99)."
            ],
            [
                "Sorting an array to find second largest without accounting for duplicate maximum values.",
                "Failing to handle case sensitivity and spaces when comparing anagram strings."
            ],
            [
                ("How can anagrams be detected in O(n) time without sorting?", "Explain character frequency counting using an int[26] or HashMap."),
                ("How do you rotate an array of size N right by K positions in-place?", "Explain three-step reversal algorithm: reverse all, reverse first k, reverse remaining."),
                ("What does findSecondLargest return if all array elements are identical?", "Explain returning Integer.MIN_VALUE or throwing IllegalArgumentException.")
            ]
        )
    ]
    return {
        "title": "Module 3 — Methods, Arrays, and Strings",
        "description": "Break programs into reusable methods and process collections of values.",
        "sequenceOrder": 3,
        "lessons": lessons
    }

def get_java_module_4():
    lessons = [
        format_lesson(
            "java",
            "OOP fundamentals", 20,
            [
                "Explain the four foundational pillars of Object-Oriented Programming",
                "Differentiate state, behavior, and identity in software entities",
                "Evaluate advantages and architectural trade-offs of OOP design"
            ],
            "Object-Oriented Programming (OOP) is a programming paradigm organized around real-world entities modeled as objects. The four core pillars are:\n1. Encapsulation: Bundling data and methods into a single unit while restricting direct access to internal state.\n2. Inheritance: Mechanism where a child class acquires the properties and behaviors of a parent class.\n3. Polymorphism: Ability of an entity to take multiple forms (overloading and overriding).\n4. Abstraction: Hiding internal implementation complexities while exposing an intuitive, clean interface.",
            "// OOP modeling mental map:\n// Class = Blueprint / Schema\n// Object = Concrete Living Instance in Heap Memory",
            "public class OOPPrinciplesDemo {\n    public static void main(String[] args) {\n        System.out.println(\"LearnHub OOP Principles Core Pillars:\");\n        System.out.println(\"1. Encapsulation (Information Hiding)\");\n        System.out.println(\"2. Inheritance (Code Reuse)\");\n        System.out.println(\"3. Polymorphism (Dynamic Dispatch)\");\n        System.out.println(\"4. Abstraction (Interface Separation)\");\n    }\n}",
            "LearnHub OOP Principles Core Pillars:\n1. Encapsulation (Information Hiding)\n2. Inheritance (Code Reuse)\n3. Polymorphism (Dynamic Dispatch)\n4. Abstraction (Interface Separation)",
            [
                "Defines the 4 core pillars foundational to Java enterprise engineering.",
                "Emphasizes decoupled responsibilities and modularity."
            ],
            [
                "Creating overly deep inheritance hierarchies that introduce tight coupling.",
                "Exposing internal mutable class fields publicly, breaking encapsulation."
            ],
            [
                ("Why is Encapsulation often called 'Information Hiding'?", "Explain preventing unauthorized or corrupted state mutations."),
                ("How does Polymorphism simplify enterprise frameworks like Spring?", "Discuss loose coupling and dependency injection."),
                ("What is the difference between Abstraction and Encapsulation?", "Explain hiding complexity vs hiding state.")
            ]
        ),
        format_lesson(
            "java",
            "Classes and objects", 25,
            [
                "Define custom Java classes with instance fields and methods",
                "Instantiate objects in heap memory using the 'new' keyword",
                "Manage object reference variables and understand garbage collection eligibility"
            ],
            "A **Class** is a blueprint from which individual objects are created. An **Object** is a concrete instance of a class holding its own copies of instance variables (state) and having access to instance methods (behavior).\nObjects are instantiated using the `new` keyword, which allocates memory on the heap and returns a reference address stored in a reference variable on the stack.",
            "public class Book {\n    String title;\n    double price;\n    void display() { System.out.println(title + \": $\" + price); }\n}\nBook b = new Book();",
            "public class ClassObjectDemo {\n    static class Student {\n        String name;\n        int enrolledCourses;\n        \n        void enroll() {\n            enrolledCourses++;\n            System.out.println(name + \" enrolled in a course! Total: \" + enrolledCourses);\n        }\n    }\n    \n    public static void main(String[] args) {\n        Student s1 = new Student();\n        s1.name = \"Alex Morgan\";\n        s1.enrolledCourses = 2;\n        \n        Student s2 = new Student();\n        s2.name = \"Sarah Connor\";\n        s2.enrolledCourses = 5;\n        \n        s1.enroll();\n        s2.enroll();\n    }\n}",
            "Alex Morgan enrolled in a course! Total: 3\nSarah Connor enrolled in a course! Total: 6",
            [
                "Two distinct instances of Student are allocated on the heap.",
                "s1 and s2 maintain isolated, independent instance field values.",
                "Invoking enroll() mutates each object's respective state."
            ],
            [
                "Assuming variables hold actual objects; variables hold references (pointers) to objects in heap memory.",
                "Invoking methods on a reference that is null, triggering NullPointerException."
            ],
            [
                ("What happens when an object on the heap no longer has any active references pointing to it?", "Explain eligibility for Garbage Collection."),
                ("What is the difference between a class and an object?", "Explain blueprint vs concrete instance."),
                ("Can multiple reference variables point to the exact same object in heap memory?", "Discuss object aliasing.")
            ]
        ),
        format_lesson(
            "java",
            "Constructors", 25,
            [
                "Implement default, no-argument, and parameterized constructors",
                "Chain constructors within the same class using this()",
                "Understand constructor overloading and automatic compiler defaults"
            ],
            "A **Constructor** is a special method called automatically when an object is instantiated. Key characteristics:\n- It has the exact same name as the enclosing class.\n- It has NO return type (not even void).\n- If no constructor is written, the compiler generates a default no-argument constructor.\n- If YOU write any constructor with parameters, the compiler no longer provides the default no-arg constructor unless explicitly defined.",
            "public class Course {\n    private String title;\n    public Course() { this(\"Untitled\"); } // Constructor chaining\n    public Course(String title) { this.title = title; }\n}",
            "public class ConstructorDemo {\n    static class CourseModule {\n        String title;\n        int lessonCount;\n        \n        // Default constructor\n        CourseModule() {\n            this(\"Core Foundations\", 10); // Constructor chaining\n        }\n        \n        // Parameterized constructor\n        CourseModule(String title, int lessonCount) {\n            this.title = title;\n            this.lessonCount = lessonCount;\n        }\n        \n        void printInfo() {\n            System.out.println(\"Module: '\" + title + \"' contains \" + lessonCount + \" lessons.\");\n        }\n    }\n    \n    public static void main(String[] args) {\n        CourseModule m1 = new CourseModule();\n        CourseModule m2 = new CourseModule(\"Advanced OOP\", 15);\n        \n        m1.printInfo();\n        m2.printInfo();\n    }\n}",
            "Module: 'Core Foundations' contains 10 lessons.\nModule: 'Advanced OOP' contains 15 lessons.",
            [
                "m1 uses the default constructor which chains to the parameterized constructor via this(...).",
                "m2 explicitly initializes title and lessonCount.",
                "printInfo() outputs the initialized state of each instance."
            ],
            [
                "Accidentally adding a return type (e.g. `public void CourseModule()`), which turns the constructor into a regular method and causes confusion.",
                "Placing `this(...)` anywhere other than the very first line of a constructor body (causes compile error)."
            ],
            [
                ("Why does `this(...)` have to be the first statement in a constructor?", "Explain guaranteeing initialization before executing body statements."),
                ("Does a class inherit constructors from its superclass?", "Explain no, constructors are not inherited but invoked via super()."),
                ("What happens if you define a parameterized constructor but still need a no-arg constructor?", "Explain needing to explicitly write the no-arg constructor.")
            ]
        ),
        format_lesson(
            "java",
            "this keyword", 20,
            [
                "Resolve variable shadowing between instance fields and parameter names",
                "Invoke overloaded constructors using this() chaining",
                "Pass the current object reference to collaborating methods"
            ],
            "In Java, `this` is a reference keyword that points directly to the current executing object instance. Primary use cases:\n1. Disambiguation: Distinguishing instance fields from method parameters with the same name (`this.field = field;`).\n2. Constructor Chaining: Calling another constructor in the same class (`this(arg1, arg2);`).\n3. Method Chaining: Returning `this` from setter methods to support fluent builder APIs.",
            "public void setName(String name) {\n    this.name = name; // this.name is the instance field; name is the parameter\n}",
            "public class ThisKeywordDemo {\n    static class LessonProgressTracker {\n        private int completed;\n        private int total;\n        \n        LessonProgressTracker(int completed, int total) {\n            this.completed = completed;\n            this.total = total;\n        }\n        \n        double getPercentage() {\n            return ((double) this.completed / this.total) * 100.0;\n        }\n    }\n    \n    public static void main(String[] args) {\n        LessonProgressTracker tracker = new LessonProgressTracker(12, 16);\n        System.out.printf(\"Current Progress: %.1f%%%n\", tracker.getPercentage());\n    }\n}",
            "Current Progress: 75.0%",
            [
                "The constructor uses `this.completed = completed` to disambiguate the instance field from the incoming argument.",
                "getPercentage calculates progress accurately based on instance state."
            ],
            [
                "Using `this` inside a `static` method (static contexts belong to the class, not an object instance).",
                "Omitting `this.` when field and parameter names match, resulting in assigning a parameter to itself with no effect on the instance field."
            ],
            [
                ("Can the `this` keyword be used in static methods? Why or why not?", "Explain absence of an object instance in static context."),
                ("What is variable shadowing in Java?", "Explain local parameters taking precedence over field names."),
                ("How does returning `this` enable fluent API design?", "Discuss method chaining.")
            ]
        ),
        format_lesson(
            "java",
            "Encapsulation", 25,
            [
                "Protect internal object state by declaring fields private",
                "Implement public getters and setters with validation logic",
                "Ensure domain invariants and prevent invalid object mutations"
            ],
            "Encapsulation is the OOP technique of bundling data (fields) and methods that manipulate that data into a single unit, while restricting direct external access to internal state. Standard pattern:\n- Declare fields as `private`.\n- Expose `public` getter and setter methods.\n- Embed validation rules inside setters (e.g. grade cannot be negative, email must contain '@'). This ensures that no external caller can ever put an object into an invalid or corrupted state.",
            "private int age;\npublic int getAge() { return age; }\npublic void setAge(int age) {\n    if (age < 0) throw new IllegalArgumentException(\"Age cannot be negative\");\n    this.age = age;\n}",
            "public class EncapsulationDemo {\n    static class UserAccount {\n        private String username;\n        private int score;\n        \n        public UserAccount(String username, int score) {\n            this.username = username;\n            setScore(score); // Use setter validation\n        }\n        \n        public String getUsername() { return username; }\n        public int getScore() { return score; }\n        \n        public void setScore(int score) {\n            if (score < 0 || score > 100) {\n                System.out.println(\"Validation Error: Score must be between 0 and 100!\");\n                return;\n            }\n            this.score = score;\n        }\n    }\n    \n    public static void main(String[] args) {\n        UserAccount user = new UserAccount(\"student_alex\", 85);\n        System.out.println(\"User: \" + user.getUsername() + \" | Score: \" + user.getScore());\n        \n        // Attempt invalid update\n        user.setScore(150);\n        System.out.println(\"Score after invalid update: \" + user.getScore());\n    }\n}",
            "User: student_alex | Score: 85\nValidation Error: Score must be between 0 and 100!\nScore after invalid update: 85",
            [
                "Fields username and score are private and inaccessible directly from outside.",
                "setScore rejects 150 because it violates the [0, 100] invariant, preserving state integrity."
            ],
            [
                "Making all fields public for convenience, forfeiting all validation and control.",
                "Writing naive getters that return references to mutable internal objects (e.g. returning mutable Date or Array without defensive copying)."
            ],
            [
                ("How does defensive copying preserve encapsulation when returning mutable fields?", "Explain cloning or copying objects before exposing references."),
                ("What are the advantages of making a class completely immutable?", "Discuss thread safety, simplicity, and hash key stability."),
                ("Why is encapsulation considered foundational to software security?", "Explain preventing unauthorized or corrupted state mutations.")
            ]
        ),
        format_lesson(
            "java",
            "Inheritance", 25,
            [
                "Establish 'is-a' relationships using the extends keyword",
                "Invoke superclass constructors and methods using super",
                "Analyze member visibility and single-inheritance constraints"
            ],
            "Inheritance allows a child class (subclass) to inherit fields and methods from an existing parent class (superclass), promoting code reuse and establishing an **is-a** relationship (e.g. an Instructor **is-a** User). In Java:\n- Classes use the `extends` keyword.\n- Java supports **single inheritance** of classes (a class can only extend one direct superclass) to prevent the 'Diamond Problem'.\n- The `super` keyword invokes superclass constructors (`super(args)`) or overridden methods.",
            "public class Child extends Parent {\n    public Child() {\n        super(); // Invokes parent constructor\n    }\n}",
            "public class InheritanceDemo {\n    static class User {\n        protected String name;\n        protected String email;\n        \n        User(String name, String email) {\n            this.name = name;\n            this.email = email;\n        }\n        \n        void displayRole() {\n            System.out.println(name + \" (\" + email + \") - General User\");\n        }\n    }\n    \n    static class Student extends User {\n        private int enrolledCourses;\n        \n        Student(String name, String email, int enrolledCourses) {\n            super(name, email); // Delegate to superclass\n            this.enrolledCourses = enrolledCourses;\n        }\n        \n        @Override\n        void displayRole() {\n            System.out.println(name + \" - Student [Enrolled in \" + enrolledCourses + \" courses]\");\n        }\n    }\n    \n    public static void main(String[] args) {\n        Student s = new Student(\"Alex Morgan\", \"alex@learnhub.com\", 3);\n        s.displayRole();\n    }\n}",
            "Alex Morgan - Student [Enrolled in 3 courses]",
            [
                "Student extends User, inheriting the name and email fields.",
                "Student's constructor delegates common field initialization to `super(name, email)`.",
                "displayRole() overrides the parent implementation to provide specialized output."
            ],
            [
                "Attempting to extend multiple classes (`class A extends B, C`), which Java strictly disallows.",
                "Forgetting that if a superclass lacks a no-arg constructor, child constructors MUST explicitly call `super(...)` on line 1."
            ],
            [
                ("Why does Java prohibit multiple class inheritance?", "Explain ambiguous state and method resolution (Diamond Problem)."),
                ("What is the ultimate root superclass of every class in Java?", "Identify java.lang.Object."),
                ("What does the super keyword accomplish when used inside a child class?", "Explain calling parent constructors and shadowed methods.")
            ]
        ),
        format_lesson(
            "java",
            "Method overriding", 25,
            [
                "Override superclass methods with identical signatures in subclasses",
                "Apply the @Override annotation to catch compiler signature mismatches",
                "Adhere to overriding rules regarding access modifiers and return types"
            ],
            "Method Overriding occurs when a subclass provides its own specific implementation of a method already defined in its superclass. Overriding rules:\n1. The method name, parameter types, and count MUST be identical to the superclass method.\n2. The return type must be identical or a covariant subtype.\n3. The access modifier cannot be more restrictive than the superclass method (e.g. cannot override a `public` method with `protected` or `private`).\n4. Use the `@Override` annotation: it directs the compiler to verify that an overriding target actually exists in the superclass.",
            "@Override\npublic String toString() {\n    return \"Custom representation\";\n}",
            "public class MethodOverridingDemo {\n    static class NotificationService {\n        void notifyUser(String message) {\n            System.out.println(\"Standard System Alert: \" + message);\n        }\n    }\n    \n    static class EmailNotificationService extends NotificationService {\n        @Override\n        void notifyUser(String message) {\n            System.out.println(\"Dispatched Secure Email: [Subject: Course Update] \" + message);\n        }\n    }\n    \n    public static void main(String[] args) {\n        NotificationService base = new NotificationService();\n        NotificationService email = new EmailNotificationService();\n        \n        base.notifyUser(\"System maintenance scheduled.\");\n        email.notifyUser(\"New Java module published!\");\n    }\n}",
            "Standard System Alert: System maintenance scheduled.\nDispatched Secure Email: [Subject: Course Update] New Java module published!",
            [
                "EmailNotificationService overrides notifyUser with specialized behavior.",
                "When called through the base type reference pointing to an email service, Java's dynamic runtime dispatch invokes the child's method."
            ],
            [
                "Misspelling an overridden method name without using `@Override`, causing the compiler to treat it as a new method instead of overriding.",
                "Attempting to override a method declared with the `final` or `static` modifier."
            ],
            [
                ("Why can static methods not be overridden in Java?", "Explain method hiding at compile-time vs dynamic dispatch at runtime."),
                ("What is covariant return typing in method overriding?", "Explain returning a subtype of the superclass method's return type."),
                ("Why cannot an overriding method reduce visibility (e.g. public to protected)?", "Explain Liskov Substitution Principle and contract violation.")
            ]
        ),
        format_lesson(
            "java",
            "Polymorphism", 25,
            [
                "Leverage subtype polymorphism and dynamic method dispatch",
                "Manage parent references pointing to subclass heap instances",
                "Differentiate compile-time (overloading) from runtime (overriding) polymorphism"
            ],
            "Polymorphism ('many forms') allows objects of different concrete classes to be treated uniformly through a shared parent reference or interface. Key concepts:\n- **Dynamic Method Dispatch**: At runtime, the JVM determines the actual concrete object in the heap and invokes the overridden method of that specific object, regardless of the reference type.\n- Allows building extensible code: new subclasses can be added without modifying existing consumer methods.",
            "Parent ref = new Child(); // Upcasting\nref.action(); // Dispatches Child.action() at runtime",
            "public class PolymorphismDemo {\n    abstract static class CourseItem {\n        abstract void start();\n    }\n    \n    static class VideoLesson extends CourseItem {\n        void start() { System.out.println(\"Streaming high-definition video lesson...\"); }\n    }\n    \n    static class InteractiveQuiz extends CourseItem {\n        void start() { System.out.println(\"Launching interactive quiz evaluation...\"); }\n    }\n    \n    public static void executeItem(CourseItem item) {\n        item.start(); // Dynamic dispatch determines actual method\n    }\n    \n    public static void main(String[] args) {\n        CourseItem[] curriculum = { new VideoLesson(), new InteractiveQuiz() };\n        for (CourseItem item : curriculum) {\n            executeItem(item);\n        }\n    }\n}",
            "Streaming high-definition video lesson...\nLaunching interactive quiz evaluation...",
            [
                "curriculum array holds CourseItem references pointing to distinct concrete instances.",
                "item.start() dispatches the appropriate method dynamically based on the actual object type in the heap."
            ],
            [
                "Attempting to access subclass-specific methods through a parent reference without explicit downcasting.",
                "Unsafe downcasting without using `instanceof` check first, causing `ClassCastException`."
            ],
            [
                ("How does the JVM implement dynamic method dispatch internally?", "Explain virtual method tables (vtable)."),
                ("What is the difference between upcasting and downcasting in Java?", "Explain safe widening to parent vs narrow casting to child."),
                ("How does polymorphism support the Open/Closed Principle (OCP)?", "Explain open for extension, closed for modification.")
            ]
        ),
        format_lesson(
            "java",
            "Abstraction", 25,
            [
                "Define abstract classes and declare abstract methods",
                "Enforce behavioral contracts on concrete subclasses",
                "Balance code sharing in abstract classes with interface contracts"
            ],
            "Abstraction is the process of hiding internal implementation details and exposing only essential functional interfaces to the user. In Java, abstraction is achieved via:\n1. **Abstract Class**: A class declared with the `abstract` keyword that CANNOT be directly instantiated with `new`. It can contain both abstract methods (without bodies) and concrete methods (with bodies, shared state, and constructors).\n2. **Abstract Method**: A method signature ending with a semicolon, forcing every concrete subclass to provide an implementation.",
            "public abstract class PaymentProcessor {\n    public abstract void process(double amount); // Subclasses MUST implement\n    public void logTransaction() { System.out.println(\"Transaction recorded\"); }\n}",
            "public class AbstractionDemo {\n    abstract static class EducationalContent {\n        private String title;\n        \n        EducationalContent(String title) {\n            this.title = title;\n        }\n        \n        public String getTitle() { return title; }\n        \n        // Abstract contract\n        abstract void renderContent();\n    }\n    \n    static class CodingExercise extends EducationalContent {\n        CodingExercise(String title) {\n            super(title);\n        }\n        \n        @Override\n        void renderContent() {\n            System.out.println(\"Rendering Code Editor for: \" + getTitle());\n        }\n    }\n    \n    public static void main(String[] args) {\n        EducationalContent exercise = new CodingExercise(\"Recursion Challenge\");\n        System.out.println(\"Lesson: \" + exercise.getTitle());\n        exercise.renderContent();\n    }\n}",
            "Lesson: Recursion Challenge\nRendering Code Editor for: Recursion Challenge",
            [
                "EducationalContent cannot be instantiated directly; it serves as a common structural template.",
                "CodingExercise fulfills the abstract contract by implementing renderContent()."
            ],
            [
                "Attempting to directly instantiate an abstract class (`new EducationalContent(...)`).",
                "Forgetting to implement all abstract methods in a concrete subclass (subclass must then also be declared abstract)."
            ],
            [
                ("Can an abstract class have constructors if it cannot be instantiated directly?", "Explain constructor chaining for subclass field initialization."),
                ("Can an abstract class contain final methods?", "Explain yes, to provide unmodifiable template logic."),
                ("What is the difference between an abstract class and an interface?", "Compare single inheritance with state vs multiple interface contracts.")
            ]
        ),
        format_lesson(
            "java",
            "Interfaces", 25,
            [
                "Declare and implement Java interfaces as pure behavioral contracts",
                "Implement multiple interfaces in a single class",
                "Utilize default and static methods introduced in modern Java"
            ],
            "An **Interface** in Java is a reference type that specifies a contract of methods that a class must implement. Key features:\n- All declared methods are implicitly `public abstract` (unless default or static).\n- All fields are implicitly `public static final` (constants).\n- A class can implement **multiple interfaces** (`implements InterfaceA, InterfaceB`), providing multiple inheritance of type.\n- Modern Java (8+) supports `default` methods (providing backward-compatible default implementations) and `static` utility methods directly on interfaces.",
            "public interface ProgressTrackable {\n    void markComplete();\n    default void logStatus() { System.out.println(\"Tracking active\"); }\n}",
            "public class InterfaceDemo {\n    interface Printable {\n        void print();\n    }\n    \n    interface Shareable {\n        void share(String recipient);\n        default void verifyPermissions() {\n            System.out.println(\"Public share permissions verified.\");\n        }\n    }\n    \n    static class Certificate implements Printable, Shareable {\n        private String recipient;\n        \n        Certificate(String recipient) { this.recipient = recipient; }\n        \n        @Override\n        public void print() {\n            System.out.println(\"Printing Official Certificate for: \" + recipient);\n        }\n        \n        @Override\n        public void share(String email) {\n            System.out.println(\"Sharing certificate with: \" + email);\n        }\n    }\n    \n    public static void main(String[] args) {\n        Certificate cert = new Certificate(\"Alex Morgan\");\n        cert.print();\n        cert.verifyPermissions();\n        cert.share(\"advisor@university.edu\");\n    }\n}",
            "Printing Official Certificate for: Alex Morgan\nPublic share permissions verified.\nSharing certificate with: advisor@university.edu",
            [
                "Certificate implements both Printable and Shareable interfaces.",
                "cert invokes the default method verifyPermissions() inherited directly from Shareable."
            ],
            [
                "Omitting the `public` modifier when implementing interface methods (methods in interfaces are implicitly public, so reducing visibility causes compiler error).",
                "Attempting to declare instance fields in an interface; all fields are constants (`public static final`)."
            ],
            [
                ("Why did Java 8 introduce default methods into interfaces?", "Explain backward compatibility when adding new methods to existing library interfaces."),
                ("How does Java resolve default method conflicts when a class implements two interfaces with the same default method?", "Explain mandatory subclass override resolution."),
                ("What is a Functional Interface?", "Explain an interface containing exactly one abstract method (Single Abstract Method - SAM).")
            ]
        ),
        format_lesson(
            "java",
            "Access modifiers", 20,
            [
                "Apply public, protected, package-private (default), and private access levels",
                "Analyze accessibility across classes, subclasses, and external packages",
                "Apply the Principle of Least Privilege in software architecture"
            ],
            "Java provides four levels of access control:\n1. `private`: Accessible ONLY within the defining class.\n2. `default` (package-private, no keyword): Accessible ONLY within the same package.\n3. `protected`: Accessible within the same package AND by subclasses in other packages.\n4. `public`: Accessible from any class anywhere across the entire JVM classpath.\nBest practice: follow the **Principle of Least Privilege**—make members private by default, and only widen access when strictly required by design.",
            "public class Service {\n    private int secretKey;\n    int packageCounter;\n    protected void audit() {}\n    public void execute() {}\n}",
            "public class AccessModifiersDemo {\n    public static class Model {\n        private String privateId = \"PRIV_123\";\n        String defaultTitle = \"Package Default Title\";\n        protected int protectedLevel = 2;\n        public boolean isPublic = true;\n        \n        public void display() {\n            System.out.println(\"Private ID: \" + privateId);\n            System.out.println(\"Default Title: \" + defaultTitle);\n            System.out.println(\"Protected Level: \" + protectedLevel);\n            System.out.println(\"Is Public: \" + isPublic);\n        }\n    }\n    \n    public static void main(String[] args) {\n        Model m = new Model();\n        m.display();\n    }\n}",
            "Private ID: PRIV_123\nDefault Title: Package Default Title\nProtected Level: 2\nIs Public: true",
            [
                "Demonstrates the 4 distinct visibility tiers available in Java.",
                "Access is verified by the compiler based on class and package boundary contexts."
            ],
            [
                "Assuming package-private (no keyword) is identical to protected (protected allows access to subclasses in foreign packages).",
                "Declaring mutable instance variables public in enterprise entities."
            ],
            [
                ("Can a top-level class be declared private or protected in Java?", "Explain no, only public or package-private are permitted for top-level classes."),
                ("What visibility does a member have when no access modifier keyword is written?", "Identify package-private."),
                ("Why should getters return defensive copies of mutable private fields?", "Explain preventing indirect modification of encapsulated state.")
            ]
        ),
        format_lesson(
            "java",
            "static and final", 25,
            [
                "Manage class-level memory using the static keyword for fields and methods",
                "Apply the final keyword to variables, methods, and classes",
                "Understand static initialization blocks and constant definitions"
            ],
            "The `static` and `final` modifiers control lifecycle, ownership, and mutability:\n- `static`: Belongs to the **class itself**, not individual object instances. A single copy of a static variable is shared among all instances. Static methods can be invoked directly on the class (`ClassName.method()`) without instantiating objects.\n- `final`:\n  - On variables: Value cannot be reassigned (immutable constant).\n  - On methods: Method cannot be overridden by subclasses.\n  - On classes: Class cannot be extended (e.g. `java.lang.String` is final for security).",
            "public static final double PI = 3.14159265359;\npublic final void lockLogic() { ... }\npublic final class ImmutableHolder { ... }",
            "public class StaticFinalDemo {\n    static class StudentEnrollmentTracker {\n        // Static class-level counter\n        private static int totalGlobalEnrollments = 0;\n        \n        // Final instance constant\n        private final int enrollmentId;\n        private final String studentName;\n        \n        public StudentEnrollmentTracker(String studentName) {\n            this.studentName = studentName;\n            totalGlobalEnrollments++; // Shared increment\n            this.enrollmentId = totalGlobalEnrollments;\n        }\n        \n        public static int getTotalEnrollments() {\n            return totalGlobalEnrollments;\n        }\n        \n        public void printBadge() {\n            System.out.println(\"Enrollment #\" + enrollmentId + \" - Student: \" + studentName);\n        }\n    }\n    \n    public static void main(String[] args) {\n        StudentEnrollmentTracker s1 = new StudentEnrollmentTracker(\"Alex\");\n        StudentEnrollmentTracker s2 = new StudentEnrollmentTracker(\"Sarah\");\n        StudentEnrollmentTracker s3 = new StudentEnrollmentTracker(\"David\");\n        \n        s1.printBadge();\n        s2.printBadge();\n        s3.printBadge();\n        System.out.println(\"Total System Enrollments: \" + StudentEnrollmentTracker.getTotalEnrollments());\n    }\n}",
            "Enrollment #1 - Student: Alex\nEnrollment #2 - Student: Sarah\nEnrollment #3 - Student: David\nTotal System Enrollments: 3",
            [
                "totalGlobalEnrollments is static; incrementing it accumulates across all 3 student objects.",
                "enrollmentId is final and bound once per instance during construction.",
                "Static method getTotalEnrollments() is called cleanly via the class name."
            ],
            [
                "Attempting to reference instance variables or `this` from inside a static method.",
                "Reassigning a final variable after it has already received its initial assignment."
            ],
            [
                ("Why is java.lang.String declared as a final class in the JDK?", "Explain security, thread safety, and immutability guarantees."),
                ("What is a static initialization block and when does it execute?", "Explain execution once when the class is first loaded by the ClassLoader."),
                ("Can an abstract class be declared final? Why or why not?", "Explain mutual contradiction: abstract requires subclassing, final forbids it.")
            ]
        ),
        format_lesson(
            "java",
            "Composition and association", 25,
            [
                "Model 'has-a' object associations instead of deep inheritance",
                "Design collaborating classes with clear separation of concerns",
                "Apply the 'Favor Composition Over Inheritance' design principle"
            ],
            "Composition and Association describe relationships where one class **contains or uses** another class ('has-a' relationship), rather than inheriting from it ('is-a' relationship).\n- **Association**: General structural relationship where objects interact (e.g. Course uses Instructor).\n- **Composition**: Strong ownership relationship where the child object's lifecycle depends strictly on the parent (e.g. Course owns Modules).\nDesign principle: **'Favor composition over inheritance'** because composition provides loose coupling, dynamic runtime swapping of components, and avoids rigid inheritance hierarchies.",
            "public class Course {\n    private List<Module> modules = new ArrayList<>(); // Composition (has-a)\n}",
            "import java.util.ArrayList;\nimport java.util.List;\n\npublic class CompositionDemo {\n    static class Instructor {\n        private String name;\n        Instructor(String name) { this.name = name; }\n        String getName() { return name; }\n    }\n    \n    static class Course {\n        private String title;\n        private Instructor instructor; // Association (has-a)\n        private List<String> modules = new ArrayList<>(); // Composition (has-a)\n        \n        Course(String title, Instructor instructor) {\n            this.title = title;\n            this.instructor = instructor;\n        }\n        \n        void addModule(String moduleTitle) {\n            modules.add(moduleTitle);\n        }\n        \n        void printOverview() {\n            System.out.println(\"Course: '\" + title + \"' | Faculty: \" + instructor.getName());\n            System.out.println(\"Modules: \" + modules);\n        }\n    }\n    \n    public static void main(String[] args) {\n        Instructor lead = new Instructor(\"Sarah Connor\");\n        Course javaCourse = new Course(\"Java Masterclass\", lead);\n        javaCourse.addModule(\"M1: Intro\");\n        javaCourse.addModule(\"M2: Control Flow\");\n        \n        javaCourse.printOverview();\n    }\n}",
            "Course: 'Java Masterclass' | Faculty: Sarah Connor\nModules: [M1: Intro, M2: Control Flow]",
            [
                "Course has-an Instructor and has-a list of modules.",
                "Demonstrates loose coupling where Instructor can exist independently while Course manages modules."
            ],
            [
                "Using inheritance just to reuse a few utility methods (e.g. extending ArrayList instead of wrapping it).",
                "Creating circular bidirectional associations that lead to infinite recursion during serialization or printing."
            ],
            [
                ("What is the difference between Aggregation and Composition?", "Explain lifecycle dependency: in composition, child dies with parent; in aggregation, child survives independently."),
                ("Why does the Gang of Four advocate 'Favor composition over inheritance'?", "Explain runtime flexibility and avoiding fragile base class problems."),
                ("How does dependency injection rely on composition?", "Discuss injecting collaborating service instances via constructors.")
            ]
        ),
        format_lesson(
            "java",
            "Packages", 20,
            [
                "Organize source code into logical hierarchical namespaces",
                "Adhere to reverse domain name package conventions (com.learnhub)",
                "Import classes and understand single-type vs wildcard imports"
            ],
            "A **Package** is a namespace that groups related classes, interfaces, and sub-packages. Packages serve two purposes:\n1. Preventing naming collisions: Multiple classes named `User` can coexist in different packages (e.g. `com.learnhub.model.User` vs `org.security.User`).\n2. Enforcing modular access control: Package-private members are encapsulated within their enclosing package.\nConventions dictate lowercase reverse domain naming (e.g. `com.learnhub.service`). The directory structure on disk must strictly mirror the package declaration.",
            "package com.learnhub.service;\n\nimport com.learnhub.entity.Course;\nimport java.util.List;",
            "public class PackagesDemo {\n    public static void main(String[] args) {\n        // Package namespacing demonstration\n        String simulatedPackage = \"com.learnhub.curriculum\";\n        String fullQualifiedName = simulatedPackage + \".CourseManager\";\n        \n        System.out.println(\"Package Namespace: \" + simulatedPackage);\n        System.out.println(\"Fully Qualified Class Name: \" + fullQualifiedName);\n        System.out.println(\"Physical Disk Path: com/learnhub/curriculum/CourseManager.java\");\n    }\n}",
            "Package Namespace: com.learnhub.curriculum\nFully Qualified Class Name: com.learnhub.curriculum.CourseManager\nPhysical Disk Path: com/learnhub/curriculum/CourseManager.java",
            [
                "Illustrates Java package declaration matching directory structure.",
                "Highlights fully qualified names used by the ClassLoader."
            ],
            [
                "Mismatch between the declared package statement and the folder path on disk (javac fails).",
                "Using wildcard imports (`import java.util.*`) and encountering ambiguous class collisions (e.g. `java.util.Date` vs `java.sql.Date`)."
            ],
            [
                ("What package is imported automatically into every Java compilation unit?", "Identify java.lang."),
                ("How do you resolve a collision between java.util.Date and java.sql.Date in the same class?", "Use fully qualified class names for one or both."),
                ("Can two public classes with the same name exist in the same package?", "Explain no, file and type name conflict.")
            ]
        ),
        format_lesson(
            "java",
            "OOP mini-project", 35,
            [
                "Architect a multi-class domain model (Bank Account & Ledger System)",
                "Enforce strict encapsulation, validation rules, and business constraints",
                "Implement polymorphism and test transactional operations"
            ],
            "In this mini-project, we architect a complete Bank Account Domain Model integrating all Module 4 concepts: inheritance, abstract methods, encapsulation, validation, and polymorphism.\n- `Account`: Abstract base class holding common state (account number, balance, owner) with encapsulated getters and setters.\n- `SavingsAccount`: Adds interest accrual.\n- `CheckingAccount`: Adds overdraft limit protection.\n- Polymorphic transaction processing ensuring non-negative balances.",
            "public abstract class Account {\n    // Encapsulated state, validation, deposit, withdraw\n}",
            "public class OOPMiniProjectDemo {\n    abstract static class Account {\n        private final String accountNumber;\n        private final String ownerName;\n        protected double balance;\n        \n        public Account(String accountNumber, String ownerName, double initialBalance) {\n            if (initialBalance < 0) throw new IllegalArgumentException(\"Initial balance cannot be negative\");\n            this.accountNumber = accountNumber;\n            this.ownerName = ownerName;\n            this.balance = initialBalance;\n        }\n        \n        public double getBalance() { return balance; }\n        public String getAccountNumber() { return accountNumber; }\n        public String getOwnerName() { return ownerName; }\n        \n        public void deposit(double amount) {\n            if (amount <= 0) throw new IllegalArgumentException(\"Deposit must be positive\");\n            this.balance += amount;\n            System.out.printf(\"[%s] Deposited: $%.2f | New Balance: $%.2f%n\", accountNumber, amount, balance);\n        }\n        \n        public abstract boolean withdraw(double amount);\n    }\n    \n    static class SavingsAccount extends Account {\n        private final double interestRate;\n        \n        public SavingsAccount(String accNo, String owner, double balance, double interestRate) {\n            super(accNo, owner, balance);\n            this.interestRate = interestRate;\n        }\n        \n        @Override\n        public boolean withdraw(double amount) {\n            if (amount > balance) {\n                System.out.printf(\"[%s] Withdrawal failed: Insufficient funds (Bal: $%.2f)%n\", getAccountNumber(), balance);\n                return false;\n            }\n            balance -= amount;\n            System.out.printf(\"[%s] Withdrew: $%.2f | Balance: $%.2f%n\", getAccountNumber(), amount, balance);\n            return true;\n        }\n    }\n    \n    public static void main(String[] args) {\n        Account savings = new SavingsAccount(\"SA-9012\", \"Alex Morgan\", 500.0, 0.03);\n        savings.deposit(150.0);\n        savings.withdraw(400.0);\n        savings.withdraw(300.0); // Should fail\n    }\n}",
            "[SA-9012] Deposited: $150.00 | New Balance: $650.00\n[SA-9012] Withdrew: $400.00 | Balance: $250.00\n[SA-9012] Withdrawal failed: Insufficient funds (Bal: $250.00)",
            [
                "Account encapsulates state with read-only fields and validated operations.",
                "SavingsAccount implements the abstract withdraw() contract with boundary checks.",
                "Demonstrates enterprise-grade transactional logic and domain modeling."
            ],
            [
                "Failing to validate negative withdrawal or deposit amounts.",
                "Directly modifying the balance field from outside classes without going through deposit/withdraw logic."
            ],
            [
                ("How would you add a CheckingAccount with a $500 overdraft limit to this design?", "Extend Account and allow balance to drop to -500 in withdraw()."),
                ("Why is accountNumber declared final in the Account class?", "Ensure immutable unique identity for financial ledgers."),
                ("How does using an abstract Account superclass allow batch processing across hundreds of mixed accounts?", "Polymorphic iteration over an Account[] or List<Account>.")
            ]
        )
    ]
    return {
        "title": "Module 4 — Object-Oriented Programming",
        "description": "Design reusable programs with classes, objects, and clear responsibilities.",
        "sequenceOrder": 4,
        "lessons": lessons
    }

print("Java modules 3 & 4 ready.")
