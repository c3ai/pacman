# Running PACMAN Tests 
Follow the instructions below for either JavaScript or Python code.
Feel free to add new test cases inside the js_test or py_test directories, and update the test specs accordingly.


## Javascript tests
1. Place files to test inside the js_test directory. Make sure they are in the first level of js_test.
2. Run `npm i` in the js_test directory if this is your first time running the jasmine test.
3. If you don't have jasmine installed globally, run `npm install -g jasmine` before proceeding.
4. Run `jasmine spec/PacmanSpec.js ../pacman` from the js_test directory.

### Understanding the test run (JS)
The output will return results for 3 tests, including runtimes for each and a total runtime. We are looking for a reasonable runtime for JS tests: less than 8 seconds.


## Python tests
1. Place files to test inside the py_test directory. Make sure they are in the first level of py_test.
2. Usage (from the py_test directory):
  `python pacman.ut.py [submission.py]`
Arguments:
  `[submission.py]`
    Path of the pacman.py file you want to test.

### Understanding the test run (Python)
The output will return results from 2 groups of tests - runtime and accuracy. The runtime test will always fail, it is used just to show the actual runtime. The accuracy test will return the output from 3 unit tests. We are looking for a reasonable runtime for Python tests: less than 1 second.
