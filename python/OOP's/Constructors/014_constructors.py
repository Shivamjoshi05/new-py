class student:
    def __init__(self,name,subject_marks):
        self.name = name
        self.subject_marks = subject_marks
    def average(self):
        total_marks = 0
        for mark in self.subject_marks.values():
            total_marks += mark if mark >=35 else 0
        return total_marks / len(self.subject_marks)
    
    def failed_subject(self):
        return[subject for subject , mark in self.subject_marks.items() if mark<35]
    
    def display(self):
        print(f"Canditate  name : {self.name}")
        print(f"Canditate Subject wise Marks:")
        for subject, marks in self.subject_marks.items():
            print(f" {subject}:{marks}")
        avg = self.average()
        print(f"Average Marks: {avg:.2f}")
        failed = self.failed_subject()
        if len(failed)==0:
            print("Result: Passed in all subjects ✅")
        elif len(failed)<=2:
            print(f"Result: Failed in {len(failed)} subject(s)  - Subjects:{',  '.join(failed)}")
        else:
            print("Result: Failed in more than 2 subject ")


def get_marks(subjects):
    marks={}
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}:"))
                if 0<=mark<=100:
                    marks[subject]=mark
                    break
                else:
                    print("Please Enter Marks in 0 to 100")
            except ValueError:
                print("Invalid Input")
    return marks

subjects = ["Maths","Phycis","Chemistry","Computer Sci","English"]

student_name = input("Enter Name of Canditate:")
student_marks = get_marks(subjects)
Student = student(student_name,student_marks)
Student.display()