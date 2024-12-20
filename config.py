import os
from langchain_anthropic import ChatAnthropic

def get_claude_model():
    """
    Configura e retorna o modelo Claude via LangChain usando variáveis de ambiente.
    """
    # Obtém a chave da API de uma variável de ambiente
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("A chave da API do Anthropic não está configurada. Defina a variável ANTHROPIC_API_KEY.")
    
    return ChatAnthropic(
        anthropic_api_key=api_key,
        model="claude-3-5-haiku-20241022",  # Modelo Claude configurado
        max_tokens=5000
    )
