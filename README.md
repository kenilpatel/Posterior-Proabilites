# Posterior-Proabilites
Bayesian rule based simple posterior probabilitiy calculation 

The task in this program is to implement a system that:

Can determine the posterior probability of different hypotheses, given priors for these hypotheses, and given a sequence of observations.

Can determine the probability that the next observation will be of a specific type, priors for different hypotheses, and given a sequence of observations.

As in the slides that we saw in class, there are five types of bags of candies. Each bag has an infinite amount of candies. We have one of those bags, and we are picking candies out of it. We don't know what type of bag we have, so we want to figure out the probability of each type based on the candies that we have picked.

The five possible hypotheses for our bag are:

h1 (prior: 10%): This type of bag contains 100% cherry candies.
h2 (prior: 20%): This type of bag contains 75% cherry candies and 25% lime candies.
h3 (prior: 40%): This type of bag contains 50% cherry candies and 50% lime candies.
h4 (prior: 20%): This type of bag contains 25% cherry candies and 75% lime candies.
h5 (prior: 10%): This type of bag contains 100% lime candies.

How to run code? 

python compute_a_posteriori.py CLLCCLLLCCL

Structure of code

Code use iterative approach using for loop to computer prior and posterior probability based on the probability of previous steps
