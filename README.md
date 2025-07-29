# LivePlot
Visualizing data from Yahoo finance to test the extent of free, readily available apis in obtaining live data

# Methodology
Making use of the following readily available Python apis to source, clean and visualize data from Yahoo Finance.
    1. yfinance - api used to obtain data from yahoo finance
    2. numpy - api used to clean data
    3. pandas - api used to structure obtained data from yahoo finance as a dataframe
    4. plotly - used for visualizing the opening and closing price of shares as a candlestick graph

# Implementation
As far as implementation is concerned, this is a relatively easy approach that obtains the stock listing name, the time period of evaluation and the data interval from the user and utilizes them as parameters to query the yfinance database to retrieve the desired results.

The visualization, which is done with plotly, converts the dataframe obtained into a candlestick chart with the time intervals on the x-axes (controlled with a slider) and share price on the y-axis

# Limitations
As the aim of this project was to test the limitation of yfinance, we can see that it is unable to provide truly live data. The data produced in the above method seems to be a day old at the latest.

# Future Growth
While the data produced is not live, the database contains a plethora of historical data which can be used to train stock price prediction models. To obtain the live element, will explore the connectivity of Python and Apache frameworks like Kafka (consideration due to prior experience). May pivot to another library in case this connection is not feasible for requirements.

# Author
Sid