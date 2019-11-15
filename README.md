# CS599

This repository for sharing the project work done for this course.
In this project we implement the PELT (Pruned Exact Linear Time) method for computing the change points for given input data and compare the number of candidates considered at each time step with other method called FPOP (Functional Pruning Optimal Partitioning)

![Image](https://github.com/as4378/CS599/blob/master/Project2/Fig1.PNG)

**Citation:** Toby Hocking, Guillem Rigaill, Paul Fearnhead et. al. On optimal multiple changepoint algorithms for large data Fig. 4

The file Project2/PELT.py contains the code that implments the PELT and FPOP algorithm for square error loss as the cost function and plots the number of candidates considered at each time step for both methods. The make file contains all the necessay commands to run the code and plot the figure. To redo the analysis change to the directory where PELT.py is and just run make on the command line.

This will produce the figure as shown above. The details are in this file [File](https://github.com/as4378/CS599/blob/master/Project2/Project2Week1.pdf)

**Dependencies**: A stable version of python3 must be installed. Additionally matplotlib must be installed for plotting in python.
