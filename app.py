import streamlit as st
import dropbox
from datetime import datetime

# 1. Configuração Visual
st.set_page_config(page_title="Casamento Adriana & Gilmar", page_icon="💍")

# Ajuste do estilo (Corrigido para unsafe_allow_html)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #f0e4d7; color: #5d4037; }
    .main { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Nosso Álbum Digital")
st.write("### Adriana & Gilmar")
st.write("28 de Junho de 2026")
st.write("---")

# 2. SEU TOKEN DO DROPBOX
DROPBOX_TOKEN = 'sl.u.AGXodsnoHSOOX1XpMFcmPTzdBF60L8HfHWQW7munRTfW6aMT9rzQd-ywO6eRDmTeR36SljwsQoEd1rY6KpsO2l1RcwlYt1wy-BDjlX3p2MlYZaANXOqvExnIW-2sTL9Ss9SwcnV1wqwK9V4z9OavDfXANFMMPpu9gOD6uxdvWgBUjyvpamoY-3mgo4GYc3-ZCsQX-6qa6TxrqL9Gfy5F6Jdjh4X9WIRuJXxt9H6xzXOz9o2bIE_6Ncg4a_1bJLccSjvPr7YJhFHOh2ZUpp1o5RMla3PHPwathfljToEthc9Ri1GuX6vRuY63_C-5Cz5pR4Ixg-T5TxubOLC6Yp5Xg5ROB6h3zp9q_B3kkmcCmKyEGSKA9MSoEHgLPk4Yc1ndGjRg-e7RYkPu_Gs1blZUT7RGhO_quXJEF4y-kJZKeq3FF96bCYLLeO1CQTAmbAtEyQmM4b5_q1g46Z9875ZI6ELkz_qsAXUe7r3upahfC7ItWQm1ObApHczBhH07HqAJLsq06Qkav2pJeemT-NtHu940ycS5jI3AntmorMySKMKNFrZ6IljkQYV27GzGzj4d4LMQyPKFSEdVIqVC35tlUkLdh2BIkgfqZkgGv6hIDfqzBjWAkVo1wVoCkXpwTDcX9_rev_WhzTuYd-Tv1zbeE1PFUjH6VQT8FtDZFzRFgLaWKR9cXD3iYR1Qk7i4fe8KvefEAS-01VdPfY62W8aUzS2JU-dFg2z_2rPyif9-3ZWf5yOBjXDHYL6uLqnau8oKXhMDDIJIOYtn5Y-6Tvk08-hUg2XT8SK9z7Bjga5i-N_iqeuSSySrQVXUXz3dcGH_5EP-BQeCMHlIZSTsvOVryTTGvZbJMkc2c23zqZNa9ljrO1YKUcOywkgrcXnvmfjz8bIYqkojyXxXskzeXh-bXBuXn4PQrw7Cp6r1XSBq14E8Lhfa4gcSKZG1FUDdd12aFE01jzgZZgznPhKXJ47ej7ZZIqKDCI4iuwh5sbFdExYWuAqP7ndoQM9rm9jsgwduKdd3q3NCtgX5UFKqD4GzCrtk6ztohHA1QywFLwVjEgLsyqnyrcpTV9Y0UD5XpbOt-31zDj9uKcrSASvb2ognTCWLKq8faRJzkQuoq1h6gNPaJxpZ4PCzE0UkJCNfQ_NDfAlaMcQdlsDHt82aq6Tu87Tn3YFJI3_tDv0k7TIB2-ExvT1SVkZAvZdiD91Ws6BNWdxwsVQVaLOyzvqXTsWQ2Zl-CQt_eZ1ol1iFeNdB9JU5RnHpOc02EH90t1YBT_avY9Fk9u9k05-5bpZwlLACCRtY_BqTQKxldjjMfek-L-tnMiSyDwQYTb3i4BnBgpM6NUuQxJZFoQ20os9TKeuk75M37M-Cej_cA_SSM6j3JKvbLFZjAimaoQ0kpDv9_EB-1q4'

# 3. Captura da Foto
arquivo_foto = st.camera_input("Toque aqui para abrir a câmera")

if arquivo_foto:
    try:
        dbx = dropbox.Dropbox(DROPBOX_TOKEN)
        timestamp = datetime.now().strftime("%H%M%S")
        nome_final = f"/foto_{timestamp}.jpg"
        
        with st.spinner('Enviando foto...'):
            dbx.files_upload(arquivo_foto.getvalue(), nome_final)
            
        st.success("✅ Foto enviada! Obrigado por celebrar conosco! ✨")
        st.balloons() 
        
    except Exception as e:
        st.error("Erro ao enviar. Verifique o Token ou a internet.")