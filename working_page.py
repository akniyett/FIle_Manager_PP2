import os
import fnmatch
import shutil
from os import path
print("Welcome, I am your file manager!")
print("""Let me contact you in your name
Please, write your name ...""")
#file=open('1.txt')
a=str(input()) #user's name
print(a +", remember if you write the name of the wrong director or file, the program redirects you to the start page!") #welcome, user's name

path = os.getcwd() #this program automatically opens ur current location
print("Your current location: "+path)
#obj=os.scandir(path)
#path='\'
#dir_list=os.listdir(path)
#print("Files and directories in", path)
#print(dir_list)
while True:

    print("If you want to work with file press 1")
    print("If you want to work with directory press 2")
    b=int(input())
    if b==1:   #for file in the current location
        obj=os.scandir(path)
        print("Files and directories in ", path)
        for entry in obj:
            if entry.is_file():
                print(entry.name)
        # f=open("1.txt", 'r')
        # f.close()
    #with open("1.txt", 'w+') as file:
    
        print("What do you wanna do with this file? Choose the option")
        print("press 1 to rename the file")
        print("press 2 to add content to this file")
        print("press 3 to rewrite content of this file")
        print("press 4 to return to the parent directory")
        print("press 5 to delete the file")
        action=int(input())
        if action==1:
            print("Write the name of file that you wanna rename")
            # f=open("1.txt", 'r')
            # f.close()
            file_name=str(input())
            expfile=os.path.join(path,file_name+".txt")
            print("Rename the file")
            newname=str(input())
          
            dest=os.path.join(path,newname+".txt")
            os.rename(expfile, dest)
            print("File renamed successfully")
            
        elif action==2:
            print("Write the name of file that you wanna add content")
            file_name=str(input())
            expfile=os.path.join(path,file_name+".txt")
            # f=open("1.txt", 'w')
            f=open(file_name+".txt",'w')
            print("Add content")
            content=str(input())
            f.write(content)
            print("Your content added to this file")
            f.close()
        elif action==3:
            print("Write the name of file that you wanna rewrite")
            file_name=str(input())
            expfile=os.path.join(path,file_name+".txt")
            f=open(file_name+".txt", 'r+')
            lines=f.read()
            f.write(lines)
            f.close()
            print("Type your content")
            f=open(file_name+".txt", 'w')
            qwerty=str(input())
            f.write(qwerty)
            print("Your content added")
            f.close()
        elif action==4:
            print("Write the name of file that you wanna return parent direction")
            file_name=str(input())
            expfile=os.path.join(path,file_name+".txt")
            f=open(file_name+".txt", 'r')
            parent=os.path.dirname(expfile)
            print("Your current direction", expfile)
            print("Your parent direction ", parent)
            parent=expfile
            #print(path)
            f.close()
        elif action==5:
            
            print("Write the name of file that you wanna delete")
            file_name=str(input())
            expfile=os.path.join(path,file_name+".txt")
            os.remove(expfile)
            print("File deleted")

        


    elif b==2:

        mom=os.path.dirname(path)
        print(mom)
        mainpapkas=os.scandir(mom)
        print("Files and directories in ", mom)
        for entry in mainpapkas:
            if entry.is_dir() or entry.is_file():
                print(entry.name)
        
        print("""Press 1 to rename the directory
Press 2 to print number of files in it
Press 3 to print number of directories in it
Press 4 to list content of the directory
Press 5 to add file to this directory
Press 6 to add new directory to this """)
        path2=mom
        action1=int(input())
        if action1==1:
            
            # path=mom
            # print(path)
            print("Write the name of directory that you wanna work with")
            dir_rename=str(input())
            expdir=os.path.join(path2,dir_rename)
            
            if os.path.isdir(expdir):
                print("Rename the directory")
                newdirname=str(input())
                # source=expdir
                dest=os.path.join(path2,newdirname)
                os.rename(expdir,dest)
                print("Directory renamed successfully")
        elif action1==2:
           
            print("Write the name of directory that you wanna work with")
            dir_cnt=str(input())
            expdir=os.path.join(path2,dir_cnt)
            # print(expdir)
            cnt=0
            with os.scandir(expdir) as entries:
                for entry in entries:
                    if fnmatch.fnmatch(entry.name, "*.txt"):
                        cnt+=1
            print(cnt)
        elif action1==3:
            
            print("Write the name of directory that you wanna work with")
            dir_cnt=str(input())
            expdir=os.path.join(path2,dir_cnt)
            is_dir=os.path.isdir(expdir)
            if is_dir==True:
                sum_dir=len([1 for x in list(os.scandir(expdir)) if x.is_dir()])
                print(sum_dir)
            else:
                print("There are no directions")
        elif action1==4:
            
            print("Write the name of directory that you wanna work with")
            dir_cnt=str(input())
            expdir=os.path.join(path2,dir_cnt)
                        
            content_dir=os.scandir(expdir)
            print("Files and directories in ", expdir)
            for entry in content_dir:
                if entry.is_dir() or entry.is_file():
                    print(entry.name)
        elif action1==5:
            
            print("Write the name of directory that you wanna work with")
            dir_cnt=str(input())
            expdir=os.path.join(path2,dir_cnt)
            print("Write the file name")
            new=str(input())
            newf=open(expdir+"\\"+new+".txt",'w')
            # print(newf)
            print("File created successfully")
            newf.close()
            
        elif action1==6:
            
            print("Write the name of directory that you wanna work with")
            dir_cnt=str(input())
            expdir=os.path.join(path2,dir_cnt)
            print("Write the directory name")
            newd=str(input())
            os.mkdir(expdir+"\\"+newd)
            print("Direction created successfully")
