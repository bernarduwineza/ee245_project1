# EE 245 Project | Phase 2
***
## Dependencies 
The project depends on these packages (most of them are common and will not probably need to be installed.)
 * numpy
 * matplotlib 
 * pickle
 * math 
 * time 
 * cProfile 
 * re
 
 There is no meachnism in this script to install the missing dependencies. 
 They will have to be installed manually!
 ***
 ## How to run the code
 In  `phase2/main.py`, replace `filepath` with the appropriate path to the file that
 contains the obstacles and configuration space data. The script will extract 
 the configuration space size and the obstacles in it. 
 It is assumed that the input file mentioned above is exactly of the same style 
 as the sample file given. (There are no blank lines after the second 
 intentionally blank line, for example.) 
 ***
 PLEASE, BE SURE TO CLOSE THE A* PLOT FOR THE SCRIPT TO CONTINUE RUNNING. 
 ***
 `main.py` creates a binary occupancy grid for the configuration space, and runs A* 
 algorithm on it to generate an efficient path. \
 `navigation2.py` uses the path created to simulate the quadrotor's flight. 
 
 ## 
 
 ## Bugs and future work 
 For unfortunate reasons, the controller for the navigation part is not 
 properly tuned. As a result, the simulation. The generated path is also printed. \
 In the future, an efficient controller would be implemented. 
 
 
***
It should be noted that another solution for this project was being worked on by one of 
the team-member. As is the case with the other solution, it is also not finished. \
It is located in `/phase2/alternate/`. At the moment, no instructions on how to run  it
it are provided. 
 