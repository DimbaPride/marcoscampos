# tests/test_agent.py

from main import analyze_identity

def test_identity_analysis():
    """
    Teste simples para verificar a saída do agente com uma história de exemplo.
    """
    history = "Em 2015, eu comecei uma nova jornada buscando inspiração."
    result = analyze_identity(history)
    assert "Mapa de Identidade" in result
