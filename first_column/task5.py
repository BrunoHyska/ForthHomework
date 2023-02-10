import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

yesterday = dt.datetime.now() - dt.timedelta(days=1)
today = dt.datetime.now()
tomorrow = dt.datetime.now() + dt.timedelta(days=1)
dates = np.array([yesterday, today, tomorrow])

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
