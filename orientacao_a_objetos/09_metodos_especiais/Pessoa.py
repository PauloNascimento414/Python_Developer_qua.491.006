class Pessoa:
    # construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # método retorna string
    def __str__(self):
        return f"Olá, meu nome é {self.nome} e tenho {len(self)} anos."

   # método retorna apenas inteiro 
    def __len__(self):
        return self.idade
    
    # método destrutor
    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucesso.")