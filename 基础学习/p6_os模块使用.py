import sys
import os
ostype=sys.platform
if ostype=='linux3' or ostype=='linux2':
  cmd='clear'
  os.system('clear')
  print(cmd,'\n')
  
else:
  cmd='cls'
  os.system('cls')
  print(cmd,'\n')
  
  
 
