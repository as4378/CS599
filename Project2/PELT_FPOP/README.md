# FastLZeroSpikeInference: A package for estimating spike times from calcium imaging data using an L0 penalty 

![https://travis-ci.com/jewellsean/FastLZeroSpikeInference](https://travis-ci.com/jewellsean/FastLZeroSpikeInference.png?branch=dev)

This package implements an algorithm for deconvolving calcium imaging data
for a single neuron in order to estimate the times at which the neuron
spikes. See [https://jewellsean.github.io/fast-spike-deconvolution/](https://jewellsean.github.io/fast-spike-deconvolution/) for tutorials and additional information. 

This algorithm solves the optimization problems

### AR(1) model

<img src="math_figures/un-constr.png" alt="alt text" width="600" height="80">

for the global optimum, where y_t is the observed fluorescence at the tth timepoint.

### Constrained AR(1) model

<img src="math_figures/constr.png" alt="alt text" width="600" height="140">

for the global optimum, where y_t is the observed fluorescence at the tth timepoint.

We introduce the constant EPS > 0, to avoid 
arbitrarily small calcium concentrations that would result in numerical  
instabilities. In practice, this means that the estimated calcium concentration 
decays according to the AR(1) model for values greater than EPS and is equal to EPS thereafter. For small EPS, the difference between the old and new formulation is negligible (the objective function differ only when, under the old formulation, c_t < EPS, and at such timesteps the difference is bounded by 2y_t * EPS + 0.5 EPS^2; in our experiments, we choose EPS = 1e-4.)

When estimating the spikes, it is not necessary to explicitly compute the 
calcium concentration. Therefore, if only the spike times are required, the user
can avoid this computation cost by setting the compute_fitted_values boolean to false. 
By default, the calcium concentration is not estimated. 

Given the set of estimated spikes produced from the estimate_spike, the calcium concentration
can be estimated with the estimate_calcium function.

For additional information visit my [website](https://jewellsean.github.io/fast-spike-deconvolution/index.html).  

R examples 
```r
sim <- simulate_ar1(n = 500, gam = 0.95, poisMean = 0.009, sd = 0.05, seed = 1)
plot(sim)
 
## Fits for a single tuning parameter

# AR(1) model
fit <- estimate_spikes(dat = sim$fl, gam = 0.95, lambda = 1)
print(fit)

# compute fitted values from prev. fit
fit <- estimate_calcium(fit)
plot(fit)

# or
fit <- estimate_spikes(dat = sim$fl, gam = 0.95, lambda = 1, estimate_calcium = T)
plot(fit)
 
# Constrained AR(1) model
fit <- estimate_spikes(dat = sim$fl, gam = 0.95, lambda = 1, constraint = T, estimate_calcium = T)
print(fit)
plot(fit)
```

Install 
-----

If ``devtools`` is installed type 

```r
devtools::install_github("jewellsean/FastLZeroSpikeInference")
```

Usage
----

Once installed type 
```{r}
library(FastLZeroSpikeInference)
```


Alpha Python Instructions
---

Below are instructions for an alpha-release of a simple c-types python wrapper for this C++ code. Only Unix type systems are currently supported. 

NB: ubuntu requires `sudo apt install clang g++` 

Within terminal, clone this repo and run the make script: 

```
git clone "https://github.com/jewellsean/FastLZeroSpikeInference.git"
cd FastLZeroSpikeInference/python
./make.sh
```

An example using this code can be viewed [here](https://github.com/jewellsean/FastLZeroSpikeInference/blob/master/examples/python/simple_example.py).

References
-----
Jewell, Hocking, Fearnhead, and Witten (2019). [Fast Nonconvex Deconvolution of Calcium Imaging Data](https://doi.org/10.1093/biostatistics/kxy083) Biostatistics. kxy083.

Jewell and Witten (2018). [Exact Spike Train Inference Via L0 Optimization](https://projecteuclid.org/euclid.aoas/1542078052)
Ann. Appl. Stat. 12 (2018), no. 4, 2457--2482. doi:10.1214/18-AOAS1162. 


Hocking, T. D., Rigaill, G., Fearnhead, P., & Bourque, G. (2017). [A log-linear time algorithm for constrained changepoint detection](https://arxiv.org/abs/1703.03352)
