#---------------
# ophalen module
#---------------
# import modulenaam
# oproepen ====> modulenaam.generate_ful_name()

# from modulenaam import generate_ful_name()
# oproepen ====> generate_ful_name()

#---------------
# os.module
#---------------

import os

# Een map aanmaken
os.mkdir('map_naam')

# De huidige map wijzigen
os.chdir('pad')

# De huidige werkmap ophalen
os.getcwd()

# Een map verwijderen
os.rmdir('map_naam')

#---------------
# sys.module
#---------------

import sys

sys.argv = ["main.py", "Gwen", "Python"]

print('Welkom {}. Geniet van de {} challenge!'.format(sys.argv[1], sys.argv[2]))

sys.exit()     # Het script afsluiten
sys.maxsize    # De maximale grootte van een integer ophalen
sys.path       # Het omgevingspad ophalen
sys.version    # De Python-versie bekijken

#---------------
# statistics.module
#---------------

from statistics import *

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # Gemiddelde (~22.9)
print(median(ages))     # Mediaan (23)
print(mode(ages))       # Modus (20)
print(stdev(ages))      # Standaardafwijking (~2.3)

#---------------
# math.module
#---------------

from math import pi, sqrt, pow, floor, ceil, log10

print(pi)           # 3.141592653589793 (pi constante)
print(sqrt(2))      # 1.4142135623730951 (vierkantswortel)
print(pow(2, 3))    # 8.0 (machtsverheffen)
print(floor(9.81))  # 9 (naar beneden afronden)
print(ceil(9.81))   # 10 (naar boven afronden)
print(log10(100))   # 2 (logaritme met grondtal 10)

#---------------
# string.module
#---------------

import string

print(string.ascii_letters) # alle letters (hoofd- en kleine letters)
print(string.digits)        # 0123456789
print(string.punctuation)   # leestekens

#---------------
# random.module
#---------------

from random import random, randint

print(random())       # Geeft een willekeurig getal tussen 0 en 0.9999...
print(randint(5, 20)) # Geeft een willekeurig geheel getal tussen 5 en 20 (inclusief)

from random import random, randint

print(random())       # Geeft een willekeurig getal tussen 0 en 0.9999...
print(randint(5, 20)) # Geeft een willekeurig geheel getal tussen 5 en 20 (inclusief)

#---------------
# base64.module
#---------------

import base64

a = "aG93ZXN0IGN5YmVyc2VjdXJpdHk="
b = base64.b64decode(a)
print(b) # b'howest cybersecurity'

c = base64.b64encode(b)
print(c) # b'aG93ZXN0IGN5YmVyc2VjdXJpdHk='

######  Eigen Bijlage ######

h = b"Reynders gwen"
g = base64.b64encode(h)
print(g)

y = "UmV5bmRlcnMgZ3dlbg=="
z = base64.b64decode(y)
print(z)