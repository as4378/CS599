# import the required libraries
library(FastLZeroSpikeInference)
library(reticulate)
library(ggplot2)
library(directlabels)

# un-comment this line and specify the path to python 64 bit version if using 32 bit version of python
# use_python("C:\\Users\\AnuraagUS\\Python\\Python35")

# using python source file for PELT algorithm
source_python("PELT.py")

# data segment to be partitioned such that change points are at locations, 20, 40, 60 and 80
data <- c(c(1:20), c(41:60), c(1:20), c(41:60), c(1:20))

# using fpop to segment the data and storing result in res
res <- FastLZeroSpikeInference::estimate_spikes(data, 1, 2000)

# "n_intervals" contains the number of candidates at each time step
cand_fpop <- res$n_intervals

# using pelt to segment the data which returns number of candidates at each time step
cand_pelt <- pelt(data, 2000, 0)

# creating a data frame combining both results for plotting
to_plot <- data.frame(data = c(c(1:100), c(1:100)), 
                      candidates = c(cand_fpop, cand_pelt[1:100]), 
                      expr = c(rep("fpop", 100), rep("pelt", 100)))

# plotting the result and saving to variable "plot"
plot <- ggplot(data=to_plot, aes(x = (data),y = (candidates),
                                 col = expr)) + 
  geom_line() +
  xlab('Time') +
  ylab('Number of candidates being considered')

# add informative labels
plot <- directlabels::direct.label(plot, "last.polygons")

# saving figure to fig1.png
png("fig1.png")
print(plot)
dev.off()
