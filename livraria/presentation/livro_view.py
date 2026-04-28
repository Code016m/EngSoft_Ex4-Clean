import tkinter as tk
from tkinter import messagebox


class LivroView:

    def __init__(self, usecase):
        self.usecase = usecase

        self.root = tk.Tk()
        self.root.title("Livraria - Clean Architecture")
        self.root.geometry("800x600")

        tk.Label(self.root, text="Título").pack()
        self.entry_titulo = tk.Entry(self.root)
        self.entry_titulo.pack()

        tk.Label(self.root, text="Autor").pack()
        self.entry_autor = tk.Entry(self.root)
        self.entry_autor.pack()

        tk.Label(self.root, text="Categoria").pack()
        self.entry_categoria = tk.Entry(self.root)
        self.entry_categoria.pack()

        tk.Label(self.root, text="Preço").pack()
        self.entry_preco = tk.Entry(self.root)
        self.entry_preco.pack()

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar).pack(pady=5)
        tk.Button(self.root, text="Listar", command=self.listar).pack(pady=5)

        tk.Label(self.root, text="Buscar por Autor").pack()
        self.entry_busca = tk.Entry(self.root)
        self.entry_busca.pack()

        tk.Button(self.root, text="Buscar", command=self.buscar).pack(pady=5)

        tk.Button(self.root, text="Sair", command=self.root.destroy).pack(pady=5)

        self.lista = tk.Listbox(self.root, width=80, height=15)
        self.lista.pack(pady=10)

    def cadastrar(self):
        try:
            livro = {
                "titulo": self.entry_titulo.get(),
                "autor": self.entry_autor.get(),
                "categoria": self.entry_categoria.get(),
                "preco": float(self.entry_preco.get().replace(",", "."))
            }

            self.usecase.cadastrar_livro(livro)
            messagebox.showinfo("Sucesso", "Livro cadastrado!")

            self.limpar_campos()

        except:
            messagebox.showerror("Erro", "Dados inválidos")

    def listar(self):
        livros = self.usecase.listar_livros()

        self.lista.delete(0, tk.END)

        for livro in livros:
            self.lista.insert(
                tk.END,
                f"{livro['titulo']} | {livro['autor']} | R$ {livro['preco']}"
            )

    def buscar(self):
        autor = self.entry_busca.get()
        livros = self.usecase.buscar_por_autor(autor)

        self.lista.delete(0, tk.END)

        for livro in livros:
            self.lista.insert(
                tk.END,
                f"{livro['titulo']} | {livro['autor']}"
            )

    def limpar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def iniciar(self):
        self.root.mainloop()
