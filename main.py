from config import get_claude_model
from prompts import get_prompt_template
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Obtenha o modelo e o template
model = get_claude_model()
prompt_template = get_prompt_template()

def analyze_identity(history):
    """
    Função para processar a análise de identidade com base na história.

    Args:
        history (str): Texto da narrativa fornecida pelo usuário.

    Returns:
        str: Resposta gerada pelo modelo.
    """
    # Formata o prompt
    formatted_prompt = prompt_template.format(history=history)

    # Envia o prompt formatado ao modelo e obtém a resposta
    response = model(formatted_prompt)  # Chama o modelo diretamente
    return response

if __name__ == "__main__":
    # Exemplo de entrada com a história do aluno
    aluno_history = """
Minha jornada começou na área da saúde, movida por um desejo genuíno de cuidar das pessoas. Desde jovem, eu via minha avó contar histórias sobre a dificuldade de acesso a médicos e tratamentos na pequena cidade onde vivíamos. Aquilo me marcou profundamente e acendeu em mim a vontade de ser a pessoa que faria a diferença para quem mais precisava.

Estudei muito, enfrentei desafios que pareciam intransponíveis e, com muito esforço, consegui meu diploma em Enfermagem. Anos depois, me especializei em saúde pública. Passei mais de uma década mergulhada nessa profissão que tanto amava. Trabalhei em hospitais cheios, com plantões intermináveis, participei de campanhas de vacinação e visitei comunidades vulneráveis, onde muitas vezes era a única profissional de saúde disponível. Meu trabalho me preenchia, mas, com o tempo, algo começou a mudar.

No fundo, eu sentia que, apesar do impacto que gerava no dia a dia, minhas ações não alcançavam tantas pessoas quanto eu desejava. As limitações do sistema, a falta de recursos e o cansaço acumulado começaram a pesar. Eu queria expandir minha voz, alcançar mais pessoas, levar a conscientização para além das paredes de uma clínica ou hospital.

Foi então que comecei a explorar o marketing digital. No início, parecia algo distante da minha realidade, quase impensável para alguém como eu, que havia passado tanto tempo em uma área tão diferente. Mas, ao aprofundar meus estudos, percebi que havia um potencial enorme ali. Eu poderia compartilhar conhecimento em saúde, alcançar milhares — talvez milhões — de pessoas com mensagens simples, educativas e transformadoras. Poderia prevenir problemas antes que se tornassem crises.

A transição não foi fácil. Deixei para trás a segurança de um emprego fixo e enfrentei os olhares de julgamento de colegas que não entendiam por que eu estava "abandonando" a saúde. Mas eu sabia que não estava desistindo. Estava transformando a maneira como impactava o mundo.

No marketing digital, comecei a criar conteúdos sobre prevenção de doenças, saúde mental e qualidade de vida. Minhas redes sociais cresceram, e logo eu estava ajudando pessoas a tomarem decisões mais informadas sobre sua saúde. Empresas de saúde começaram a me procurar, e percebi que poderia usar meu conhecimento técnico para ajudar marcas a comunicar melhor seus serviços e alcançar quem realmente precisava.

Hoje, olho para minha trajetória com orgulho. Não foi uma mudança fácil, mas foi uma das decisões mais importantes da minha vida. Ainda estou cuidando das pessoas, mas agora de uma forma diferente. Estou conectando, informando e inspirando. E isso, para mim, é tão significativo quanto estar ao lado de um paciente.

Minha missão nunca mudou — apenas encontrou um novo caminho. 
    """
    
    # Processa a análise de identidade com a história fornecida
    try:
        resultado = analyze_identity(aluno_history)
        print("Resultado do Modelo:\n", resultado)

        # Salvar em TXT
        output_txt_file = "mapa_identidade.txt"
        if hasattr(resultado, "content"):  # Verifica se o objeto possui um atributo 'content'
            resultado_texto = resultado.content
        else:
            resultado_texto = str(resultado)

        with open(output_txt_file, "w", encoding="utf-8") as f:
            f.write(resultado_texto)
        print(f"Resultado salvo como TXT: {output_txt_file}")

    except Exception as e:
        print("Erro durante a execução:", str(e))

