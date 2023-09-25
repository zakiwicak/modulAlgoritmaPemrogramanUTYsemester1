import re
# agar cepat import regular expressions
inputan = input("pass : ")
val = True
while val:
    if (len(inputan) < 6 or len(inputan) > 16):
        break
    elif not re.search("[a-z]", inputan):
        break
    elif not re.search("[A-Z]", inputan):
        break
    elif not re.search("[0-9]", inputan):
        break
    elif not re.search("[$#@]", inputan):
        break
    elif re.search("\s", inputan):
        break
    else:
        print("valid")
        val = False
        break
if val:
    print("tidak valid")
