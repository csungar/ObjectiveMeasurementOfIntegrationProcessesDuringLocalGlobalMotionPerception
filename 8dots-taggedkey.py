
"""
Demo of the ElementArrayStim, a highly optimised stimulus for generating
arrays of similar (but not identical) elements, such as in global form
arrays or random dot stimuli.

Elements must have the same basic texture and mask, but can differ in any
other way (ori, sf, rgb...).

This demo relies on numpy arrays to manipulate stimulus characteristics.
Working with array vectors is fast, much faster than python for-loops, which
would be too slow for a large array of stimuli like this.

See also the star#xntaxField demo.
"""

from __future__ import division
#from psychopy import logging
#logging.console.setLevel(logging.INFO)

from builtins import range
from psychopy import visual, core, event
from psychopy.tools.coordinatetools import cart2pol
from numpy import sin, pi
#from experiment import *
#from copy import deepcopy

import numpy as np
import pdb
import argparse
import time

file = open('dataoutput.txt','w')
file.write(' NEW EXPERIMENT ')
#How to run the code
#python 8dots.py --N=8 --theta=0.1 --circle_size=5 --distance_between_groups=100 --distance_between_points=10 --color 1 1 1

parser = argparse.ArgumentParser()
parser.add_argument('--N', help='number of points', default=2, type=int)
parser.add_argument('--theta', help='theta', default=0.08, type=float)
parser.add_argument('--circle_size', help='theta', default=15, type=int)
parser.add_argument('--distance_between_groups', help='distance_between_groups', default=100, type=int)
parser.add_argument('--distance_between_points', help='distance_between_points', default=10, type=int)
parser.add_argument('--color', help='color', default=[1,1,1], nargs='*') #black [-1,-1,1]
args = parser.parse_args()

# We only need these two commands from numpy.random:
from numpy.random import random, shuffle

import psychopy.gui

gui = psychopy.gui.Dlg()

gui.addField("First Name:")
gui.addField("Last Name:")
gui.addField("Age:")
gui.addField("Gender (M/F):")

gui.show()
print gui.data


win = visual.Window([1366, 768], units='pix', monitor='testMonitor')

N = args.N #8
fieldSize = 500
elemSize = args.circle_size #15
coherence = 0.5
color = args.color #[1,1,1] (white)
#color distance (btw local/btw global) modify number of pairs
# build a standard (but dynamic!) global form stimulus
xys = random([N, 2]) * fieldSize - fieldSize / 2.0  # numpy vector
#pdb.set_trace()
#xys = [[0, 0], [20, 20],[20, 20],[20, 20],[20, 20],[20, 20],[20, 20],[20, 20]]
globForm = visual.ElementArrayStim(win=win,
    nElements=N, sizes=elemSize, elementTex=None,
    xys=xys, units='pix', colors=color, colorSpace='rgb',
    elementMask='circle')
globForm1 = visual.ElementArrayStim(win=win,
    nElements=N, sizes=elemSize, elementTex=None,
    xys=xys, units='pix', colors=color, colorSpace='rgb',
    elementMask='circle')
globForm2 = visual.ElementArrayStim(win=win,
    nElements=N, sizes=elemSize, elementTex=None,
    xys=xys, units='pix', colors=color, colorSpace='rgb',
    elementMask='circle')
globForm3 = visual.ElementArrayStim(win=win,
    nElements=N, sizes=elemSize, elementTex=None,
    xys=xys, units='pix', colors=color, colorSpace='rgb',
    elementMask='circle')
globForm4 = visual.ElementArrayStim(win=win,
    nElements=N, sizes=elemSize, elementTex=None,
    xys=xys, units='pix', colors=color, colorSpace='rgb',
    elementMask='circle')

'''
# calculate the orientations for global form stimulus
def makeCoherentOris(XYs, coherence, formAngle):
    # length along the first dimension:
    nNew = XYs.shape[0]


    # random orientations:
    newOris = [30, 60]

    # select some elements to be coherent
    possibleIndices = list(range(nNew))  # create an array of indices
    shuffle(possibleIndices)  # shuffle it 'in-place' (no new array)
    coherentIndices = possibleIndices[0: int(nNew * coherence)]

    # use polar coordinates; set the ori of the coherent elements
    theta, radius = cart2pol(XYs[: , 0], XYs[: , 1])
    newOris[coherentIndices] = formAngle - theta[coherentIndices]

    return newOris

#globForm.oris = makeCoherentOris(globForm.xys, coherence, 45)
'''
# Give each element a life of 10 frames, and give it a new position after that
lives = 1#random(N) * 10  # this will be the current life of each element
#x = 60
#y = 60

herts1=7
hertsval1=60/herts1
#hertsval1=240/herts1
herts2=9
hertsval2=60/herts2
#hertsval2=240/herts2
herts3=11
hertsval3=60/herts3
#hertsval3=240/4*herts3
herts4=13
hertsval4=60/herts4
#hertsval4=240/herts4

