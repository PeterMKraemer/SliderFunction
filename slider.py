#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:20:15 2018
@author: peterkraemer
"""

from expyriment import control, stimuli,io
import numpy as np
import pygame
from pygame.locals import *

#control.set_develop_mode(True)

exp = control.initialize()
######################  STIMULI  ######################
#   creating elements on screen

# picture
path_picture =   '/Users/peterkraemer/Desktop/experiment/PICTURES/snack1.bmp'
picture      =   stimuli.Picture(path_picture, position=(0,200))

# bar
barLength = 300
barThick = 10
posBar=(0,-100)
bar = stimuli.Rectangle((barLength,barThick),corner_rounding=None,position=posBar)
bar.preload()
barEndLeft = stimuli.Rectangle((5,barThick*3),position=((-(barLength+2)/2), posBar[1]))
barEndLeft.preload()
barEndRight = stimuli.Rectangle((5,barThick*3),position=(((barLength+2)/2), posBar[1]))
barEndRight.preload()

# slider
posSlider = (0,posBar[1]) # initial position of the slider


#def MoveSlider():
#    
#    key2 = exp.keyboard.check(keys=None, check_for_control_keys=True)
#    if key2 == 275:
#        pos = (pos[0]+10, pos[1])
#        if pos[0] > barLength/2: # fixes upper end of the scale
#            pos = (barLength/2,pos[1])
#    elif key2 == 276:
#        pos = (pos[0]-10, pos[1])
#        if pos[0] < -barLength/2: # fixes lower end of the scale
#            pos = (-barLength/2,pos[1])
#    Presenting(pos)
##
#
##            
##
##    
##
#exp.register_wait_callback_function(MoveSlider)
#
def PlotStimuli(pos):
    composition = stimuli.BlankScreen()
    picture.plot(composition)
    bar.plot(composition)
    barEndLeft.plot(composition)
    barEndRight.plot(composition)
    slider = stimuli.Rectangle((3,30),position=pos, colour = (194, 24, 7))
    slider.plot(composition)
    composition.present()



# sliding function
def sliding(pos,commit):
    while commit==0:
#         create a composition to show multiple elements at the same time
        keys=pygame.key.get_pressed()
        if keys[K_RIGHT]:
            pos = (pos[0]+10, pos[1])
            if pos[0] > barLength/2: # fixes upper end of the scale
                pos = (barLength/2,pos[1])
        elif keys[K_LEFT]:
            pos = (pos[0]-10, pos[1])
            if pos[0] < -barLength/2: # fixes lower end of the scale
                pos = (-barLength/2,pos[1])
        PlotStimuli(pos)           
        
        
        
#        print (keys[K_LEFT])
#        key, rt = exp.keyboard.wait(keys=[13,275,276], duration=None, wait_for_keyup=False, callback_function=MoveSlider(pos), process_control_events=True)
        key,rt= exp.keyboard.wait(keys=[13], duration = 50)
#        key=exp.keyboard.check()
#        MoveSlider
        if key == 13:
            commit = 1
            return pos[0]
#        elif key == 275:
#            pos = (pos[0]+10, pos[1])
#            if pos[0] > barLength/2: # fixes upper end of the scale
#                pos = (barLength/2,pos[1])
#        elif key == 276:
#            pos = (pos[0]-10, pos[1])
#            if pos[0] < -barLength/2: # fixes lower end of the scale
#                pos = (-barLength/2,pos[1])
#        Presenting(pos)
#        exp.clock.wait(100)

# position - money translation
scaleMax = 5 # upper end of the scale
moneyPerPixel=scaleMax/barLength # = CHF/Pixel

## start ##
control.start(exp,skip_ready_screen=True)
Presenting(posSlider)
#pos=posSlider

    
val = (sliding(posSlider,0)-(-barLength/2))*moneyPerPixel
#key, rt = exp.keyboard.wait(keys=13, duration=None, wait_for_keyup=False, callback_function=MoveSlider(), process_control_events=True)
#val=posSlider[0]
print(val)

## end ##
control.end()