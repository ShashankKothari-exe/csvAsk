import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




st.set_page_config(
    page_title="CSV Analysis APP",
    page_icon="〽️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

#To hide hamburger menu
hide_streamlit_style = """


            <!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
          margin: 0;
        }

        .wrapper {
          position: relative;
          z-index: 1;
          display: inline-block;
          width: 100vw;
        }

        .hidefooter {
          position: absolute;
          width: 150px;
          height: 35px;
          background: rgb(242,240,246);
          right: 0px;
          bottom: 0px;
          z-index: 2;
          display: block;
          color: rgb(0, 0, 0);
        }
    
        iframe {
          display: block;
          background: #ffffff;
          border: none;
          height: 99vh;
          width: 99vw;
        }
        #MainMenu {visibility: hidden;}
        </style>    

</head>
<body>
  <div class="wrapper">
    <div class="hidefooter"></div>
    <iframe src="https://<<your.app.URL>>/?embed=true">
        <p>Your browser doesn't support iframes</p>
    </iframe>
    </div>
</body>
</html>
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 












#importing dataset
df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
try:
    dataset=st.file_uploader("Choose a CSV file", accept_multiple_files=False)
    df = pd.read_csv(dataset)
    try:
        df.drop(['Unnamed: 0'],axis=1,inplace=True)
    except:
        ""     
    df.to_csv('tmpdataset.csv', index=False)
    dsstr=dataset.name
    del dataset
except:
    dsstr="Randomly generated"
    df.to_csv('tmpdataset.csv', index=False)
finally:
    ""   
def showStats():
    st.write('Mean:')
    st.write(df.mean())
    st.write('\nMedian:')
    st.write(df.median())
    st.write('Mode:')
    st.write(df.mode(axis='columns', numeric_only=True))
    st.write('\nStandard Deviation:')
    st.write(df.std())
    st.write('\ncorrelation coefficient:')
    st.write(df.corr())
    st.write('\ncorvariance:')
    st.write(df.cov())

    st.line_chart(df)
    df.plot.scatter(x=list(df)[0], y=list(df)[1], title='Scatter Plot')
    st.scatter_chart(
    df,
    x=list(df)[0],
    y=list(df)[1],
    )

    st.bar_chart(df)
    fig, ax = plt.subplots()
    ax.hist(df, bins=20)
    st.pyplot(fig)

def defaultMsg():
    st.write("Go to the chat section to ask questions about your data.")
    df.shape


dsstr+' Dataset:'
st.dataframe(df.style.highlight_max(axis=0))
try:
    showStats()
except:
    ''
finally:
    defaultMsg()
    " "
    " "
    "Link to this project on my GitHub:"
    st.page_link("https://github.com/ShashankKothari-exe/csvAsk", label="csvAsk", icon="〽️")