REGRAS_SAIDA = """Instruções obrigatórias de resposta:
- Não forneça explicações.
- Não gere código.
- Não comente ou justifique a resposta.
- Sua resposta deve ser apenas a string: {regra}"""

PROMPT_DIFICULDADE = """
Você atuará como um avaliador experiente em questões de programação competitiva. Seu objetivo é classificar a seguinte questão com base em seu nível de dificuldade.

Classificações possíveis:
- Fácil: Pode ser resolvida com conhecimentos básicos de programação e algoritmos simples.
- Médio: Requer conhecimentos intermediários, incluindo estruturas de dados comuns e análise de complexidade.
- Difícil: Envolve algoritmos avançados, estruturas de dados complexas ou técnicas sofisticadas como programação dinâmica, grafos avançados ou otimização.

Questão:
{enunciado}

{regras_da_saida}
Resposta:"""


PROMPT_ASSUNTO = """
Você atuará como um classificador de assuntos em questões de programação. Seu papel é ler a questão fornecida e categorizá-la de forma objetiva em uma das classes a seguir:

1. Fundamentos de Matemática – Aritmética, lógica, matemática discreta, geometria básica, teoria dos grafos (básica).
2. Fundamentos de Computação – Noções de informática, lógica de programação e introdução à computação.
3. Algoritmos e Estruturas de Dados – Questões que envolvem análise de algoritmos, estruturas de dados, programação dinâmica, grafos, árvores, ordenações e buscas.

Questão:
{enunciado}

{regras_da_saida}
Resposta:"""

PROMPT_SUBASSUNTO = """
Você atuará como um classificador especializado em subassuntos de questões de programação com base no assunto principal e em critérios de dificuldade técnica.

Dado:
- Um enunciado de questão de programação.
- Um assunto principal ao qual ela pertence (ex: Fundamentos de Matemática).
- Uma lista estruturada de subassuntos possíveis, incluindo o nível mínimo necessário para resolvê-los.

Seu objetivo:
- Identificar o subassunto mais específico que representa o conteúdo da questão.
- Indicar o nível de proficiência exigido (PJ, P1 ou P2).
- Indicar também o grupo principal do subassunto (por exemplo: Conceitos de Grafos, Fundamentos de Lógica, etc).

Formato obrigatório da resposta (sem explicações, sem justificativas, apenas o texto no formato abaixo):

<Grupo>, <Subassunto>, <Nível>

Exemplo de resposta válida:
Conceitos de Grafos, Caminhos e ciclos, PJ

Questão:
{enunciado}

Assunto principal:
{assunto_principal}

Lista de subassuntos:
{conteudo_estruturado_subassuntos}

{regras_da_saida}

Resposta:
"""