import math
import random
from collections import Counter

min_count=3
max_count=100
p=2
q=2
c=2
n=2
m=2
d=2
e=2
euler=2
data=2
prime=[]
plain=[]
number=[]
original=[]
res=[]
res2=[]
text=""

def prime_generator():
    global min_count
    global max_count
    
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(max_count) + 1)):
            if min_count % x == 0: 
                isprime = False
                break
        
        if isprime:
            if(min_count<max_count):
                prime.append(min_count)
        
        min_count += 1
        if(min_count>=max_count):
            random.shuffle(prime)
            break



def d_generator():
    global d,euler
    while(d<euler):
        if(math.gcd(d,euler)==1):
            break
        else:
            d+=1

def e_generator():
    global e,euler
    while(e<euler):
        if((e*d)%euler==1):
            break
        else:
            e+=1

def encryption():
    global c,data,e,n
    c=pow(data,e)%n
    print("Cypher text: "+str(c))

def decryption():
    global c,d,data,n
    data=pow(c,d)%n
    


#def convert_to_number():
 #   global data,text
  #  data=list(data)
   # for x in data:
    #    text+=str(ord(x))
     #   print(text)

def convert_to_number():
    global data,number,plain,res,res2
    original=list(data)
    plain=sorted(set(data))
    for x in range(1,len(plain)+1):
        number.append(x)
    res = dict(zip(plain, number))
    res2 = dict(zip(number, plain))
    data=""
    for x in original:
        data+=str(res[x])
    #data=''.join(str(z) for z in number)
    print("Converted plain text: "+data)
    data=int(data)


def convert_to_plaintext():
    global res2,data,original
    text=""
    for x in str(data):
        x=int(x)
        text+=str(res2[x])
    print("Final text is: "+text)



data=input("Input message: ")
convert_to_number()


count=input("Input bit number: ")
count=int(count)
min_count=pow(2,count-1)
max_count=pow(2,count)
prime_generator()
p=prime[0]
q=prime[-1]
print("Prime numbers are: "+str(p)+" and "+str(q))
n=p*q
euler=(p-1)*(q-1)
d_generator()
e_generator()

encryption()
decryption()

convert_to_plaintext()


###### p*q must be greater than converted plain text number
###### use 1-6 character long string and less than 11 bit number, for larger input - complexity is higher
