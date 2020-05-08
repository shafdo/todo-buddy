
import eel
import os
import subprocess
import time

eel.init('web')

f = open("minidatabase.txt","a")
f.close()
try:
    time.sleep(1)
    subprocess.call("attrib +h minidatabase.txt",shell=True)
except:
    pass

eel.start("index.html", block=False,size=(992, 700))
@eel.expose
def writetofile(imgid,tn,td):
    print(tn,td)

    f = open("minidatabase.txt","a")
    stringtogo = imgid+":"+tn+":"+td+"\n"
    f.write(stringtogo)
    f.close()


@eel.expose
def readfromfile():
    X = open("minidatabase.txt","r")
    res = X.read().splitlines()
    X.close()
    return res



@eel.expose
def updator(tn):
    clear = lambda:os.system("cls")
    clear()

    tnwithI = tn+"[I]"
    tnwithC = tn+"[C]"

    f = open("minidatabase.txt","r")
    res = f.read().splitlines()
    f.close()

    alteredlist = []

    for i in res:
        colonlist = i.split(":")
        print("Colonlist ---> ",colonlist)
        if colonlist[1] == tnwithI:
            colonlist[1] = tnwithC

        back2colon = ":".join(colonlist)
        print("Back2Colon ---> ",back2colon)

        i=back2colon
        alteredlist.append(i)

    f = open("minidatabase.txt","w")

    for i in alteredlist:
        i = i+"\n"
        f.write(i)

    f.close()
            

@eel.expose
def reset():
    try:
        os.remove("minidatabase.txt")
    except:
        pass









while True:
    eel.sleep(10)



