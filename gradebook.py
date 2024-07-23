import json
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
                'names': student.names,
                'gpa': student.gpa,
                'courses': [{'name': c['course'].name, 'credits': c['credits'], 'score': c['score']} for c in student.courses_registered]
            })
        return transcripts
    
    def save_to_file(self, filename):
        data = {
            'students': [
                {
                    'email': student.email,
                    'names': student.names,
                    'courses_registered': [
                        {'course': course['course'].name, 'credits': course['credits'], 'score': course['score']}
                        for course in student.courses_registered
                    ],
                    'gpa': student.gpa
                }
                for student in self.student_list
            ],
            'courses': [
                {'name': course.name, 'trimester': course.trimester, 'credits': course.credits}
                for course in self.course_list
            ]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.student_list = [
                    self._create_student_from_dict(student_data)
                    for student_data in data['students']
                ]
                self.course_list = [
                    Course(course_data['name'], course_data['trimester'], course_data['credits'])
                    for course_data in data['courses']
                ]
        except FileNotFoundError:
            pass
    
    def _create_student_from_dict(self, data):
        student = Student(data['email'], data['names'])
        student.courses_registered = [
            {
                'course': Course(course['course'], 'N/A', course['credits']),
                'credits': course['credits'],
                'score': course['score']
            }
            for course in data['courses_registered']
        ]
        student.calculate_GPA()
        return student

