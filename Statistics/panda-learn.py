import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader as web

style.use('ggplot')


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("INPX", "yahoo", start, end)