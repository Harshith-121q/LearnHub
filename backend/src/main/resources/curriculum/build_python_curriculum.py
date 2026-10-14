import json
import os
from python_modules_1_2 import get_python_module_1, get_python_module_2
from python_modules_3_4 import get_python_module_3, get_python_module_4
from python_modules_5_6 import get_python_module_5, get_python_module_6
from python_modules_7_8 import get_python_module_7, get_python_module_8

def main():
    modules = [
        get_python_module_1(),
        get_python_module_2(),
        get_python_module_3(),
        get_python_module_4(),
        get_python_module_5(),
        get_python_module_6(),
        get_python_module_7(),
        get_python_module_8()
    ]
    
    total_lessons = sum(len(m["lessons"]) for m in modules)
    print(f"Python Curriculum Assembly: {len(modules)} modules, {total_lessons} total lessons.")
    
    for idx, m in enumerate(modules, 1):
        print(f"  Module {idx}: {m['title']} -> {len(m['lessons'])} lessons")
        for l_idx, l in enumerate(m["lessons"], 1):
            l["sequenceOrder"] = l_idx
            
    course_data = {
        "title": "Python Programming Masterclass",
        "description": "Learn Python syntax, control flow, built-in data structures, functions, modules, object-oriented programming, exceptions, file processing, APIs, database connectivity, testing, and practical projects.",
        "category": "Programming Languages",
        "difficultyLevel": "BEGINNER",
        "learningObjectives": "Master Python syntax, built-in data collections, modular scripting, object-oriented abstractions, file processing, REST APIs, databases, unit testing, and full software applications.",
        "prerequisites": "No prior programming experience required. Basic computer literacy.",
        "estimatedDuration": 3000, # 50 hours
        "modules": modules
    }
    
    out_path = os.path.join(os.path.dirname(__file__), "python-curriculum.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(course_data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {out_path} ({os.path.getsize(out_path)} bytes).")

if __name__ == "__main__":
    main()
