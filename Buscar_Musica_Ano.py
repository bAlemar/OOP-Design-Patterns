import pandas as pd
from Continuacao_Funcionalidades import *


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

    def run(self):
        self.Encontrar_data()
                
def main():
    script_ano = Buscar_Musica_Ano()
    script_ano.Encontrar_data()
    script_continuacao = Next_Step()
    script_continuacao.funcao_para_continuar(Buscar_Musica_Ano())


if __name__ == '__main__':
    main()