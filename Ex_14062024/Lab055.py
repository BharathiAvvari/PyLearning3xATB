def allowed_to_enter_python_class(name, password):
    if name == "David" and password == "1234":
        print("You are allowed to enter")
    else:
        print("You are not allowed to enter")


allowed_to_enter_python_class("David", "1234")


# another way using match case

def allowed_to_enter_python_class(name, password):
    match (name, password):
        case ("David", "1234"):
            print("David is allowed to enter")
        case ("John", "5678"):
            print("John is allowed to enter")
        case _:
            print("You are not allowed to enter")


allowed_to_enter_python_class("David", "1234")
allowed_to_enter_python_class("John", "5678")
