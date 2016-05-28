import random
import urllib
import time
import pygame

class wordGen():

    def __init__(self):
        print raw_input("Hangman <Press Enter>")
        print "Loading... Please wait"

    def lstWord(self):
        self.words = []
        self.fhand = urllib.urlopen('http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt')
        #time.sleep(5)
        for self.line in self.fhand:
            self.line = ''.join(self.line.rstrip())
            self.words.append(self.line)

    def choiceWord(self):
        self.hangWord = list(''.join(random.choice(self.words)))
        print "List hangWord for comparison: ", self.hangWord

    def lengthWord(self):
        self.lhw = len(self.hangWord)
        print "self.lhw is a ", type(self.lhw)

    def alreadyletter(self):
        self.alr = []

    def checkWord(self):
        self.fillword = []
        self.fillword.append('_, '* self.lhw)
        self.fillword = '_,'.join(self.fillword).split(',')
        self.fillword.remove(' ')
    #
    def firstLine(self):
        self.intro = raw_input('You have 10 lives, the word is %d letters long, good luck!\nContinue...' %self.lhw)
        print self.intro
        print "Str word for display: ", ''.join(self.fillword)


    def replay(self):
        again = raw_input("Play again 'yes or 'no'? ")
        print again
        if again == 'yes':
            print "Loading... Please wait"
            g.lstWord()
            g.choiceWord()
            g.lengthWord()
            g.alreadyletter()
            g.checkWord()
            g.firstLine()
            g.chances()
            g.game_loop()

        else:
            raw_input('<Press Enter to exit>')
            exit()

    def chances(self):
        self.life = 10

    def game_loop(self):

        while True:
            self.guess = raw_input("Please guess a letter in word or the whole word: ").lower()
            self.guestWholeWord = list(self.guess)

            if self.guestWholeWord == self.hangWord:
                print ''.join(self.guestWholeWord)
                print raw_input('Correct! <Press Enter>')
                g.replay()

            if self.guess in self.alr:
                print "You have already guessed %s, try again" %self.guess
            elif self.guess in self.hangWord:
                self.pos = self.hangWord.index(self.guess)
                for self.pos, self.ltr in enumerate(self.hangWord):
                    if self.ltr == self.guess:
                        self.fillword[self.pos] = self.ltr
                print 'Correct!\n', ' '.join(self.fillword)

                if self.fillword == self.hangWord:
                    print raw_input('Correct! <Press Enter>')
                    g.replay()

            else:
                self.life -= 1
                print 'You are incorrect, you have %d life left' %self.life
                if self.life == 0:
                    print 'You loose!, the word was: ', ' '.join(self.hangWord)
                    g.replay()

            self.alr.append(self.guess)
g = wordGen()
g.lstWord()
g.choiceWord()
g.lengthWord()
g.alreadyletter()
g.checkWord()
g.firstLine()
g.chances()
g.game_loop()
