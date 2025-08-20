Whack-a-Mole

Description

This is a classic Whack-a-Mole game built with Pygame. The objective is to click as many green "moles" as you can before the time runs out. Be careful not to click the red decoys, as this will decrease your score! This game also tracks your high score and lifetime accuracy(I think).

How to Play

    Start the game: Run the Python script. You'll see a menu screen. Click the "Start" button to begin.

    Whack the moles: Green and red circles will appear on the screen and start moving.

    Click the green moles: Each time you click a green mole, your score increases by one.

    Avoid the red moles: Clicking a red mole will decrease your score by one.

    Beat the clock: You have 10 seconds to reach the target score of 10 points.

    Win or Lose:

        If you reach the target score before the timer runs out, you win!

        If the timer runs out before you reach the target score, you lose.

Features

    Classic Whack-a-Mole Gameplay: Fast-paced action that tests your reflexes.

    Scoring System: Gain points for hitting the correct mole and lose points for hitting the wrong one.

    Timer: A 10-second timer adds a sense of urgency to the game.

    High Score Tracking: The game saves and displays your highest score.

    Click Analytics: The game tracks your lifetime total clicks and clicks on the target to calculate and display your accuracy.

    Sound Effects: The game includes sounds for various events, such as starting the game, winning, and losing.

Requirements

    Python 3.x

    Pygame library

Setup and Installation

    Install Python: If you don't have Python installed, download it from python.org.

    Install Pygame: Open your terminal or command prompt and run the following command:
    Bash

pip install pygame

Download the Game Files: Make sure you have all the game files in the same directory:

    Pygame_Project_Julian_110424.py (or PygameProject.py)

    highscore.txt

    totalclick.txt

    target_clicks.txt

    All the .mp3 sound files.

Run the Game: Open your terminal or command prompt, navigate to the directory where you saved the files, and run the following command:
Bash

    python Pygame_Project_Julian_110424.py

Sound Files

This game uses the following sound files:

    youwin.mp3: Plays when you win the game.

    Slap.mp3: Plays when you successfully hit a mole.

    gameover.mp3: Plays when you lose the game.

    wrongmole.mp3: Plays when you hit a red decoy mole.

    loading.mp3: Plays when the game is loading.

    bossmusic.mp3: Plays during the game.

