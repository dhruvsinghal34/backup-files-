import time
import os
import shutil

def main():
    path = "C:/Dhruv/projects/BarCodeSacnner-master"
    days =30
    second = (time.time())-(days*24*60*60)
    if(os.path.exists(path)):
        for rootfolder,subfolders,files in os.walk(path):
            statinfo = os.stat(path).st_ctime
            if(second > statinfo):
                shutil.rmtree(path)
            else:
                for folders in subfolders:
                    folderPath = os.path.join(rootfolder,folders)
                    time2 = os.stat(folderPath).st_ctime
                    if(second > time2):
                        shutil.rmtree(folderPath)
                    else:
                        print("no such folder exits")
                for file in files:
                    filesPath = os.path.join(rootfolder,file)
                    fileTime = os.stat(filesPath).st_ctime
                    if(second > fileTime):
                        os.remove(filesPath)
                    else:
                        print("no files exits")
                    
                    
    else:
         print("the path does not exits")

if __name__ == '__main__':
    main()
         
     
         
     
     
