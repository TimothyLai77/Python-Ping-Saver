from matplotlib import pyplot as plt
from matplotlib import ticker
import pandas as pd

plt.rcParams["figure.figsize"] = [20, 10]
plt.rcParams["figure.autolayout"] = True

# read data
dataFrame = pd.read_csv('toplot.csv', names=['Date', 'Time', 'Ping'] , header=None)

# to handle the error/timeout when ping doesn't exit properly
if 'error/timedout' in dataFrame.values : 
    dataFrame['Ping'] = dataFrame['Ping'].str.replace('error/timedout', '0') # replace the errors with 0
    dataFrame['Ping'] = dataFrame['Ping'].astype(float) # convert data from string to float


# graph stuff

plt.scatter(dataFrame.Time, dataFrame.Ping,s=3, alpha=0.5,c=dataFrame.Ping, cmap='plasma') # plot

ax = plt.gca();

plt.gca().set_yscale('log')

xticks = plt.gca().get_xticks()
plt.gca().set_xticks(xticks[::len(xticks) // 10]) # set new tick positions
plt.gca().tick_params(axis='x', rotation=30) # set tick rotation

# Log scale yaxis tick formatting: https://stackoverflow.com/a/61352317
ax.yaxis.set_major_locator(ticker.MultipleLocator(100))  # major y tick positions every 100

ax.yaxis.set_minor_locator(ticker.NullLocator())  # no minor ticks
ax.yaxis.set_major_formatter(ticker.ScalarFormatter())  # set regular formatting



plt.gcf().autofmt_xdate() # format the dates

plt.savefig('plot.png');
plt.show() # show graph
