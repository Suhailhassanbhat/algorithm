#Suhail Bhat, Week 1 Programming Exercise
#Function to calculate mean of numbers without using sum(), mean(), count(), len(). 


#import pandas to read the csv file
import pandas as pd 
# Read csv file 
data = pd.read_csv("data.csv") 
# transpose data
series = data.T 
# Reset index
series = data.reset_index() 
# convert numbers to float from string
series = data.astype(float) 
#rename column to avoid confusion
series = series.rename(columns ={"index":"numbers"}) 

# Mean function 
def mean():
    total = 0 # inital sum is zero
    count = 0 # initial count is zero
    for number in series.numbers: # starting a for loop to read in numbers one at a time
        total = total + number # as it reads numbers, it adds it to total, eventually giving us the sum of all numbers
        count = count + 1 # adds one to count with each number, gives 50 at the end
    print("mean of the numbers is", round(total/count, 2)) # dividing total / count gives us average 56.05
mean() # this function will work even if dataset is changed
