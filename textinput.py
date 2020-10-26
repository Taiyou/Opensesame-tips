from __future__ import absolute_import, division

import psychopy
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
from psychopy.hardware import keyboard

# Store info about the experiment session
endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
# Setup the Window
# store frame rate of monitor if we can measure it
frameDur = 1.0 / round(win.getActualFrameRate())

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "textBox"
textBoxClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="ペアーの文字を入力してください (スペースで次に進みます)",
    font='ヒラギノ角ゴシック W5',
    pos=(-100, 300), height=50, 
    wrapWidth=None, ori=0, 
    color=[1.000, 1.000, 1.000],
    colorSpace='rgb',
    opacity=1, 
    languageStyle='LTR',
    depth=0.0);

TextBox = visual.TextBox2(
     win, text='ここです', font='ヒラギノ角ゴシック W5',
     pos=(-300, 200),     letterHeight=32,
     size=(700, 300), borderWidth=2.0,
     color=[-1.000, -1.000, -1.000],
     colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.015,
     anchor='top-left',
     fillColor=[1.000, 1.000, 1.000], 
     borderColor=[-1.000,-1.000,-1.000],
     flipHoriz=False, flipVert=False,
     editable=True,
     name='TextBox',
     autoLog=True,
)
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "textBox"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
textBoxComponents = [text, TextBox, key_resp]
for thisComponent in textBoxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
textBoxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "textBox"-------
while continueRoutine:
    # get current time
    t = textBoxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=textBoxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)

    # *TextBox* updates
    if TextBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextBox.frameNStart = frameN  # exact frame index
        TextBox.tStart = t  # local t and not account for scr refresh
        TextBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextBox, 'tStartRefresh')  # time at next scr refresh
        TextBox.setAutoDraw(True)

    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in textBoxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "textBox"-------
TextBox.setAutoDraw(False)
for c in win._editableChildren:
    if c() == TextBox:
        win._editableChildren.remove(c)

log.write_vars()

# the Routine "textBox" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()
