from pathlib import Path

class DadosCompartilhados:
    def __init__(self):
        self.resposta = None
        self.nome_questao =  None
        self.rota_questao = None
        self.resposta_certa = None
        self.dica = None
    
    def rota_resposta(self,rota):
        diretorio_do_script = Path(__file__).resolve().parent
        return diretorio_do_script.parent.parent / 'site' / 'solucoes' /  f'{rota}'
    
    def rota_dica(self,rota):
        diretorio_do_script = Path(__file__).resolve().parent
        return diretorio_do_script.parent.parent / 'site' / 'dicas' /  f'{rota}'

# Instância global que será usada por outros arquivos
dados = DadosCompartilhados()

dados.resposta_certa= {
    "rede_social": dados.rota_resposta('rede_reference_py3.py'),
    "supermercado": dados.rota_resposta('super_py3.py'),
    "irmaos": dados.rota_resposta('ranido_py3.py'),
    "codigo": dados.rota_resposta('codigo.cpp')
}

dados.dica= {
    "rede_social": dados.rota_dica('rede_social.txt'),
    "supermercado": dados.rota_dica('rede_social.txt'),
    "irmaos": dados.rota_dica('irmaos.txt'),
    "codigo": dados.rota_dica('codigo.txt')
}
