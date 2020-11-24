class Student:
    school = "Gimnazija Slobodan Skerovic"
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    def correct_name(self):
        while not self.name.isalpha():
            print("Looks like you have made a mistake when adding the name", self.name)
            del self.name
            self.name = input("Please enter a new name of the student: ")
    def can_you_be_a_student(self):
        if self.age < 14:
            print(self.name,"can not be a student, because",self.name,"is too young.")
        else:
            print(self.name,"can be a student. Welcome!")
    def tell_me_about_yourself(self):
        print("Hi! I am", self.name,", and I am a student of",self.school,". I am",self.age,"years old and my GPA is", self.grades )

alex = Student("Alex", 12, 4.0)
alex.tell_me_about_yourself()
bob = Student("Bob", 16, 3.9)
bob.tell_me_about_yourself()

def who_is_a_better_student(student1, student2):
    if student1.grades > student2.grades:
        print(student1.name,"is a better student than",student2.name)
    elif student2.grades > studnet1.grades:
        print(student2.name,"is a better student than",student1.name)
    else:
        print(student1.name,student2.name,"have the same GPA!")
who_is_a_better_student(alex, bob)