import json
import os
from java_modules_1_2 import get_java_module_1, get_java_module_2
from java_modules_3_4 import get_java_module_3, get_java_module_4
from java_modules_5_6 import get_java_module_5, get_java_module_6
from java_modules_7_8 import get_java_module_7, get_java_module_8

def main():
    modules = [
        get_java_module_1(),
        get_java_module_2(),
        get_java_module_3(),
        get_java_module_4(),
        get_java_module_5(),
        get_java_module_6(),
        get_java_module_7(),
        get_java_module_8()
    ]
    
    total_lessons = sum(len(m["lessons"]) for m in modules)
    print(f"Java Curriculum Assembly: {len(modules)} modules, {total_lessons} total lessons.")
    
    for idx, m in enumerate(modules, 1):
        print(f"  Module {idx}: {m['title']} -> {len(m['lessons'])} lessons")
        for l_idx, l in enumerate(m["lessons"], 1):
            l["sequenceOrder"] = l_idx
            
    course_data = {
        "title": "Java Programming Masterclass",
        "description": "Learn Java from the first program through control flow, methods, arrays, object-oriented programming, collections, file handling, modern Java features, JDBC, testing, and a final project.",
        "category": "Programming Languages",
        "difficultyLevel": "BEGINNER",
        "learningObjectives": "Master core Java syntax, OOP architecture, collections, exceptions, modern streams, concurrency, JDBC databases, unit testing, and full project development.",
        "prerequisites": "Basic computer literacy and enthusiasm to write code. No prior programming experience required.",
        "estimatedDuration": 3600, # 60 hours
        "modules": modules
    }
    
    out_path = os.path.join(os.path.dirname(__file__), "java-curriculum.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(course_data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {out_path} ({os.path.getsize(out_path)} bytes).")

if __name__ == "__main__":
    main()
