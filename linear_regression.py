import pandas as pd
import numpy as no
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

ca_api_data = pd.read_csv('apib12tx.csv')
print(ca_api_data.columns)

#make a histogram
grade12 = plt.figure(1)
ca_api_data['API12B'].hist()


# histogram of meals, which is pct of students 
meals=plt.figure(2)
ca_api_data['MEALS'].hist()

ca_api_data.plot(kind="scatter", x='MEALS', y='API12B')

#set up basic regression analysis
x=ca_api_data[['MEALS']].values
y=ca_api_data[['API12B']].values

my_regression =LinearRegression()
my_regression.fit(x,y)

#make a scatter plot in blue and plot line in red

plt.scatter(x,y, color='blue')

#draw regression line in red

plt.plot(x, my_regression.predict(x), color='red', linewidth='1')

#what is the slope?
print(my_regression.coef_)

#what is the intercept(i.e. MEALS = 0)
print(my_regression.intercept_)

#what is the expected score for a school with 80 percent lower income students?
print(my_regression.predict([[80]]))

outperforming_schools = ca_api_data[(ca_api_data['MEALS']>=80)& (ca_api_data['API12B']>=900)]
print(outperforming_schools[['SNAME', 'MEALS', 'API12B']])

#get set up for statsmodels
X_stats = ca_api_data[['MEALS']].values
Y_stats = ca_api_data[['API12B']].values
X_stats=sm.add_constant(X_stats)

#create and print the model
my_model = sm.OLS(Y_stats, X_stats).fit()
my_predictions = my_model.predict(X_stats)

print(my_model.summary())
plt.show()