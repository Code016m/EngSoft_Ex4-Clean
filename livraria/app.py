from infrastructure.txt_repository import TxtLivroRepository
from core.usecases.livro_usecase import LivroUseCase
from presentation.livro_view import LivroView


def executar_app():
    repo = TxtLivroRepository()
    usecase = LivroUseCase(repo)
    view = LivroView(usecase)
    view.iniciar()


if __name__ == "__main__":
    executar_app()
