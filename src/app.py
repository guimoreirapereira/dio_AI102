import streamlit as st
from services.blob_service import upload_blob

def configure_interface():
    st.title("Desafio DIO")
    upload_file = st.file_uploader("arquivo", type=["png", "jpg", "jpeg"])

    if upload_file is not None:
        filename = upload_file.name

        #envar par ao blob storage
        blob_url = upload_blob(upload_file, filename)

        if blob_url:
            st.write(f"Arquivo {filename} enviado com sucesso para blob storage")
            credit_card_info = ""
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar Arquivo {filename} enviado com sucesso para blob storage")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="imagem enviada", use_column_width=True)
    st.write("Resultado da Validação")
    if credit_card_info and credit_card_info['card_name']:
        st.markdown(f"<h1 style='color: green;'>Cartão valido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Banco emissor: {credit_card_info['bank_nam']}")
        st.write(f"Data de validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão invalido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de credito válido")


if __name__ == "__main__":
    configure_interface()


    