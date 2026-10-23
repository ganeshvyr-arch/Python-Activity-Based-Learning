# Student Performance Trend Analysis

subjects = ["English", "Mathematics", "Physics", "Chemistry", "Programming"]

num_exams = int(input("Enter the number of examinations: "))

if num_exams < 2:
    print("Please enter at least 2 examinations.")

else:
    marks = []

    for exam in range(num_exams):
        print("\nEnter marks for Examination", exam + 1)
        exam_marks = []

        for subject in subjects:
            score = float(input("Enter marks in " + subject + ": "))

            if score < 0 or score > 100:
                print("Invalid marks! Marks must be between 0 and 100.")
                raise SystemExit

            exam_marks.append(score)

        marks.append(exam_marks)

    print("\n===== STUDENT PERFORMANCE REPORT =====")

    total_marks = 0
    total_subjects = 0

    for i in range(len(subjects)):
        first_marks = marks[0][i]
        latest_marks = marks[num_exams - 1][i]

        change = latest_marks - first_marks

        print("\nSubject:", subjects[i])
        print("First Examination Marks:", first_marks)
        print("Latest Examination Marks:", latest_marks)

        if change > 0:
            print("Performance: Improved by", round(change, 2), "marks")
        elif change < 0:
            print("Performance: Declined by", round(abs(change), 2), "marks")
        else:
            print("Performance: No change")

        subject_total = 0

        for exam in range(num_exams):
            subject_total += marks[exam][i]

        subject_average = subject_total / num_exams

        print("Average Marks:", round(subject_average, 2))

        if subject_average < 40:
            print("Status: Weak Subject")
        else:
            print("Status: Satisfactory")

        total_marks += subject_total
        total_subjects += num_exams

    overall_average = total_marks / total_subjects

    print("\n===== OVERALL RESULT =====")
    print("Overall Average:", round(overall_average, 2))

    if overall_average >= 75:
        print("Classification: Excellent")
    elif overall_average >= 60:
        print("Classification: Good")
    elif overall_average >= 40:
        print("Classification: Average")
    else:
        print("Classification: Needs Improvement")