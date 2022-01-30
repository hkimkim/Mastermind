# MasterMind for Single Player 

Author: Heekyung Kim  
Date: April 23, 2021

## Description: 

This program simulates the MasterMind Game for one player via GUI. The program creates 4 color secret code, which the player must guess within 10 rounds. The player is given hints via score key pegs each round, where black peg represents correct color in correct position of the player's guess and red peg represents correct color but out of position.

## Design
This program was designed based on the Model-View-Controller software design. 
The View is the GUI of the game screen, which receives user input through screen click event and displays data retrieved from Model. The Model is the game data, where the data for game is stored and manipulated upon player request. The Controller was the bridge between the GUI and the data of the program.

## How to Run the Program in the terminal

``` 
python3 mastermind.py
```

## Files included in the program:
- constants.py: Python file that contains all the constants  
- Controller.py: Python file with Controller class that links data and GUI  
- Model.py: Python file with Model class that manages game data  
- View.py: Python file with View class that manages GUI  
- mastermind.py:  driver file to run the game  
- test_mastermind_game.py: Test file for the Model class that test the game functions (PyUnit)  

**/gui**			&emsp;&emsp;&emsp;&emsp;	   Directory that contains class files used in View.py  
   Board.py &emsp;&emsp;&emsp;&emsp;			Python file with Board class  
   Button.py &emsp;&emsp;&emsp;&emsp;	Python file with Button class  
   Marble.py &emsp;&emsp;&emsp;&emsp;	Python file with Marble class  
   Point.py	&emsp;&emsp;&emsp;&emsp;		Point file with Point class  
   Pointer.py &emsp;&emsp;&emsp;&emsp;	Pointer file with Pointer class  
   Popup.py	&emsp;&emsp;&emsp;&emsp;		Popup file with PopUp class  

**/img**		&emsp;&emsp;&emsp;&emsp;		            Directory that contains all the gif used in the program  
   checkbutton.gif   &emsp;&emsp;&emsp;&emsp;     image for check button  
   file_error.gif		&emsp;&emsp;&emsp;&emsp;      image for file error message  
   leaderboard_error.gif &emsp;&emsp;&emsp;&emsp;	image for leaderboard file error message  
   logo.gif	&emsp;&emsp;&emsp;&emsp;		         image for logo  
   Lose.gif	&emsp;&emsp;&emsp;&emsp;		         image for lose message  
   quit.gif	&emsp;&emsp;&emsp;&emsp;		         image for quit button  
   quitmsg.gif	&emsp;&emsp;&emsp;&emsp;		      image for quit message  
   start.gif	&emsp;&emsp;&emsp;&emsp;		      image for start button  
   winner.gif	&emsp;&emsp;&emsp;&emsp;		      image for win message  
   reset.gif	&emsp;&emsp;&emsp;&emsp;		      image for reset button  

## Languages/Modules used:
 - Python
 - PyUnit
 - python turtle module
 - time 
 - random