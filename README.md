<h2> Little Projects!</h2>

This repository is full of little oddball projects we've made over the years that do... things! Some of them were built to solve puzzles, some of them were made to back up jokes, a few of them are just little time-savers or ways to check something. And none of them is really enough on their own to constitute a whole project, although some of them here or there ended up taking a lot longer to work out than expected, those are the best learning opportunities!

**Contents:**

- <i>Number Word &lt;cough&gt;</i>: Containing two useable functions, this script builds up a list of words that can be made with number/letter exchanges (like EGOIST/360157). Mainly used to work playful jokes into embedded numbers, like costs, bills, things like that.

- <i>Morse Trial</i>: A suite of functions which interpret morse code, with the assumption that you get the dots and dashes raw, without spacing or delimiters. It does so by using a dynamic partition divide and conquor algorithm to check paired subsequences and throw out any which have either side invalid at any point detected. Fun fact, even simple messages often have thousands of possible solutions, even when allowing only translated strings which are comprised of valid english words only!

- <i>Math Game</i>: A small game file written in processing that prompts the player to solve simple arithmetic problems with a point feedback system proportional to the time taken to answer the questions. A project meant to experiment with and build processing interface utilities, it implements multiple asynchronous timers, toggle and momentary buttons, a state machine, and an assortment of graphics modes. Mainly a toy project to get all those things working together.

- <i>Dog Vision</i>: A script which loads images from a source directory and converts them to an image scaling which is designed to emulate to visual color sensitivities of canine eyes. It is based research into the spectral sensitivity of canine cone receptors and color image mapping transforms for spectral shifting on different monitors (mainly weighted geometric averaging and the gamma transform). It _doesn't_ just remove red and scale down green- it re-maps the color spectrum to account for cross-spectrum dichromism.

- _simpleIRC_: A very light duty and basic IRC client we made in college that interfaced Python to a chat programatically. It exposes an interface for messaging, detecting addresses and mentions, and replying on a script level. As a result, it definitely supports bots, and we did connect a couple to it back in the day (long gone AIML chatter bots and one choose your own adventure bot), but mostly we actually used it to be a more convenient, stripped down chat client with a simple text-input CLI, and attached a couple easy-make features, like timers and calculators, that we wanted to have at our fingertips in the circles we ran in. Maybe technically obsolete, is IRC still active?

