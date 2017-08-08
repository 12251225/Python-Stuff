<<<<<<< HEAD

import csv
import pandas  as pd
import matplotlib.pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta

d=lambda x:pd.datetime.strptime(x,'%d-%b-%y')
dateparse = lambda x:d(x)
df= pd.read_csv("Mike's SQL export.csv", parse_dates=['CALENDAR_DATE'],date_parser=dateparse)

print(df[:5])

x=df['CALENDAR_DATE']
y=df['MEASURE_QTY']

plt.plot(x[:5000],y[:5000])
plt.show()
=======
#test case
import csv
import pandas  as pd
import matplotlib.pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta

d=lambda x:pd.datetime.strptime(x,'%d-%b-%y')
dateparse = lambda x:d(x)
df= pd.read_csv("Mike's SQL export.csv", parse_dates=['CALENDAR_DATE'],date_parser=dateparse)

print(df[:5])

x=df['CALENDAR_DATE']
y=df['MEASURE_QTY']

plt.plot(x[:5000],y[:5000])
plt.show()
>>>>>>> fbca7da7abe4ab3d4609abfd3dad9c5f7cbf0209
