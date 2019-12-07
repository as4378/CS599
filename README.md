# CS599

This repository for sharing the project work done for this course.
In this project we implement the PELT (Pruned Exact Linear Time) method for computing the change points for given input data and compare the number of candidates considered at each time step with other method called FPOP (Functional Pruning Optimal Partitioning).


The details are in this file [File](https://github.com/as4378/CS599/blob/master/Project2/Project2Week1.pdf)


![Image](https://github.com/as4378/CS599/blob/master/Project2/Fig1.PNG)

**Citation:** Toby Hocking, Guillem Rigaill, Paul Fearnhead et. al. On optimal multiple changepoint algorithms for large data Fig. 4


**Dependencies**: A stable version of R(atleast 3.5.1) and python3 must be installed both 64 bit. Additionally following libraries must be installed in R:

1. reticulate

2. ggplot2

3. directlabels

To redo the analysis you will need to clone this directory. After that in main.R in lines 7 and 8 if you are not using 64 bit version of python then download the 64 bit version of python and and uncomment and update the line ```use_python("path to 64 bit version of python")```, otherwise leave this line commented.

After this, on terminal change to this directory and type make on command line. This will run the program and the plot will be created in file fig1.png.
