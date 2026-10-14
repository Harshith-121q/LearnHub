import json
import os

def format_lesson_content(lang, title, objectives, explanation, syntax, code_example, expected_output, walkthrough, common_mistakes, questions):
    md = []
    md.append("### 🎯 Learning Objectives")
    for obj in objectives:
        md.append(f"- {obj}")
    md.append("")
    
    md.append("### 📖 Concept Explanation")
    md.append(explanation.strip())
    md.append("")
    
    if syntax:
        md.append("### 💻 Syntax & Core Principles")
        md.append(f"```{lang}\n{syntax.strip()}\n```")
        md.append("")
        
    if code_example:
        md.append("### 🚀 Hands-On Working Example")
        md.append(f"```{lang}\n{code_example.strip()}\n```")
        md.append("")
        
    if expected_output:
        md.append("**Expected Console Output:**")
        md.append(f"```text\n{expected_output.strip()}\n```")
        md.append("")
        
    if walkthrough:
        md.append("### 🔍 Step-by-Step Code Walkthrough")
        if isinstance(walkthrough, list):
            for i, step in enumerate(walkthrough, 1):
                md.append(f"{i}. {step}")
        else:
            md.append(walkthrough.strip())
        md.append("")
        
    if common_mistakes:
        md.append("### ⚠️ Common Mistakes to Avoid")
        for mistake in common_mistakes:
            md.append(f"- {mistake}")
        md.append("")
        
    if questions:
        md.append("### 📝 Practice Exercises & Challenges")
        for i, q in enumerate(questions, 1):
            if isinstance(q, tuple) or isinstance(q, list):
                md.append(f"{i}. **{q[0]}**\n   *Hint:* {q[1]}")
            else:
                md.append(f"{i}. {q}")
        md.append("")
        
    return "\n".join(md)

print("Helper defined.")
