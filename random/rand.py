import random  as rd

#generate a float number between 0 and 1
flt = rd.random()
print('Generated number:',flt) 

for i in range(10):
    print('Number ',i+1,':',rd.random())

randset=[rd.random() for i in range(3)]

print('List of 3 generated reals[0-1]:',randset)

x=rd.uniform(1,10)
print(x)

n=rd.randint(1,50)
print(n)

print('Gauss distribution')
for i in range(10):
    print(rd.gauss(0,1))

fruits=['mango','pineapple','apple','bananas','orange'] 

print('A random choice:',fruits[rd.randint(0,len(fruits)-1)])
print('Another random choice:',rd.choice(fruits))

print(rd.choices(fruits,k=3))# avec remise: repetition possible:k [0-+infini]
print(rd.choices(fruits,k=8))# avec remise: repetition possible:k [0-+infini]

print(rd.sample(fruits,k=4))# sans remise: repetition impossible k e[0-n]

rd.shuffle(fruits)

print('fruits:',fruits)

#exercise 1

nums=[1,2,3,4,5,6]
choices10000=list()
for i in range(10000):
    choices10000.append(rd.choice(nums))

choices1000=rd.choices(choices10000,k=1000) 

count6=choices1000.count(6)
count4=choices1000.count(4)  

print('count6:',count6)
print('count4:',count4)

m=count6/len(choices1000)
n=count4/len(choices1000)

print('m:',m)
print('n:',n)

print(1/6)


#exercise 2

CAPITAL=1000
capital=CAPITAL
bet=1
def aTestOfGameA(bet):

    global  capital
    x=rd.choices([0,1],k=1, weights=[0.51,0.49])
    if x[0]==1:
        capital+=1
    else:
        capital-=bet

def aTestOfGameB(bet):
    global capital
    if capital%3==0:
        x=rd.choices([0,1],weights=[0.91,0.09])
    else :
        x=rd.choices([0,1],weights=[0.26,0.74])

    if x[0]==1:
        capital+=1
    else:
        capital-=bet




def aTestOfGameC():
    x=rd.randint(0,1)
    if x==1:
        aTestOfGameA(bet)
    else:
        aTestOfGameB(bet)


def rateGame():
    return capital>=CAPITAL

def conclude(name):
    if rateGame():
        print('The game',name,'is winning')
    else:
        print('The game',name,'is losing')
    print('The remaining sum is:',capital)    


def playGames(testNumber):

    #Game A
    capital=CAPITAL
    for i in range(testNumber):
        aTestOfGameA(bet)
    conclude('A')

    #Game B
    capital=CAPITAL 
    for i in range(testNumber):
        aTestOfGameB(bet)
    conclude('B')

    #Game C
    capital=CAPITAL
    for i in range(testNumber):
        aTestOfGameC()
    conclude('C')



playGames(10000)