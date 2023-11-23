option=""
progress=0
module_trailer=0
module_retriever=0
exclude=0
pass_mark=0
defer_mark=0
fail_mark=0
total_marks=0

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
        # Now you can use pass_mark, defer_mark, and fail_mark in your coded
