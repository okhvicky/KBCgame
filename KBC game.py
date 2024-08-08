#---------- The KBC Game ------------
print('                  Deviyo or Sajano')
print('-------****--- Welcome to The KBC Game.---*****-------')
print()
print('''Rules of the game:
1.You will be asked 5 questions from general knowledge. 
2.You have to select your answer from the 4 options provided. 
3.For every correct answer you will be awarded with 1000 Rs.
4.In case of wrong answer, you will be penalized by 500 Rs''')
print()
playeramt=0
prize=1000
penalty=500

right=1
wrong=1
correct=0
incorrect=0

greet=input('Are you ready!!! - ').lower()
if greet=='yes':
    print('Toh ye raha apka phela sawal?')
else:
    print("(wrong input) Type 'yes'")
print()                #question 1

print('''Who is prime minister of India, since 2014?
A.Narendra modi, B.Rahul Gandhi, C.Amit Shah, D.Yogi adityanath''')
print()
ans=input('Chose you answer from (A/B/C/D) : ').lower()
if ans=='a':
    playeramt=playeramt+prize
    correct+=right
    print('Right answer, you won 1000₹')
else:
    playeramt=playeramt-penalty
    incorrect+=wrong
    print('Wrong answer,you loose 500₹')
print()                #question 2

print('''Which state is also known as the “fruit bowl” of India?
A.Goa, B.Punjab, C.Kashmir, D.Himachal Pradesh''')
print()
ans1=input('Chose you answer from (A/B/C/D) : ').lower()
if ans1=='d':
    playeramt=playeramt+prize
    correct+=right
    print('Right answer, you won 1000₹')
else:
    playeramt=playeramt-penalty
    incorrect += wrong
    print('Wrong answer, you loose 500₹')
print()                #question 3

print('''Which is the national sport of India?
A.Hockey, B.Football, C.Cricket, D.Nothing''')
print()
ans2=input('Chose you answer from (A/B/C/D) : ').lower()
if ans2=='d':
    playeramt = playeramt + prize
    correct+=right
    print('Right answer, you won 1000₹')
else:
    playeramt = playeramt - penalty
    incorrect += wrong
    print('Wrong answer, you loose 500₹')
print()                #question 4

print('''Who was the author of Ramayana?
A.Krishna das, B.Tulsi das, C.Valmiki, D.Ved vyas''')
print()
ans3=input('Chose you answer from (A/B/C/D) : ').lower()
if ans3=='c':
    playeramt = playeramt + prize
    correct += right
    print('Right answer, you won 1000₹')
else:
    playeramt = playeramt - penalty
    incorrect += wrong
    print('Wrong answer, you loose 500₹')
print()                #question 5

print('''Who killed bali in ramayana?
A.Laxman, B.Bheem, C.Sugreev, D.Raghava''')
print()
ans4=input('Chose you answer from (A/B/C/D) : ').lower()
if ans4=='d':
    playeramt = playeramt + prize
    correct += right
    print('Right answer, you won 1000₹')
else:
    playeramt = playeramt - penalty
    incorrect += wrong
    print('Wrong answer, you loose 500₹')
print()


print('GAME OVER --- Here are the results of the game:')
if playeramt>0:
    print(f"Total amount won: {playeramt} Rs.")
else:
    print(f"You loss: {playeramt} Rs.")

print(f"Number of correct answers: {correct}")
print(f"Number of incorrect answers: {incorrect}")
print()
print('--- Apke saath khel ke bahut acha laga, milta hu agle assignment me ---')
