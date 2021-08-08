from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def display_stationarity_info(message, ts) :

    # Get ADF statistics, and print results.
    adf_result = adfuller(ts)
    print('\n%s' % message)
    print('-------------------------------------------')
    print('ADF Statistic    \t %g' % adf_result[0])
    print('p-value          \t %g' % adf_result[1])    
    for k,v in adf_result[4].items() :
        print('Critical value (%s) \t %s' % (k, v))


    # Determine rolling statistics.
    rolling = ts.rolling(window=12)   # Get a Rolling object, which enables us to determine rolling values over a specified window size (12 months here).
    rolling_mean = rolling.mean()     # Calculate the rolling mean, over 12-month windows.
    rolling_std  = rolling.std()      # Calculate the rolling standard deviation, over 12-month windows. 

    # Plot rolling statistics.
    orig = plt.plot(ts, color='blue', label='Original')
    mean = plt.plot(rolling_mean, color='orange', label='Rolling mean')
    std  = plt.plot(rolling_std,  color='purple', label = 'Rolling std dev')

    plt.legend()
    plt.title(message)
    plt.show()

