
# Student Marks Management System

def calculate_average(marks):
    return sum(marks) / len(marks)


def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    name = input("Enter student name: ")

    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark for subject {i + 1}: "))
        marks.append(mark)

    average = calculate_average(marks)
    result = check_result(average)

    print("\n--- Student Report ---")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Result:", result)


if __name__ == "__main__":
    main()
