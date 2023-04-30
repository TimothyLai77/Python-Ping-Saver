from matplotlib import pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# read data
dataFrame = pd.read_csv('toplot.csv', names=['Date', 'Time', 'Ping'] , header=None)

# to handle the error/timeout when ping doesn't exit properly
if 'error/timedout' in dataFrame.values : 
    dataFrame['Ping'] = dataFrame['Ping'].str.replace('error/timedout', '0') # replace the errors with 0
    dataFrame['Ping'] = dataFrame['Ping'].astype(float) # convert data from string to float

# graph stuff
plt.scatter(dataFrame.Time, dataFrame.Ping) # plot
plt.gcf().autofmt_xdate() # format the dates
plt.show() # show graph
