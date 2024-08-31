import streamlit as st
# Title of the application
st.title('My First Streamlit Application')

# Heading or text
st.write("this is text")

# Markdown
st.markdown("this is markdown")

# Slider
number=st.slider("pick the value " , 0 ,100)

# print the selected number
st.write(f" you selected {number}")

# Adding Button
if st.button('Hit me'):
    st.write("helllo g")

# add radio button with options
# st.radio('Pick one:', ['nose','ear'])

# genure=st.radio('whats your favorite genure',['comedy','darama'])

# add drop downlist
#options=st.selectbox(
   # 'how you would like to connect' ,
    #('Gmail', 'Home PHONE', 'MOBILE PHONE')
#)

# Adding drop down list in the left side bar
options=st.sidebar.selectbox(
    'how you would like to connect' ,
    ('Gmail', 'Home PHONE', 'MOBILE PHONE')
)
st.sidebar.text_input("enter your whatsup number")

#file uploader option
uploaded_file =st.file_uploader('File uploader') 

# file uploader in the side bar option
uploaded_file =st.sidebar.file_uploader('File uploader') 

# Display the uploaded file

if uploaded_file is not None:
    st.image(uploaded_file)

# Add a progress bar
