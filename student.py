import json # for storing data parmanent
students =[]
def load_data():
    global students
    try:
        with open("students.json","r") as file: # yha file ka extension json esliye h qki json direct list or dict me data store kar leta h or .text extension me hume khud split karna pdta h
           students = json.load(file) 
    except:
        students = []
        
def save_data():
    with open("students.json","w") as file:
        json.dump(students,file)

def add_student():
    name = input("Enter your name")
    roll_num= int(input("Enter your roll number"))
    marks = int(input("Enter yout marks"))
    student = { 
        "name": name ,
        "roll_num": roll_num,
        "marks": marks
          }
    students.append (student)
    save_data()
    print ("Studnt added successfully")
 
def view_student():
        for i in students:
            print(i)

load_data()
while True:
    print("\n 1-- Add Student")
    print("\n2-- View Student")
    print(" 3-- Exit")

    choice = input("Enter your choice")
    if(choice == "1"):
        add_student()
    elif (choice == "2"):
        view_student()
    elif (choice == "3"):
        break
    else:
        print("Invalid choice please enter another choice")


