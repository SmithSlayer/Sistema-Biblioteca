class  livros:
    def __init__(self,  titulo, autor, codigo_identificacao):
        self.titulo=titulo
        self.autor=autor
        self.codigo_identificacao=codigo_identificacao
    def imprimir(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}, Codígo de Identificação: {self.codigo_identificacao}')
    def set_titulo(self, titulo):
        self.__titulo=titulo
    def get_titulo(self):
        return self.__titulo
    def set_autor(self, autor):
        self.__autor=autor
    def get_autor(self):
        return self.__autor
    def set_codigo_identificacao(self, codigo_identificacao):
        self.__codigo_identificacao=codigo_identificacao
    def get_codigo_identificacao(self):
        return self.__codigo_identificacao
        
class aluno:
    def __init__(self, nome, sobrenome, ra):
        self.nome=nome
        self.sobrenome=sobrenome
        self.ra=ra
    def imprimiraluno(self):
        print(f'Aluno: {self.nome} {self.sobrenome}, Registro Acadêmico: {self.ra}')
    def set_nome(self, nome):
        self.__nome=nome
    def get_nome(self):
        return self.__nome
    def set_sobrenome(self, sobrenome):
        self.__sobrenome=sobrenome
    def get_sobrenome(self):
        return self.__sobrenome
    def set_ra(self, ra):
        self.__ra=ra
    def get_ra(self):
        return self.__ra
    

#Registro geral classe livro
            
c=livros("Brasil, país do futuro", "Stefan Zweig", "0001")
c.imprimir()

#Registro geral aluno

b=aluno("Jefferson Kauhan", "Ribeiro", "2024123456")
b.imprimiraluno()

#Novos registros alunos

b.set_nome("Sid")
print("O novo nome é: " + b.get_nome())

b.set_sobrenome("Ney")
print("O novo sobrenome é: " + b.get_sobrenome())

b.set_ra("00032222")
print("O novo registro acadêmico é: " +b.get_ra())

#Registro novo livros
c.set_autor("Stefan")
print("O novo nome do autor é: " +c.get_autor())
c.set_titulo("Brasil, país do futuro")
print("O novo titulo é: " +c.get_titulo())
c.set_codigo_identificacao("0002")
print("O novo codígo de identificação é: " +c.get_codigo_identificacao())