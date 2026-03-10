import streamlit as st
import dropbox
from datetime import datetime

# 1. Configuração Visual
st.set_page_config(page_title="Casamento Adriana & Gilmar", page_icon="💍")

# Estilo para botões e layout
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #f0e4d7; color: #5d4037; font-weight: bold; }
    .main { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Nosso Álbum Digital")
st.write("### Adriana & Gilmar")
st.write("28 de Junho de 2026")
st.write("---")

# 2. CONFIGURAÇÃO DE ACESSO (Suas chaves fornecidas)
APP_KEY = '8qqcj9yjtmw8lic'
APP_SECRET = 'tnspu3a9c0xpeeh'
# Este token longo que você passou funciona como o "Refresh Token"
REFRESH_TOKEN = 'sl.u.AGUko160ahwBTqIttavg0m57OQ4AqyIEpUAIaNWKC2a1noiuA77mFdls2UM_x_BkdMeAoSkGDq-IUiCgJJ9UzKsJz_aVI-VZ6-wqYC5cnQ4N_4Z18P2773hEmYy_aoN3mJeBgxRsoNBd6KtYERxISrlwn1Fc2ki4whMcopJPUXAtQd0oE2Me7nkK6o1HRFxlRhqE2wPKG8CIMwu6BBFee8L0-AtAmmWGsNhFex0x0eS9CgZQG0Jm6kmZVbqZJIHK9if0SgecVObzhp-f3e-Tzhsirw2BSYn1g9E-DQLY_9QkSz9hevBKFG6mQdVKyPTk60-YC70jL8WQYZPCYXy4aEeKAcs2IdgKN96wlomL9HzggCIZl_yugBn71oRl0goX_UnL9uUTrCb06p7M-rpGD4WuS5Ya0xMHiDFtrZcnIDTELBZN_55DYr3Pi7oPDmoC3_S1-PYxsxyW28cBY8BPxhDqMzUeal5799P8vHLd_d5n7aJyvSrTbEIig5M3S05Sak_AdegTMnJZTf9mWxxSLq-IHzF8bkX8i2E_cLl8sLoa375iMOiKAQapas3Bw8gruQDW9cjut3clCtZuLhiKFbIgEU6PZVeTm2FwFpeWs3qEBwRwZXR7__IvvnWpbijKteOe1h65Ulz4OY2n7E3PrUgzWgE6N_lOzNs0LUnetX1sc02i0P-3gGimpnljltco0XGAG5s3kK9_iBb1aVozpCGRZsSG-g-eJqXhtP9L-ui7kIx9pjJoiWQssB5-uMtQAmsDilxEJGj5sNZy--UAKDL9eJih59LJQ1Dlv4_EJACCrgRn9WNPVHlBmHONHr_LcnPqVN8YHOW_ydmuH_aWk6HLqFX6x7nSXWxIum6G-BZQbUjB_MjK3LtJxb0ZXlx5MT3IRMn3Z7npgjx5yOBXTZh9Yct0OPeBTR50nq0f_yBX6QeF74QeQg4Bs-hLw7bzP0kuNOFkZdImIslWed_tjXvTFe4IPoL-JgLC1uc0xuBFrYK-PUJZ7s4lBQeMxGNdJ3jazO5cEdadTi5h8gofFtqVTOyRoHxTFBmHMilpRbDkhAPFvwV5z4FPfjtvYTZDyjE8m9oR-YqxgMhV4PsLAmxbzpYO2Gj2FcaUF02sWOtBpy5ynNejzmyCWW4N-pwWbse-fsR10ZNg_8rP_twtMmirxEw5WugJJh1AHoGrYedBjxneekk1ZMxJkIhMmifJLGy3YyGxwFa1k5I87mVp9OQdWKxva4fs11wVYKH-nz9OfA1F8w_bO1dweJ9jZCI80sryjXrVzBCCylNxGVfkrgybtutIr0pvc2Kn1_hToOjMP2_NR4m_pkUkzm5H3f_XFcRMOuKpr3cIf3KAmw04FHRmKCOyhdg5mgmssjHtOoE0Cp7j3nlpPzIWICS9AuUbdxs'

# 3. Função de Captura e Upload
arquivo_foto = st.camera_input("Toque abaixo para tirar a foto")

if arquivo_foto:
    try:
        # Conexão automática que se renova sozinha usando as chaves
        dbx = dropbox.Dropbox(
            app_key=APP_KEY,
            app_secret=APP_SECRET,
            oauth2_refresh_token=REFRESH_TOKEN
        )
        
        # Gerar nome único para a foto (Ex: foto_20260310_143005.jpg)
        agora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_final = f"/foto_{agora}.jpg"
        
        with st.spinner('Enviando para o álbum de Adriana & Gilmar...'):
            dbx.files_upload(arquivo_foto.getvalue(), nome_final)
            
        st.success("✨ Foto enviada com sucesso! Obrigado por celebrar conosco!")
        st.balloons()
        
    except Exception as e:
        st.error(f"Erro ao enviar: {e}")
        st.info("Tente novamente ou verifique sua conexão com a internet.")
