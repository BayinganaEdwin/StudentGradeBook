class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.gpa = 0.0
    
    def calculate_GPA(self):
        if self.courses_registered:
            total_credits = sum(course['credits'] for course in self.courses_registered)
            total_points = sum(course['credits'] * course['score'] for course in self.courses_registered)
            self.gpa = total_points / total_credits
        else:
            self.gpa = 0.0
    
    def register_for_course(self, course, score):
        self.courses_registered.append({'course': course, 'credits': course.credits, 'score': score})
        self.calculate_GPA()

