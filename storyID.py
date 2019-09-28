#storyID.py
n = "Ryan"
a = 4
g = "Male"

#we need a different key system

#will make the storyID for the database 
def makeStoryID(name, age, gender):
    sID = name + str(age)
    if gender.upper() == "MALE":
        sID += "0"
    elif gender.upper() == "FEMALE":
        sID += "1"
    else:
        sID += "2"
    
    return sID

print(makeStoryID(n, a, g))
