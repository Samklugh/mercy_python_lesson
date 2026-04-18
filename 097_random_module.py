# ***************************
# random module in python
# ***************************

# The random module in Python provides functions for generating random numbers and performing random operations. It is a built-in module that can be imported and used in any Python program. Some of the commonly used functions in the random module include: 

# 1. random(): This function returns a random float number between 0.0 and 1.0.

import random
number = random.random()
print(f"\n\nRandom float number between 0.0 and 1.0: {number}")


# 2. randint(a, b): This function returns a random integer between a and b (inclusive).

random_integer = random.randint(1, 10)
print(f"\n\nRandom integer between 1 and 10: {random_integer}")

# 3. choice(seq): This function returns a random element from a non-empty sequence.

my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(f"\n\nRandom element from the list: {random_element}")
# 4. shuffle(seq): This function shuffles the elements of a sequence in place.
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"\n\nShuffled list: {my_list}")

# 5. sample(population, k): This function returns a list of k unique elements chosen from the population sequence or set.
my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)
print(f"\n\nRandom sample of 3 elements from the list: {random_sample}")

# 6. randrange(start, stop[, step]): This function returns a randomly selected element from the range created by the start, stop, and step arguments.
random_range = random.randrange(1, 10, 2)
print(f"\n\nRandom number from the range 1 to 10 with a step of 2: {random_range}")

# 7. uniform(a, b): This function returns a random float number between a and b (inclusive).
random_float = random.uniform(1.0, 10.0)
print(f"\n\nRandom float number between 1.0 and 10.0: {random_float}")

# 8. seed(a=None): This function initializes the random number generator with a seed value. If a is not provided, the current system time is used as the seed.
random.seed(42) # Setting a seed value for reproducibility
random_number = random.random()
print(f"\n\nRandom number with seed 42: {random_number}")

# 9. getrandbits(n): This function returns a random integer with n random bits.
random_bits = random.getrandbits(8) # Get a random integer with 8 random bits
print(f"\n\nRandom integer with 8 random bits: {random_bits}")

# 10. randbytes(n): This function returns a bytes object containing n random bytes.
random_bytes = random.randbytes(16) # Get 16 random bytes
print(f"\n\nRandom bytes: {random_bytes}")

# 11. randrange(start, stop): This function returns a randomly selected element from the range created by the start and stop arguments. For example, if we want to get a random number between 1 and 10, we can use the randrange function as follows:
random_number = random.randrange(1, 11) # Get a random number between 1 and 10 (inclusive)
print(f"\n\nRandom number between 1 and 10: {random_number}")

# 12. randbytes(n): This function returns a bytes object containing n random bytes. For example, if we want to get 16 random bytes, we can use the randbytes function as follows:
random_bytes = random.randbytes(16) # Get 16 random bytes
print(f"\n\nRandom bytes: {random_bytes}")

# 13. sample: This function returns a list of k unique elements chosen from the population sequence or set. For example, if we want to get a random sample of 3 elements from a list, we can use the sample function as follows:
my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3) # Get a random sample of 3 elements from the list
print(f"\n\nRandom sample of 3 elements from the list: {random_sample}")

# 14. uniform(a, b): This function returns a random float number between a and b (inclusive). For example, if we want to get a random float number between 1.0 and 10.0, we can use the uniform function as follows:
random_float = random.uniform(1.0, 10.0) # Get a random float number between 1.0 and 10.0
print(f"\n\nRandom float number between 1.0 and 10.0: {random_float}")

# 15. triangular(low, high, mode): This function returns a random float number between low and high (inclusive) with a specified mode. The mode parameter is optional and specifies the value at which the probability density function peaks. If mode is not provided, it defaults to the midpoint between low and high. For example, if we want to get a random float number between 1.0 and 10.0 with a mode of 5.0, we can use the triangular function as follows:

random_triangular = random.triangular(1.0, 10.0, 5.0) # Get a random float number between 1.0 and 10.0 with a mode of 5.0
print(f"\n\nRandom float number between 1.0 and 10.0 with a mode of 5.0: {random_triangular}")


# 16. betavariate(alpha, beta): This function returns a random float number drawn from a beta distribution with parameters alpha and beta. The beta distribution is a continuous probability distribution defined on the interval [0, 1] and is often used in Bayesian statistics and modeling of random variables that represent proportions or probabilities. For example, if we want to get a random float number from a beta distribution with alpha = 2.0 and beta = 5.0, we can use the betavariate function as follows:

random_beta = random.betavariate(2.0, 5.0) # Get a random float number from a beta distribution with alpha = 2.0 and beta = 5.0
print(f"\n\nRandom float number from a beta distribution with alpha = 2.0 and beta = 5.0: {random_beta}")