theta = 0
blinktheta = 0
centerdot=[0,0] # [x,y] for the invisible center dot for our other 8 dots to surround
squaresidesize = 100 # the size of the sides of the square divided by two
radius = 15 # the radius between a pair of circles

#No need to modify these as they are calculated from above.
stationarydot1 = [centerdot[0]-squaresidesize,centerdot[1]-squaresidesize]
stationarydot2 = [centerdot[0]+squaresidesize,centerdot[1]-squaresidesize]
stationarydot3 = [centerdot[0]+squaresidesize,centerdot[1]+squaresidesize]
stationarydot4 = [centerdot[0]-squaresidesize,centerdot[1]+squaresidesize]

flag = True
while flag==True:
    textStim = visual.TextStim(win, text = "Please press space bar to start. ")
    textStim.draw()
    win.flip()
    for keys in event.getKeys():
        if keys in ['space']:
            flag = False
textStim = visual.TextStim(win, text = "")
flag = True
left = False
right = False
timergoing = False
while flag==True:

    # take a copy of the current xy and ori values
    newXYs = globForm1.xys
    newOris = globForm1.oris

    # find the dead elemnts and reset their life
    #deadElements = (lives > 10)  # numpy vector, not standard python
    #lives[deadElements] = 0

    # for the dead elements update the xy and ori
    # random array same shape as dead elements
    #newXYs[deadElements, : ] = random(newXYs[deadElements, : ].shape) * fieldSize - fieldSize/2.0

    # for new elements we still want same % coherent:
    #new = makeCoherentOris(newXYs, coherence, 45)
    #newOris[deadElements] = [30, 60]

    # update the oris and xys of the new elements

    # delete + for stationary dots 
    theta = 0.2
    #dont change this blink speed, alter the frequencies using herts
    blinktheta += 0.1

    dot1 = [(np.cos(theta)*radius)+(stationarydot1[0]), (np.sin(theta)*radius)+(stationarydot1[1])]
    dot2 = [(np.cos(theta)*-radius)+(stationarydot1[0]), (np.sin(theta)*-radius)+(stationarydot1[1])]

    dot3 = [(np.cos(theta)*radius)+(stationarydot2[0]), (np.sin(theta)*radius)+(stationarydot2[1])]
    dot4 = [(np.cos(theta)*-radius)+(stationarydot2[0]), (np.sin(theta)*-radius)+(stationarydot2[1])]

    dot5 = [(np.cos(theta)*radius)+(stationarydot3[0]), (np.sin(theta)*radius)+(stationarydot3[1])]
    dot6 = [(np.cos(theta)*-radius)+(stationarydot3[0]), (np.sin(theta)*-radius)+(stationarydot3[1])]

    dot7 = [(np.cos(theta)*radius)+(stationarydot4[0]), (np.sin(theta)*radius)+(stationarydot4[1])]
    dot8 = [(np.cos(theta)*-radius)+(stationarydot4[0]), (np.sin(theta)*-radius)+(stationarydot4[1])]

    #globForm.xys = [dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8]
    #globForm.opacities = 0.2*np.sin(15*theta)+0.75
    
    globForm1.opacities=np.sin(hertsval1*blinktheta)*0.25+0.75
    globForm1.xys = [dot4,dot8]
    globForm2.opacities = np.sin(hertsval2*blinktheta)*0.25+0.75
    globForm2.xys = [dot3,dot7]
    globForm3.opacities = np.sin(hertsval3*blinktheta)*0.25+0.75
    globForm3.xys = [dot2,dot6]
    globForm4.opacities = np.sin(hertsval4*blinktheta)*0.25+0.75
    globForm4.xys = [dot1,dot5]

    #globForm.pris =

    x = np.cos(blinktheta)
    y = np.sin(blinktheta)
    #print(x,y)
    #file.write(x)

    globForm1.draw()
    globForm2.draw()
    globForm3.draw()
    globForm4.draw()
    text_cross = visual.TextStim(win, text = "+")
    text_cross.draw()

    textStim = visual.TextStim(win, text = "")
    for keys in event.getKeys():
        if keys in ['escape']:
            flag = False
        elif keys in ['right']:
            right = True
            left = False
        elif keys in ['left']:
            right = False
            left = True
        else: continue

    if right==True:
        textStim = visual.TextStim(win, text = "+")
       
        time = core.getTime()
        file.write('right pressed at time:'+str(time)+',')
        right = False  
        if timergoing == True:

            timergoing = False
    elif left==True:
        textStim = visual.TextStim(win, text = "+")
        file.write('left pressed at time:'+str(time)+',')
        left = False  
    
 
    textStim.draw()
    win.flip()

    lives = lives + 1
    event.clearEvents('mouse')  # only really needed for pygame windows
    

win.close()
file.close()
core.quit()