import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint
import plotly.express as px

st.set_page_config(
   page_title="C'est le mauvais choix"
)

st.title("Tu ne veux vraiment pas ? 😭")
st.link_button("Si si je suis désolé ne pleure pas", "https://adelemarcon.github.io/DM6adele.html",type="primary",use_container_width=True)
st.link_button("Non", "https://mauvaischoix.streamlit.app/",type="primary",use_container_width=True)
st.image('https://github.com/adelemarcon/NON/blob/main/tortuenon.png?raw=true')
