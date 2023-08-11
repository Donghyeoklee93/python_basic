# conditional statement
# executing different commands based on conditions

orgin_pass = "1234"
input_pass = input("Enter password >>>")

if input_pass == orgin_pass:
    print("Succeed to log in")
    print("Welcome")
elif input_pass == "":
    print("No input was provided")
else:
    print("Wrong password")
    print("please check password")
