import pandas as pd

class Buscar_Musica():
    def __init__(self) -> None:
        df = pd.read_csv('base.csv')
        self.df = df
        return

    def __verificar_musica(self,match_musica) -> bool:
        """
        Verifica a musica e printa ela
        """
        
        if len(match_musica) > 0:
            return True
        else:
            return False

    def Encontrar_Musica(self):
        while True:
            musica = str(input('Insira Musica que Deseja Escutar'))
            match_musica = self.df[self.df['Titulo'].str.lower() == musica.lower()]
            if self.__verificar_musica(match_musica):
                print(match_musica)
                return musica
            else:
                print("A musica que você digitou não foi encontrada")

    def run(self):
        musica = self.Encontrar_Musica()


        
        
        


def main():
    script_buscar = Buscar_Musica()
    script_buscar.run()
    while True:
        print("""
        Musica Encontrada com SUCESSO!!!
        ==============//=================//====================
        Deseja registrar encontrar Musica?
                
        Digite 1 para registrar encontrar musica 
        Digite 2 para voltar para Layout
        """)
        resposta_input = str(input('Digite 1 ou 2: '))
        if resposta_input == '1':
            script_buscar = Buscar_Musica()
            script_buscar.run()
        else:
            # Insere layout
            return '2'
if __name__ == '__main__':
    main()




        