import os
import random
import sys

def main():
    # Pass an insult file in as a command line argument, like so.. 'C:\Users\username\Desktop\insults.txt'
    # or you can add insults to the file provide
    counter = 0

    if len(sys.argv)>1:
        insultFile = sys.argv[1]
    else:
        insultFile = './insults.txt' 
    if os.path.isfile(insultFile):
        insults = 'yes'
        file = open(insultFile, 'r')
        list = file.readlines()
    else:
        insults = "no"
    print "Welcome to guess the number\n==========================="
    print "\nI'm thinking of a number, you have to guess what it is.\n"

    num = random.randrange(100)
    guess = ""

    while guess != num:
        guess = int(raw_input("Take a guess: "))
        if guess < num:
            if insults == "yes":
                print random.choice(list)
            print "Guess higher next time\n"
            counter=counter+1
        elif guess > num:
            if insults == "yes":
                print random.choice(list)
            print "Guess lower next time\n"
            counter=counter+1
    print "!!***CONGRATULATIONS***!!"
    print 'It took you this many tries: ', counter
    print 'Beat that!'
    raw_input()
    if insults == "yes":
        file.close()

main()  
