
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

#np.random.seed(0)
headers = ['Schedule$', 'ScheduleH']
file=pd.read_csv('Kim Scheudle FP8 W3&4.csv', names=headers)
print(file[5:6])


