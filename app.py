import streamlit as st
import dropbox
from datetime import datetime
from PIL import Image

# 1. Configuração da Página e Estilo CSS Customizado
st.set_page_config(page_title="Adriana & Gilmar 2026", page_icon="💍", layout="centered")

st.markdown("""
    <style>
    /* Fundo e Fonte */
    .main { background-color: #fdfbfb; }
    h1 { color: #5d4037; font-family: 'Playfair Display', serif; text-align: center; padding-top: 10px; }
    h3 { color: #8d6e63; font-family: 'Playfair Display', serif; text-align: center; font-style: italic; }
    
    /* Customização do Botão de Câmera */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background-color: #8d6e63;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #5d4037; color: white; }
    
    /* Ajuste da imagem de capa */
    .uploaded-img { border-radius: 15px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 2. Topo Premium com a Foto de Vocês
try:
    img_capa = Image.open("capa.jpg")
    st.image(img_capa, use_container_width=True)
except:
    # Caso a foto ainda não tenha sido subida, ele mostra um divisor elegante
    st.write("---")

st.title("Nosso Álbum de Memórias")
st.write("### Adriana & Gilmar")
st.write("<p style='text-align: center; color: #8d6e63;'>28 de Junho de 2026</p>", unsafe_allow_html=True)
st.write("---")

# 3. CONFIGURAÇÃO DROPBOX (Seu Token Atual)
ACCESS_TOKEN = 'sl.u.AGUko160ahwBTqIttavg0m57OQ4AqyIEpUAIaNWKC2a1noiuA77mFdls2UM_x_BkdMeAoSkGDq-IUiCgJJ9UzKsJz_aVI-VZ6-wqYC5cnQ4N_4Z18P2773hEmYy_aoN3mJeBgxRsoNBd6KtYERxISrlwn1Fc2ki4whMcopJPUXAtQd0oE2Me7nkK6o1HRFxlRhqE2wPKG8CIMwu6BBFee8L0-AtAmmWGsNhFex0x0eS9CgZQG0Jm6kmZVbqZJIHK9if0SgecVObzhp-f3e-Tzhsirw2BSYn1g9E-DQLY_9QkSz9hevBKFG6mQdVKyPTk60-YC70jL8WQYZPCYXy4aEeKAcs2IdgKN96wlomL9HzggCIZl_yugBn71oRl0goX_UnL9uUTrCb06p7M-rpGD4WuS5Ya0xMHiDFtrZcnIDTELBZN_55DYr3Pi7oPDmoC3_S1-PYxsxyW28cBY8BPxhDqMzUeal5799P8vHLd_d5n7aJyvSrTbEIig5M3S05Sak_AdegTMnJZTf9mWxxSLq-IHzF8bkX8i2E_cLl8sLoa375iMOiKAQapas3Bw8gruQDW9cjut3clCtZuLhiKFbIgEU6PZVeTm2FwFpeWs3qEBwRwZXR7__IvvnWpbijKteOe1h65Ulz4OY2n7E3PrUgzWgE6N_lOzNs0LUnetX1sc02i0P-3gGimpnljltco0XGAG5s3kK9_iBb1aVozpCGRZsSG-g-eJqXhtP9L-ui7kIx9pjJoiWQssB5-uMtQAmsDilxEJGj5sNZy--UAKDL9eJih59LJQ1Dlv4_EJACCrgRn9WNPVHlBmHONHr_LcnPqVN8YHOW_ydmuH_aWk6HLqFX6x7nSXWxIum6G-BZQbUjB_MjK3LtJxb0ZXlx5MT3IRMn3Z7npgjx5yOBXTZh9Yct0OPeBTR50nq0f_yBX6QeF74QeQg4Bs-hLw7bzP0kuNOFkZdImIslWed_tjXvTFe4IPoL-JgLC1uc0xuBFrYK-PUJZ7s4lBQeMxGNdJ3jazO5cEdadTi5h8gofFtqVTOyRoHxTFBmHMilpRbDkhAPFvwV5z4FPfjtvYTZDyjE8m9oR-YqxgMhV4PsLAmxbzpYO2Gj2FcaUF02sWOtBpy5ynNejzmyCWW4N-pwWbse-fsR10ZNg_8rP_twtMmirxEw5WugJJh1AHoGrYedBjxneekk1ZMxJkIhMmifJLGy3YyGxwFa1k5I87mVp9OQdWKxva4fs11wVYKH-nz9OfA1F8w_bO1dweJ9jZCI80sryjXrVzBCCylNxGVfkrgybtutIr0pvc2Kn1_hToOjMP2_NR4m_pkUkzm5H3f_XFcRMOuKpr3cIf3KAmw04FHRmKCOyhdg5mgmssjHtOoE0Cp7j3nlpPzIWICS9AuUbdxs'

st.write("📸 **Capture um momento especial deste dia!**")
arquivo_foto = st.camera_input("Toque para abrir a câmera")

if arquivo_foto:
    try:
        dbx = dropbox.Dropbox(ACCESS_TOKEN)
        agora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_final = f"/foto_{agora}.jpg"
        
        with st.spinner('Guardando sua foto com carinho...'):
            dbx.files_upload(arquivo_foto.getvalue(), nome_final)
            
        st.success("✅ Recebemos sua foto! Muito obrigado por fazer parte da nossa história.")
        st.balloons()
        
    except Exception as e:
        st.error("Ops! Ocorreu um probleminha. Tente novamente em instantes.")
