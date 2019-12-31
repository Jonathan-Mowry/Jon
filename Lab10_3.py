#Jon Mowry
import pickle
import os as sys

INSTRUCTOR_FILE = "teachers.dat"

class Instructor:
    def __init__(self):
        self.__wNumber = "w-number"
        self.__name = "name"
        self.__rank = "rank"
        self.__department = "department"
        self.__division = "division"        

    def setW_Number(self, number):
        self.__wNumber = number
    def setName(self, name):
        self.__name = name
    def setRank(self, rank):
        self.__rank = rank
    def setDepartment(self, department):
        self.__department = department
    def setDivision(self, division):
        self.__division = division    

    def getW_Number(self):
        return self.__wNumber
    def getName(self):
        return self.__name
    def getRank(self):
        return self.__rank
    def getDepartment(self):
        return self.__department
    def getDivision(self):
        return self.__division

    def printEverything(self):
        print("{} {:<15} {:<20} {:<20} {:<20} {:<20}".format(self.__wNumber, ":", self.__name, self.__rank, self.__department, self.__division), sep="")

    def __str__(self):
        return "W-Number: " + self.__wNumber + \
        "\nName: " + self.__name + \
        "\nRank: " + self.__rank + \
        "\nDepartment: " + self.__department + \
        "\nDivision: " + self.__division


def main():
    teach_dict = Instructor()
    teachers = unpickleAndRead(INSTRUCTOR_FILE)
    choice = 0
    while choice != 9:    
        choice = menuBuilder()

        if choice == 1:
            viewAllContacts(teachers, teach_dict)
        elif choice == 2:
            viewByRank(teachers, teach_dict)
        elif choice == 3:
            viewByDepartment(teachers, teach_dict)
        elif choice == 4:
            viewByDivision(teachers, teach_dict)
        elif choice == 5:
            viewSingleContact(teachers, teach_dict)
        elif choice == 6:
            addInstructor(teachers, teach_dict)
        elif choice == 7:
            editTeacher(teachers, teach_dict)
        elif choice == 8:
            deleteTeacher(teachers, teach_dict)
        elif choice == 9:
            exitProgram(INSTRUCTOR_FILE, teachers)
        else:
            sys.system("CLS")
            print("Please enter a number 1 through 9.")
            pressEnterToContinue()


def menuBuilder():
    sys.system("CLS")
    print("WSCC Instructor Information System")
    print("----------------------------------")
    print("1) View all instructors\n2) View instructors by rank")
    print("3) View all instructors by department\n4) View an instructor by division")
    print("5) View an instructor\n6) Add an instructor\n7) Edit an instructor")
    print("8) Delete an instructor\n9) Exit program")
    choice = int(input("Please select one of the choices: "))
    return choice

#Choice 1
def viewAllContacts(teachers,teach_dict):
    sys.system("CLS")
    if is_empty(teachers) == False:
        print("All instructors\n")
        w_numberWrite()   
        stringItem = []        
        for key, index in teachers.items():
            keyIndex = key                
            stringItem = splitter(keyIndex, teachers)        
            teach_dict.setW_Number(keyIndex)
            teach_dict.setName(stringItem[0])
            teach_dict.setRank(stringItem[1])
            teach_dict.setDepartment(stringItem[2])
            teach_dict.setDivision(stringItem[3])
            teach_dict.printEverything()
    else:
        print("There are not any instructors!")     
    pressEnterToContinue()


#Choice 2
def viewByRank(teachers, teach_dict):
    rankIsPresent = False
    sys.system("CLS")
    rank = input("Enter the rank you wish to search by: ")
    #if that exists
    w_numberWrite()
    for key, index in teachers.items():
            keyIndex = key                
            stringItem = splitter(keyIndex, teachers)
            if rank in stringItem[1]:
                sendToClassForView(stringItem, keyIndex, teach_dict)
                rankIsPresent = True
    if rankIsPresent == False:
        sys.system("CLS")
        print("There isn't any rank by that name.")    
    pressEnterToContinue()


#Choice 3
def viewByDepartment(teachers, teach_dict):
    departmentIsPresent = False
    sys.system("CLS")
    rank = input("Enter the department you wish to search by: ")
    #if that exists
    w_numberWrite()
    for key, index in teachers.items():
            keyIndex = key                
            stringItem = splitter(keyIndex, teachers)
            if rank in stringItem[2]:
                sendToClassForView(stringItem, keyIndex, teach_dict)
                departmentIsPresent = True
    if departmentIsPresent == False:
        sys.system("CLS")
        print("There isn't any rank by that name.")    
    pressEnterToContinue()


