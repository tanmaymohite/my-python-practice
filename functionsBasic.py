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


myHeader(creationDate="29/08/2021", topic= "Function introduction", authorName= "")