

subjects = [
    "English",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Programming"
]

applicants = []

num_applicants = int(input("Enter the number of applicants: "))

if num_applicants <= 0:
    print("Number of applicants must be positive.")

else:
    for i in range(num_applicants):
        print("\n===== Applicant", i + 1, "=====")

        applicant_id = int(input("Enter applicant ID: "))
        name = input("Enter applicant name: ")

        marks = []
        valid = True

        for subject in subjects:
            score = float(input("Enter marks in " + subject + ": "))

            if score < 0 or score > 100:
                print("Invalid marks! Marks must be between 0 and 100.")
                valid = False
                break

            marks.append(score)

        if not valid:
            print("Applicant record rejected due to invalid marks.")
            continue

        total = sum(marks)
        percentage = total / len(subjects)

        mathematics_marks = marks[1]


        subject_eligible = True

        for score in marks:
            if score < 40:
                subject_eligible = False
                break

        if (
            subject_eligible
            and percentage >= 60
            and mathematics_marks >= 60
        ):
            status = "Eligible"
        else:
            status = "Not Eligible"

        applicant = [
            applicant_id,
            name,
            marks,
            total,
            percentage,
            mathematics_marks,
            status
        ]

        applicants.append(applicant)

    eligible_applicants = []

    for applicant in applicants:
        if applicant[6] == "Eligible":
            eligible_applicants.append(applicant)


    eligible_applicants.sort(
        key=lambda applicant: (
            -applicant[4],
            -applicant[5],
            applicant[0]
        )
    )

    print("\n========== ADMISSION RESULTS ==========")

    for applicant in applicants:
        print("\nApplicant ID:", applicant[0])
        print("Name:", applicant[1])
        print("Total Marks:", applicant[3], "/ 500")
        print("Aggregate Percentage:", round(applicant[4], 2), "%")
        print("Mathematics Marks:", applicant[5])
        print("Admission Status:", applicant[6])

    print("\n========== FINAL RANKED LIST ==========")

    if len(eligible_applicants) == 0:
        print("No eligible applicants found.")

    else:
        print("Rank | ID | Name | Percentage | Maths Marks")

        rank = 1

        for applicant in eligible_applicants:
            print(
                rank, "|",
                applicant[0], "|",
                applicant[1], "|",
                round(applicant[4], 2), "% |",
                applicant[5]
            )

            rank += 1

    print("\nTotal Applicants:", len(applicants))
    print("Eligible Applicants:", len(eligible_applicants))
    print(
        "Not Eligible Applicants:",
        len(applicants) - len(eligible_applicants)
    )
