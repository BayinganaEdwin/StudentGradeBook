from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
    
    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
    
    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
    
    def register_student_for_course(self, student_email, course_name, score):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, score)
    
    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()
    
    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.gpa, reverse=True)
    
    def search_by_grade(self, min_grade, max_grade):
        return [s for s in self.student_list if min_grade <= s.gpa <= max_grade]
    
    def generate_transcript(self):
        transcripts = []
        for student in self.student_list:
            transcripts.append({
                'email': student.email,
                'names': student.names,
                'gpa': student.gpa,
                'courses': [{'name': c['course'].name, 'credits': c['credits'], 'score': c['score']} for c in student.courses_registered]
            })
        return transcripts

