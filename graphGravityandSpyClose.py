#!/usr/bin/env python2
"""
Created on Tue Apr 25 16:15:21 2017

@author: nickwilliams
"""


import matplotlib   
import matplotlib.pyplot as plt
from math import pow
import ephem
from datetime import date, timedelta, datetime 
from yahoo_finance import Share



def get_history(symbol):
    stock = Share(symbol).get_historical(str((date.today()-timedelta(days=4000))), str(date.today()))
    return stock

indexplanets = ('moon', 'mercury', 'saturn', 'jupiter', 'neptune', 'uranus',
    'venus','mars')  

spy = get_history('SPY')

x2 = []
for d in range(len(spy)):
    graphd = datetime.strptime(spy[d]['Date'], '%Y-%m-%d').date()
    x2.append(graphd)
y3 = [spy[d]['Close'] for d in range(0,len(spy))]
plt.subplot(len(indexplanets)+1,1,1)
plt.plot(x2[49:],y3[49:])
plt.title('XLE close')
# beautify the x-labels
plt.gcf().autofmt_xdate()
plotcount = 2
for i in range(0,len(indexplanets)):
    plt.subplot(len(indexplanets)+1,1,(plotcount+i))
    y = [pull(d,indexplanets[i]) for d in x2]
    y2 = []
    x3 = []
    for p in range(49,len(y)):
        total = 0
        count = 0
        for m in range(0,50):
            total += y[p-m]
            count +=1
        print count
        avg = total/50.0
        y2.append(avg)
        x3.append(x2[p])
    print len(x3), len(y[49:])
    plt.plot(x3,y[49:],'r', x3,y2,'g')
    plt.title('%s gravitational pull on earth based on daily distance' %(indexplanets[i]))
    plt.gcf().autofmt_xdate()
# plot
#plt.plot(x2,y1)
#plt.title('Saturn gravitational pull on earth based on daily distance')
#plt.gcf().autofmt_xdate()
#plt.subplot(3,1,2)
#plt.plot(x2,y2)
#plt.title('Moon gravitational pull on earth based on daily distance')
#plt.gcf().autofmt_xdate()


plt.show()