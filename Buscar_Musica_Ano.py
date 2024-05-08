import pandas as pd

class Buscar_Musica_Ano():
    def __init__(self) -> None:
        df = pd.read_csv('base.csv')
        self.df = df

    def __verificar_Ano(self,match_ano) -> bool:
        """
        Verifica a musica e printa ela
        """
        if len(match_ano) > 0:
            return True
        else:
            return False

    def Encontrar_data(self):
        while True:
            ano = str(input('Insira Musica que Deseja Escutar'))
            match_ano = self.df[self.df['Ano_Publicacao'] == ano]
            if self.__verificar_Ano(match_ano):
                print(match_ano)
                return match_ano
            else:
                print("A musica que você digitou não foi encontrada")
                
def main():
    script_ano = Buscar_Musica_Ano()
    script_ano.Encontrar_data()
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
            script_ano = Buscar_Musica_Ano()
            script_ano.Encontrar_data()
        else:
            # Insere layout
            return '2'


if __name__ == '__main__':
    main()