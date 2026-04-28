from abc import ABC, abstractmethod


class LivroRepository(ABC):

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def salvar(self, livro):
        pass
