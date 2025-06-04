class Prompt:
	def __init__(self, enunciado:str) -> None:
		"""Classe que contém o enunciado da questão.

		Args:
			enunciado (str): Enunciado da questão.

		Returns:
			None
		"""		
		self.enunciado = enunciado

	def texto(self) -> str:

		prompt = f""""""