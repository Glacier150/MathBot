import math

print('Hello there!')
#It says to print 'hello there'
username=input("What's your name? ")
#It says to print 'What's your name' and takes the string input as the variable 'username'
def QuadForm(A, B, C):
  A=float(input('What is A '))
  B=float(input('What is B? '))
  C=float(input('What is C? '))
  print('Alright give me a minute to think')
  pre_sqrt=B**2-4*A*C
  print('I got', pre_sqrt, 'when I multiplied 4AC and subtracted it from B squared')
  if pre_sqrt<0:
    print('The question has no solution')
  else:
    post_sqrt=math.sqrt(pre_sqrt)
    print('I got',post_sqrt,'from the square root')
    print('I got',(round(post_sqrt,2)),'after I rounded')
    print('And I got',((B*-1)+(round(post_sqrt,2)))/(2*A),'and',((B*-1)-(round(post_sqrt, 2)))/(2*A),'for my final answers')

def add(N1, N2):
  pass

def sub(N1, N2):
  pass

def div(N1, N2):
  pass

def multi(N1, N2):
  pass