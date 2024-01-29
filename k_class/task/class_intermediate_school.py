# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드
class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.student_count = 0
        self.teacher_count = 0

    def print_school(self):
        print(self.name, self.address, self.teacher_count, self.student_count)


# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:
    def __init__(self, name, grade, school, teacher):
        self.name = name
        self.grade = grade
        self.school = school
        self.teacher = teacher
        self.ability = 0
        school.student_count += 1

    def print_student(self):
        print(self.name, self.grade, self.ability)
        self.school.print_school()
        self.teacher.print_teacher()



# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드
class Teacher:
    def __init__(self, name, subject, school):
        self.name = name
        self.subject = subject
        self.school = school
        school.teacher_count += 1


    def print_teacher(self):
        print(self.name, self.subject)
        self.school.print_school()

    def teach_for_student(self, students):
        for student in students:
            student.ability += 1


school = School('코리아IT', '역삼동')
teacher = Teacher('한동석', 'Ai', school)
students = [
    Student('서경덕', 2, school, teacher),
    Student('이기영', 3, school, teacher),
    Student('장상화', 3, school, teacher),
    Student('조성현', 1, school, teacher),
    Student('김훈종', 1, school, teacher)
]

print('=====학교 정보=====')
school.print_school()
print('=====선생님 정보=====')
teacher.print_teacher()
print('=====학생들 정보=====')
for i in range(len(students)):
    students[i].print_student()

teacher.teach_for_student(students)
print('=====학생들 정보=====')
for i in range(len(students)):
    students[i].print_student()

teacher.teach_for_student(students)
print('=====학생들 정보=====')
for i in range(len(students)):
    students[i].print_student()

print('=====학교 정보=====')
school.print_school()

# 강사님 코드
# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드
class School:
    def __init__(self, name, location, student_count=0, teacher_count=0):
        self.name = name
        self.location = location
        self.student_count = student_count
        self.teacher_count = teacher_count

    def print_info(self):
        print(self.name, self.location, self.student_count, self.teacher_count)


# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드
class Teacher:
    def __init__(self, name, subject, school):
        self.name = name
        self.subject = subject
        self.school = school
        self.school.teacher_count += 1

    def print_info(self):
        print(self.name, self.subject)
        self.school.print_info()

    def teach(self, students):
        for student in students:
            student.ability += 1


# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:
    def __init__(self, name, grade, school, teacher, ability=0):
        self.name = name
        self.grade = grade
        self.school = school
        self.teacher = teacher
        self.ability = ability
        self.school.student_count += 1

    def print_info(self):
        print(self.name, self.grade, self.ability)
        self.school.print_info()
        self.teacher.print_info()


school = School('영동고등학교', '서울')
teacher = Teacher('한동석', '컴퓨터', school)
students = [
    Student('홍길동', 1, school, teacher),
    Student('이순신', 1, school, teacher),
    Student('장보고', 2, school, teacher)
]

teacher.teach(students)
for student in students:
    student.print_info()








