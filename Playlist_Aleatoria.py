import pandas as pd
import random

class Playlist_aleatoria:
    def __init__(self) -> None:
        self.df = pd.read_csv('base.csv')

    def aletorio(self):
        """
        Extrair as musicas e embaralha
        """
        todas_musicas = list(self.df['Titulo'].unique())
        random.shuffle(todas_musicas)
        return todas_musicas

    def run(self):
        lista_musicas = self.aletorio()
        for pos,musica in enumerate(lista_musicas):
            print(f'#{pos} {musica}')
def main():
    script_playlist_aleatoria = Playlist_aleatoria()
    script_playlist_aleatoria.run()
    
    return

if __name__ == '__main__':
    main()    