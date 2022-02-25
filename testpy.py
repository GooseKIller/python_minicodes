import os
pan=os.listdir(path="dlete")
os.chdir("dlete")
for i in range(0,len(pan)):
    os.remove(pan[i])
quit('popo.txt')
