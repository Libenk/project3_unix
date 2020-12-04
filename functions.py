
import os, sys
import pathlib

import time
import subprocess
import time
from datetime import datetime
def main():
    #welcome screen
    os.system('clear') 
    print("Thank you for using our advisor tool")
    stamp = datetime.now()
    print(stamp)
    # #prompting user for full name
    # Full_name = input("please enter your full name:\n")
    # os.system('clear')

    # input id number
    id_num = input("please enter your VT student id:\n")
    os.system('clear')
    # simulate= input("choose a service\nA:Get student Report\nB:Simulate GPA\n")
    # os.system('clear')


    di = open("C:/Users/liben/Desktop/" + "results" + ".html", 'w')
    f = open("DATABASE.txt", "r")
    lines = f.readlines()
    s = True
    passer=False
    data = {}
    for line in lines:
        if (id_num in line):
            passer=True
            break
    if(passer==True):
        for line in lines:
            if id_num in line:
                s = False
            if s == False and line != "{\n" and line != "}\n":
                b = line.strip("\n")
                b = line.strip(" ")
                c = b.split(':')
                data[c[0]] = c[1]
            if line == "}\n" and s==False:
                break
        id_num=(data["ID"])
        Full_name=(data['FULL_NAME'])
        E_G_D=(data['GRAD_DATE'])
        hours_taken=(data['CREDITS'])
        class_TAKEN=(data['CLASSES_TAKEN'])
        GPA=(data['GPA'])
        class_rank=(data['CLASS_RANK'])
        Standing=(data['STANDING'])
        major=(data['MAJOR'])
        db=(data['D.O.B'])
        dgpa=(data["D_GPA"])
    else:
        print("ID number doesnt exist in  our database.\nTry again later.")
        return None
    print(str(stamp))
    #clean helper functions
    dent = "<ul><ul><ul><ul><ul><ul><ul>"
    end_dent = "</ul></ul></ul></ul></ul></ul></ul>"

    saveFile = open("C:/Users/liben/Desktop/"+"results" +".html", 'w')
    saveFile.write("<h1>    time stam p      <h1>" + str(stamp))
    saveFile.write("<h1>     Students Advisor Report       <h1>"                              )
    saveFile.write("<h2>Students full name: <h2>"               +dent + Full_name   + end_dent)
    saveFile.write("<h2>Student Id Number:<h2> "                +dent + id_num      + end_dent)
    saveFile.write("<h2>Students D.O.B: <h2>"                   +dent + db       + end_dent)
    saveFile.write("<h2>Students major: <h2>"                   +dent + major       + end_dent)
    saveFile.write("<h2>Expected graduation date: <h2>"         +dent + E_G_D       + end_dent)
    saveFile.write("<h2>Total hours taken:<h2> "                +dent + hours_taken + end_dent)
    saveFile.write("<h2>Students class rank: <h2>"              +dent + class_rank  + end_dent)
    saveFile.write("<h2>Students GPA: <h2>"                     +dent + GPA         + end_dent)
    saveFile.write("<h2>Students Departmental GPA: <h2>"        +dent + dgpa  + end_dent)
    saveFile.write("<h2>Students Standing: <h2>"                +dent + Standing  + end_dent)

    p = subprocess.Popen(["echo", "Form complete, please view saved file\nThank you for using our software"], stdout=subprocess.PIPE)
    out = p.communicate()[0]
    out=out.decode()
    print(out)
    os.system('clear')
    time.sleep(3)
    os.system('clear')

if __name__ == '__main__':
    print('PyCharm')
    main()

