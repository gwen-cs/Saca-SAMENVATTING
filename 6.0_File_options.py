#------------------------
# werken met ('utf-8')
#------------------------

ascii_string = "foobar"
non_ascii_string = " → "

ascii_bytes = ascii_string.encode("utf-8")
non_ascii_bytes = non_ascii_string.encode("utf-8")

print (ascii_bytes.decode('utf-8'))
print(non_ascii_bytes.decode('utf-8'))

#------------------------
# werken met bestanden
#------------------------

with open("demo.txt", "w") as fp:
    fp.write("Hallo Gwen")
    # maakt een document aan met de naam demo.txt en zet daar text in "Hallo Gwen"

# opvragen van bestanden (niet voor grote bestanden)

with open("demo.txt", 'r') as fp:
    content = fp.read()
    # opened het document aan met de naam demo.txt en zet daar hele document in
    content = fp.readline()
    # opened het document aan met de naam demo.txt en zet daar de eerste regel in

# opvragen van bestanden (voor grote bestanden)

# Optie 1: met readline() en een while-lus
with open("demo.txt", 'r') as fp:
    line = fp.readline()
    while line:
        print(line, end='')
        line = fp.readline()

# Optie 2: direct itereren over het bestandsobject
with open("demo.txt", 'r') as fp:
    for line in fp:
        print(line.strip())


# "r"   read   ==>  Als het bestand niet bestaat, treedt er een fout op
# "w"   write  ==>  Als het bestand al bestaat, wordt de inhoud gewist (overschreven).
#                   Als het bestand niet bestaat, wordt er een nieuw bestand aangemaakt.
# "x"   create ==>  Opent het bestand voor exclusieve creatie.
#                   Als het bestand al bestaat, treedt er een fout op.
# "a"   Append ==>  Opent het bestand om te schrijven.
#                   Als het bestand bestaat, wordt nieuwe data achteraan het bestand toegevoegd (appended).
#                   Als het bestand niet bestaat, wordt er een nieuw bestand aangemaakt.
# "b"   read    ==> Opent het bestand in binaire modus. Lezen en schrijven van/naar het bestand gebeurt in bytes.
# "t"   read    ==> Opent het bestand in tekstmodus.
#                   Lezen en schrijven van/naar het bestand gebeurt in strings. (standaard)

# Methode 1: write() gebruiken (voegt automatisch GEEN nieuwe regel \n toe)
with open("demo.txt", 'a') as fp:
    fp.write("Awesome, I can append a file")

# Methode 2: writelines() gebruiken voor een lijst van regels
with open("demo.txt", 'a') as fp:
    fp.writelines(["look I'm a\n", "list\n"])

# Methode 3: print() omleiden met de parameter file=fp
with open("demo.txt", 'a') as fp:
    print("Now a newlines is automatically added (look at the default value of end parameter in print definition)", file=fp)

# een pad opbouwen

import os
path = "/etc/ssh/sshd_config" # gewoon als tekst (strings)
path = os.path.join("/etc", "ssh", "sshd_config") # gebruikt het juiste scheidingsteken voor het huidige besturingssysteem

from pathlib import Path
p = Path("/etc")
p = p / "ssh" / "sshd_config"

# Bestandssysteemoperaties

#   Omschrijving	                    Python-code	                    Linux CLI equivalent
#   Huidige werkmap ophalen	            os.getcwd()	                    pwd
#   Huidige werkmap wijzigen            os.chdir("/tmp")	            cd /tmp
#   Map aanmaken	                    os.mkdir("/tmp/tst")	        mkdir /tmp/tst
#   Map aanmaken, inclusief 	        os.makedirs("/tmp/tst/a/b/c")	mkdir -p /tmp/tst/a/b/c
#       ontbrekende submappen
#   Bestand/map statistieken ophalen	os.stat("/tmp/tst")	            stat /tmp/tst
#   Bestandsmodus (rechten) wijzigen	os.chmod("/tmp/tst", 0o600)	    chmod 600 /tmp/tst
#   Bestandseigenaar wijzigen	        os.chown("/tmp/tst", 33, 33)	chown www-data:www-data /tmp/tst
#   Bestand verwijderen	                os.remove("/tmp/tst/file")	    rm /tmp/tst/file
#   Lege map verwijderen	            os.rmdir("/tmp/tst/a/b/c")	    rmdir /tmp/tst/a/b/c
#   Niet-lege map verwijderen	        shutil.rmtree("/tmp/tst/a")	    rm -r /tmp/tst/a


# maakt een list van al de directory
import os

directory_content = os.listdir("./")
print(directory_content)  # list
# vb. ['.idea', '.venv', 'demo.txt', 'main.py', 'README.md', 'testmap']


# print een lijst af regel per regel met de directory
import os

for rootdir, dirs, files in os.walk('.'):  # walk is echt bedoeld om te gebruiken in een lus
    print(f"directory {rootdir} has {len(dirs)} subdirectories and {len(files)} files")

# vb
# directory .\.idea\inspectionProfiles has 0 subdirectories and 1 files
# directory .\.venv has 3 subdirectories and 3 files
# directory .\.venv\Include has 0 subdirectories and 0 files