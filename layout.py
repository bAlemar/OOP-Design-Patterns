from Cadastro import *
from Buscar_Musica_Titulo import *
from Buscar_Musica_Ano import *
from Playlist_Aleatoria import * 



def layout_main() -> str:
    print("""
    # 1 Cadastro Musica
    # 2 Buscar Musica pelo Titulo
    # 3 Buscar musica pelo ano Publicação
    # 4 Playlist Aleatoria
    # 5 Sair
    """)
    resposta = str(input('Digite a funcionalidade que deseja utilizar:'))
    
    if resposta == '1':
        cadastro = Cadastro_Musica()
        cadastro.run()
    if resposta == '2':
        script_buscar = Buscar_Musica()
        script_buscar.run()
    if resposta == '3':
        script_ano = Buscar_Musica_Ano()
        script_ano.Encontrar_data()
    if resposta == '4':
        script_playlist_aleatoria = Playlist_aleatoria()
        script_playlist_aleatoria.run()
    if resposta == '5':
        KeyError('Você saiu do Script')
                    


if __name__ == '__main__':
    layout_main()