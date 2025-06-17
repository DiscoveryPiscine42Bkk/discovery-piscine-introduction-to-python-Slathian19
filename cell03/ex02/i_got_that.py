msg = True

while True:
    if msg:
        user = input("What you gotta say? : ")
        msg = False
    else:
        user = input("I got that! Anything else? : ")
    
    if user == "STOP":
        break