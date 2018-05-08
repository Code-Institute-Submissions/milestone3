Phil Surgenor - Milestone Project 3
===

<br>

## Practical Python
[visit the project website here](https://philsurgenor.github.io/milestone3/)

For this project, I decided to build a game called 'Guess The Phrase' (working title). 

Below is a short step by step guide to how the game will work.

1 - Enter a username & press 'LET'S GO' button <br>
2 - Q1 appears on next page as an image <br>
3 - User writes answer in text input box and presses 'GUESS' button <br>

4 - If answer is correct:

            - Add 50 points to user's score
            - Navigate to next question
            
If answer is incorrect:

            - Take off 1 life
            - Print wrong answer above text input box
            
5 - If user presses 'PASS' button instead, navigate to next question <br>
6 - When all questions have been answered / passed on or user runs out of lives navigate to game-over page

            - Display user's final score
            - Print a list of all users' scores in table form

<br>

## Technologies

 - Balsamiq Mockups
 - HTML 5
 - CSS 3
 - Bootstrap 4
 - Javascript / jQuery
 - Python & Flask

<br>

## Testing

You will be able to find all my automated tests in the folder game-tdd. Any manual tests will also be clearly documented below.

There is also a file called python_console_game.py in this folder. Before introducing my code into flask I have decided to a simple version of the game that will work in the python console. As I test and create new functionality, I will add it to the simple game so I'm sure it works before things get too complicated with the web app.

### Verifying and Adding Users to a .txt file

The first set of tests can be found in add_username_test.py. For this, the test usernames were stored in a list. I was able to assertain that my tests were running correctly and I could pick up wether the username was left blank, wether it already existed in the list or wether it was unique.

Once I was sure my tests were running correctly, I created a new file called verify_username_test.py. The three tests carried out are very simialer to the first set, but this time the test usernames were stored in a .txt file. I was also able to append new unique usernames to this file.

