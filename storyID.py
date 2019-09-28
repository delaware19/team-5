name = "Ryan"
age = 4
gender = "Male"

#we need a different key system
def makeStoryID(n, a, g):
    sID = name + str(age)
    if gender.upper() == "MALE":
        sID += "0"
    elif gender.upper() == "FEMALE":
        sID += "1"
    else:
        sID += "2"
    
    return sID

print(makeStoryID(name, age, gender))
