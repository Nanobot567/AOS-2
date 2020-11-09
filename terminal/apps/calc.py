print("welcome to calculator, the simple calculator. for help, type 'calhelp'.")
cmd = ""
while cmd != "esc":
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    numcount = 0
    ans = 0

    cmd = input("AOST/calc/: ")
    if cmd == "calhelp":
        print("showing all available commands:")
        print("\nadd ", "subtract ", "multiply ", "divide \n")
        while cmd != "esc":
            cmd = input("AOST/calc/help/: ")
            if cmd == "add":
                print("the add command lets you add two to four numbers.")
            if cmd == "subtract":
                print("the subtract command lets you subtract two to four numbers.")
            if cmd == "multiply":
                print("the multiply command allows you to multiply two to four numbers.")
            if cmd == "divide":
                print("the divide command divides two to four numbers.")
    if cmd == "add":
        while cmd != "get sum":
            int(num1)
            int(num2)
            int(num3)
            int(num4)
            cmd = input("Add a number, or get sum? ")
            if cmd == "add":
                int(num1)
                int(num2)
                int(num3)
                int(num4)
                numcount = numcount + 1
                if numcount == 1:
                    num1 = input("Number 1: ")
                if numcount == 2:
                    num2 = input("Number 2: ")
                if numcount == 3:
                    num3 = input("Number 3: ")
                if numcount == 4:
                    num4 = input("Number 4: ")
                if numcount >= 4:
                    print("Sorry, but you can't add more numbers.")
        int(num1)
        int(num2)
        int(num3)
        int(num4)
        if numcount == 1:
            ans = num1
            print("\n")
            print("The sum is... \n")
            print(ans)
            print("\n")
        if numcount == 2:
            ans = int(num1 + num2)
            print("\n")
            print("The sum is... \n")
            print(ans)
            print("\n")
        if numcount == 3:
            ans = int(num1 + num2 + num3)
            print("\n")
            print("The sum is... \n")
            print(ans)
            print("\n")
        if numcount == 4:
            ans = int(num1 + num2 + num3 + num4)
            print("\n")
            print("The sum is... \n")
            print(ans)
            print("\n")