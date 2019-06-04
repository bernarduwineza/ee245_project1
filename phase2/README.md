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
 In  `./main.py`, replace `filepath` with the appropriate path to the file that
 contains the obstacles and configuration space data. The script will extract 
 the configuration space size and the obstacles in it. 
 It is assumed that the input file mentioned above is exactly of the same style 
 as the sample file given. (There are no blank lines after the second 
 intentionally blank line, for example.)
 
 ## Bugs 
 For unfortunate reasons, the controller for the navigation part is not 
 properly tuned. 
 
 