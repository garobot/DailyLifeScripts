from sys import platform
import os
import subprocess as sp
print("Enter the wifi profile whose passwd you forgot: ")
name=input()
if platform == "linux" or platform == "linux2":
      pass # linux
elif (platform == "darwin"):
      pass #OS X
elif platform == "win32":
      output = sp.getoutput(["netsh" ,"wlan","show","profile",name ,"key=clear"])
      stop=output.find('\n Cost settings')
      startingstr="Key Content            : "
      start=output.find(startingstr)
      for i in output[start+len(startingstr):]:
            if(i!='\n'):
                  print(i,end="")
            else:
                  break