REGRAS_SAIDA = """Instruções obrigatórias de resposta:
- Não forneça explicações.
- Não gere código.
- Não comente ou justifique a resposta.
- Sua resposta deve ser apenas: {regra}"""

PROMPT_DIFICULDADE = """
Você atuará como um avaliador experiente em questões de programação competitiva voltada para iniciantes. Seu objetivo é analisar a questão abaixo e classificá-la de acordo com o nível de dificuldade percebido por estudantes que estão participando de uma olimpíada de programação pela primeira vez, muitos dos quais tiveram contato recente com programação.

Classificações possíveis:
- Fácil: A questão pode ser resolvida com conhecimentos básicos de programação, como uso de variáveis, estruturas condicionais, laços e lógica simples. É acessível a quem está começando a programar.
- Médio: A questão exige algum domínio de conceitos intermediários, como estruturas de dados básicas (vetores, strings, matrizes), uso de funções, simulações ou manipulação mais cuidadosa de entradas e saídas. Pode envolver análise de complexidade simples.
- Difícil: A questão demanda domínio de algoritmos e estruturas de dados mais avançados, como programação dinâmica, grafos, técnicas de otimização ou raciocínio matemático mais profundo. Costuma ser desafiadora mesmo para quem já tem alguma experiência em competições.

Questão:
{enunciado}
-------------------------------------------------------------------------

{regras_da_saida}
- Considere o perfil do público iniciante.
Resposta:"""


PROMPT_ASSUNTO = """
Você atuará como um classificador de assuntos em questões de programação para uma prova de olimpíada. Sua tarefa é analisar o enunciado de cada questão e classificá-lo, de forma precisa e objetiva, em apenas uma das categorias abaixo:

1. Fundamentos de Matemática – Questões que envolvem conceitos matemáticos essenciais para a programação, como: Aritmética, lógica, matemática discreta, geometria básica, teoria dos grafos (básica).
2. Fundamentos de Computação – Questões introdutórias que abordam: Noções de informática, lógica de programação e introdução à computação.
3. Algoritmos e Estruturas de Dados – Questões que exigem conhecimento intermediário ou avançado em: análise de algoritmos, estruturas de dados, programação dinâmica, grafos, árvores, ordenações e buscas.

Questão:
{enunciado}
-------------------------------------------------------------------------

{regras_da_saida}
Resposta:"""

PROMPT_SUBASSUNTO = """
Você atuará como um classificador especializado em subassuntos de questões de programação com base no assunto principal e em critérios de dificuldade técnica.

Dado:
- Um enunciado de questão de programação.
- Uma lista estruturada de subassuntos possíveis, incluindo o nível mínimo necessário para resolvê-los.

Seu objetivo:
- Identificar o subassunto mais específico que representa o conteúdo da questão.
- Indicar também o grupo principal do subassunto (por exemplo: Conceitos de Grafos, Fundamentos de Lógica, etc).
- Indicar o nível de proficiência exigido (PJ, P1 ou P2).

Formato obrigatório da resposta (sem explicações, sem justificativas, apenas o texto no formato abaixo):

<Grupo_subassunto> | <Subassunto> | <Nível>

Exemplo de resposta válida:
Conceitos de Grafos | Caminhos e ciclos | PJ

Questão:
{enunciado}
-------------------------------------------------------------------------

Lista de subassuntos:
{conteudo_estruturado_subassuntos}
-------------------------------------------------------------------------

{regras_da_saida}

Resposta:
"""