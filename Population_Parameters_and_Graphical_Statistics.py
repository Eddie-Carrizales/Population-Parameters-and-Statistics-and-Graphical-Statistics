import numpy as np
import random
import math
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Chapter 8.1 and 8.2 Descriptive Statistics
# ---------------------- step 0 ----------------------
# Name: Edilberto Carrizales
# Language: Python
# Language version: 3.9

# ---------------------- step 1: Load Chapter8.txt (and set up random number generator)----------------------
path = "C:/Users/Eddie Carrizales/OneDrive/Desktop/data.txt"  # add your path here or put .txt in the same place as this .py

population_data = np.loadtxt(path, delimiter=',')
# print(population_data)

# Set the seed (note comment this to get different random samples and not same random samples)
# random.seed(1234)

# Create a random number generator
def random_indexes(size):
    indexes = []
    for i in range(size):
        indexes.append(random.randint(0, size - 1))
    # print(indexes)
    return indexes

# create empty calculation description dataframe
pd.set_option('display.max_columns', None)
calculations_df = pd.DataFrame({"Descriptions": ["Length", "Minimum", "Maximum", "Mean", "Variance",
                                                 "Standard Deviation", "25% Quartile", "75% Quartile",
                                                 "Interquartile Range", "Lower limit", "Upper limit",
                                                 "Outliers found"]})

# ---------------------- step 2: The Population ----------------------
# Function that will be used to describe given sample data
def describe_sampled_data(name, given_data, deg_of_freedom):
    # The number of datapoints in the population:
    data_length = given_data.shape[0]
    print("Length   : " + str(data_length))

    # Minimum value
    data_min_value = np.min(given_data)
    print("Minimum  : " + str(data_min_value))

    # Maximum value
    data_max_value = np.max(given_data)
    print("Maximum  : " + str(data_max_value))

    # The mean
    data_mean_value = np.mean(given_data)
    data_sum = 0
    for i in range(data_length):
        data_sum += given_data[i]
    data_mean_value = data_sum / data_length
    data_mean_value = round(data_mean_value, 4)
    print("Mean     : " + str(data_mean_value))

    # Variance
    data_sum = 0
    for i in range(data_length):
        data_sum += given_data[i]**2
    data_variance = (data_sum / (data_length - deg_of_freedom)) - data_mean_value**2
    data_variance = round(data_variance, 4)
    print("Variance : " + str(data_variance))

    # Standard Deviation
    data_sum = 0
    for i in range(data_length):
        data_sum += (given_data[i] - data_mean_value)**2
    data_stdev = math.sqrt(data_sum / (data_length - deg_of_freedom))
    data_stdev = round(data_stdev, 4)
    print("Standard Deviation  : " + str(data_stdev))

    # The 25% Quartile
    sorted_data = np.sort(given_data)
    data_25_index = (data_length + 1) / 4
    data_25_quartile = sorted_data[round(data_25_index)]
    print("25% Quartile        : " + str(data_25_quartile))

    # The 75% Quartile
    data_75_quartile = np.percentile(given_data, 75)
    print("75% Quartile        : " + str(data_75_quartile))

    # The Interquartile range
    data_interquartile_range = data_75_quartile - data_25_quartile
    print("Interquartile Range : " + str(data_interquartile_range))

    # The lower outlier limit from the interquartile range
    data_lower_limit = data_25_quartile - 1.5 * data_interquartile_range
    print("Lower limit         : " + str(data_lower_limit))

    # The upper outlier limit from the interquartile range
    data_upper_limit = data_75_quartile + 1.5 * data_interquartile_range
    print("Upper limit         : " + str(data_upper_limit))

    # The count of the number of outliers in the population
    outliers = np.logical_or(given_data < data_lower_limit, given_data > data_upper_limit)
    num_outliers = np.sum(outliers)
    print("Outliers found      : " + str(num_outliers))

    # insert all into data frame
    calculations_df[name] = [str(data_length), str(data_min_value), str(data_max_value), str(data_mean_value),
                      str(data_variance), str(data_stdev), str(data_25_quartile), str(data_75_quartile),
                      str(data_interquartile_range), str(data_lower_limit), str(data_upper_limit),
                      str(num_outliers)]

