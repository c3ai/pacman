![alt text](pacman.png)

## Introduction
Hello, and welcome to your assignment for the Forward Deployed Solution Engineer role at C3! First, thank you for your time and energy spent in this process; we fully understand that you probably have a million other things to do, but this is an important screening step before moving into the advanced stages of interviews.

Your assignment is to write a program that navigates a 2-dimensional board covered in coins which are picked up as you move over them, much like the game of Pac-Man. Your program will take a single input which contains 4 components: board dimensions, an initial position, movements, and walls.

Coins are in every position of the rectangular board except for the initial position and positions that have walls. If Pac-Man is instructed to move into a wall (on the perimeter of the board or as defined by the walls input) it should have no effect (Pac-Man stays in place).


## Program Input
Your program will take as input a multiline string consisting of:

1. The board dimensions: defined by X and Y coordinates, identifying the top right corner of the room rectangle - that is to say, (0,0) is in the bottom left corner, and (X,Y) is in the top right corner. This board is divided up in a grid based on these dimensions; a board that has dimensions `X=5` and `Y=5` has 5 columns and 5 rows for 25 possible positions.
2. The initial position: the initial position of Pac-Man in (x,y) coordinates.
3. The movements: instructions in cardinal directions where e.g. N and E mean "go north" and "go east", respectively. The board is oriented facing north; thus, moving north from (0,0) lands Pac-Man at (0,1).
4. The walls: the positions of walls on the board in (x,y) coordinates. Pac-Man cannot move through walls.

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


## Program Output
The `pacman` function should return Pac-Man's final location in (x,y) and the number of coins that have been collected across all movements in the following format:

```js
[finalXposition, finalYposition, totalCoins]
```

For example, the above input should return:  

```js
[1, 4, 7]
```
We will be testing edge cases on your code, so if there are any problems with the inputs, execution of the instructions, or any other cases you can think of, have your `pacman` function return `[-1, -1, 0]`.


## Tips
- Your solution can make use of any existing open source libraries.
- Feel free to use your favorite IDE to code up and test your solution before copying and pasting back into HackerRank.


## Evaluation Criteria
The point of the exercise is for us to see some of the code you wrote (and should be proud of). There isn't a single solution and the problem intentionally allows you creative freedom and ability to flex your skill. We believe we can learn a lot from how you approach a small challenge like this, and think it can be fun to write as well!

We will consider:
- Code organization
- Quality
- Readability