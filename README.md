![alt text](fds-pacman2.png)

# Introduction
Hello, and welcome to your take-home assignment for the Forward Deployed Solution Engineer role at C3! First, thank you for your time and energy spent in this process; we fully understand that you probably have a million other things to do, but this is an important screening step before moving into the advanced stages of interviews.

Your assignment is to write a program that navigates a 2-dimensional board covered in coins which are picked up as you move over them, much like the game of Pac-Man. Your program will take a single file input which contains 4 components: `board_dimension`, `initial_position`, `movements`, and `walls`.

Coins are in every position of the rectangular board except for the positions that have `walls` and the `initial_position`. If Pac-Man is instructed to move into a wall (on the perimeter of the board or as defined by the `walls` input) it should have no effect (Pac-Man stays in place).

# Program Input
Your program will take as input the name of a text file (ie. "input.txt") residing in the same directory as your code, and that contains the following inputs:

1. `board_dimension` is given on the first line. It is defined by [X and Y coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinate_system), identifying the top right corner of the room rectangle - that is to say, (0,0) is in the bottom left corner, and (X,Y) is in the top right corner. This board is divided up in a grid based on these dimensions; a board that has dimensions `X=5` and `Y=5` has 5 columns and 5 rows for 25 possible positions.
2. `initial_position` is given on the second line. It is the initial position of Pac-Man in (x,y) coordinates.
3. `movements` are given on the third line. They are instructions in [cardinal directions](https://en.wikipedia.org/wiki/Cardinal_direction) where e.g. N and E mean "go north" and "go east", respectively. The board is oriented facing north; thus, moving north from (0,0) lands Pac-Man at (0,1).
4. `walls` are given on the remaining lines. They are the positions of walls on the board in (x,y) coordinates. Pac-Man cannot move through walls. Note: Many modern text editors automatically add in a newline character to the end of the file. These trailing newline characters should be ignored.

For an input file to be valid, it must contain a `board_dimension`, an `initial_position` and at least one movement in `movements`.

Example input values:
```
5 5
1 2
NNESEESWNWW
1 0
2 2
2 3
```

The above input should inform your program that you have a 5 x 5 board with walls placed at positions `[(1,0),(2,2),(2,3)]`. Pac-Man will start at position `(1,2)` and will "attempt" to move in the following sequence: `N-N-E-S-E-E-S-W-N-W-W`.

# Program Output
Given the inputs described above, your program should have two outputs:

- Pac-Man's final location in (x,y)
- The number of coins that have been collected across all movements

Your program output should be in the form of returned values from your `pacman` function, and follow the format specified in the starter code files in the git repo.

Example (matching the input above):  

Python:
```py
# finalXposition, finalYposition, totalCoins
return (1, 4, 7)
```
Javascript:
```js
// [finalXposition, finalYposition, totalCoins]
return [1, 4, 7]
```
We will be testing edge cases on your code, so if there are any problems with the inputs, execution of the instructions, or any other cases you can think of, have your `pacman` function return `[-1, -1, 0]` (js) or `(-1, -1, 0)` (py).

# Getting Started
1. Clone this git repository and build your solution using the files in starter_code
2. Once you think you have a working solution, test it with the 3 sample test files we have provided (instructions are within the test_files folder)
3. Create your own test files
4. Ensure your code runs with our test scripts smoothly - this is exactly how we'll be testing your code (with our own tests) after submission

# Deliverable
## The program
- Must be written in Python or JavaScript following the starter code templates
- Can make use of any existing open source libraries that don't directly address the problem statement (use your best judgement).

## How to submit
Submit a zipped copy of the whole repository with your solution code and any tests you created in the correct test folder. For example, python solution code should be in the py_test folder and we should be able to run the test script without moving any of your files around.

# Evaluation Criteria
The point of the exercise is for us to see some of the code you wrote (and should be proud of). There isn't a single solution and the problem intentionally allows you creative freedom and ability to flex your skill. We believe we can learn a lot from how you approach a small challenge like this, and think it can be fun to write as well!

We will especially consider:
- Code organization
- Quality, including tests you may write yourself
- Readability
- Actually solving the problem (edge cases included)
