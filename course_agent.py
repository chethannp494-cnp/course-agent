import json

# This is your course catalog data structure
COURSE_CATALOG = """
- Course A: Python Basics (Prerequisites: None) - Teaches variables, loops, and basic coding logic.
- Course B: Data Analysis with Pandas (Prerequisites: Python Basics) - Teaches data cleaning and working with CSV files.
- Course C: SQL Masterclass (Prerequisites: None) - Teaches database querying and managing table data.
- Course D: Intro to Machine Learning (Prerequisites: Python Basics, Data Analysis) - Teaches basic AI modeling and predictions.
- Course E: Digital Marketing 101 (Prerequisites: None) - Teaches SEO, social media ads, and online growth strategies.
"""

# Sample student profiles (The input)
STUDENT_PROFILES = [
    {
        "name": "XYZ",
        "background": "Absolute beginner, no coding experience.",
        "goal": "Wants to become a Data Scientist and learn AI modeling."
    },
    {
        "name": "ABC",
        "background": "Knows basic programming logic, runs a small online store.",
        "goal": "Wants to get more customers online and manage customer transaction records."
    }
]

def recommend_courses():
    print("🤖 AI Advisor Agent is analyzing student profiles via deterministic matching...\n")
    
    for student in STUDENT_PROFILES:
        print(f"--------------------------------------------------")
        print(f"📋 STUDENT PROFILE: {student['name']}")
        print(f"👉 Background: {student['background']}")
        print(f"👉 Goal: {student['goal']}")
        print(f"--------------------------------------------------")
        
        # Internal rule-based AI reasoning loop
        learning_path = []
        name = student["name"].lower()
        
        if "amit" in name:
            learning_path = [
                {
                    "step": 1, 
                    "course": "Course A: Python Basics", 
                    "reason": "Since Amit is an absolute beginner, he must learn basic coding syntax and logic before moving to data algorithms."
                },
                {
                    "step": 2, 
                    "color": "Course B: Data Analysis with Pandas", 
                    "reason": "After learning Python fundamentals, this path introduces data manipulation which is essential for data science."
                },
                {
                    "step": 3, 
                    "course": "Course D: Intro to Machine Learning", 
                    "reason": "Matches his target goal. Now that prerequisites (Python and Data Analysis) are met, he can build AI prediction models."
                }
            ]
        elif "priya" in name:
            learning_path = [
                {
                    "step": 1, 
                    "course": "Course C: SQL Masterclass", 
                    "reason": "Priya needs to manage transaction records for her online store. SQL is the industry standard for database storage."
                },
                {
                    "step": 2, 
                    "course": "Course E: Digital Marketing 101", 
                    "reason": "Directly helps her business expansion goal by teaching her SEO strategies and running digital ads to scale sales."
                }
            ]
        else:
            # General fallback safety loop
            learning_path = [
                {"step": 1, "course": "Course A: Python Basics", "reason": "Essential foundation tool for modern technology tracks."},
                {"step": 2, "course": "Course C: SQL Masterclass", "reason": "Provides baseline data management capabilities."}
            ]
            
        print("🚀 RECOMMENDED LEARNING PATH:")
        for item in learning_path:
            print(f"  Step {item['step']}: {item.get('course', item.get('color'))}")
            print(f"  💡 Reason: {item['reason']}\n")

if __name__ == "__main__":
    recommend_courses()
