from sender import *

for i in range(len(All)):
    try:
        if All[i][2]:
            resp = All[i][1].send("9162292949")
            print("#" + str(i + 1) + " " + All[i][0] + " : " + resp["message"])
    except:
        print("#" + str(i + 1) + " " + All[i][0] + " : Failed to send SMS - Exception")
