import math

print('Hello there!')
username=input("What's your name? ")
print("In case you didn't know, I solve quadratic equations, but a warning,", username,". At this stage in development, I can only accurately process whole numbers. As a matter of fact, during testing, I've been off by several hundreds before. Anyway, let's start.")
RawOpB=float(input('What is the opposite of B? '))
RawB=float(input('What is B? '))
RawA=float(input('What is A? '))
RawC=float(input('And lastly what is C? '))

print('Alright give me a minute to think')

#putting a hashtag first turns the line into a comment that the program will ignore

pre_sqrt=RawB**2-4*RawA*RawC
print('I got', pre_sqrt, 'when I multiplied 4AC and subtracted it from B squared')
post_sqrt=math.sqrt(pre_sqrt)
print('I got',post_sqrt,'from the square root')
print('I got',(round(post_sqrt,1)),'after I rounded')
print('And I got',(RawOpB+(round(post_sqrt,2))),'and',(RawOpB-(round(post_sqrt, 2))),'for my final answers')