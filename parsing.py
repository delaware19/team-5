#possible issue if the split string does not exist will not work
#  however, if these are the functions used should not be an issue

#takes in the the string of TEXT_CAPTIONS and will turn it into an array
#  that can be traversed for each of the story "pages" to put the correct
#  text per story "page"
def parseText(textStr):
    textArr = textStr.split(" ### ")
    
    return textArr

#takes in the array of TEXT_CAPTIONS and will turn it into a string that
#  is saved into the database, and is parsed by parseText
def translateText(textArr):
    textStr = ""
    for i in range(len(textArr)):
        textStr += textArr[i] + " ### "
        
    return textStr

#takes in the the string of IMAGE_LIST and will turn it into an array
#  that can be traversed for each of the story "pages" to put the correct
#  image per story "page"
def parseImage(imageStr):
    imageArr = imageStr.split(", ")
    
    return imageArr

#takes in the array of IMAGE_LIST and will turn it into a string that
#  is saved into the database, and is parsed by parseImage
def translateImage(imageArr):
    imageStr = ""
    for i in range(len(imageArr)):
        if i == len(imageArr) - 1:
            imageStr += imageArr[i]
        else:
            imageStr += imageArr[i] + ", "
        
    return imageStr

print(parseText("this is caption 1 ### this is caption 2 ###"))
print(translateText(['this is caption 1', 'this is caption 2']))

print(parseImage("test1, test2"))
print(translateImage(['test1', 'test2']))
