# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 01:58:50 2022

@author: SPTINT-07
"""
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/varshitha/athlete_events.csv")
plt.scatter(data['Height'],data['Weight'])
plt.title("SCATTER PLOT GRAPH")
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
