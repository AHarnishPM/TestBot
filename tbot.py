import time
import random
from textwrap import wrap


def instr():
    req = raw_input("> ")

    if "?" in req:
        list()
    elif req == "add":
        add()
    elif req == "sub":
        sub()
    elif req == "q":
        quit()
    elif req == "mult":
        mult()
    elif req == "div":
        div()
    elif req == "echo":
        echo()
    elif req == "lmem":
        memlines()
    elif req == "cmem":
        memclear()
    elif req == "amem":
        memadd()
    elif req == "rmem":
        memread()
    elif req == "smem":
        memsrc()
    elif req == "knockknock":
        knockknock()
    elif req == "vault":
        vault()
    elif req == "revecho":
        revecho()
    else:
        print "Invalid command, type '?' if you're confused"
        instr()


def list():
    print "?: list of commands"
    print "q: exit program"
    print "add: add two numbers together"
    print "sub: subtract second number from first number"
    print "mult: multiply two numbers together"
    print "div: divide first number by second number"
    print "echo: returns the input"
    print "lmem: counts amount of lines in memory"
    print "cmem: clears memory file"
    print "amem: adds a line of data in to the end of memory file"
    print "rmem: reads memory file"
    print "smem: searches memory for lines containing a certain string"
    print "knockknock: Tell a knock knock joke to the bot"
    print "vault: game where you try to guess a vault code"
    print "revecho: reverses order of word inputed"
    instr()

def quit():
    exit

def add():
    num1 = int(raw_input("First Number:"))
    num2 = int(raw_input("Second Number:"))
    total = num1 + num2
    print total
    instr()

def sub():
    num1 = int(raw_input("First Number:"))
    num2 = int(raw_input("Second Number:"))
    total = num1 - num2
    print total
    instr()

def mult():
    num1 = int(raw_input("First Number:"))
    num2 = int(raw_input("Second Number:"))
    total = num1 * num2
    print total
    instr()

def div():
    num1 = int(raw_input("First Number:"))
    num2 = int(raw_input("Second Number:"))
    total = num1 / num2
    print total
    instr()

def echo():
    input = raw_input("input: ")
    print "output: " + input
    instr()

def memlines():
    file = open("mem.txt", 'r')
    linecount = 0

    content = file.read()
    linelist = content.split("\n")

    for i in linelist:
        if i:
            linecount += 1

    print "mem.txt has %r lines" % linecount

    file.close()
    instr()

def memclear():
    file = open("mem.txt", 'w')
    file.truncate

    print "cleared mem.txt"
    file.close()
    instr()

def memadd():
    file = open("mem.txt", 'a')
    file.write("\n" + raw_input("String to add> "))
    file.close()

    instr()

def memread():
    file = open("mem.txt", 'r')
    output = file.read()
    print output
    file.close()

    instr()

def memsrc():
    file = open("mem.txt", "r")
    content = file.read()
    linelist = content.split("\n")

    srcword = raw_input("Search for> ")

    for i in linelist:
        if len(i) > 1 and srcword in i:
            print i
        else:
            pass
    file.close()

    instr()

def knockknock():
    tslp = 0.5
    print "USER> Knock Knock"
    time.sleep(tslp)
    print "TBOT> Who's there?"
    time.sleep(tslp)
    kline1 = raw_input("USER> ")
    time.sleep(tslp)
    print "TBOT> " + kline1 + " who?"
    time.sleep(tslp)
    raw_input("USER> ")
    time.sleep(tslp)
    print "TBOT> Very funny."

    instr()

def vault():

    s = 0.5

    print "There's a vault with all of your money in it, but there's an issue."
    time.sleep(1.5)
    print "You have amnesia."
    time.sleep(s)
    print "Luckily for you, you only made the code two digits."
    time.sleep(s)
    print "Guess away!"
    print "(if you're a pansy, type decrypt to find the actual code)"
    print "(or just type q to leave the game)"

    vcode = str(random.randint(0, 9)) + str(random.randint(0,9))

    while True:
        guess = raw_input("CODE> ")

        if guess == vcode:
            print "You got in!"
            print "Sadly, you forgot that you put the money in a bank account."
            break

        elif guess == "decrypt":
            print "I'm dissapointed in you."
            time.sleep(3)
            print vcode

        elif guess == "q":
            break

        else:
            print "WRONG CODE"

        instr()

def revecho():
    inw = raw_input("Word> ")
    inletters = wrap(inw, 1)

    inletters.reverse()

    o = 0
    string = ">"
    for i in inletters:
        string = string + str(inletters[o])
        o += 1

    print string

    instr()


print "I am TestBot. What would you like to do?"
print "\"?\" for list of commands"


instr()
