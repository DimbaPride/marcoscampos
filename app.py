import streamlit as st
from config import get_claude_model
from prompts import get_prompt_template

# Função para processar a análise de identidade
def analyze_identity(history):
    """
    Processa a análise de identidade com base na história.

    Args:
        history (str): Texto da narrativa fornecida pelo usuário.

    Returns:
        str: Resposta gerada pelo modelo.
    """
    # Obtenha o modelo e o prompt
    model = get_claude_model()
    prompt_template = get_prompt_template()

    # Formata o prompt
    formatted_prompt = prompt_template.format(history=history)

    # Envia o prompt formatado ao modelo e obtém a resposta
    response = model.invoke(formatted_prompt)

    # Extrai o conteúdo do modelo
    if hasattr(response, "content"):
        return response.content
    return str(response)

# Interface do Streamlit
def main():
    st.title("Agente de Identidade")
    st.write("Forneça uma narrativa abaixo para gerar um mapa de identidade")

    # Caixa de texto para o cliente inserir a narrativa
    user_input = st.text_area("Insira a história aqui:", height=200)

    # Botão para processar a narrativa
    if st.button("Gerar Mapa de Identidade"):
        if user_input.strip() == "":
            st.warning("Por favor, insira uma história antes de gerar o mapa.")
        else:
            with st.spinner("Gerando mapa de identidade..."):
                try:
                    # Chama a função analyze_identity
                    resultado = analyze_identity(user_input)

                    # Exibe o resultado
                    st.success("Mapa de Identidade Gerado!")
                    st.text_area("Resultado:", value=resultado, height=400)

                    # Botão para baixar o resultado como TXT
                    st.download_button(
                        label="Baixar Mapa como TXT",
                        data=resultado,
                        file_name="mapa_identidade.txt",
                        mime="text/plain",
                    )

                except Exception as e:
                    st.error(f"Ocorreu um erro: {e}")

# Inicia o aplicativo Streamlit
if __name__ == "__main__":
    main()
