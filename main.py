from gradebook import GradeBook

def main():
    gradebook = GradeBook()
    filename = 'gradebook.json'
    
    gradebook.load_from_file(filename)
    
    while True:
        print("\n1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            email = input("\nEnter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            gradebook.save_to_file(filename)
            print("\nStudent added successfully.\n")
        
        elif choice == '2':
            name = input("\nEnter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            gradebook.save_to_file(filename)
            print("\nCourse added successfully.\n")
        
        elif choice == '3':
            student_email = input("\nEnter student email: ")
            course_name = input("Enter course name: ")
            score = float(input("Enter course score: "))
            gradebook.register_student_for_course(student_email, course_name, score)
            gradebook.save_to_file(filename)
            print("\nStudent registered for course and GPA calculated successfully.\n")
        
        elif choice == '4':
            gradebook.calculate_ranking()
            print("\nRanking calculated successfully.\n")
            for student in gradebook.student_list:
                print(f"{student.email} - GPA: {student.gpa}")
        
        elif choice == '5':
            min_grade = float(input("\nEnter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            students = gradebook.search_by_grade(min_grade, max_grade)
            print("\nSearch completed. Students within the grade range:\n")
            for student in students:
                print(f">> {student.names} (GPA: {student.gpa})")
        
        elif choice == '6':
            transcripts = gradebook.generate_transcript()
            print("\nTranscripts generated successfully.\n")
            for transcript in transcripts:
                print(f"Transcript for {transcript['names']}:\nGPA: {transcript['gpa']}\n")
        
        elif choice == '7':
            gradebook.save_to_file(filename)
            print("\nExiting the program.\n")
            break

if __name__ == "__main__":
    main()

