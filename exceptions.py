print("hello")

try:
    #try to see whether this gives an exception
    import blah
except Exception:
    #if there is an exception throw this message
     print("this requested module does not exist")   
else:
    #if there is no exceptions then execute this code
    print(blah.companyName)


print("world")