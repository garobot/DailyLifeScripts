from sys import platform
import os
import subprocess
print("Enter the wifi profile whose passwd you forgot: ",end="")
name=input()
if platform == "linux" or platform == "linux2": # linux
      #output = subprocess.getoutput(["sudo cat /etc/NetworkManager/system-connections/",name ,".nmconnection"])
      file='/etc/NetworkManager/system-connections/{}.nmconnection'.format(name)
      output = subprocess.getoutput(['sudo cat {}'.format(file)])
      startingstr="psk="
elif (platform == "darwin"):
      pass #OS X
elif platform == "win32":  #Windows
      output = subprocess.getoutput(["netsh" ,"wlan","show","profile",name ,"key=clear"])
      stop=output.find('\n Cost settings')
      startingstr="Key Content            : "

#common code
start=output.find(startingstr)
print("Required password is: ")
for i in output[start+len(startingstr):]:
      if(i!='\n'):
            print(i,end="")
      else:
            break
print()
