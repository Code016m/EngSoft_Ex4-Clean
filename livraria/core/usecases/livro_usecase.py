class LivroUseCase:

    def __init__(self, repository):
        self.repository = repository

    def listar_livros(self):
        return self.repository.listar()

    def cadastrar_livro(self, livro):
        self.repository.salvar(livro)

    # NEW FEATURE
    def buscar_por_autor(self, autor):
        livros = self.repository.listar()

        return [
            livro for livro in livros
            if livro["autor"].lower() == autor.lower()
        ]
