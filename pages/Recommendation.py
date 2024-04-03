import streamlit as st
import pandas as pd
import numpy as np

# Import datasets
products = pd.read_csv("Datasets/product_info.csv")
groups = pd.read_csv("Datasets/Groups.csv")
recommendations = pd.read_csv("Datasets/Product_Recommendations.csv").set_index("Group name")

# Style the title with CSS
st.markdown(
        """
        <style>
        .title1 {
            color: #FF006E;
            font-size: 60px;
            text-align: center;
            padding: 10px;
            background-color: #FFF5E1;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            margin-top: -30px;
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

name = st.session_state["user_name"]

with st.container():
    st.markdown(f"""<p class="welcome-text">Hello, A very warm WELCOME {name}!<br> It is lovely to have you!<br> Please enter your details😍🌟</p>""", unsafe_allow_html=True)


# Skin tone 

_,col1, col2,_ = st.columns([0.5,1,2,1])

with col1:
    st.write("##")
    st.write(f"""<p style="margin-left: 55px;">Skin tone :</p>""",unsafe_allow_html=True)
with col2:
    skin_tone = st.selectbox("", groups["Skin tone"].unique(), index=0)

# Skin type 

_,col3, col4, _ = st.columns([0.5,1,2,1])

with col3:
    st.write("##")
    st.write(f"""<p style="margin-left: 55px;">Skin type :</p>""",unsafe_allow_html=True)
with col4:
    skin_type = st.selectbox("", groups["Skin type"].unique(), index=0)

# Hair color

_,col5, col6, _ = st.columns([0.5,1,2,1])

with col5:
    st.write("##")
    st.write(f"""<p style="margin-left: 55px;">Hair color :</p>""",unsafe_allow_html=True)
with col6:
    hair_color = st.selectbox("", groups["Hair color"].unique(), index=0)

# Eye color

_,col7, col8, _ = st.columns([0.5,1,2,1])

with col7:
    st.write("##")
    st.write(f"""<p style="margin-left: 55px;">Eye color :</p>""",unsafe_allow_html=True)
with col8:
    eye_color = st.selectbox("", groups["Eye color"].unique(), index=0)

skin_tone_label = [k for k,v in dict(pd.Series(groups["Skin tone"].unique())).items() if v==skin_tone]
skin_type_label = [k for k,v in dict(pd.Series(groups["Skin type"].unique())).items() if v==skin_type]
hair_color_label = [k for k,v in dict(pd.Series(groups["Hair color"].unique())).items() if v==hair_color]
eye_color_label = [k for k,v in dict(pd.Series(groups["Eye color"].unique())).items() if v==eye_color]

group_name = int(str(skin_tone_label[0])+str(eye_color_label[0])+str(skin_type_label[0])+str(hair_color_label[0]))

products_list = recommendations.loc[group_name].Recommendations
products_list = products_list.strip("[]").split("\n")
products_list = [product.strip().strip("'") for product in products_list]
cosmetics = []
for item in products_list:
    cosmetics.extend(item.split("' '"))
cosmetics = [cosmetic.strip() for cosmetic in cosmetics]

secondary_categories=[]
for i in cosmetics:
    category_2nd = products[products.product_name==i].secondary_category
    if str(category_2nd.values[0])=="nan":
        continue        
    elif category_2nd.shape == ():
        secondary_categories.append(category_2nd)
    else:
        secondary_categories.append(category_2nd.iloc[0])
            
secondary_categories = [k+" ("+str(v)+")" for k,v in {i:secondary_categories.count(i) for i in secondary_categories}.items()]
secondary_categories.insert(0,"All (30)")

tertiary_categories=[]
for i in cosmetics:
    category_3rd = products[products.product_name==i].tertiary_category
    if str(category_3rd.values[0])=="nan":
        continue        
    elif category_3rd.shape == ():
        tertiary_categories.append(category_3rd)
    else:
        tertiary_categories.append(category_3rd.iloc[0])
            
tertiary_categories = [k+" ("+str(v)+")" for k,v in {i:tertiary_categories.count(i) for i in tertiary_categories}.items()]
tertiary_categories.insert(0,"All (30)")

# Add custom CSS styles
st.markdown(
    """
    <style>
    .product-name {
        font-size: 24px;
        margin-bottom: 10px;
        color: #333;
        background-color: #6ec6ff;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)
# col9,col10,_ = st.columns([2,1,2])

# if col10.button("Show Products"):

with st.container():
    st.markdown(f"""<p class="welcome-text" style="margin-top: 20px">Category Filter</p>""", unsafe_allow_html=True)


# Primary category filter
_,col11, col12,_ = st.columns([0.5,1,2,1])

with col11:
    st.write("##")
    st.write(f"""<p style="margin-left: 0px;">Primary Category :</p>""",unsafe_allow_html=True)
with col12:
    primary_category = st.selectbox("", secondary_categories)
    filtered_cosmetics = cosmetics.copy()
    if primary_category!="All (30)":
        for i in cosmetics:
            if products[products.product_name==i].secondary_category.values[0]!=" ".join(primary_category.split(" ")[:-1]):
                filtered_cosmetics.remove(i)
        tertiary_categories = []
        for i in filtered_cosmetics:
            category_3rd = products[products.product_name==i].tertiary_category
            if str(category_3rd.values[0])=="nan":
                continue        
            elif category_3rd.shape == ():
                tertiary_categories.append(category_3rd)
            else:
                tertiary_categories.append(category_3rd.iloc[0])
            
        tertiary_categories = [k+" ("+str(v)+")" for k,v in {i:tertiary_categories.count(i) for i in tertiary_categories}.items()]
        tertiary_categories.insert(0,"All ("+str(len(filtered_cosmetics))+")")

        
# Secondary category filter
_,col13, col14, _ = st.columns([0.5,1,2,1])
with col13:
    st.write("##")
    st.write(f"""<p style="margin-left: 0px;">Secondary cateogry :</p>""",unsafe_allow_html=True)
with col14:
    secondary_category = st.selectbox("",tertiary_categories, index=0)
    if secondary_category.split(" ")[0]!="All":
        for i in filtered_cosmetics:
            if products[products.product_name==i].tertiary_category.values[0]!=" ".join(secondary_category.split(" ")[:-1]):
                filtered_cosmetics.remove(i)

bg_colors = ["#ff9a9e", "#fad0c4", # Warm Flame
        "#ffecd2", "#fcb69f", # Juicy Peach
        "#ff9a9e", "#fecfef", # Lady Lips
        "#a1c4fd", "#c2e9fb", # Winter Neva
        "#cfd9df", "#e2ebf0", # Heavy Rain
        "#fdfbfb", "#ebedee", # Cloudy Knoxville
        "#f5f7fa", "#c3cfe2", # Saint Petersberg
        "#667eea", "#764ba2", # Plum Plate
        "#ff6b6b", "#fda085", # Sunset
        "#ee9ca7", "#ffdde1", # Grapefruit Sunset
        "#bdc3c7", "#2c3e50", # Deep Space
        "#acb6e5", "#86fde8", # Shroom Haze
        "#74ebd5", "#acb6e5", # Shifter
        "#fc5c7d", "#6a82fb", # Royal
        "#ee0979", "#ff6a00"]  # Mauve

st.write(f"""<h1 style="margin-top: 20px;">Products:</h1>""",unsafe_allow_html=True)
# Iterate through the list of products and display the names
for product in enumerate(filtered_cosmetics):
    st.markdown(f"""<div class='product-name' style="background-color:{bg_colors[product[0]]};">{product[1]}</div>""", unsafe_allow_html=True)


# Add custom CSS styles for the layout
st.markdown(
    """
    <style>
    .custom-box {
        border: 2px solid #3498db;
        background-color: #f2f2f2;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }
    .column-label {
        font-size: 18px;
        margin-bottom: 5px;
        color: #666;
    }
    .dropdown {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)



