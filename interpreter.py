from time import sleep
import sys
from colorama import init, Fore, Back, Style

######

# Initializes Colorama
init(autoreset=True)

global section
section = -1
global nextfiles
nextfiles = []

def choose(question,answers,section_):
  sleep(0.75)
  global section
  global nextfiles
  iteration = 0
  print(f'\n{question}\n')
  for i in answers:
    iteration += 1
    print(f'{iteration}) {i}\n')
  action = int(input(f'What do you do? '))
  section = section + action + section_
  mainloop(section+1)

def show(string,delay):
  print(string)
  sleep(delay)

def mainloop(file):
  iteration = -1
  if file == None:
    print(Fore.RED + '''Null exception! (Internal Error) 
Cannot have a file with value of "NoneType"
Exit code -1 ''')
    sys.exit()
  try:
    f = open(f'{file}.txt','r')
    readout = f.read()
    readout = readout.split('\n')
  except:
    print(f'''{Fore.RED}There is no file/directory {file}.txt! (External Error)
Please create one!\n''')
    sys.exit()
  #Interpriter Code
  for i in readout:
    if not '//' in i[:2]:
      if '!' in i[:1]:
        in_ = (i[1:])
        question = in_.split('=')[0]
        answers = in_.split('=')[1]
        index = int(in_.split('=index:')[1])
        iteration += 1
        choose(question,answers.split('-'),iteration+index)
      else:
        show(i,0.5) 

if __name__ == "__main__": #Only runs if the file is not imported
  print(f'''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░█████╗░██╗░░░██╗░█████╗░░█████╗░████████╗███████╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║░░╚═╝░╚████╔╝░██║░░██║███████║░░░██║░░░█████╗░░
██║░░██╗░░╚██╔╝░░██║░░██║██╔══██║░░░██║░░░██╔══╝░░
╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░███████╗
░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')
  mainloop('main')