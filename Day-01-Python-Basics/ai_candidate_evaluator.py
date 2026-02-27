print("=== AI Candidate Evaluator ===")
name= input("Enter your name: ")
age= int((input("Enter your age: ")))
python_skill = int(input("Rate your Python Skill (1-10): "))

print("\n--- Candidate Summary---")
print("Name:",name)
print("Age:" , age)
print("Python Skill:", python_skill)

if age>=18 and python_skill >=5:
    print("Status: Eligible for AI Internship")
else:
    print("Status: Not Eligible Yet")

# Skill Level Classification
if python_skill >= 8:
    print("Level: High Potential Candidate")
elif 3 <= python_skill <= 5:
    print("Level: Beginner Level")
elif python_skill < 3:
    print("Level: Needs Serious Preparation")
else:
    print("Level: Intermediate Learner")



