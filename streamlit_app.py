from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")

st.subheader("Hi, I'am Chimbersly Perez :wave:")
st.title("A Phython Explorer")
st.write("I Love Coding")
st.write("[Learn More >](https://phytonandvba.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do!")
        st.write("##")
        st.write( 
            """
            - I accept python tutorial
            - I love Debugging
            - I accept any work you want me to do!
            """
        )
        st.write("[Youtube Channel >](https://youtube.com/c/CodingIsFun)")

with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_columns, text_columns = st.columns((1, 2))


with text_columns:
        st.subheader("MY PROJECT!!!")
        st.write(
            """
            -Learn how to get more interest in coding!
            
            -Get more interesting Guide!

            """
        )
