import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO put in stack and ####CHECK####
  file = open(filename, 'r')
  lines = file.read()
  stack = Stack()
  key = { ')': '(', ']': '[', '}': '{' }
  
  for line in lines:
    length = len(line)
    for char in range(length):
      if line[char] in [ '[', '(', '{' ]:
        stack.push(line[char])
      elif line[char] in [']', ')', '}' ]:
        if stack.peek() == key[line[char]]:
          stack.pop()
        else:
          return False
  if len(stack) == 0:
    return True
  else:
    return False


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


