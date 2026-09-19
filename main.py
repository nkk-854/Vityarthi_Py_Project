import json
from pandas import DataFrame

filename = "record.json"

# Load existing records or initialize as a list
try:
    with open(filename, "r") as f:
        record = json.load(f)
        print("Existing file loaded successfully.")
except FileNotFoundError:
    print(f"File '{filename}' not found. Creating a new one...")
    record = []

class Student_Grade_Management_System:
    def __init__(self, name="", uniqueid="", marks=0):
        self.name = name
        self.uniqueid = uniqueid
        self.marks = marks

    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

    def to_add_student_details(self, name, id, marks, grade):
        new_record = {"Name": name, "Unique ID": id, "Marks": marks, "Grade": grade}
        record.append(new_record)
        with open(filename, "w") as f:
            json.dump(record, f, indent=4)
        print("Student added successfully.")

    def to_view_score(self):
        return record

    def to_update_score(self, target_name, new_marks):
        for student in record:
            if student["Name"] == target_name:
                student["Marks"] = new_marks
                student["Grade"] = self.calculate_grade(new_marks)
                with open(filename, "w") as f:
                    json.dump(record, f, indent=4)
                    print("Score updated successfully.")
                break            
        else:
                print("Student not found.")

sms = Student_Grade_Management_System()

while True:
    print("------Welcome------")
    print("1. Add Credentials")
    print("2. View Credentials")
    print("3. Update Credentials")
    print("4. To create CSV File")
    print("5. Exit")

    try:
        Choice = int(input("Choose from the given option [1-4]: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if Choice == 1:
        nam = input("Enter Name: ")
        i = input("Enter Unique ID: ")
        while True:
            try:
                mark = int(input("Enter marks: "))
                if 1 <= mark <= 100:
                        break
                else:
                        print("Invalid marks! Range should be (1-100). Try again.")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        grad = sms.calculate_grade(mark)
        sms.to_add_student_details(nam, i, mark, grad)

    elif Choice == 2:
        scores = sms.to_view_score()
        if not scores:
            print("No records found.")
            break
        else:
            df = DataFrame(scores)
            print("\n----- Student Records Table -----")
            print(df.to_string(index=False))
            break

    elif Choice == 3:
        nam = input("Enter Name of student to update: ")
        while True:
            try:
                mark = int(input("Enter marks: "))
                if 1 <= mark <= 100:
                    break
                else:
                    print("Invalid marks! Range should be (1-100). Try again.")
            except ValueError:
                    print("Invalid input! Please enter an integer.")
        sms.to_update_score(nam, mark)

    elif Choice == 4:
        score=sms.to_view_score()
        df=DataFrame(score)
        df.to_csv("Record CSV.csv",index=False)
        print("File created successfully")
        
    elif Choice == 5:
        print("---Thanks for using---")
        break
    else:
        print("Invalid Input")
