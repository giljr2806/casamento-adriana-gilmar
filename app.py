import streamlit as st
import dropbox
from datetime import datetime
import base64

# 1. Configuração da Página
st.set_page_config(page_title="Adriana & Gilmar 2026", page_icon="💍")

# Função para colocar a imagem de fundo (Background)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string.decode()}");
        background-size: cover;
        background-position: center;
    }}
    /* Caixa branca semi-transparente para o texto não sumir */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.7);
        padding: 30px;
        border-radius: 20px;
        margin-top: 50px;
    }}
    h1, h3, p {{ color: #5d4037 !important; text-align: center; }}
    .stButton>button {{ width: 100%; border-radius: 50px; height: 3.5em; background-color: #8d6e63; color: white; border: none; font-weight: bold; }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Tenta carregar a imagem com o nome exato que está no seu GitHub
try:
    add_bg_from_local('capa.JPG')
except:
    st.warning("Imagem de fundo não encontrada. Verifique o nome do arquivo no GitHub.")

# 2. Conteúdo do App
st.title("Nosso Álbum Digital")
st.write("### Adriana & Gilmar")
st.write("**28 de Junho de 2026**")
st.write("---")

# 3. CONFIGURAÇÃO DROPBOX
ACCESS_TOKEN = 'sl.u.AGUko160ahwBTqIttavg0m57OQ4AqyIEpUAIaNWKC2a1noiuA77mFdls2UM_x_BkdMeAoSkGDq-IUiCgJJ9UzKsJz_aVI-VZ6-wqYC5cnQ4N_4Z18P2773hEmYy_aoN3mJeBgxRsoNBd6KtYERxISrlwn1Fc2ki4whMcopJPUXAtQd0oE2Me7nkK6o1HRFxlRhqE2wPKG8CIMwu6BBFee8L0-AtAmmWGsNhFex0x0eS9CgZQG0Jm6kmZVbqZJIHK9if0SgecVObzhp-f3e-Tzhsirw2BSYn1g9E-DQLY_9QkSz9hevBKFG6mQdVKyPTk60-YC70jL8WQYZPCYXy4aEeKAcs2IdgKN96wlomL9HzggCIZl_yugBn71oRl0goX_UnL9uUTrCb06p7M-rpGD4WuS5Ya0xMHiDFtrZcnIDTELBZN_55DYr3Pi7oPDmoC3_S1-PYxsxyW28cBY8BPxhDqMzUeal5799P8vHLd_d5n7aJyvSrTbEIig5M3S05Sak_AdegTMnJZTf9mWxxSLq-IHzF8bkX8i2E_cLl8sLoa375iMOiKAQapas3Bw8gruQDW9cjut3clCtZuLhiKFbIgEU6PZVeTm2FwFpeWs3qEBwRwZXR7__IvvnWpbijKteOe1h65Ulz4OY2n7E3PrUgzWgE6N_lOzNs0LUnetX1sc02i0P-3gGimpnljltco0XGAG5s3kK9_iBb1aVozpCGRZsSG-g-eJqXhtP9L-ui7kIx9pjJoiWQssB5-uMtQAmsDilxEJGj5sNZy--UAKDL9eJih59LJQ1Dlv4_EJACCrgRn9WNPVHlBmHONHr_LcnPqVN8YHOW_ydmuH_aWk6HLqFX6x7nSXWxIum6G-BZQbUjB_MjK3LtJxb0ZXlx5MT3IRMn3Z7npgjx5yOBXTZh9Yct0OPeBTR50nq0f_yBX6QeF74QeQg4Bs-hLw7bzP0kuNOFkZdImIslWed_tjXvTFe4IPoL-JgLC1uc0xuBFrYK-PUJZ7s4lBQeMxGNdJ3jazO5cEdadTi5h8gofFtqVTOyRoHxTFBmHMilpRbDkhAPFvwV5z4FPfjtvYTZDyjE8m9oR-YqxgMhV4PsLAmxbzpYO2Gj2FcaUF02sWOtBpy5ynNejzmyCWW4N-pwWbse-fsR10ZNg_8rP_twtMmirxEw5WugJJh1AHoGrYedBjxneekk1ZMxJkIhMmifJLGy3YyGxwFa1k5I87mVp9OQdWKxva4fs11wVYKH-nz9OfA1F8w_bO1dweJ9jZCI80sryjXrVzBCCylNxGVfkrgybtutIr0pvc2Kn1_hToOjMP2_NR4m_pkUkzm5H3f_XFcRMOuKpr3cIf3KAmw04FHRmKCOyhdg5mgmssjHtOoE0Cp7j3nlpPzIWICS9AuUbdxs'

foto = st.camera_input("Toque para abrir a câmera")

if foto:
    try:
        dbx = dropbox.Dropbox(ACCESS_TOKEN)
        nome_final = f"/foto_{datetime.now().strftime('%H%M%S')}.jpg"
        with st.spinner('Enviando...'):
            dbx.files_upload(foto.getvalue(), nome_final)
        st.success("✅ Foto enviada!")
        st.balloons()
    except Exception as e:
        st.error(f"Erro: {e}")
