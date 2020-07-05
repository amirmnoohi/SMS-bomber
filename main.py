from sender import *

i = 0
for service in All:
    try:
        if service[2]:
            resp = service[1].send("9162292949")
            print("#" + str(i+1) + " " + service[0] + " : " + resp["message"])
    except:
        print("#" + str(i+1) + " " + service[0] + " : Failed to send SMS - Exception")
    i += 1
