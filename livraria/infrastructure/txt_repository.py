import os

class TxtLivroRepository:

    def __init__(self):
        self.arquivo = "banco.txt"

        if not os.path.exists(self.arquivo):
            open(self.arquivo, "w").close()

    def listar(self):
        livros = []

        with open(self.arquivo, "r", encoding="utf-8") as f:
            for linha in f.readlines():
                dados = linha.strip().split(";")

                if len(dados) == 4:
                    livros.append({
                        "titulo": dados[0],
                        "autor": dados[1],
                        "categoria": dados[2],
                        "preco": float(dados[3])
                    })

        return livros

    def salvar(self, livro):
        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write(
                f"{livro['titulo']};"
                f"{livro['autor']};"
                f"{livro['categoria']};"
                f"{livro['preco']}\n"
            )
