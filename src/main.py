# Copyright (C) 2025 by Mahdi Hosseini Asaad
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from PIL import Image, ImageTk
import random
import os
import sys


def errorfunc ():
    print ( "A problem occurred. Is the contents of the Images folder empty?" )
    sys.exit ( -1 )

def myrandom ( mylist ): # This function returns a random element from a list such that no element is repeated consecutively.
    if not mylist: errorfunc ()
    if not hasattr ( myrandom, "previous" ):   myrandom.previous = None
    choices = [ item for item in mylist if item != myrandom.previous ]
    choice  = random . choice ( choices )
    myrandom.previous = choice
    return choice

page  = Tk ()
page  . title ("Py Violin Sheet - Version 0.0.1")

imlbl = Label(page)
imlbl . pack ()

imlbl = Label ( page, font = ( "Arial", 30 ) )
imlbl . pack ()

page  . mainloop ()