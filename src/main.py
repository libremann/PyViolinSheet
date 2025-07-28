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

image_folder = "./Images"

image_names = [f for f in os.listdir(image_folder) if f.lower().endswith(".png")] # Create a list from the image files name


def errorfunc ():
    print ( "A problem occurred. Is the contents of the Images folder empty?" )
    print ( "Is it not empty? you can send a message to my email or Telegram. The contact information is available on my GitHub profile page.")
    print ("If you're experiencing an issue, please describe it on the following page so we can address it as quickly as possible:" )
    print ( "\nGithub : https://github.com/libremann" )
    print ("\nEnjoy :) ")
    sys.exit ( -1 )

def myrandom ( mylist ): # This function returns a random element from a list such that no element is repeated consecutively.
    if not mylist: errorfunc ()
    if not hasattr ( myrandom, "previous" ):   myrandom.previous = None
    choices = [ item for item in mylist if item != myrandom.previous ]
    choice  = random . choice ( choices )
    myrandom.previous = choice
    return choice

def update_image():
    FP = myrandom ( image_names ) # Get a random image 
    img_path = os.path.join ( image_folder, FP )

    img = Image.open ( img_path )
    img = img.resize ( ( 400, 300 ) )
    tk_img = ImageTk.PhotoImage ( img )

    imlbl.config ( image = tk_img )
    imlbl.image = tk_img
 
    txtlbl.config ( text = os.path.splitext ( FP )[0] )

    page.after ( 4000, update_image ) # 4 Secounds to show a new random image!

page  = Tk ()
page  . title ("Py Violin Sheet - Version 0.0.1")

imlbl = Label ( page )
imlbl . pack ()

txtlbl = Label ( page, font = ( "Arial", 30 ) )
txtlbl . pack ()

update_image ()

page  . mainloop ()