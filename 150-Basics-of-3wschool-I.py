
"""

###########Exercice 1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are")


##########Exercice 2
import os

os.sytem('clear')


print("DOne!")

##########Exercice 3
import time

import os


print(time.ctime(), time.strftime("%H:%M:%S"))

fist = input()

second = input()

print(second, " ", fist)

##########Exercice 4

ma_liste = []

for i in range(4):

    a = input()
    ma_liste.append(i)


mon_tuple = tuple(ma_liste)


print("List : ", ma_liste, "\nTuple : " ,mon_tuple)


##########Exercice 5

firstname = input()
lastname = input()

print(lastname, " ", firstname)


##########Exercice 6

ma_liste = []

a = 0

for i in range(4):
    a = input()
    ma_liste.append(a)

mon_tuple = tuple(ma_liste)

print( "liste : ", ma_liste, "\n Tuple : ", mon_tuple )


##########Exercice 7

file_name = input()

step = len(file_name)

extension = ""

for i in range(len(file_name)):
    if( file_name[i] == ".")  :
        step = i

    if(i >= step) :
       extension += "" + str(file_name[i])


print(extension)

##########Exercice 8

color = ["Red", "Green", "White", "Black"]

print(color[0], " Et : ", color[-1c])



##########Exercice 9

exam_st_date = (11, 12, 2014)

print("The exam had started from %i/%i/%i"%exam_st_date)


##########Exercice 10

n = int(input())
print(n + ((n*10)+n) + ((n * 100) + (n * 10) + n))


##########Exercice 11

def abss(a) :
    return type(a)


a = -10

print(abs(a))

##########Exercice 12



import calendar

a = calendar.month(2021, 4)

print(a)

##########Exercice 13

print("a string that you \"don't\" have to escape
      This is a ....... multi-line
     heredoc string --------> example")

#########Exercice 14


from datetime import date, time, datetime

madate = date(2021, 4, 5)

madate1 = date(2021, 4, 10)

one = madate1 - madate


print(one)



##########Exercice 15

print("Le rayon est : ", 6*6)




##########Exercice 16

number = int(input())

number = 17 - number

if(number < 0) :
    print(abs(number))
else:
    print(number)



##########Exercice 17

number = int(input())

if((number > 100) && (number < 1000 || number < 2000))




##########Exercice 31

nombre_1 = int(input())

nombre_2 = int(input())

def pgcd(nombre_1, nombre_2):

    if(nombre_1 < nombre_2):
        a = nombre_1
        nombre_1 = nombre_2
        nombre_2 = a

    while((nombre_1 % nombre_2) != 0 ):
        tmp = int(nombre_1 / nombre_2)
        mod = nombre_1 % nombre_2

        nombre_1 = mod
        nombre_2 = tmp

    return nombre_2

##########Exercice 32

#a = pgcd(nombre_1, nombre_2)

ppcm = int((nombre_1 * nombre_2) / pgcd(nombre_1, nombre_2))

print(ppcm)


##########Exercice 33

var = []

for i in range(3):
    var.append(int(input()))

if((var[0] == var[1]) or (var[0] == var[2]) or (var[2] == var[1] )):
    print("The sum equals to : 0")
else: 
    print(sum(var))


##########Exercice 35

var1 = int(input())
var2 = 0


while(var2==0):
    var2 = int(input())


if((var1 == var2) or (var1+var2 == 5) or (var1/var2 == 5)):
    print(True)
else:
    print(False)


##########Exercice 36

var1 = input()

var2 = input()

try: 
    value_1 = int(var1)
    value_2 = int(var2)

except ValueError:
    print("The two objects are not integers !")

else: 

    print("Nous avons : ", value_1+value_2)


##########eXECICE 37

my_inf = {'name' : 'Linson', 'age': 19, 'adress': 'Benin'}


print(my_inf['name'])

print(my_inf['age'])


print(my_inf['adress'])



##########Exercice 38

x = 4

y = 4

print((x*y)**2)



##########Exercice 39

import math

a = [4, 5]
b = [6, 7]

d = math.sqrt( (a[0]+b[0])**2  +   (a[1]*b[1])*2 )

print(d)

##########Exercice 40

import os

d = 'D:\DATA\Pictures\My Webdesign Creations\Perfect W\Pages\/readme.txt'

try: 

    open(d, 'r')

except FileExistsError:

    print("The file doesn't exist !")

else: 

    print("The file exist !")

    
#########Exercice 41

try :
    file = open('montext.txt')
    file.close()

except FileNotFoundError :

    print("Le fichier n'a pas été retrouvé")



##########Exercice 42

from platform import *


a = platform.platform()

print(a)


##########Exercice 43

import platform, os

print(platform.platform('os'))

print(os.name)

print(platform.system())

print(platform.release())



##########Exercice 44

import site

print(site.getsitepackages())



##########Exercice 45

import os

print(os.system('clear'))



##########Exercice 46

import os, sys

var = os.path.realpath(__file__)

print(os.path.basename(var))


##########Exercice 47

import multiprocessing


print(multiprocessing.cpu_count())



##########Exercice 48

var = input()

new = 0
new1 = 0

try : 
    
    new = float(var)
    new1 = int(var)

except ValueError:
    print("This file cannot be converted !")

else: 
    print("Done !")    



##########Exercice 49

print("that'shere")


##########Exercice 50

import cProfile

def myfunc():
    a = [i for i in range(1000)]

cProfile.run('myfunc()')

##########Exercice 51

import cProfile

def decouper():

    var = "fghdfhfhdfgh"

    ma_list = []

    a = ""

    for i in var :

        a += i

        if(i == " "):

            ma_list.append(a)

            a = ""

    return ma_list



cProfile.run("decouper()")


##########Exercice 53

import os

print(os.environ)


##########Exercice 54 :

import os

import socket

a = os.environ.get('COMPUTERNAME')

if a is not None :

    print("Erreur")

    b = socket.gethostbyname(a)

    print(b)



print(a)

print(os.environ.get('COMPUTERNAME'))


##########Exercice 55

import os

print(os.system('echo %username%'))


##########Exercice 56



###########Exercice 57 

import time

a = time.time()

def myfunc():
    a = [i for i in range(1000)]

b = time.time()


c = b - a

print(c)


##########Exercice 58

a = []
n = 4

for i in range(4):

    try: 
        a.append(int(input()))
    except TypeError:
        print("Toutes vos entrées ne sont pas entières !")


    print(sum(a))


##########Exercice 59

feet = float(input())
inch = float(input())

feet = feet * 12

inch += feet

height = inch*2.54

print("The total height in centimeters is : ", height, "cm")



##########Exercice 60

a = 10

b = 5

c = a**2 + b**2 

print("The hypotenus is : ", c)


##########Exercice 61

distance = float(input())

print("The distance in inches is : ", distance*12)
print("The distance in yard is : ", distance*36)
print("The distance in miles is : ", distance*63360)


##########Exercice 62

m = int(input("Give a minute"))
h = int(input("Give an hour"))

time = m*60 + h*3600


print(time)

##########Exercice 63

import os

print(os.path.abspath(__file__))


##########Exercice 64

import os, time

print("Creation time : ", time.ctime(os.path.getctime(__file__)))
print("Creation time : ", time.ctime(os.path.getmtime(__file__)))


##########Exercice 65

height = float(input("Give your height : "))
weight = float(input("Give your weight : "))

print("The body mass is : ", height/weight**2)


##########Exercice 66

pression = float(input("Give the pression : "))

print("The pression in pka makes : ", pression*0.145038)
print("The pression in mmhg makes : ", pression*7.50062)
print("The pression in  makes : ", pression/101.362)


##########Exercice 68

a = input()

number = list(a)

number = map(lambda x : int(x), number)

print(sum(number))


##########Exercice 69

numbers = []

for i in range(3):
    numbers.append(int(input()))

a = max(numbers)

b = min(numbers)

c = sum(numbers) - (a + b)

print("Nous avons : ", b, c, a)


##########Exercice 70

import os, glob

directory = 'D:\CODE\Python\Python-learning\Python-Basics-Part_1'

myfiles = glob.glob('*.py')

myfiles.sort(key=os.path.getmtime)

print(myfiles)


##########Exercice 71

import os, math

print(sorted(os.listdir()))


##########Exercice 72

import math

print(dir(math))


##########Exercice 73

a = [1, 3]

b = [3, 5]

midpoint = [ (a[0] + b[0])/2, (a[1] + b[1])/2 ]

print(midpoint)



##########Exercice 74

import hashlib

var = "Voici la chaine"

ordre = 4

hash_value = ""

for i in range(len(var)):

    if(ord(var[i]) > 96 and ord(var[i]) <123):

        if((ord(var[i]) - 4) < 97):

            value_to_add = 97 - (ord(var[i]) - 4 )

            hash_value += chr(122 - value_to_add)
            continue
        
        hash_value += chr(ord(var[i]) - 4)
       

    if(ord(var[i]) > 64 and ord(var[i]) < 91):

        if((ord(var[i]) - 4) < 64):

            value_to_add = 65 - (ord(var[i]) - 4 )

            hash_value += chr(91 - value_to_add)
            continue

        hash_value += chr(ord(var[i]) - 4)



##########Exercice 75

import sys

print(sys.copyright)


##########Exercice 76


import sys

print(sys.argv[0])

print(len(sys.argv))

print(str(sys.argv))


##########Exercice 77

import sys, os

if(sys.byteorder == 'little'):
    print("Little Endian")
else: 
    print("Big Endian")


###########Exercice 78

import os

a = os.__file__.split((os.path.basename(os.__file__)))

b = str(a[0])

print(os.listdir(b))




##########Exercice 79

import sys

a = True

print(sys.getsizeof(a), "bytes")


##########Exercice 80

import sys

print(sys.getrecursionlimit())


##########Exercice 81

n = int(input("Donnez votre entrée n : "))

my_string = ""

for i in range(n):
    b = input("Give your string : ")
    my_string += b

print(my_string)


##########Exercice 82

a = [f for f in range(40) if f%2 != 0]

print(sum(a))



##########Exercice 83

my_list = [i for i in range(45)]

a = int(input("Give a number : "))

test = False

for i in my_list:
    if(i>a):
        test = True
        
if test is not True:    
    print("Aucun élément de la liste n'est plus grand que : ", a)
else: 
    print("Au moins un élément de la liste n'est plus grand que i")


##########Exercice 84

a = input('Give a string : ')
b = input('Give a character : ')

c = list(a)

counter = 0

for i in c:
    if(b == i):
        counter+=1

print("Le nombre d'occurrence est  : ", counter)


##########Exercice 85

import os

a = "D:\CODE\Python\Python-learning\Python-Basics-Part_1\master_modules.docx"

b = os.path.isdir(a)

if (b):
    print("L'entrée est un dossier !")

c = os.path.isfile(a)

if (c):
    print("L'entrée est un fichier !")


##########Exercice 86

a = input()

print(" La valeur ASCII de", a, " est : ", ord(a))


x
##########Exercice 87

import os

a = os.path.getsize('D:\CODE\Python\Python-learning\Python-Basics-Part_1\master_modules.docx')
print(a)



##########Exercice 88

a = int(input())

b = int(input())

print(a, " + ", b, " = ", a + b)



##########Exercice 89

a = int(input())

if(a == 1):
    print('First day of the month !')



##########Exercice 90 non fait 

my_code = open(__file__, 'r')

code_source = open('Python_Code.txt', 'a+')

a = 0
b = ""

try : 

    open('code_source', 'w')

    for i in my_code : 


        a += 1
        if(a >= 287 and a <= 308):
            #print(i)

            b = my_code.readline()
            print(b)
            #code_source.write(b)


except FileNotFoundError:

    print("Il y a eu une erreur lors de l'ouverture du fichier !")

print(code_source)


##########Exercice 91

var = int(input())

var1 = int(input())

tmp = 0

print("Voici la première variable : ", var, "et voici la seconde variable : ", var1)

tmp = var
var = var1
var1 = tmp

#var, var1 = var1, var

print("Voici la première variable : ", var, "et voici la seconde variable : ", var1)



##########Exercice 92


##########Exercice 93

var = input()

print("La variable qui comporte l'élément ' ", var, " ' a pour type : ", type(var))




##########Exercice 94

my_value = b'string'

binary_conversion = list(my_value)

print(binary_conversion)


##########Exercice 95


my_string = input()

try : 
    float(my_string)

except ValueError:
    print("This string is not numeric")

else : 
    print("The string is a numerical string that equal to : ", )


##########Exercice 96



##########Exercice 97

var = sorted(set(globals().keys()))

print(var)


##########Exercice 98

import time

print(time.ctime())



#########Exercice 99

import os

os.system('clear')



##########Exercice 100

import _socket

a = _socket.gethostname()

print(a)



##########Exercice 101

import requests

var = requests.get('https://chat.openai.com/chat')

print(var.text)


##########Exercice 102

import os 

print(os.system('ls'))


##########Exercice 103

import os

path = __file__

print(os.path.basename(path))



##########Exercice 104

import os

print(os.environ)


##########Exercice 105


import os

#Uniquement Valide sur UNIX

print("Le processus qui s'exécute est : ", os.getegid)
print("Le processus qui s'exécute est : ", os.geteguid)
print("Le processus qui s'exécute est : ", os.getepuid)



##########Exercice 106

string = "text.txt"

my_list = string.split('.')

print(my_list)


##########Exercice 107

import time, os

try : 

    my_file = open("C:/fichier/text.txt", "r")

except FileExistsError : 
    print("Le fichier n'existe pas ! ")

print("Voici mon fichier : ", __file__)
print("access_time", time.ctime(os.path.getatime(__file__)))
print("Modified_time", time.ctime(os.path.getmtime(__file__)))
#print("size", os.path.getsize(my_file) )




##########Exercice 108



try :
    var = open('c:/fichier/text.txt', "r")
except FileNotFoundError :

    print("Votre fichier n'a pas été retrouvé !")

line = var.readline()

while line : 
        
    print(line)
    line = var.readline()


##########Exercice 109

a = float(input())

if(a > 0):
    print("Positive")
elif(a < 0):
    print("Negative")
else:
    print("Equal")


##########Exercice 110

my_list = [ i for i in range(100) if type(i//5) == int ]

print(my_list)

new_list = list(filter(lambda x : x % 15 == 0, my_list))

print(new_list)



###########Exercice 111

import os, glob

#my_list = os.listdir()

my_list = glob.glob("*.py")

print(my_list)




##########Exercice 112

my_list = [-4, -5, 1, 2, -3, 4, 5, 6]


del my_list[0]


print(my_list)



##########Exercice 113

try :
    var = int(input())
    print("C'est pas un nombre")
except ValueError :
    print("Ce n'est pas un nombre")



##########Exercice 114

my_list = [-4, -5, 1, 2, -3, 4, 5, 6]

new_list = []

for i in my_list:
    new_list.append(my_list[i]) if(my_list[i] > 0) else print("")

print(new_list)


##########Exercice 115

from functools import reduce

my_list = [1, 2, 3, 4, 5, 6]

result = reduce(lambda x, y: x*y, my_list)

print(result)



##########Exercice 116

#Go on internet and just takes some characters of unicode and print i
#To easy, you can let it down !



##########Exercice 117

var = "The same value"

var1 = "The same value"

print("Les deux entrée ont le même emplacement mémoire : ", hex(id(var))) if(hex(id(var)) == hex(id(var1))) else print("Les deux entrée ont des places différentes en mémoire")



##########Exercice 118

my_list = [1, 2, 4, 5]

byt_tab = bytearray(my_list)

for i in byt_tab:
    print(i)





##########Exercice 119


number = input()

print("That's the original string : ", number)

print('%.9s' % number)



##########Exercice 120

string = input()

print("That's the original string : ", string)

print('%.9s' % string)


##########Exercice 121

var = 1

try : 
    
    x

    print("The variable is defined")

except NameError :

    print("La variable n'est pas définie !")

else:
    print("The variable is defined !")




##########Exercice 122

#This exercice is very interesting 'cause it shows you a way to use the type() function in python. You can get a minimal value
#without destroying the function


numeric_value = 99

list_value = ['0', '2', '4']

dict_value = {'x':10, 'y':15}

print(type(numeric_value)())
print(type(list_value)())
print(type(dict_value)())



##########Exercice 123

import sys

print(sys.float_info)
print(sys.int_info)
print(sys.maxsize)


##########Exercice 124

var = []

for i in range(2) : 

    var.append(int(input()))

if(var[0] != var[1]):
    print("Les deux variables sont différentes !")
else: 
    print("Les deux variables sont égales !")


    
##########Exercice 125

mon_tuple = ('1', '2', '3')

print(len(mon_tuple))



##########Exercice 126
import os

from inspect import getmodule

var = str(getmodule(os))

print("Le module de OS est : ", var)


##########Exercice 127

var = int(input())

size = var.bit_length()


print("Nous avons la taille en bits qui est de  : ", size, " bits")



##########Exercice 128

str = input()

for i in str:
    if(ord(i) > ord('a') and ord(i) < ord('z')):
        print("There are lowercase caracters!")
        break


print("There are not lowercase caracters!")



##########Exercice 129

def rightjust(caractere, number, chain):

    i = 0

    while i < number :
        chain +=caractere

        i += 1
    return chain


def leftjust(caractere, number, chain):

    i = 0
    chain_before = ""

    while i < number :
        chain_before +=caractere
        print(i)
        i += 1
    chain_before += chain

    return chain_before

original_string = "22.52"

str1 = leftjust('0', 4, original_string)

print(str1 )

str1 = rightjust('0', 4, original_string)

print(str1 )


##########Exercice 130

str = input()

print('"', str , '"')



##########Exercice 131

my_list = ['a', 'b', 'c']

x, y, z = my_list

print(x, y, z)



##########Exercice 132

from os import path

print(path.expanduser('~'))


##########Exercice 133

from time import time, sleep

start = time()

sleep(2)

running_time = time() - start

print("The running time is : ", running_time)



##########Exercice 134

nom, prenom = input("Entrez votre nom et prénom (séparé par des espaces)").split()


#########Exercice 135

a = input()

print("x=", a)



##########Exercice 136------------------NOT-DONE

import os


def subfolder(path_value):

    print("Voici le contenu du sous-dossier : ")

    all = os.listdir(content)

    print(all)



tmp_path = ""

content = ""

path = input()

try: 
    dir = os.path.dirname(path)
except FileNotFoundError :
    print("Your Directory is unavalaible!")

directory = os.listdir(dir)

print("The directory type is : ", type(directory))

for i in directory:

    content += path

    content += i

    if(os.path.isdir(content)):

        subfolder(content)

    print("Voici le fichier ", i)

    content = ""

  


##########Exercice 137

my_dict = {'nom' : 'DOUMATE', 'prenom' : 'Linson', 'age' : 'Inconnu'}


for key, value in my_dict.items():

    print(" Nous avons : ", key, " et ", value, "\n" )




##########Exercice 138

import random

var = [1, 0]

choice = random.choice(var)

print(choice)

if(choice == 1):
    print(True)
if(choice == 0):
    print(False)



##########Exercice 139

ip_address = input("Give an IPv4 ADRESS :")

ip = ip_address.split(".")

unavailable = False

if(len(ip) > 4):
    print("Your IPv4 ADRESS is not valid!")
else:

    for i in ip:

        i = int(i)

        if(i < 0 or i > 255):
            print("Your IPv4 ADDRESS is invalid!")
            unavailable = True
            break

    print("Your IPv4 ADRESS is valid!") if not unavailable else print("")



##########Exercice 140


dec = int(input())

decomposition = []




while(((dec%16) != 0) or ((dec//16) != 0)):

    decomposition.append(dec%16)

    dec = (dec//16)


print(decomposition)

decomposition = decomposition[::-1]

print(decomposition)

conv = []

for i in range(len(decomposition)):


    if(decomposition[i] == 10):
        conv.append("a")
        continue

    if(decomposition[i] == 11):
        conv.append("b")
        continue

    if(decomposition[i] == 12):
        conv.append("c")
        continue

    if(decomposition[i] == 13):
        conv.append("d")
        continue

    if(decomposition[i] == 14):
        conv.append("e")
        continue

    if(decomposition[i] == 15):
        conv.append("f")
        continue

    conv.append(decomposition[i])


result = ""

for i in conv:

    result +=  str(i)

print(result)




##########Exercice 141


dec = int(input())

decomposition = []


while(((dec%2) != 0) or ((dec//2) != 0)):

    decomposition.append(dec%2)

    dec = (dec//2)


print(decomposition)

decomposition = decomposition[::-1]

result = ""

for i in decomposition:

    result +=  str(i)

print(result)



##########Exercice 142 

i = 0

chain = input()

my_list = list(chain)

previous_carac = 0

while(i < len(my_list)):

    carac = my_list[i]

    counter = 0

    j = i

    #print("Voici J : ", j)

    while( j < len(my_list) and my_list[j] == carac):

        counter+=1

        #print("Le caractère ici est : ", my_list[j], "\n")

        #print("Et le compteur est là :", counter, "\n")

        j+=1

    if(i == 0):
        i+=counter
        previous_carac = counter
        continue

    if(counter != previous_carac):

        print(False)

        break;

    if(counter == previous_carac):
        
        i = j

        previous_carac = counter

if(i == len(my_list)):
    print(" True !")





##########Exercice 143

import platform

var = platform.architecture()

print(var)



##########Exercice 144

import random

ages =  [20, 14, 52, 45, 5]
prenoms =  ['Afi', 'Bea', 'Lea', 'Carl', 'Perla']

my_types = {1 : [i for i in range(1500, 80000)], 2 : set([i for i in range(1500, 80000)]), 3 : {i:j for i, j in zip(ages, prenoms)}}

choice = random.choice(list(my_types.keys()))

var = my_types[choice]

print(var)

if(type(var) == set):

    print("La variable est un Ensemble !")

if(type(var) == list):

    print("La variable est une Liste !")


if(type(var) == dict):

    print("La variable est un Dictionnaire !")



##########Exercice 145

my_list = {'1': 'name', '2': 'firstname', '3': 'password'};

for i, j in my_list.items():

    print(i, j)

    

##########Exercice 146


import os

import inspect

file_path = os.path.dirname(inspect.getabsfile(os)) 

modules_string = str((os.listdir(file_path)))

modules_names = modules_string.split(',')

modules = {"cle" : "valeurs"}

for i in modules_names:

    name = "Bibliotèque de "

    name += i[2:-4]

    modules[name] = i[2:-1]


for keys, values in modules.items():

    print(keys ," : ", values, "\n")



##########Exercice 147

numbers = []

for i in range(2):
    numbers.append(int(input())) 

if(numbers[0]%numbers[1] == 0):
    print(numbers[0], "est divisible par ", numbers[1])

if(numbers[1]%numbers[0] == 0):
    print(numbers[1], "est divisible par ", numbers[0])




##########Exercice 148

sequence = set([i for i in range(99)])

max = 0
min = 0

for i in sequence: 
    if(i < min):
        min = i
    if(i > max):
        max = i

print("MAX : ", max, "\nMIN : ", min)


##########Exercice 149

number = int(input())

result = sum([i*i*i for i in range(number) if(i>0 and i<number)])

print(result)


##########Exercice 150

my_numbers = [x for x in range(4, 8) if((x%2)!=0)]

sequence = [x for x in range(100) if(x/3) == 0]

for i in sequence:
    print(True) if my_numbers[0] ** my_numbers[1] == i else print (False)
"""














