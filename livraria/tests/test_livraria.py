import unittest
from core.usecases.livro_usecase import LivroUseCase


class FakeRepo:

    def __init__(self):
        self.livros = []

    def listar(self):
        return self.livros

    def salvar(self, livro):
        self.livros.append(livro)


class TestLivro(unittest.TestCase):

    def test_cadastrar(self):
        repo = FakeRepo()
        usecase = LivroUseCase(repo)

        usecase.cadastrar_livro({
            "titulo": "Teste",
            "autor": "Autor",
            "categoria": "Cat",
            "preco": 10
        })

        self.assertEqual(len(usecase.listar_livros()), 1)


if __name__ == "__main__":
    unittest.main()
