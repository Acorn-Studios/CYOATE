#importer the interpreter for the engine as 'inter'
import interpreter as inter
import sys

print('''Use %?{ to create a question.
Use %Q to quit
''')

while True:
  input_ = input('>')
  if '%Q' in input_:
    sys.exit()
    quit()
  if '%?{' in input_:
    input_question = input('Input a question>')
    input_ = input('Input a choice>')
    while input_ != '}':
      input_ = input('Input a choice>')