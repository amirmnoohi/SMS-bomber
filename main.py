from sender import *

phone_number = str(input("Enter Your Phone Number(Without First Zero), eg: 9123456789 : "))
for i in range(len(All)):
    try:
        if All[i][2]:
            resp = All[i][1].send(phone_number)
            print("#" + str(i + 1) + " " + All[i][0] + " : " + resp["message"])
    except:
        print("#" + str(i + 1) + " " + All[i][0] + " : Failed to send SMS - Exception")
