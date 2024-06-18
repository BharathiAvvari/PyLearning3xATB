# Incase of multiple conditions we use match case in python(just like switch in JAVA)
numbers = int(input("Enter a number\n"))
match numbers:

    case 1:
        print("You have entered One")
    case 2:
        print("You have entered Two")
    case 3:
        print("You have entered Three")
    case _:
        print("Not in the list")

browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("FF code executed!")
    case _:
        print("No browser Found!")
