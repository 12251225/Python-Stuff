import matplotlib.pyplot as plt
import pandas as pd



file=pd.read_csv('Kim Scheudle FP8 W3&4.csv')

x=file['FISCAL_WEEK']
y=file['Schedule_Hourss']


#pop = [2.519, 3.682, 4.54, 5.546]
print(x)
#plt.scatter(year, pop)
#plt.show()
