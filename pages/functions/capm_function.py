import numpy as np
import plotly.express as px


# function to plot interactive plotly chart


def interactive_plot(df):
    fig= px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y = df[i], name = i)
    fig.update_layout(width = 450, margin = dict(l=20, r =20, t =50, b =20), legend = dict(orientation = 'h', yanchor = 'bottom',
        y = 1.02, xanchor = 'right', x = 1,))
    return fig

# fucntion to normalize the prices based on the initial price

def normalize(df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i]/df[i][0] 
    return df

# function to calculate daily returns

def daily_retrun(df):
    df_daily_retrun = df.copy()
    for i in df.columns[1:]:
        for j in range(1,len(df)):
            df_daily_retrun[i][j] = ((df[i][j] -df[i][j-1])/df[i][j-1])*100
        df_daily_retrun[i][0] = 0
    return df_daily_retrun

# fucntion to calculate beta

def calculate_beta(stocks_daily_return, stock):
    rm = stocks_daily_return['SP500'].mean()*252
    

    b,a = np.polyfit(stocks_daily_return['SP500'], stocks_daily_return[stock], 1)
    return b,a

