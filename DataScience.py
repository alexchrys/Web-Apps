# %%
import yfinance as yf
import pandas as pd

# %%
#Lets create our Dataframe
ticker1 = "GOOGL"
ticker2 = "AMZ"

tickerData1 = yf.Ticker(ticker1)
tickerData2 = yf.Ticker(ticker2)

df_1 = tickerData1.history(period= "1d", start= "2013-4-30", end= "2018-4-30")
df_2 = tickerData2.history(period= "1d", start= "2013-4-30", end= "2018-4-30")


df_1.head()
#to create an optimal line chart, we have to transform the Date Index to a column and then merge the two Datafames.

df_1 = df_1.reset_index(level=0)
df_1.head()
df_2 = df_2.reset_index(level=0)
df_2.head()


tickerDf = pd.merge(df_1, df_2, how="inner", on= "Date", sort=True, suffixes=("_GOOGL", "_AMZ"))

# %%
tickerDf.head()

# %%
#Lets create our visualization
tickerDf.plot(x="Date", y=["Close_GOOGL","Close_AMZ"])

# %%



