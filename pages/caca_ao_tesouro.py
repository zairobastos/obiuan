import streamlit as st
from pathlib import Path
import sys
sys.path.append('./pages')  # Caminho absoluto
from variavel import dados

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
    col12, col22, col32 = st.columns([1.5, 1, 1])

    with col22:
        st.header("Caça ao Tesouro")

    st.text("Capitão Tornado é um pirata muito cruel que faz qualquer coisa por dinheiro. Há alguns dias, o capitão soube da existência de um tesouro numa ilha deserta, e agora tenta determinar sua posição.")
    st.text("A ilha pode ser vista como um quadriculado N × N de terra cuja posição (0, 0) está a sudoeste, a posição (N - 1, 0) está a sudeste, a posição (0, N - 1) está a noroeste e a posição (N - 1, N - 1) está a nordeste. Em alguma posição desse quadriculado está o tesouro.")
    st.text("Uma curiosidade importante é a perna de pau que o capitão possui. Ela impede que o capitão se locomova em direções que não a horizontal ou a vertical: para ir da posição (1, 1) para a posição (3, 2), por exemplo, o capitão é obrigado a gastar três passos. É claro que o capitão sempre escolhe, dentro de suas limitações, um caminho com o menor número de passos possível. Chamamos esse modo de andar de passos de capitão. Um exemplo de caminho por passos de capitão entre (1, 1) e (3, 2) é ilustrado na figura a seguir.")

    st.image("./images/tesouro1.png",width=300)

    st.text("Como em toda boa caça ao tesouro, o capitão não conhece a posição onde o tesouro se encontra: ele possui um mapa que corresponde à geografia da ilha. Em algumas posições desse mapa, existem pistas escritas. Cada pista consiste em um número D, que indica a menor distância em passos de capitão entre a posição em que a pista se encontra e a do tesouro.")

    st.image("./images/tesouro2.png",width=500)

    st.text("Observe que, dependendo da disposição das pistas, a posição do tesouro pode estar determinada de maneira única ou não. Na figura acima e à esquerda, as duas pistas são suficientes para se saber, com certeza, onde está o tesouro; na figura à direita, as quatro pistas dadas ainda possibilitam que tanto a posição (0, 2) quanto a (2, 2) guardem o tesouro. Nesse último caso, não se pode determinar, com certeza, qual é a localização do tesouro.")
    st.text("Dadas as pistas que o capitão possui, sua tarefa é determinar se as pistas fornecem a localização exata do tesouro e, caso positivo, qual ela é.")

    st.subheader("Entrada")
    st.text("A primeira linha contém dois inteiros positivos N e K, onde N é a dimensão do quadriculado e K é o número de pistas no mapa que o capitão possui.")
    st.text("Cada uma das próximas K linhas contêm três inteiros X, Y e D, informando que existe uma pista na posição (X, Y) contendo o número D. Essa pista indica que o tesouro encontra-se a D passos de capitão da posição da pista.")
    st.text("É garantido que, com essas pistas, existe ao menos uma localização possível para o tesouro. Além disso, o mapa não contém duas pistas na mesma posição.")

    st.subheader("Saída")
    st.text("Se as pistas forem suficientes para determinar com certeza a localização do tesouro, seu programa deve imprimir uma única linha com dois inteiros, X e Y , indicando que o tesouro encontra-se na posição (X, Y).")
    st.text("Caso contrário, seu programa deve imprimir uma única linha com dois inteiros iguais a -1, como nos exemplos de saída a seguir.")

    st.subheader("Restrições")
    st.markdown("&emsp; • 2 ≤ N ≤ 100")
    st.markdown("&emsp; • 1 ≤ K ≤ 100")

    st.subheader("Sua resposta")
    st.markdown("A resposta da questão na aplicação é em ***cpp***.")
    resposta = st.text_area("", 
                            placeholder="Escreva aqui...",
                            height=150)
    col13, col23, col33 = st.columns([4, 0.42, 0.3])
    # CSS com classes diferentes
    
    with col23:
        if st.button("Pedir dicas", key="dicas"):
            dados.resposta = resposta
            dados.nome_questao = "Caça ao Tesouro"
            dados.rota_questao = "caca_ao_tesouro"
            st.switch_page('pages/dicas.py')
    with col33:
        if st.button("Enviar", key="enviar"):
            dados.resposta = resposta
            dados.nome_questao = "Caça ao Tesouro"
            dados.rota_questao = "caca_ao_tesouro"
            st.switch_page('pages/resposta.py')

with col2:
    if st.button("", icon="🏠", key="image_main"):
        st.switch_page("./main_page.py")