#Choice 4
def viewByDivision(teachers, teach_dict):
    divisionIsPresent = False
    sys.system("CLS")
    rank = input("Enter the division you wish to search by: ")
    #if that exists
    w_numberWrite()
    for key, index in teachers.items():
            keyIndex = key                
            stringItem = splitter(keyIndex, teachers)
            if rank in stringItem[3]:
                sendToClassForView(stringItem, keyIndex, teach_dict)
                divisionIsPresent = True
    if divisionIsPresent == False:
        sys.system("CLS")
        print("There isn't any division by that name.")    
    pressEnterToContinue()


#Choice 5
def viewSingleContact(teachers, teach_dict):
    sys.system("CLS")
    w_number = input("Enter the w-number of the instructor you wish to view: ")
    if w_number in teachers:
        stringItem = []        
        stringItem = splitter(w_number, teachers)        
        teach_dict.setW_Number(w_number)
        teach_dict.setName(stringItem[0])
        teach_dict.setRank(stringItem[1])
        teach_dict.setDepartment(stringItem[2])
        teach_dict.setDivision(stringItem[3])
        print(teach_dict)
    else:
        print("The w-number you have entered does not exist")
    pressEnterToContinue()


#Choice 6
def addInstructor(teachers, teach_dict):
    sys.system("CLS")
    w_number = input("Please enter the instructor's w-number: ")    
    if w_number in teachers:
        print("The w-number you have entered is currently in use please use another w-number.")
    else:
        setAttributes(teachers, teach_dict, w_number)
        print("The instructor was successfully added.")
    pressEnterToContinue()


#Choice 7
def editTeacher(teachers, teach_dict):
    sys.system("CLS")
    w_number = input("Please enter the w-number of the instructor: ")
    if w_number in teachers.keys():
        setAttributes(teachers, teach_dict, w_number)   
        print("Instructor edited!")
    else:
        print("The inputed w-number doesn't correspond to a known instructor")
    pressEnterToContinue()
    

#Choice 8
def deleteTeacher(teachers, teach_dict):
    sys.system("CLS")
    number = input("Enter the w-number of the instructor to be deleted: ")
    if number in teachers.keys():
        del teachers[number]
        print("The instructor has been deleted")
    else:
        print("The inputed w-number doesn't correspond to a known instructor")
    pressEnterToContinue()


#Choice 9
def exitProgram(teacherFile, teacherDictionary):
    pickleAndWrite(teacherFile, teacherDictionary)


def unpickleAndRead(teacherFile):
    instructor = {}
    try:
        inputFile = open(teacherFile, "rb")
        instructor = pickle.load(inputFile)
    except FileNotFoundError:
        print("File not found!")        
    else:
        inputFile.close()    

    return instructor


def pickleAndWrite(teacherFile, teacherDictionary):
    outputFile = open(teacherFile, "wb")
    pickle.dump(teacherDictionary, outputFile)
    outputFile.close()


def w_numberWrite():
    print("W-Number", "{:>20} {:>20} {:>20} {:>20}".format("Name", "Rank", "Department", "Division"), sep="")
    print("--------", "{:>20} {:>20} {:>20} {:>20}".format("----", "----", "----------", "--------"), sep="")


def splitter(keyIndex, teachers):
    item = teachers[keyIndex]
    stringItem = str(item)
    for item in stringItem:            
        stringItem = stringItem.replace("'", "")            
        stringItem = stringItem.replace("(", "")            
        stringItem = stringItem.replace(")", "")       
    stringItem = stringItem.rsplit(",")
    return stringItem


def sendToClassForView(stringItem, keyIndex, teach_dict):
    teach_dict.setW_Number(keyIndex)
    teach_dict.setName(stringItem[0])
    teach_dict.setRank(stringItem[1])
    teach_dict.setDepartment(stringItem[2])
    teach_dict.setDivision(stringItem[3])
    teach_dict.printEverything()


def setAttributes(teachers, teach_dict, w_number):
    teacher = input("Please enter the instructor's name: ")
    rank = input("Please enter the instructor's rank: ")
    department = input("Please enter the instructor's department: ")
    division = input("Please enter the instructor's division: ")
    teach_dict.setW_Number(w_number)
    teach_dict.setName(teacher)
    teach_dict.setRank(rank)
    teach_dict.setDivision(division)
    teach_dict.setDepartment(department)       
    teachers[teach_dict.getW_Number()] = (teach_dict.getName(), teach_dict.getRank(),
        teach_dict.getDepartment(), teach_dict.getDivision())


def is_empty(dictionary):
    if dictionary:        
        return False
    else:        
        return True


def pressEnterToContinue():
    input("Press enter to continue...")


main()
