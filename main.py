from sender import *

phone_number = str(input("Enter Your Phone Number(Without First Zero), eg: 9123456789 : "))
number_of_sms = int(input("Number Of SMS, eg: 20 : "))
sent_sms = 0
end = False
while number_of_sms:
    for i in range(len(All)):
        resp = All[i][1].send(phone_number)
        if resp["code"] == 200:
            sent_sms += 1
        else:
            print(All[i][0] + " : " + resp["message"])
            print(resp)
            print("========================")
        if sent_sms == number_of_sms:
            print(str(number_of_sms) + " SMS sent successfully")
            end = True
            exit(0)
