# Python-Ping-Saver

Pings www.google.com about every second and writes to a csv file with the format: `mm/dd/yyyy,hh:mm:ss,pingCount,pingTime,highPingCount` Example: `04/20/2023,15:47:19,5,577.407,2`.

- It's not very well written (first time writing python lol), originally wrote this quickly because my ISP was giving me issues.

- Later updated (2024)... because my ISP was giving me more issues, added new features like a threshold in `ping.py` and it counts number of high pings. Those can be plotted later.

  - This is actually pretty dumb, you can probably do this with pandas or numpy somehow but this was faster to do.

# Sample Plot

![sample plot](https://raw.githubusercontent.com/TimothyLai77/Python-Ping-Saver/main/sampleplot.png)
