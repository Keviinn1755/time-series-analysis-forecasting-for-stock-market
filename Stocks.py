import streamlit as st

#page configure and headline title

st.set_page_config(
    page_title="Stocks View",
    page_icon="chart_with_downwards_trends:",
    layout="wide"
)

st.title("Trading Guide :bar_chart:")

st.header("We provide the Greatest platform for you to collect all information prior in stocks.")

st.image("sam.jpg")

st.markdown("## We provide the following services")

st.markdown("### :one: Stock Information")
st.write("Through this page, you can see all the  information about stock.")

st.markdown("### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forcasting models.Use this tool to gain valuable insights into market trends and make informed investment decisons")

st.markdown("### :three: CAPM Return")
st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stocks asset based on its risk and market performance")

st.markdown("### :four: CAPM Beta")
st.write("Calculates Beta and Expected Return for Individual Stocks")