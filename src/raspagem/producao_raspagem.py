"""Classe responsável por realizar a raspagem de dados da produção."""

from src.raspagem.vitivinicultura_raspagem import VitiviniculturaRaspagem


class ProducaoRaspagem(VitiviniculturaRaspagem):
    """
    Classe responsável por realizar a raspagem de dados
    da produção de vinhos, sucos e derivados do Rio Grande do Sul.
    """

    def __init__(self, ano: int, subopcao: str | None):
        super().__init__()
        self.ano = ano
        self.construir_url()

    def construir_url(self):
        self.url = self.url + f"?opcao=opt_02&ano={self.ano}"
