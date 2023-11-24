#Calling graphics.py
from graphics import *

#initializing variables
option=""
progress=0
module_trailer=0
module_retriever=0
exclude=0
pass_mark=0
defer_mark=0
fail_mark=0
total_marks=0

def draw_histogram():
    height_1=0
    height_2=0
    height_3=0
    height_4=0

    # Create a graphics window.
    win = GraphWin("Histogram", 400, 300)

    # Window
    label = Text(Point(80, 24), 'Histogram Results')
    label.draw(win)

    #creating the 1st column
    height_1=280-(progress*10)
    label = Text(Point(60, (height_1-15)), progress)
    box = Rectangle(Point(24, 280), Point(96, height_1)) # Height is 14 * 10 = (280 - 140) = 140
    box.setFill("blue")
    box.draw(win)
    label.draw(win)

    #creating 2nd column
    height_2=280-(module_trailer*10)
    label = Text(Point(145, (height_2-15)), module_trailer)
    box = Rectangle(Point(106, 280), Point(178, height_2)) # Height is 10 * 10 = 100
    box.setFill("red")
    box.draw(win)
    label.draw(win)

    #creating 3rd column
    height_3=280-(module_retriever*10)
    label = Text(Point(230, (height_3-15)), module_retriever)
    box = Rectangle(Point(188, 280), Point(260, height_3)) # Height is 7 * 10 = 70
    box.setFill("green")
    box.draw(win)
    label.draw(win)

    #creating 4th column
    height_4=280-(exclude*10)
    label = Text(Point(310, (height_4-15)), exclude)
    box = Rectangle(Point(270, 280), Point(342, height_4)) # Height is 2 * 10 = 20
    box.setFill("pink")
    box.draw(win)
    label.draw(win)

    #naming the  columns
    label = Text(Point(60, 290), "Progress")
    label.draw(win)
    label = Text(Point(145, 290), "Trailer")
    label.draw(win)
    label = Text(Point(230, 290), "Retriever")
    label.draw(win)
    label = Text(Point(310, 290), "exclude")
    label.draw(win)

    win.getMouse()
    win.close()

def get_valid_mark(marks):
    while True:
        try:
            mark = int(input(marks))
            if mark in range(0, 121, 20):
                return mark
            else:
                print("Out of Range")
        except ValueError:
            print("Error: Enter a valid integer.")

while True:
    option=input("Enter 'y' to run the program & 'q' to quit : ")
    if option == "y":
        pass_mark = get_valid_mark("Enter Pass Mark: ")
        defer_mark = get_valid_mark("Enter Defer Mark: ")
        fail_mark = get_valid_mark("Enter Fail Mark: ") 

        total_marks=pass_mark+defer_mark+fail_mark

        if total_marks != 120:
            print("out of range")

        elif pass_mark == 120:
            print("Progress")
            progress += 1

        elif pass_mark == 100:
            print("Progress (module trailer) ")
            module_trailer += 1

        elif fail_mark>=80 and fail_mark<=120:
            print("Exclude")
            exclude += 1

        else:
            print("Do not progress - module retriever")
            module_retriever += 1

        outcome = progress+module_trailer+module_retriever+exclude

    elif option == "q":
        print("Program was terminated")
        break
    else:
        print("Invalid Input \n")


draw_histogram()

