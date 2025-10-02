# grid_login_test
This mini project showcases my ability to run login test case scripts in parallel using Selenium Grid. There are three test cases in this mini project:
1. Positive login test
2. Negative username test
3. Negative password test\
I configured one hub and three nodes with different ports from the same machine. The objective was to reduce tests execution time by distributing the tests across multiple nodes using Selenium Grid.
## Prerequisites:
- Git installed
- Java installed
- Python installed
- `selenium` package installed
  ```
  pip install selenium
  ```
- Selenium Grid JAR downloaded (I'm using `selenium-server-4.35.0.jar` in this project)
- `pytest` package installed
  ```
  pip install pytest
  ```
- `pytest-xdist` package installed
  ```
  pip install pytest-xdist
  ```
## How to Run the Tests:
1. Open your terminal or command prompt.
2. Enter the following command
   ```
   git clone https://github.com/YudhaWidianto/grid_login_test.git
   ```
   This will clone the repository locally and create a folder called `grid_login_test` with all of the repo's files.
3. Start the grid hub.
   ```
   java -jar selenium-server-4.35.0.jar hub
   ```
4. Open [http://localhost:4444](http://localhost:4444) to see the Selenium Grid UI. Note that there are no registered nodes yet.
5. Open three new terminal window, and start a node on each window. For the first node:
   ```
   java -jar selenium-server-4.35.0.jar node --port 5555
   ```
   For the second node:
   ```
   java -jar selenium-server-4.35.0.jar node --port 5556
   ```
   For the third node:
   ```
   java -jar selenium-server-4.35.0.jar node --port 5557
   ```
   Now you should see three nodes in the Grid UI.
6. In order to run the tests, open another terminal window, change the current directory:
   ```
   cd grid_login_test
   ```
   Then, run:
   ```
   pytest -n 3 automat_grid/
   ```
   This tells `pytest-xdist` to run the test in `automat_grid` folder in 3 parallel threads. Three Chrome instances should run in parallel at this point.
## Result and Impact
With Selenium Grid, I was able to run the test execution time from 13.97s to 11.70s by distributing the tests in parallel across 3 nodes. This improved test efficiency and might allow quicker feedback in a development cycle.
