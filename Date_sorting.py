import os
import datetime
import glob
import shutil

a=str(os.getcwd())#sciezka gdzie znajduje sie program
c=a+"/Date_sorting.py"
files = glob.glob('/media/pawel/SUCKER/KOUD N/C++/*') #wyszukiwanie plikow w katalogu /home/pawel/Desktop/elo/
#print(len(files))
files.remove(c)
#print(files)
for i in range(len(files)):
    x=(files[i])
    print(x)
    #print(str(datetime.datetime.fromtimestamp(os.path.getmtime(x))))
    date_of_creation=str(datetime.datetime.fromtimestamp(os.path.getmtime(x)))

    rok=str(a+"/"+date_of_creation[:4])#sciezka folderu rok
    miesiac=str(rok+"/"+date_of_creation[:7])#sciezka folderu miesiac
    dzien=str(miesiac+"/"+date_of_creation[:10])#sciezka folderu dzien
    # create the directories if they do not exist
    if not os.path.exists(rok):
        os.makedirs(rok)

    if not os.path.exists(miesiac):
        os.makedirs(miesiac)

    if not os.path.exists(dzien):
        os.makedirs(dzien)

    # move the file to the appropriate directory
    shutil.move(x, dzien)