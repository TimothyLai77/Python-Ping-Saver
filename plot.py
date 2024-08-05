from matplotlib import pyplot as plt
from matplotlib import ticker
import pandas as pd
import sys
# Command Line args to plot on log scale or not
if(len(sys.argv) > 1 and sys.argv[1] == 'log') :
    plotOnLog = True
else:
    plotOnLog = False


plt.rcParams["figure.figsize"] = [20, 10]
plt.rcParams["figure.autolayout"] = True

# read data
dataFrame = pd.read_csv('toplot.csv', names=['Date', 'Time', 'Ping', 'highPing'] , header=None)

# to handle the error/timeout when ping doesn't exit properly
if 'error/timedout' in dataFrame.values : 
    dataFrame['Ping'] = dataFrame['Ping'].str.replace('error/timedout', '0') # replace the errors with 0
    dataFrame['Ping'] = dataFrame['Ping'].astype(float) # convert data from string to float


# ============= Graph Stuff =============
# ------------- Plot Raw Pings -------------
plt.subplot(1, 2, 1)
plt.scatter(dataFrame.Time, dataFrame.Ping,s=3, c=dataFrame.Ping, cmap='plasma') # plot

# get current axes and assign to ax
ax = plt.gca();
ax.set_facecolor('#c2c2c2')
# change the ticks along the x axis
xticks = ax.get_xticks() # returns list of x locations?
ax.set_xticks(xticks[::len(xticks) // 10]) # set new tick positions
ax.tick_params(axis='x', rotation=30) # set tick rotation

# Log scale yaxis tick formatting: https://stackoverflow.com/a/61352317

if plotOnLog : 
    ax.set_yscale('log') # change y scale
    logScaleTitle=' [log scale]'
else:
    logScaleTitle=' [linear scale]'
ax.yaxis.set_major_locator(ticker.MultipleLocator(100))  # major y tick positions every 100

ax.yaxis.set_minor_locator(ticker.NullLocator())  # no minor ticks
ax.yaxis.set_major_formatter(ticker.ScalarFormatter())  # set regular formatting

plt.gcf().autofmt_xdate() # format the dates
plt.title("Raw Plot (ms vs. Time)"+logScaleTitle)# the tihe graph

# add y=200 line to see pings past threshold
threshold=200
plt.axhline(y = threshold, color = 'r', alpha=0.5, linestyle = 'dotted') 


# ------------- Plot High Pings -------------
plt.subplot(1, 2, 2)
plt.plot(dataFrame.Time, dataFrame.highPing)
plt.title("Cumulative # of pings past threshold="+str(threshold)+" ms")
# x axis stuff.... Can't really be bothered to figure out how to not duplicate code but whatever
ax = plt.gca();
ax.set_facecolor('#c2c2c2')
xticks = ax.get_xticks() # returns list of x locations?
ax.set_xticks(xticks[::len(xticks) // 10]) # set new tick positions
ax.tick_params(axis='x', rotation=30) # set tick rotation

plt.savefig('plot.png'); # output
plt.show() # show graph
