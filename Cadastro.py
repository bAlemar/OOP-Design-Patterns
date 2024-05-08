# Vamos supor que entrou dentro da classe 1.
import re
import csv
import uuid
import pandas as pd

class Cadastro_Musica():

    def __validacao_input_musica_artista(self,dado):
        """
        Retorna True caso Musica Válida
        """
        padrao = re.compile(r'^[a-zA-Z0-9\s]+$')
        if padrao.match(dado):
            return True
        else:
            return False

    def cadastro_musica(self):
        while True:      
            musica = input('Insira o Nome da Musica:')
            if self.__validacao_input_musica_artista(musica):
                break
            else:
                print("Erro ao Inserir Musica, por favor apenas letras e numeros")
        return musica
    
    def cadastro_artista(self):
        while True:
            titulo = input('Insira o Nome do Artista:')
            if self.__validacao_input_musica_artista(titulo):
                break
            else:
                "Erro ao Inserir Artista, por favor apenas letras e numeros"
        return titulo

    def __validacao_data(self,dado):
        padrao = re.compile(r'\d{4}')
        if padrao.match(dado):
            return True
        else:
            return False
        
    
    def cadastro_data(self):
        while True:
            data = input('Insira o Nome da Data')
            if self.__validacao_data(data):
                return data
            else:
                print("Erro ao Inserir Artista, por favor siga esse padrão: \n 1999)")

    
    def registrar_na_base(self,id,musica,artista,data):
        file_path = 'base.csv'
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer =  csv.writer(file)
            writer.writerow([id,musica,artista,data])
    
    def id_unico(self):
        """
        Gera um Id Unico
        """
        df = pd.read_csv('base.csv')
        id_existentes = list(df['ID_Musica'].unique())
        while True:
            id = uuid.uuid4()
            if id not in id_existentes:
                return id

    
    def run(self):
        id_musica = self.id_unico()
        musica = self.cadastro_musica()
        artista = self.cadastro_artista()
        data = self.cadastro_data()
        self.registrar_na_base(id_musica,musica,artista,data)
        

def main():
    cadastro = Cadastro_Musica()
    cadastro.run()
    while True:
        print("""
        Musica Registrada com SUCESSO!!!
        ==============//=================//====================
        Deseja registrar outra Musica?
              
        Digite 1 para registrar outra musica 
        Digite 2 para voltar para Layout
        """)
        resposta_input = str(input('Digite 1 ou 2: '))
        if resposta_input == '1':
            cadastro = Cadastro_Musica()
            cadastro.run()
        else:
            # Insere layout
            return '2'
        

if __name__ == '__main__':
    main()
    
    
