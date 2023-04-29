from matplotlib import pyplot as plt
import pandas as pd


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True


dataFrame = pd.read_csv('LittleToPlot.csv', names=['Date', 'Time', 'Count', 'Ping'] , header=None)
dataFrame['Ping'] = dataFrame['Ping'].str.replace('error/timedout', '0') # replace the errors with 0
dataFrame['Ping'] = dataFrame['Ping'].astype(float) # convert data from string to float



plt.scatter(dataFrame.Time, dataFrame.Ping)
plt.show()
