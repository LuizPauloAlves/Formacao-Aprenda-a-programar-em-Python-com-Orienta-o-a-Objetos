# 1
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

# 2
    def __str__(self):
        return f'Nome do Livro: {self._titulo.ljust(30)} | Nome do Autor: {self._autor.ljust(30)} | Ano de Publicacao: {str(self._ano_publicacao).ljust(10)} | Diponibilidade: {self.disponivel}'

# 3
    def emprestar_livro(self):
        if self._disponivel:
            self._disponivel = not self._disponivel
        else:
            return 'Livro indisponivel'
    
    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Indisponível'

# 4
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis


# 2 - continuacao

livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
print(livro1)
print(livro2)

# 3 - continuacao

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(livro3)
print(f'Emprestando Livro --- {livro3._titulo}')
livro3.emprestar_livro()
print(livro3)

# 4 - continuacao

livros = [livro1, livro2, livro3]
livros_disponiveis_2020 = Livro.verificar_disponibilidade(2020)
print(f'Livros disponíveis em 2020:')
for livro in livros_disponiveis_2020:
    print(livro)
