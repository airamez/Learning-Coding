# It is possible to 'raise' exceptions using 'raise' command
# An exception can have mutiple parameters
try:
    raise Exception("Param 1", "Param 2", "Param 3")
except Exception as myException:
    print(type(myException))
    print(myException.args)
    print(myException)

    param1, param2, param3 = myException.args
    print("param 1 =", param1)
    print("param 2 =", param2)
    print("param 3 =", param3)
