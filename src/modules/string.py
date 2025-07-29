from tkinter import *
import tkinter.font as font

from PIL import Image, ImageTk

import random
import os
import sys

def Fixedsize ( text ) :
    if len ( text ) == 2:
        return text + " "
    return text


def myrandom ( mylist ): # This function returns a random element from a list such that no element is repeated consecutively.
    if not mylist: errorfunc ()
    if not hasattr ( myrandom, "previous" ):   myrandom.previous = None
    choices = [ item for item in mylist if item != myrandom.previous ]
    choice  = random . choice ( choices )
    myrandom.previous = choice
    return choice


def errorfunc ():
    print ( "A problem occurred. Is the contents of the Images folder empty?" )
    print ( "Is it not empty? you can send a message to my email or Telegram. The contact information is available on my GitHub profile page.")
    print ("If you're experiencing an issue, please describe it on the following page so we can address it as quickly as possible:" )
    print ( "\nGithub : https://github.com/libremann" )
    print ("\nEnjoy :) ")
    sys.exit ( -1 )
