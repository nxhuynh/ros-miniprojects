# Speech-controlled Turtlebot

## DESCRIPTION
This miniproject uses the speech recognition software pocketSphinx, and the 
HLP-R speech framework to develop a simple grammar for speech recognition 
and send commands to a turtlebot.

## CREDITS
hlpr-speech is cloned from https://github.com/HLP-R/hlpr_speech.git
(commit 86c2440263a0e193d7d2a6080397653ff1f5c49b)

## INSTRUCTIONS
1.    Install sphinxbase
    i.    Download the sphinxbase package from: https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/ (Links to an external site.)Links to an external site.
    ii.    Set up sphinxbase by following the tutorial: https://github.com/cmusphinx/sphinxbase (Links to an external site.)Links to an external site.
    ▪    Do not install from the github source files

2.    Install pocketsphinx
    i.    Download the pocketsphinx package from: https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/ (Links to an external site.)Links to an external site.
    ii.    Set up pocketsphinx by following the tutorial: https://github.com/cmusphinx/pocketsphinx (Links to an external site.)Links to an external site.

3.     Set up the HLP-R speech package (this is an open source codebase maintained across several groups working in computational HRI, faculty PIs include: Andrea Thomaz, Scott Niekum, Sonia Chernova, Baris Akgun)  Needless to say, do not push any of your changes back to the main HLP-R branch.
    i.    git clone the hlpr_speech repo into your workspace (https://github.com/HLP-R/hlpr_speech.git (Links to an external site.)Links to an external site.) 
    ii.    Run catkin_make from your workspace folder.   

4.    Creating a dictionary for the speech commands
    i.    The speech_listener and speech_gui have a parameter where you specify a .yaml file containing the mapping between keywords and speech commands. The default is kps.yaml file.  Create your own .yaml file for this project and put it in the hlpr_speech_recognition/data/ directory.
    ii.    The speech_recognizer makes use of pocketsphinx and needs three files in the hlpr_speech_recognition/data directory. First is a list of each speech phrase to be recognized in a text file, this is expected to be kps.txt.  Add your new commands here and then do step three to create the other files necessary.
    iii.    Go to the following link and generate the .dic and .lm file. Replace the previous files with the new ones and rename them 6858.dic and 6858.lm respectively.
    ▪    http://www.speech.cs.cmu.edu/tools/lmtool-new.html (Links to an external site.)Links to an external site.

5.    Running speech recognition: Now you should have the ability to recognize your limited grammar of speech commands.  
    i.    Running speech with mic input: roslaunch hlpr_speech_recognition speech_listener.launch
    ii.    Running speech with gui input: roslaunch hlpr_speech_recognition speech_rec.launch     

6.    Have your turtle listen and respond in some way to the topic hlpr_speech_commands

