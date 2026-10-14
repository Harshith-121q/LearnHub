import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def verify_curricula():
    res = urllib.request.urlopen('http://localhost:8080/api/courses')
    resp = json.loads(res.read())
    page = resp['data']
    print(f"Total Published Courses: {page.get('totalElements')}")
    for c in page['content']:
        print(f"Course #{c['id']}: {c['title']}")
        print(f"  Category: {c['category']} | Level: {c['difficultyLevel']} | Status: {c['status']}")
        print(f"  Duration: {c['estimatedDuration']} mins | Lessons: {c.get('totalLessonsCount')} | Modules: {c.get('totalModulesCount')}")

    # Inspect Course 1 details (Java)
    res_java = urllib.request.urlopen('http://localhost:8080/api/courses/1')
    c1 = json.loads(res_java.read())['data']
    print(f"\nCourse 1 Detailed Inspection: '{c1['title']}'")
    print(f"  Modules in course: {len(c1['modules'])}")
    total_l_1 = sum(len(m['lessons']) for m in c1['modules'])
    print(f"  Total lessons in course: {total_l_1}")
    first_lesson = c1['modules'][0]['lessons'][0]
    print(f"  Sample Lesson 1: '{first_lesson['title']}' (Duration: {first_lesson['estimatedDuration']}m)")
    print(f"  Sample Content Preview (first 200 chars):\n  {first_lesson['content'][:200]}...")
    if first_lesson.get('codeExample'):
        print(f"  Sample Code Example:\n  {first_lesson['codeExample'][:150]}...")

    # Inspect Course 2 details (Python)
    res_py = urllib.request.urlopen('http://localhost:8080/api/courses/2')
    c2 = json.loads(res_py.read())['data']
    print(f"\nCourse 2 Detailed Inspection: '{c2['title']}'")
    print(f"  Modules in course: {len(c2['modules'])}")
    total_l_2 = sum(len(m['lessons']) for m in c2['modules'])
    print(f"  Total lessons in course: {total_l_2}")
    first_py_lesson = c2['modules'][0]['lessons'][0]
    print(f"  Sample Lesson 1: '{first_py_lesson['title']}' (Duration: {first_py_lesson['estimatedDuration']}m)")
    print(f"  Sample Content Preview (first 200 chars):\n  {first_py_lesson['content'][:200]}...")

if __name__ == '__main__':
    verify_curricula()
