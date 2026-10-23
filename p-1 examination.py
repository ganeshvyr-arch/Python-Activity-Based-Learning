# Examination Result and Grace-Mark Validation

subjects = ["English", "Mathematics", "Physics",
            "Chemistry", "Programming"]

PASS_MARKS = 40
MAX_MARKS = 100
GRACE_LIMIT = 5

original_marks = []

print("EXAMINATION RESULT SYSTEM")
print("-" * 35)

# Input and validate marks
for subject in subjects:
    marks = int(input("Enter marks in " + subject + ": "))

    if marks < 0 or marks > MAX_MARKS:
        print("Invalid marks! Marks must be between 0 and 100.")
        raise SystemExit

    original_marks.append(marks)

# Copy original marks
final_marks = original_marks.copy()

# Find failed subjects
failed_subjects = []

for i in range(len(final_marks)):
    if final_marks[i] < PASS_MARKS:
        failed_subjects.append(i)

grace_used = 0

# Apply grace-mark policy
if len(failed_subjects) == 1:
    index = failed_subjects[0]
    required_grace = PASS_MARKS - final_marks[index]

    if final_marks[index] >= 35 and required_grace <= GRACE_LIMIT:
        final_marks[index] += required_grace
        grace_used = required_grace

# Calculate total and check subject-wise passing
total = 0
all_passed = True

print("\nFINAL MARKS REPORT")
print("-" * 50)
print("Subject       Original   Grace   Final")

for i in range(len(subjects)):
    grace = final_marks[i] - original_marks[i]

    print(subjects[i], " " * (14 - len(subjects[i])),
          original_marks[i], "      ", grace,
          "     ", final_marks[i])

    total += final_marks[i]

    if final_marks[i] < PASS_MARKS:
        all_passed = False

# Calculate percentage
maximum_total = len(subjects) * MAX_MARKS
percentage = (total / maximum_total) * 100

# Determine classification
if not all_passed:
    classification = "FAIL"
elif percentage >= 75:
    classification = "DISTINCTION"
elif percentage >= 60:
    classification = "FIRST CLASS"
elif percentage >= 50:
    classification = "SECOND CLASS"
else:
    classification = "PASS CLASS"

# Display final result
print("-" * 50)
print("Total Marks:", total, "/", maximum_total)
print("Percentage:", round(percentage, 2), "%")
print("Grace Marks Used:", grace_used)
print("Final Classification:", classification)