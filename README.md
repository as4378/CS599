# CS599

This repository for sharing the project work done for this course.
In Project1 we implement the least angle regression algorithm for computing the complete lasso path for given input data.
In particular we are computing the lasso path for prostate cancer data in package faraway as shown below:

![Image](https://github.com/as4378/CS599/blob/master/Project2/Fig1.PNG)

**Citation:** Toby Hocking, Guillem Rigaill, Paul Fearnhead et. al. On optimal multiple changepoint algorithms for large data Fig. 4

The file Project2/PELT.py contains the code that implments the least angle regression algorithm and plots the lasso path.
The make file contains all the necessay commands to run the code and plot the figure. To redo the analysis change to the directory where lasso.R is and just run make on the command line.

This will produce the figure in fig1.pdf. The details are in this file [File](https://github.com/as4378/CS599-MachineLearning/blob/master/Project1/Project1_documentation.pdf)

**Dependencies**: A stable version of R must be installed. Additionally lars package must be installed as the function uses internal functions available in this package and the lars class object. Also, package faraway which contains the data for prostate cancer must be installed.
