import input_module
import logic_module
import display_module
def main():
    students_name,students_score =input_module.get_student_data()
    student_grade =logic_module.calculate_grade(students_score)
    display_module.display_result(students_name,students_score,student_grade)
main()