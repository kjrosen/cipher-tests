from mimetypes import init

def calculator():
    num1 = input("What's the first number? > ")
    
    try:
        num1 = int(num1)
    except:
        print("Okay wise guy, I'll give it a shot")
    
    fun = input("What are you doing to it? + - * / ")
    if fun != "+" and fun != "-" and fun != "*" and fun != "/":
        fun_type = None
        print("Yeah sure that'll work.")
    else:
        fun_type = 0
    
    num2 = input("What's the second number? > ")
    try:
        num2 = int(num2)
    except:
        print("Funny. Sure.")

    if type(num1) == str or type(num2) == str or fun_type == None:
        return "{} {} {}".format(num1,fun,num2)

    elif fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "/":
        return num1 / num2

print(calculator())