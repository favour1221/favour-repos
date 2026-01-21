def add_student(name, score1, score2, score3):
    student = {
        "name": name,
        "scores": [score1, score2, score3]
    }
    return student


def calculate_result(student):
    total = sum(student["scores"])
    average = total / len(student["scores"])
    student["total"] = total
    student["average"] = average
    return student


def display_result(student):
    print("\n--- Student Result ---")
    print("Name:", student["name"])
    print("Scores:", student["scores"])
    print("Total Score:", student["total"])
    print("Average Score:", student["average"])


def main():
    # Student data already defined
    name = "Samuel"
    score1 = 54
    score2 = 48
    score3 = 60

    student = add_student(name, score1, score2, score3)
    student = calculate_result(student)
    display_result(student)


main()