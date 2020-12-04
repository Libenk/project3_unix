import os, sys, pathlib, time, subprocess
from datetime import datetime

def main():
    #welcome screen
    os.system('clear')
    hello = subprocess.Popen(['echo', 'Thank you for using our advisor tool design for our Unix class'], stdout=subprocess.PIPE)
    time.sleep(1)
    hello_out = hello.communicate()[0]
    hello_out=hello_out.decode()
    print(hello_out)
    
    # maybe we dont need to print this to screen but just in our output file??? doesnt matter to me though
    #time stamp
    stamp = datetime.now()
    #print(stamp)

    # input id number
    id_num = input("please enter your VT student id:\n")
    os.system('clear')

    getting_info = subprocess.Popen(['echo', 'Gathering student information, please hold'], stdout=subprocess.PIPE)
    info_out = getting_info.communicate()[0]
    info_out=info_out.decode()
    print(info_out)
    time.sleep(2)
    os.system('clear')
    
    #di = open("/home/big_dave/Desktop" + "results" + ".html", 'w')
    f = open("/home/big_dave/Unix_project_3/project3_unix/DATABASE.txt", "r")
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
        class_TAKEN=(data['CLASSES_TAKEN']) # are we not using this?
        GPA=(data['GPA'])
        class_rank=(data['CLASS_RANK'])
        Standing=(data['STANDING'])
        major=(data['MAJOR'])
        db=(data['D.O.B'])
        dgpa=(data["D_GPA"])
    else:
        null_ = subprocess.Popen(['echo', 'ID number doesnt exist in our database. Please try again later.'], stdout=subprocess.PIPE)
        out_n = null_.communicate()[0]
        out_n=out_n.decode()
        print(out_n)
        return None
   #print(str(stamp))

    #clean helper functions
    dent = "<ul><ul><ul><ul><ul><ul><ul>"
    end_dent = "</ul></ul></ul></ul></ul></ul></ul>"

    saveFile = open("/home/big_dave/Unix_project_3/project3_unix/"+"results_number_2" +".html", 'w')
    
    saveFile.write("<h1>     Students Advisor Report       <h1>"                              )
    saveFile.write("<h2>Students full name: <h2>"               +dent + Full_name   + end_dent)
    saveFile.write("<h2>Student Id Number:<h2> "                +dent + id_num      + end_dent)
    saveFile.write("<h2>Students D.O.B: <h2>"                   +dent + db          + end_dent)
    saveFile.write("<h2>Students major: <h2>"                   +dent + major       + end_dent)
    saveFile.write("<h2>Expected graduation date: <h2>"         +dent + E_G_D       + end_dent)
    saveFile.write("<h2>Total hours taken:<h2> "                +dent + hours_taken + end_dent)
    saveFile.write("<h2>Students class rank: <h2>"              +dent + class_rank  + end_dent)
    saveFile.write("<h2>Students GPA: <h2>"                     +dent + GPA         + end_dent)
    saveFile.write("<h2>Students Departmental GPA: <h2>"        +dent + dgpa        + end_dent)
    saveFile.write("<h2>Students Standing: <h2>"                +dent + Standing    + end_dent)
    saveFile.write("<h2>    time stamp:    <h2>"                +dent + str(stamp)  + end_dent)

    p = subprocess.Popen(['echo', 'Form complete, please view saved file\nThank you for using our software'], stdout=subprocess.PIPE)
    out = p.communicate()[0]
    out=out.decode()
    print(out)

if __name__ == '__main__':
    main()
