import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import base64
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Sephora", page_icon=":lipstick:", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

lottie_coding = load_lottiefile("Images/Animations/Box.json")
lottie_coding2 = load_lottiefile("Images/Animations/Makeup.json")

# Define the img_to_bytes and img_to_html functions
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' width='200' style='padding: 10px;'>".format(
        img_to_bytes(img_path)
    )
    return img_html

st.markdown(
    """
    <style>
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background-color: #FFF5E1;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .title {
        color: #FF006E;
        font-size: 36px;
        font-weight: bold;
        margin-left: 20px; /* Add margin to separate the title from the logo */
    }
    .logo {
        width: 100px; /* Adjust the width as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container div that holds both the logo and the title
st.markdown(
    """
    <div class="title-container">
        {}
        <div class="title">Personalized Recommendation System</div>
    </div>
    """.format(img_to_html("Images/Sephora-Logo.png")), # Replace with the path to your logo image
    unsafe_allow_html=True
)


with st.container():
    st.markdown('<p class="welcome-text">Welcome to the personalized recommendation system for Sephora! 🛍️🌟 Our innovative platform is designed to make your beauty product discovery journey delightful. 🌺🎉 We curate tailored suggestions based on your unique preferences, so you can uncover the perfect cosmetics that match your style. 💄🔍 Whether it is skincare, makeup, or fragrance, let us guide you to your beauty haven! 😍🌟</p>', unsafe_allow_html=True)

# Create two columns for animation and text
col1, col2 = st.columns([1, 2])

# Display the animation in the first column
with col1:
    st.lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=500,
        width=500,
        key=None,
    )


# Display the new text in the second column within a centered box
with col2:
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 400px; margin-left: 50px">
            <h2 style="margin-top: 20px; text-align: center; text-decoration: underline;">Wide Range Of Categories</h2>
            <div style="background-color: #7B68EE; padding: 10px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); text-align: center;">
                <p style="color: #333; font-size: 24px;">
                    Our service offers bespoke recommendations for a diverse range of cosmetic categories, including skincare💆‍♀️, makeup💄, haircare💇‍♀️, and fragrance🌸. Allow us to help you achieve your most radiant self! 😊
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Create two columns for animation and text
col3, col4 = st.columns([2, 1])

# Display the animation in the first column
with col4:
    st.lottie(
        lottie_coding2,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=500,
        width=500,
        key=None,
    )


# Display the new text in the second column within a centered box
with col3:
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 500px; margin-left: 50px; margin-bottom: 100px;">
            <h2 style="text-align: center; text-decoration: underline;">Personalized Beauty Guidance</h2>
            <div style="background-color: #FFD700; padding: 0px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); text-align: center;">
                <p style="color: #333; font-size: 24px;">
                    Our recommendations are tailored to your individual needs, taking into account factors such as skin type, personal preferences, and budget💰. Our goal is to assist you in discovering the most suitable products for your unique requirements and to empower you to make informed decisions about your beauty regimen💅. Whether you are in search of a revitalizing moisturizer or the ideal shade of lipstick💋, our service is here to guide you.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Style the title with CSS
st.markdown(
        """
        <style>
        .title2 {
            color: #FFFFFF;
            font-size: 40px;
            text-align: center;
            padding: 10px;
            background-color: #1E90FF;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            margin-top: -30px;
            display: inline-block;
        }
        .bold-text {
            font-weight: bold;
        }
        .welcome-text {
        font-size: 24px;
        text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Display the Sephora box with bold text
st.markdown('<div style="text-align:center; margin-bottom: 20px;"><div class="title2"><span class="bold-text">Wide range of products</span></div></div>', unsafe_allow_html=True)



# Display the images in a single row with boxes around them and background colors
_,col5, col6, col7, col8,_ = st.columns([0.5,1,1,1,1,0.5])

with col5:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:center;">Cosmetics</div>""",unsafe_allow_html=True)
    st.image("Images/Gifts.jpg",width=220)
    
with col6:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:      center;">Cleanser</div>""",unsafe_allow_html=True)
    st.image("Images/Cleanser.jpg",width=220)
    
with col7:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:      center;">Masks</div>""",unsafe_allow_html=True)
    st.image("Images/Masks.jpg",width=220)

with col8:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:      center;">Mini</div>""",unsafe_allow_html=True)
    st.image("Images/minis.jpg",width=220)
    
# Display the images in a single row with boxes around them and background colors
_,col9, col10, col11, col12,_ = st.columns([0.5,1,1,1,1,0.5])

with col9:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:center;">High Tech</div>""",unsafe_allow_html=True)
    st.image("Images/Hightech.jpg",width=220)
    
with col10:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:      center;">Moiturizer</div>""",unsafe_allow_html=True)
    st.image("Images/Moisturizer.jpg",width=220)
    
with col11:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:      center;">Lip Balm</div>""",unsafe_allow_html=True)
    st.image("Images/Lip.jpg",width=220)

with col12:
    st.markdown(f"""<div style="font-size: 24px; font-weight: bold; color: #FF6B88; text-align:      center;">Sunscreen</div>""",unsafe_allow_html=True)
    st.image("Images/Sunscreen.jpg",width=220)

# Style the title with CSS
st.markdown(
        """
        <style>
        .title3 {
            color: #FFFFFF;
            font-size: 40px;
            text-align: center;
            padding: 10px;
            background-color: #FF69B4;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            margin-top: 30px;
            display: inline-block;
        }
        .bold-text {
            font-weight: bold;
        }
        .welcome-text {
        font-size: 24px;
        text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Display the Sephora box with bold text
st.markdown('<div style="text-align:center; margin-bottom: 20px;"><div class="title3"><span class="bold-text">Recommendation</span></div></div>', unsafe_allow_html=True)


# Display a message and prompt user to enter their name
st.write(f"""<h1 size:18px>Let's start with our recommendations!</h1>""",unsafe_allow_html=True)

col11, col12, _ = st.columns([1,2,2])

with col11:
    st.text("")
    st.text("")
    st.write("Please enter your good name  :")

with col12:
    st.session_state["user_name"] = st.text_input("")

custom_css = """
<style>
    .stTextInput input {
        background-color: #ADD8E6;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

if st.button("Continue"): 
    switch_page("Recommendation")












