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
import tkinter.font as font

from PIL import Image, ImageTk

import random
import os
import sys

from modules import string

image_names_1 = [f for f in os.listdir("./Images/1") if f.lower().endswith(".png")] # Create a list from the image files name
image_names_2 = [f for f in os.listdir("./Images/2") if f.lower().endswith(".png")] # Create a list from the image files name
image_names_3 = [f for f in os.listdir("./Images/3") if f.lower().endswith(".png")] # Create a list from the image files name
image_names_4 = [f for f in os.listdir("./Images/4") if f.lower().endswith(".png")] # Create a list from the image files name

image_names = image_names_1 + image_names_2 + image_names_3 + image_names_4 # This is temporary and can be changed.


def update_image ():
    FP = string.myrandom ( image_names ) # Get a random image 
    img_path = os.path.join( ( "Images/"+FP[FP.find ('S=')+2:FP.find ('S=')+3] ), FP )
    
    img = Image.open ( img_path )
    img = img.resize ( ( 400, 350 ) )
    tk_img = ImageTk.PhotoImage ( img )

    imlbl . config ( image = tk_img, borderwidth = 0, relief = "flat", highlightbackground = "white", highlightthickness = 1 )
    imlbl . image = tk_img

    Handlbl . config ( text = FP[FP.find ('H=')+2:FP.find ('H=')+3] )
    Strlbl  . config ( text = FP[FP.find ('S=')+2:FP.find ('S=')+3] )
    Notelbl . config ( text = string.Fixedsize ( FP[FP.find ('N=')+2:-4] ) )

    page.after ( 4000, update_image ) # 4 Secounds to show a new random image!




page  = Tk ()
page  . title ( "Py Violin Sheet - Beta" )
page  . config ( bg = "white" )
page  . resizable ( False, False )

Fontmono = font.Font ( family = "Fonts/Roboto Mono.ttf", size=30 )

imlbl = Label ( page )
imlbl . pack ()


txtfrm = Frame ( page, bg = "white" )
txtfrm . pack ()

HandI   = ImageTk.PhotoImage ( Image.open ( "./Icons/hand.png" ) . resize ( (50, 50) ) )
Handlbl = Label ( txtfrm, image=HandI, bg = "white" )
Handlbl . pack  ( side = LEFT, padx = 5 )
Handlbl = Label ( txtfrm, text="Fin", font = Fontmono, fg = "black", bg = "white" )
Handlbl . pack  ( side = LEFT, padx = 5 )

StrI    = ImageTk.PhotoImage ( Image.open ( "./Icons/string.png" ) . resize ( (50, 50) ) )
Strlbl  = Label ( txtfrm, image=StrI, bg = "white" )
Strlbl  . pack  ( side = LEFT, padx = 5 )
Strlbl  = Label ( txtfrm, text="Str", font = Fontmono, fg = "black", bg = "white" )
Strlbl  . pack  ( side = LEFT, padx = 5 )

noteI   = ImageTk.PhotoImage ( Image.open ( "./Icons/note.png" ) . resize ( (50, 50) ) )
Notelbl = Label ( txtfrm, image=noteI, bg = "white" )
Notelbl . pack  ( side = LEFT, padx = 5 )
Notelbl = Label ( txtfrm, text="Note", font = Fontmono, fg = "black", bg = "white" )
Notelbl . pack  ( side = LEFT, padx = 5 )


update_image ()

page . mainloop ()
