from gradebook import GradeBook

def main():
    gradebook = GradeBook()
    
    while True:
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
        
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            score = float(input("Enter course score: "))
            gradebook.register_student_for_course(student_email, course_name, score)
        
        elif choice == '4':
            gradebook.calculate_ranking()
            for student in gradebook.student_list:
                print(f"{student.email} - GPA: {student.gpa}")
        
        elif choice == '5':
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            students = gradebook.search_by_grade(min_grade, max_grade)
            for student in students:
                print(f"{student.email} - GPA: {student.gpa}")
        
        elif choice == '6':
            transcripts = gradebook.generate_transcript()
            for transcript in transcripts:
                print(f"Email: {transcript['email']}, Names: {transcript['names']}, GPA: {transcript['gpa']}")
                for course in transcript['courses']:
                    print(f"  Course: {course['name']}, Credits: {course['credits']}, Score: {course['score']}")
        
        elif choice == '7':
            break

if __name__ == "__main__":
    main()

