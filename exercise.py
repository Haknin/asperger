'''
#ex1:
name = input("enter your name: ")
age = input("enter your age: ")
max_age =int(100)
num=int(age)
x=100-num
y=x+2023
sp=input("put a number: ")
for i in range (int(sp)):
    print('hey' ,name , 'the year you will turn 100 is:' ,y,"\n" )
'''

#ex2
'''
num=int(input("put a number: "))
if num %4 == 0:
    print("4 on 4")
elif num %2 == 0:
    print("ZUGI")
else:
    print("E ZUGI")
    
#ex2/2
num=int(input("put a number: "))
check=int(input("put a number: "))
if num % check == 0:
    print("very good")
else:
    print("no no no")
'''
'''
#ex3
a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in a:
    if element < 5 :
        print(element , end = ' ')
'''
'''
#ex4
num = int(input("put anumber: "))
i=1
if num % i == 0:
    print(i)
    i++1
'''
'''
input1=input("put a number")
num = int(input1)
limit = num
HILUK=[]
for i in range (1, limit+1):
    if num % i ==0:
        HILUK.append(i)

print(num,"divites by" ,HILUK,)
'''

'''
#ex6
word = str(input("word please: "))
drow = word [::-1]
if word == drow:
    print("NODER", word, "NODER")
else:
    print("fuck off yo twat")

'''
'''
#ex8
import random
the_hand = [ "s","r","p" ]
bot_rps1 = random.choice(the_hand)
bot_rps2 = random.choice(the_hand)

print(bot_rps1)
print(bot_rps2)

# (bot1, bot2) = (s,r)2 (s,s)3 (s,p)1 (p,p)3 (p,r)1 (p,s)2 (r,p)2 (r,r)3 (r,s)1

if (bot_rps1 , bot_rps2) == ("s","p") or (bot_rps1 , bot_rps2) ==("p","r") or (bot_rps1 , bot_rps2) ==("r","s"):
    print("player 1 wins")
elif (bot_rps1, bot_rps2) == ("s", "r") or (bot_rps1 , bot_rps2) ==("p", "s") or (bot_rps1 , bot_rps2) ==("r", "p"):
    print("player 2 wins")

else:
    print("teko teko")
'''
'''
#ex9
import random
num = range(1,10)
num_guess= int(input("guess the number 1-9: "))
num_random = random.choice(num)
print(num_random)

if num_random == num_guess:
    print ("YESS YES YES YES")
'''
'''
ex10
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = [x for x in set(a) if x in b]

print(common_elements)

'''
'''
#ex11
def prime(num):
    for i in range (2,num):
        if num % i == 0:
            return False
    if num ==1 or  num==0:
        return False
    return True

#examples:
print(prime(0))
print(prime(1))
print(prime(2))
print(prime(5))
'''
'''
#ex12
a = [5, 10, 15, 20, 25]
lisr=[]
lisr.append(a[0])
num = len(a)
lisr.append(a[num-1])

print(lisr)
'''
'''
#ex13
def fibonacci(num):
    list_f=[1,1]
    for i in range (2,num):
        num_next = list_f[i-1] + list_f[i-2]
        list_f.append(num_next)
        i+=1
    return list_f

num=int(input("how many fibunacho numbers you want: "))
print(fibonacci(num))
'''
#ex14
'''
def lister_copier(old_list):





import random
old_list=[]
for i in range (10):
    num = range(1,100)
   ` num_random = random.choice(num)
    print(num_random)
    old_list.append(num_random)
print(old_list)

old_list = list(set(old_list))
print(old_list)
'''
''' #ex16
import random
import string

def gen_random():
    random_letter = random.choice(string.ascii_letters)
    num_r = random.randint(1, 9)
    random_number = str(num_r)
    passwd = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 9))) + ''.join(random.choices(string.digits, k=random.randint(3, 9)))
    return passwd

user_names = []
for i in range(0, 5):
    username = input("Insert your username: ")
    user_names.append(username)

new_pass = input("Do you want a new password? (y/n): ")

# Generate multiple random passwords using map()
passwords = list(map(lambda x: gen_random(), range(len(user_names))))

# Associate usernames with passwords using map()
user_pass_dict = dict(zip(user_names, passwords))

# Print the generated passwords for respective usernames
for username, password in user_pass_dict.items():
    print(f"Username: {username}, Password: {password}")

'''