from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def print_result(title, result):
    print(f"\n=== {title} ===")
    if isinstance(result, list):
        for row in result:
            print(row)
    else:
        print(result)


def main():
    subject_id = 1
    group_id = 1
    student_id = 1
    teacher_id = 1

    print_result("Select 1", select_1())
    print_result("Select 2", select_2(subject_id))
    print_result("Select 3", select_3(subject_id))
    print_result("Select 4", select_4())
    print_result("Select 5", select_5(teacher_id))
    print_result("Select 6", select_6(group_id))
    print_result("Select 7", select_7(group_id, subject_id))
    print_result("Select 8", select_8(teacher_id))
    print_result("Select 9", select_9(student_id))
    print_result("Select 10", select_10(student_id, teacher_id))


if __name__ == "__main__":
    main()