# 17. gammavariate(alpha, beta): This function returns a random float number drawn from a gamma distribution with parameters alpha and beta. The gamma distribution is a continuous probability distribution defined on the interval [0, ∞) and is often used in modeling of waiting times and lifetimes of objects. For example, if we want to get a random float number from a gamma distribution with alpha = 2.0 and beta = 3.0, we can use the gammavariate function as follows:
random_gamma = random.gammavariate(2.0, 3.0) # Get a random float number from a gamma distribution with alpha = 2.0 and beta = 3.0
print(f"\n\nRandom float number from a gamma distribution with alpha = 2.0 and beta = 3.0: {random_gamma}")

# 18. vonmisesvariate(mu, kappa): This function returns a random float number drawn from a von Mises distribution with parameters mu and kappa. The von Mises distribution is a continuous probability distribution defined on the interval [0, 2π) and is often used in modeling of circular data such as angles and directions. For example, if we want to get a random float number from a von Mises distribution with mu = 0.0 and kappa = 1.0, we can use the vonmisesvariate function as follows:


random_vonmises = random.vonmisesvariate(0.0, 1.0) # Get a random float number from a von Mises distribution with mu = 0.0 and kappa = 1.0
print(f"\n\nRandom float number from a von Mises distribution with mu = 0.0 and kappa = 1.0: {random_vonmises}")

# 19. weibullvariate(alpha, beta): This function returns a random float number drawn from a Weibull distribution with parameters alpha and beta. The Weibull distribution is a continuous probability distribution defined on the interval [0, ∞) and is often used in modeling of lifetimes of objects and failure rates. For example, if we want to get a random float number from a Weibull distribution with alpha = 2.0 and beta = 3.0, we can use the weibullvariate function as follows:

random_weibull = random.weibullvariate(2.0, 3.0) # Get a random float number from a Weibull distribution with alpha = 2.0 and beta = 3.0
print(f"\n\nRandom float number from a Weibull distribution with alpha = 2.0 and beta = 3.0: {random_weibull}")


# 20. normalvariate(mu, sigma): This function returns a random float number drawn from a normal (Gaussian) distribution with mean mu and standard deviation sigma. The normal distribution is a continuous probability distribution defined on the interval (-∞, ∞) and is often used in modeling of natural phenomena and measurement errors. For example, if we want to get a random float number from a normal distribution with mu = 0.0 and sigma = 1.0, we can use the normalvariate function as follows:

random_normal = random.normalvariate(0.0, 1.0) # Get a random float number from a normal distribution with mu = 0.0 and sigma = 1.0
print(f"\n\nRandom float number from a normal distribution with mu = 0.0 and sigma = 1.0: {random_normal}")


# 21. paretovariate(alpha): This function returns a random float number drawn from a Pareto distribution with parameter alpha. The Pareto distribution is a continuous probability distribution defined on the interval [1, ∞) and is often used in modeling of wealth distribution and other phenomena that exhibit power-law behavior. For example, if we want to get a random float number from a Pareto distribution with alpha = 2.0, we can use the paretovariate function as follows:

random_pareto = random.paretovariate(2.0) # Get a random float number from a Pareto distribution with alpha = 2.0
print(f"\n\nRandom float number from a Pareto distribution with alpha = 2.0: {random_pareto}")


# 22. lognormvariate(mu, sigma): This function returns a random float number drawn from a log-normal distribution with parameters mu and sigma. The log-normal distribution is a continuous probability distribution defined on the interval (0, ∞) and is often used in modeling of stock prices and other phenomena that exhibit multiplicative growth. For example, if we want to get a random float number from a log-normal distribution with mu = 0.0 and sigma = 1.0, we can use the lognormvariate function as follows:

random_lognorm = random.lognormvariate(0.0, 1.0) # Get a random float number from a log-normal distribution with mu = 0.0 and sigma = 1.0
print(f"\n\nRandom float number from a log-normal distribution with mu = 0.0 and sigma = 1.0: {random_lognorm}")

# 23. gaussvariate(mu, sigma): This function returns a random float number drawn from a Gaussian distribution with mean mu and standard deviation sigma. The Gaussian distribution is a continuous probability distribution defined on the interval (-∞, ∞) and is often used in modeling of natural phenomena and measurement errors. For example, if we want to get a random float number from a Gaussian distribution with mu = 0.0 and sigma = 1.0, we can use the gaussvariate function as follows:

# random_gauss = random.gaussvariate(0.0, 1.0) 
# Get a random float number from a Gaussian distribution with mu = 0.0 and sigma = 1.0
# print(f"\n\nRandom float number from a Gaussian distribution with mu = 0.0 and sigma = 1.0: {random_gauss}")


# These are just a few examples of the functions available in the random module. The random module provides many more functions for generating random numbers and performing random operations, which can be useful in various applications such as games, simulations, and data analysis.