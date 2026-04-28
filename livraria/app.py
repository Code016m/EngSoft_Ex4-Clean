from livraria.infrastructure.txt_repository import TxtLivroRepository
from livraria.core.usecases.livro_usecase import LivroUseCase
from livraria.presentation.livro_view import LivroView

repo = TxtLivroRepository()
usecase = LivroUseCase(repo)
view = LivroView(usecase)

view.iniciar()
