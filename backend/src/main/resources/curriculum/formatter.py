import json

def format_lesson(lang, title, duration, objectives, explanation, syntax, code_example, expected_output, walkthrough, common_mistakes, questions):
    """
    Formats the lesson content markdown according to the 10-point educational template.
    """
    md = []
    
    # 1. Learning Objectives
    md.append("### 🎯 Learning Objectives")
    for obj in objectives:
        md.append(f"- {obj}")
    md.append("")
    
    # 2. Concept Explanation
    md.append("### 📖 Concept Explanation")
    md.append(explanation.strip())
    md.append("")
    
    # 3. Syntax & Key Concepts
    if syntax:
        md.append("### 💻 Syntax & Key Concepts")
        md.append(f"```{lang}\n{syntax.strip()}\n```")
        md.append("")
        
    # 4. Working Example (embedded in markdown as well, and also passed in codeExample field)
    if code_example:
        md.append("### 🚀 Hands-On Working Example")
        md.append(f"```{lang}\n{code_example.strip()}\n```")
        md.append("")
        
    # 5. Expected Output
    if expected_output:
        md.append("**Expected Output:**")
        md.append(f"```text\n{expected_output.strip()}\n```")
        md.append("")
        
    # 6. Step-by-Step Walkthrough
    if walkthrough:
        md.append("### 🔍 Step-by-Step Walkthrough")
        if isinstance(walkthrough, list):
            for i, step in enumerate(walkthrough, 1):
                md.append(f"{i}. {step}")
        else:
            md.append(walkthrough.strip())
        md.append("")
        
    # 7. Common Mistakes & Pitfalls
    if common_mistakes:
        md.append("### ⚠️ Common Mistakes to Avoid")
        for mistake in common_mistakes:
            md.append(f"- {mistake}")
        md.append("")
        
    # 8. Practice Questions & Challenges
    if questions:
        md.append("### 📝 Practice Questions & Challenges")
        for i, q in enumerate(questions, 1):
            if isinstance(q, (tuple, list)):
                md.append(f"{i}. **{q[0]}**\n   *Hint:* {q[1]}")
            else:
                md.append(f"{i}. **{q}**")
        md.append("")
        
    full_content = "\n".join(md)
    
    return {
        "title": title,
        "estimatedDuration": duration,
        "content": full_content,
        "codeExample": code_example.strip() if code_example else ""
    }
