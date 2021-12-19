
"""
Demo of the ElementArrayStim, a highly optimised stimulus for generating
arrays of similar (but not identical) elements, such as in global form
arrays or random dot stimuli.

Elements must have the same basic texture and mask, but can differ in any
other way (ori, sf, rgb...).

This demo relies on numpy arrays to manipulate stimulus characteristics.
Working with array vectors is fast, much faster than python for-loops, which
would be too slow for a large array of stimuli like this.

See also the starField demo.
"""

from __future__ import division

from builtins import range
from psychopy import visual, core, event
from psychopy.tools.coordinatetools import cart2pol
from numpy import sin, pi
import numpy as np
import pdb
import argparse

#How to run the code
#python 8dots.py --N=8 --theta=0.1 --circle_size=5 --distance_between_groups=100 --distance_between_points=10 --color 1 1 1
    
parser = argparse.ArgumentParser()
parser.add_argument('--N', help='number of points', default=8, type=int)
parser.add_argument('--theta', help='theta', default=0.05, type=float)
parser.add_argument('--circle_size', help='theta', default=10, type=int)
parser.add_argument('--distance_between_groups', help='distance_between_groups', default=100, type=int)
parser.add_argument('--distance_between_points', help='distance_between_points', default=10, type=int)
parser.add_argument('--color', help='color', default=[1,1,1], nargs='*') #black [-1,-1,1]
args = parser.parse_args()

# We only need these two commands from numpy.random:
from numpy.random import random, shuffle

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
    elementMask='circle', opacities=0.5)

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
theta=0

while not event.getKeys():
    # take a copy of the current xy and ori values
    newXYs = globForm.xys
    newOris = globForm.oris
    
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
    
    theta += args.theta
    distance_between_groups = args.distance_between_groups #100
    distance_between_points = args.distance_between_points #10
    #t=0
    #flicker_frequency = 30
    #current_frame = 1
    #while True:
    #When to draw stimuli
        #if current_frame % (2*flicker_frequency) < flicker_frequency :
        #    opacities = sin(theta)
       #    dot2.draw()
       #    dot2.draw()
         #   dot3.draw()
        #    dot3.draw()
         #   dot4.draw()
         #   dot4.draw()

     # Show whatever has been drawn. Sometimes the stimuli, other times a blank screen. flip() waits for the next monitor update so the loop is time-locked to the screen here.
  # increment by 1.
 # make a center fixed
    dot1 = [np.cos(theta)*distance_between_points-distance_between_groups/2-np.cos(90)*distance_between_points, np.sin(theta)*distance_between_points-distance_between_groups/2]	
    dot2 = [np.cos(theta+90)*distance_between_points-distance_between_groups/2-np.cos(90)*distance_between_points, np.sin(theta+90)*distance_between_points-distance_between_groups/2]
                    
    dot3 = [(np.cos(theta)*distance_between_points)-distance_between_groups/2-np.cos(90)*distance_between_points, (np.sin(theta)*distance_between_points)+distance_between_groups/2-np.sin(90)*distance_between_points]
    dot4 = [(np.cos(theta+90)*distance_between_points)-distance_between_groups/2-np.cos(90)*distance_between_points, (np.sin(theta+90)*distance_between_points)+distance_between_groups/2-np.sin(90)*distance_between_points]
                    
    dot5 = [(np.cos(theta)*distance_between_points)+distance_between_groups/2-10, (np.sin(theta)*distance_between_points)-distance_between_groups/2]
    dot6 = [(np.cos(theta+90)*distance_between_points)+distance_between_groups/2-10, (np.sin(theta+90)*distance_between_points)-distance_between_groups/2]
                    
    dot7 = [(np.cos(theta)*distance_between_points)+distance_between_groups/2-10, (np.sin(theta)*distance_between_points)+distance_between_groups/2-np.sin(90)*distance_between_points]
    dot8 = [(np.cos(theta+90)*distance_between_points)+distance_between_groups/2-10, (np.sin(theta+90)*distance_between_points)+distance_between_groups/2-np.sin(90)*distance_between_points]

    globForm.xys = [dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8]
    #pdb.set_trace()    
    #globForm.pris = 
    
    x = np.cos(theta)
    y = np.sin(theta)
    print(x, y)
    globForm.draw()

    win.flip()
    #current_frame += 1

    event.clearEvents('mouse')  # only really needed for pygame windows
	
    #t=0
    #flicker_frequency = 30
    #current_frame = 0
    #while True:
    # When to draw stimuli
    #    if current_frame % (2*flicker_frequency) < flicker_frequency :
    #        dot1.opacities = sin(t*pi*2)
        #    dot2.draw()
        #    dot2.draw()
         #   dot3.draw()
        #    dot3.draw()
         #   dot4.draw()
         #   dot4.draw()

     # Show whatever has been drawn. Sometimes the stimuli, other times a blank screen. flip() waits for the next monitor update so the loop is time-locked to the screen here.
    #win.flip()
    #current_frame += 1  # increment by 1.
win.close()
core.quit()

# The contents of this file are in the public domain.
