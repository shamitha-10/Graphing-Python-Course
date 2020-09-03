

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='3HD0BB62EJKUQB2O', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='BSE',interval='60min', outputsize='full')
data['4. close'].plot()
plt.plot()
plt.show()