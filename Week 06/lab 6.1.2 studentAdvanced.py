# Program that allows user to create students, their modules and grades
    # It allows user to see the inputted students and detail
# Copied from lab - need better understanding

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
 # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"])) 

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lamda functions
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu() 
