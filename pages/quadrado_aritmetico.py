import streamlit as st
from pathlib import Path
from streamlit.components.v1 import html

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None  # Isso remove o menu padrão
)

# CSS personalizado
st.markdown("""
<style>
/* Oculta a navegação automática */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Estiliza seus expanders */
div[data-testid="stExpander"] {
    margin-bottom: 0.5rem;
    border: none !important;
}

/* Estiliza os checkboxes */
.stCheckbox {
    margin-bottom: 0.5rem;
}

/* Checkbox personalizado */
.stCheckbox .stCheckbox:checked::before {
    background-color: #4CAF50;
}

/* Espaçamento entre itens */
div[data-testid="stExpander"] div[role="button"] {
    padding: 0.5rem 1rem;
}

/* Estilo quando expandido */
div[data-testid="stExpander"] div[aria-expanded="true"] {
    font-weight: bold;
    color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)

# 2. Estrutura de navegação
navigation = {
    "Algoritmos de Ordenação e Busca": {
        "Pastas": "pages/pastas.py",
        "Rede social": "pages/rede_social.py",
    },
    "Conceitos de Aritmética e Geometria": {
        "Idade de Camila": "pages/idade_de_camila.py",
        "Acelerador de partículas": "pages/acelerador_de_particulas.py",
        "Mesa redonda": "pages/mesa_redonda.py",
        "Supermercado": "pages/supermercado.py",
        "A idade de Dona Mônica": "pages/a_idade_da_dona_monica.py",
        "Game-10": "pages/game_10.py",
        "Janela": "pages/janela.py",
        "Tiro ao alvo": "pages/tiro_ao_alvo.py",
        "Vende-se": "pages/vende_se.py",
        "Álbum de fotos": "pages/album_de_fotos.py",
        "Colchão": "pages/colchao.py",
        "Expressões": "pages/expressoes.py",
        "Caça ao Tesouro": "pages/caca_ao_tesouro.py",
        "Desafio cartográfico": "pages/desafio_cartografico.py",
        "Altas Aventuras": "pages/altas_aventuras.py",
        "Multiplicação de Matrizes": "pages/multiplicacao_de_matrizes.py",
        "Cometa": "pages/cometa.py",
        "Cadeiras do auditório": "pages/cadeiras_do_auditorio.py",
        "Caminho das Pontes": "pages/caminho_das_pontes.py",
        "Auto Estrada": "pages/auto_estrada.py",
        "Ogros": "pages/ogros.py",
        "Chocolate": "pages/chocolate.py",
        "Cubo e quadrado": "pages/cubo_e_quadrado.py",
        "Média ou mediana": "pages/media_ou_mediana.py",
        "Atlanta": "pages/atlanta.py",
        "Estrada": "pages/estrada.py",
        "Fotografia": "pages/fotografia.py",
        "Piso da escola": "pages/piso_da_escola.py",
        "Chocolate em Barra": "pages/chocolate_em_barra.py",
        "Lençol": "pages/lencol.py",
        "Quadrado Aritmético": "pages/quadrado_aritmetico.py"
    },
    "Conceitos de Grafos": {
        "Torneio": "pages/torneio.py",
        "Bomba": "pages/bomba.py",
        "Tarzan": "pages/tarzan.py",
        "Macacos me Mordam!": "pages/macacos_me_mordam.py",
        "O Chefe": "pages/o_chefe.py",
        "O Tabuleiro Esburacado": "pages/o_tabuleiro_esburacado.py"
    },
    "Conceitos de Matemática Discreta": {
        "Cálculo rápido": "pages/calculo_rapido.py",
        "Irmãos": "pages/irmaos.py",
        "Frequência": "pages/frequencia.py",
        "Soma de casas": "pages/soma_de_casas.py",
        "Vira!": "pages/vira.py",
        "Banda": "pages/banda.py",
        "Competição de chocolate": "pages/competicao_de_chocolate.py",
        "Frete da Família Silva": "pages/frete_da_familia_silva.py",
        "Pizza": "pages/pizza.py",
        "Passatempo": "pages/passatempo.py",
        "Matriz Escada": "pages/matriz_escada.py",
        "Caixinha de Palitos": "pages/caixinha_de_palitos.py",
        "Quadrado Mágico": "pages/quadrado_magico.py"
    },
    "Estruturas de Dados":{
        "Zero para cancelar": "pages/zero_para_cancelar.py",
        "Figurinhas da copa": "pages/figurinhas_da_copa.py",
        "Botas Trocadas": "pages/botas_trocadas.py",
        "Frequência na aula": "pages/frequencia_na_aula.py",
        "Tempo de resposta": "pages/tempo_de_resposta.py",
        "Pandemia": "pages/pandemia.py",
        "Bolas": "pages/bolas.py",
        "Cortando o Papel": "pages/cortando_o_papel.py",
        "Notas": "pages/notas.py",
        "Jogo de Cartas": "pages/jogo_de_cartas.py",
        "Falha de segurança": "pages/falha_de_seguranca.py",
        "Poligrama": "pages/poligrama.py",
        "Candidatas": "pages/candidatas.py",
        "Soma": "pages/soma.py",
        "Baldes": "pages/baldes.py",
        "Arranha-céu": "pages/arranha_ceu.py",
        "Código": "pages/codigo.py",
        "Famílias de Troia": "pages/familias_de_troia.py",
        "Colheita de Caju": "pages/colheita_de_caju.py"
    },
    "Estratégias de Algoritmos":{
        "Cobra Coral": "pages/cobra_coral.py",
        "Truco": "pages/truco.py",
        "Casamento de inteiros": "pages/casamento_de_inteiros.py",
        "Sanduíche": "pages/sanduiche.py",
        "Senha da Vó Zinha": "pages/senha_da_vozinha.py",
        "Cifra da Nlogônia": "pages/cifra_da_nlogonia.py",
        "Três por Dois": "pages/tres_por_dois.py",
        "Calçada Imperial": "pages/calcada_imperial.py",
        "Chuva": "pages/chuva.py",
        "Cinco": "pages/cinco.py",
        "Falta uma": "pages/falta_uma.py",
        "Festa olímpica": "pages/festa_olimpica.py",
        "Jogo do Preto e Branco": "pages/jogo_do_preto_e_branco.py",
        "Ralouim": "pages/ralouim.py",
        "Etiquetas": "pages/etiquetas.py",
        "Elevador": "pages/elevador.py",
        "Fuga": "pages/fuga.py",
        "Câmara de Compensação": "pages/camara_de_compensacao.py",
        "Tapetes": "pages/tapetes.py",
        "Escada perfeita": "pages/escada_perfeita.py"
    },
    "Informática Básica": {
        "Fechadura": "pages/fechadura.py",
        "Catálogo de Músicas": "pages/catalogo_de_musicas.py",
        "Escalonamento ótimo": "pages/escalonamento_otimo.py",
        "Reduzindo detalhes em um mapa": "pages/reduzindo_detalhes_em_um_mapa.py",
        "Telescópio": "pages/telescopio.py",
        "Notas da Prova": "pages/notas_da_prova.py",
        "Chuva": "pages/chuva1.py",
        "Lanche na empresa": "pages/lanche_na_empresa.py",
        "OBI": "pages/obi.py",
        "Telefone": "pages/telefone.py",
        "Telemarketing": "pages/telemarketing.py",
        "Repositórios": "pages/repositorios.py"
    },
    "Programação":{
        "Camisetas da Olimpíada": "pages/camisetas_da_olimpiada.py",
        "Postes": "pages/postes.py",
        "Cálculo": "pages/calculo.py",
        "Língua do P": "pages/lingua_do_p.py",
        "Banco": "pages/banco.py",
        "Batalha Naval": "pages/batalha_naval.py",
        "Avião": "pages/aviao.py",
        "Dario e Xerxes": "pages/dario_e_xerxes.py",
        "Simulador": "pages/simulador.py"
    },
    "Algoritmos de Geometria":{
        "Retângulo": "pages/retangulo.py",
        "Exploração do Capitão Levi": "pages/exploracao_do_capitao_levi.py",
    },
    "Algoritmos de Matemática":{
        "Blefe": "pages/blefe.py",
    },
    "Algoritmos de Programação Dinâmica":{
        "Dona Formiga": "pages/dona_formiga.py",
        "Taxa": "pages/taxa.py",
        "Ciclovias": "pages/ciclovias.py",
        "O Banco Inteligente": "pages/o_banco_inteligente.py",
        "Sacoleiro": "pages/sacoleiro.py",
        "Subsequências": "pages/subsequencias.py",
        "Museu": "pages/museu.py"
    },
    "Algoritmos em Árvores":{
        "Dona Minhoca": "pages/dona_minhoca.py",
        "Promoção de Primeira": "pages/promocao_de_primeira.py",
        "Metrô da Nlogônia": "pages/metro_da_nlogonia.py"
    },
    "Algoritmos em Grafos":{
        "Fissura Perigosa": "pages/fissura_perigosa.py",
        "Mapa": "pages/mapa.py",
        "Quebra-cabeça": "pages/quebra_cabeca.py",
        "Labirinto": "pages/labirinto.py",
        "Trem da mina": "pages/trem_da_mina.py",
        "Grand Prix da Nlogônia": "pages/grand_prix_da_nlogonia.py",
        "Detetive": "pages/detetive.py",
        "Mancha": "pages/mancha.py",
        "Frete": "pages/frete.py",
        "Mina": "pages/mina.py",
        "Lobo Mau": "pages/lobo_mau.py"
    },

}

# 3. Sidebar com expanders e checkboxes
with st.sidebar:

    st.title("Navegação")
    
    # Container principal
    nav_container = st.container()
    
    with nav_container:
        # Variável para controlar a página atual
        if 'current_page' not in st.session_state:
            st.session_state.current_page = None

        # Inicializa o estado se não existir
        if 'expander_expandido' not in st.session_state:
            st.session_state.expander_expandido = False

        for category, pages in navigation.items():
            with st.expander(category, expanded=False):
                for page_name, page_path in pages.items():
                    # Cria um checkbox para cada página
                    checked = st.session_state.current_page == page_path
                    if st.checkbox(
                        page_name,
                        value=checked,
                        key=f"nav_checkbox_{page_path}",
                        disabled=checked  # Desabilita o checkbox da página atual
                    ):
                        if Path(page_path).exists():
                            if not st.session_state.current_page == page_path:
                                st.session_state.current_page = page_path
                                st.switch_page(page_path)
                        else:
                            st.error(f"Página não encontrada: {page_path}")

col1, col2 = st.columns([20, 0.5])

with col1:
    st.title("OBI-UAN")
    col12, col22, col32 = st.columns([1, 1, 1])

    with col22:
        st.header("Quadrado Aritmético")

    st.text("Arnaldo e Bernardo são dois garotos que compartilham um peculiar gosto por curiosidades matemáticas. Nos últimos tempos, sua principal diversão tem sido investigar propriedades matemágicas de tabuleiros quadrados preenchidos com inteiros. Um belo dia, Arnaldo desenhou o tabuleiro da seguinte figura.")

    col14, col24, col34 = st.columns([1.3, 1, 1])

    with col24:
        st.image("./images/quadrado1.png",width=200)

    st.text("— Olha só, várias somas nesse quadrado são iguais! — exclamou Bernardo.")
    st.text("— Como assim? — devolveu, intrigado, Arnaldo.")
    st.text("— Observe:")

    col15, col25, col35 = st.columns([1, 2, 1])

    with col25:
        st.image("./images/quadrado2.png",width=600)

    st.text("— É mesmo! (-41) + 40 + 54 dá 53, 28 + (-29) + 54 também! — exclamou Arnaldo.")
    st.text("— Eu já verifiquei: existem 6 formas de escolhermos 3 células deste quadrado de forma que cada linha e coluna tenha exatamente uma célula escolhida. Em todas elas, a soma dá 53. Além disso, todos os números são distintos nesse quadrado. — notou Bernardo, exibindo suas habilidades aritméticas.")
    st.text("— Que bacana! Esse quadrado é realmente mágico! Ou, melhor, esse quadrado é realmente aritmético! Será que existem mais quadrados como esse?")
    st.text("Uma escolha legal de células é uma escolha em que toda linha e toda coluna tenha exatamente uma célula escolhida. Um quadrado aritmético de tamanho N e soma S é um tabuleiro de inteiros de N linhas e N colunas em que qualquer escolha legal tem soma S e em que todos os números são distintos.")
    st.text("Sua tarefa, neste problema, é gerar um quadrado aritmético de tamanho N e soma S, dados N e S. Como Arnaldo e Bernardo vão querer conferir a sua solução em suas calculadoras, você não deve gerar um quadrado em que alguma célula tenha valor absoluto maior do que 10⁹.")

    st.subheader("Entrada")
    st.text("A primeira e única linha da entrada contém dois números inteiros N e S (1 ≤ N ≤ 1000 e -1000 ≤ S ≤ 1000) representando, respectivamente, o tamanho e a soma do quadrado aritmético pedido.")

    st.subheader("Saída")
    st.text("Seu programa deve imprimir N linhas, cada uma com N inteiros entre -10⁹ e 10⁹, representando o quadrado aritmético pedido. Para uma mesma entrada, podem existir vários quadrados aritméticos válidos; seu programa deve imprimir qualquer um deles, mas apenas um.")
    st.text("É garantido que existirá pelo menos um quadrado aritmético válido para cada entrada testada.")

    st.subheader("Restrições")
    st.markdown("&emsp; • 1 ≤ N ≤ 1000")
    st.markdown("&emsp; • -1000 ≤ S ≤ 1000")
    st.markdown("&emsp; • -10⁹ ≤ valor de cada célula ≤ 10⁹")

    st.subheader("Informações sobre a pontuação")
    st.markdown("&emsp; • Em um conjunto de casos de teste que totaliza 30 pontos, N ≤ 3;")
    st.markdown("&emsp; • Em um conjunto de casos de teste que totaliza 70 pontos, N ≤ 100;")

    st.subheader("Sua resposta")
    resposta = st.text_area("", 
                            placeholder="Escreva aqui...",
                            height=150)
    col13, col23, col33 = st.columns([4, 0.42, 0.3])
    # CSS com classes diferentes
    
    with col23:
        dicas = st.button("Pedir dicas", key="dicas")
    with col33:
        enviado = st.button("Enviar", key="enviar")

with col2:
    if st.button("", icon="🏠", key="image_main"):
        st.switch_page("./main_page.py")

