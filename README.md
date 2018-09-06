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
            
5 - If user presses 'PASS' button instead, navigate to next question:

            - Every 3 passes will take off 1 life
            

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

You will be able to find all my automated tests in the folder **game-tdd**. Any manual tests will also be clearly documented below.

There is also a file called **python_console_game.py** in this folder. Before introducing my code into flask I have decided to a simple version of the game that will work in the python console. As I test and create new functionality, I will add it to the simple game so I'm sure it works before things get too complicated with the web app.

<br>

### Verifying and Adding Users to a .txt file

The first set of tests can be found in **add_username_test.py**. For this, the test usernames were stored in a list. I was able to assertain that my tests were running correctly and I could pick up wether the username was left blank, wether it already existed in the list or wether it was unique.

Once I was sure my tests were running correctly, I created a new file called **verify_username_test.py**. The three tests carried out are very simialer to the first set, but this time the test usernames were stored in a .txt file. I was also able to append new unique usernames to this file.

##### Manual Testing
Once the tests passed I transferred the code from both **add_username_test** and **verify_username_test** to **python_console_game**. There I manually tested the code by running the game in the console. Although the fundamentals of the code were correct, I had to adjust it slightly so that it would work inside the other functions in the game.

<br>

### Looping Through Questions
In the file **questions_test.py**, I have taken some of the code from the walkthrough project: Quiz Game. The code I have used takes a .txt file and splits the lines into questions and answers. I have used the print() function to manually test that both questions and answers go into to their respective lists.

Once I was sure this worked, I was able to bring the code into the **python_console_game.py** file so that it could loop through the questions and tell me if I was correct or not with my answers. I was also able to add a dynamic question_num function, that displayed the correct number of question being asked.

<br>

### Taking Off A Life Every 3 Passes
I have conducted 6 tests for this section. The tests can be found in **passed_questions_test.py**. The Tests were created to verify that every third question the user passed on 1 life was taken off. I also added some print statements so that I could manually check that the function was doing what it was supposed to. By using a loop in my tests, I could simulate a user passing a question one at a time rather than just giving the function a number, using number modulo 3 and using the result to determine how many lives to take off. This made it as close to real life as I could.

The functionality will be added to the **python_console_game.py** file.


<br>

### Final Scoring
In the file **scoring_test.py**, I have run five unit tests to calculate the final scoring of the game. This is the score that will be printed out after the game is completed. This code will then be placed into the **python_console_game.py** file. After some consideration, I decided A better gaming experience would be to have every 3rd pass take off a life. Therefore I have adjusted the code in **python_console_game.py** to only calculate the final score using correct answers and number of lives left. I will also include a function that will count every time a question is passed and take off a life every third pass.

When the game ends completely, either by finishing all the questions or by running out of lives, the game prints out a list of all the users and their scores. This was achieved by adding the username and score to **final_scores_test.txt** in the same way a username is added. Once this happens, another function triggers that prints all the usernames and scores. This was achieved in the same way as the **questions()** function logic works.


<br>

### Other Manual Tests
You will find a few other files within the **game-tdd** folder that are not specifically documented about here. These are functions that were tested manually. I decided to put each function in its own file while I was working on it. Once I was happy it produced the results I needed, the code was then intergrated with the main game.

After playing the game to conduct some manual tests, I noticed the **verify_username()** function was causing some problems. When I tried to add a username that already existed, I got the proper warning that the username was already taken. The problem was when I added a unique username after, it wasn't returned and therefore the score was saved in **final_scores_test.txt** with the username: none. I will try and fix this with a while loop. After replacing **If Statement** with **While Loop** the problem was fixed.
