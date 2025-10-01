# grid_login_test
This mini project showcases my ability to run login test case scripts in parallel using Selenium Grid. I configured a hub and two nodes with different ports from the same machine. The objective was to reduce tests execution time by automating them with Selenium Grid.
## Prerequisites:
- Git installed
- Java installed
- Python installed
- selenium package installed
  ```
  pip install selenium
  ```
- Selenium Grid JAR downloaded (I'm using `selenium-server-4.35.0.jar` in this project)
- pytest package installed
  ```
  pip install pytest
  ```
- pytest-xdist package installed
  ```
  pip install pytest-xdist
  ```
## How to run the tests:
1. Open your terminal or command prompt.
2. Type the following command
   ```
   git clone https://github.com/YudhaWidianto/grid_login_test.git
   ```
4. Press Enter. This will clone the repository locally and create a folder called `grid_login_test` with all of the repo's files.
5. Start the grid hub.
   ```
   java -jar selenium-server-4.35.0.jar hub
   ```
6. Open [http://localhost:4444](http://localhost:4444) to see the Selenium Grid UI. Note that there are no registered Nodes yet.
7. Open a new terminal window, and start the first node.
   ```
   java -jar selenium-server-4.35.0.jar node --port 5555
   ```
   Note that a node has been added in the Grid UI.
8. Open another new terminal window, and start the second node.
   ```
   java -jar selenium-server-4.35.0.jar node --port 6666
   ```
   Now you should see both nodes in the Grid UI.
9. In order to run the tests, open another terminal window, change the current directory:
   ```
   cd grid_login_test
   ```
   Then, run:
   ```
   pytest -n 2
   ```
   This tells `pytest-xdist` to run the test in 2 parallel threads. Two Chrome instances should run in parallel at this point.
