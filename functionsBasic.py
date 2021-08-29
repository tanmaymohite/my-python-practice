# Function definition
def line():
    print("*********************************************")

def myHeader(authorName, topic, creationDate):
    line()
    print("     Welcome to Python world")
    print("Program: " + topic)
    print("Author : " + authorName)
    print("Date   : " + creationDate)
    line()
    print("")

def myFooter():
    print("")
    line()
    print("Thanks for using program, see you next time")
    line()



myHeader(creationDate="29/08/2021", topic= "Function introduction", authorName= "Tanmay Mohite")

print("Function: A function is a reusable statement block")

myFooter()