# Print the description of the entire population
print("The Population")
print("---------------------")
degrees_of_freedom = 0
describe_sampled_data("The population", population_data, degrees_of_freedom)
print("")


# ---------------------- step 2: 1000 Unit Sample ----------------------

# Sample 1000 elements from the dataset
data_1000_samples = population_data[random_indexes(1000)]

# print the description of the 1000 sampled population
print("1000 Unit Sample")
print("---------------------")
degrees_of_freedom = 1
describe_sampled_data("1000 Unit Sample", data_1000_samples, degrees_of_freedom)
print("")

# ---------------------- step 3: 10000 Unit Sample ----------------------

# Sample 10000 elements from the dataset
data_10000_samples = population_data[random_indexes(10000)]

# print the description of the 10000 sampled population
print("10000 Unit Sample")
print("---------------------")
degrees_of_freedom = 1
describe_sampled_data("10000 Unit Sample", data_10000_samples, degrees_of_freedom)
print("")

# ---------------------- step 4: 100000 Unit Sample ----------------------

# Sample 100000 elements from the dataset
data_100000_samples = population_data[random_indexes(100000)]

# print the description of the 100000 sampled population
print("100000 Unit Sample")
print("---------------------")
degrees_of_freedom = 1
describe_sampled_data("100000 Unit Sample", data_100000_samples, degrees_of_freedom)
print("")

# ---------------------- step 5: The Central Limit Theorem ----------------------
# print(calculations_df)
print(tabulate(calculations_df, headers='keys', tablefmt='psql', numalign="right"))

# Do the statistics start to converge on the parameters as the size of the sample increases?
# Yes, the central limit theorem tells us that as the sample size (n) increases, the samples will
# tend to yield statistics (such as the sample mean) that are closer to the true population parameters.
# Thus, the statistics will converge on the population parameters as the size increases.

# Chapter 8.3 Scatter Plot

# create sequence of angles from 0 to 360 with 18 degree interval
radian_angles_data = [0]
degrees_angles_data = [0]
angles_sum = 0
while radian_angles_data[-1] != math.radians(360):
    angles_sum += 18
    radian_angles_data.append(math.radians(angles_sum))
    degrees_angles_data.append(angles_sum)

# create x and y values to plot
x_values = []
y_values = []
for i in range(len(radian_angles_data)):
    x_values.append(math.cos(radian_angles_data[i]) * 5)
    y_values.append(math.sin(radian_angles_data[i]) * 5)

# table with one column being the angle in degrees, one column being the x-position, and one column being the y-position
plots_df = pd.DataFrame({'Angles (Degrees)': degrees_angles_data, 'X_Position': x_values, 'Y_Position': y_values})
# print(plots_df)
print("")
print(tabulate(plots_df, headers='keys', tablefmt='psql', numalign="right"))

# --------- create scatter plots using matplot ---------

# scatter plot of angle vs. x-position
plt.title('Plot of Angles vs. X-positions')
plt.xlabel('Angles')
plt.ylabel('X-positions')
plt.scatter(radian_angles_data, x_values)
plt.plot(radian_angles_data, x_values)
plt.show()

# scatter plot of angle vs. y-position
plt.title('Plot of Angles vs. Y-positions')
plt.xlabel('Angles')
plt.ylabel('Y-positions')
plt.scatter(radian_angles_data, y_values)
plt.plot(radian_angles_data, y_values)
plt.show()

# scatter plot of x-position vs. y-position
plt.figure(figsize=(6, 6))
plt.title('Plot of X-position vs. Y-positions')
plt.xlabel('X-position')
plt.ylabel('Y-positions')
plt.scatter(x_values, y_values)
plt.plot(x_values, y_values)
plt.show()

