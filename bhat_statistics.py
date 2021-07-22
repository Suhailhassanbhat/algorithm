#Suhail Bhat
# Purpose: To analyze the personal income data on county basis, published for the first time in December last year by the Bureau of Labor statistics. This granular data gives us a peek into about 5,000 odd counties in the United States. The broader goal of this analysis is also to link these data points to voting patterns. One of the theories that floated during and after 2016 General Election said that there is an economic anxiety among voters that translates into them voting for an unusual (anti-establishment) candidate, Donald Trump. Going step by step; find outliers(meaning low income counties), check the voting pattern(who they voted for at least in the last four elections) and validate if there is an association between the two. The personal income per capita data is available here https://apps.bea.gov/itable/iTable.cfm?ReqID=70&step=1.

# Guidelines by Susan McGregor on her Youtube channel-susane mcg- helped building this code https://www.youtube.com/watch?v=VEsBBEn8dmY&list=PLehYFEvQGUkEaz8FYUAiF1wybTRvR0pCs&index=3

# Importing libraries here; csv to read the file, matplotlib to make graphs, statistics for analysis, numpy because we are dealing with numbers here.
import numpy as np
import matplotlib.pyplot as plt
import statistics
import csv

# Making an empty list of numbers here
county_income = []

# Now let us read the file and with the help of a for loop go through every number and add it to the empty list above. Ignore nan values.
with open('county_income.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            county_income.append(int(row['personal_income']))
        except Exception:
            pass
county_income

# Making quartiles, 25 percentile and 75 percentile i.e. Q1, Q3
quartiles = np.percentile(county_income, [25, 75])
iqr = quartiles[1]-quartiles[0]

# Calculate upper_bound and lower_bound here
upper_bound = quartiles[1] + iqr*1.5
lower_bound = quartiles[0] - iqr*1.5

# calculate mean
income_mean = statistics.mean(county_income)

# Calculate standard deviation
income_std_dev = np.std(county_income)

#Datapoints for plotting standard deviations
mean_measures = [income_mean]
for i in range(4):
    mean_measures.append(income_mean+i*income_std_dev)
    mean_measures.append(income_mean-i*income_std_dev)

# Calculate median
income_median = statistics.median(county_income)

# Plot histograms of personal income in grey
my_hist = plt.hist(county_income, histtype='bar', bins= 20, color='grey')

# Plotting median in blue
plt.vlines(income_median, 0, 1600, color =['blue'], linestyles='dashed', linewidth=3)

# Plotting quartiles in blue
plt.vlines(quartiles, 0, 1600, color =['blue', 'blue'], linestyles='dashed', linewidth=2)

# plotting upper bound and lower bound in blue
plt.vlines([upper_bound, lower_bound], 0, 1600, color =['blue', 'blue'], linestyles='dashed', linewidth=2)

# plotting mean measures such as mean, standard deviations in green
plt.vlines(mean_measures, 0, 1600, color =['green'], linestyles='dashed', linewidth=2)

plt.show()

# What more can be done with this?
# The counties that fall below the first standard deviation are the most interesting ones. If the voting patterns are studied over the length of 20 years that would give us an idea about how much voters care about personal income. The racial composition of these counties would be interesting to check as well. 