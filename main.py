import pygame

# Inicialia a biblioteca do pygame
pygame.init()

# Criar uma tela
tamanho_tela = (960, 540)
tela = pygame.display.set_mode(tamanho_tela)

# Cria um relógio para controlar o FPS
relogio = pygame.time.Clock()

# Título da tela
pygame.display.set_caption("Urubu Runner")

# Importa a fonte
fonte_titulo = pygame.font.Font('assets/fontes/LeafCrownDemoRegular.ttf', 150)
fonte_menu = pygame.font.Font('assets/fontes/LeafCrownDemoOutline.ttf', 80)

# Planos de Fundo
vagalumes = pygame.image.load('assets/planoFundo/fireflys.png') # Carrega a imagem dos vagalumes
grama_estrada = pygame.image.load('assets/planoFundo/grass&road.png') # Carrega a imagem da grama da estrada
plantas = pygame.image.load('assets/planoFundo/grasses.png') # Carrega a imagem das plantas
fundo_floresta = pygame.image.load('assets/planoFundo/jungle_bg.png') # Carrega a imagem do fundo da floresta
cipos = pygame.image.load('assets/planoFundo/lianas.png') # Carrega a imagem dos cipós
ceu = pygame.image.load('assets/planoFundo/sky.png') # Carrega a imagem do céu
arvore = pygame.image.load('assets/planoFundo/tree_face.png') # Carrega a imagem da árvore
arvores_arbustos = pygame.image.load('assets/planoFundo/trees&bushes.png') # Carrega a imagem das árvores e arbustos

# Redimensiona as imagens do plano de fundo
fundo_floresta = pygame.transform.scale(fundo_floresta, tamanho_tela)
arvores_arbustos = pygame.transform.scale(arvores_arbustos, tamanho_tela)
arvore = pygame.transform.scale(arvore, tamanho_tela)
ceu = pygame.transform.scale(ceu, tamanho_tela)
cipos = pygame.transform.scale(cipos, tamanho_tela)
plantas = pygame.transform.scale(plantas, tamanho_tela)
grama_estrada = pygame.transform.scale(grama_estrada, tamanho_tela)
vagalumes = pygame.transform.scale(vagalumes, tamanho_tela)

# Jogador Urubu
index_urubu_parado = 0 # Índice para controlar a animação do urubu
index_urubu_voando = 0 # Índice para controlar a animação do urubu

lista_urubu_parado = [] # Lista para armazenar as imagens do urubu
lista_urubu_voando = [] # Lista para armazenar as imagens do urubu voando
animaVooReverso = False

# Carrega as imagens do urubu parado
for imagem in range(5):
    urubu_parado_superficie = pygame.image.load(f"assets/parado/tile00{imagem}.png") # Carrega a imagem do urubu
    lista_urubu_parado.append(urubu_parado_superficie)

# Carrega as imagens do urubu voando
for imagem in range(5, 10):
    urubu_voando_superficie = pygame.image.load(f"assets/pulo/tile00{imagem}.png") # Carrega a imagem do urubu voando
    lista_urubu_voando.append(urubu_voando_superficie)

# Cria o retângulo do urubu a partir da lista de imagens
urubu_retangulo_parado = lista_urubu_parado[index_urubu_parado].get_rect(center = (480, 350)) # Cria o retangulo do urubu
urubu_retangulo_voando = lista_urubu_voando[index_urubu_parado].get_rect(center = (100, 250)) # Cria o retangulo do urubu

# Textos do Menu
titulo = fonte_titulo.render("Urubu Runner", True, (255, 255, 255)) # Renderiza o texto do título
menu_jogar = fonte_menu.render("Aperte Espaço para Jogar", True, (255, 255, 255)) # Renderiza o texto do menu

# Loop do jogo
jogo_comecou = False

while True:
    # Checa os eventos do jogo
    for evento in pygame.event.get():
        print(evento)

        if evento.type == pygame.QUIT:
            # Fecha a janela
            pygame.quit()

            # Fecha o jogo
            exit()

    # Preenche a tela com a cor laranja
    tela.fill((205, 92, 92))

    # Desenha o plano de fundo na tela
    tela.blit(ceu, (0, 0))
    tela.blit(fundo_floresta, (0, 0))
    tela.blit(arvores_arbustos, (0, 0))
    tela.blit(cipos, (0, 0))
    tela.blit(plantas, (0, 0))
    tela.blit(grama_estrada, (0, 0))
    tela.blit(arvore, (0, 0))
    tela.blit(vagalumes, (0, 0))

    if not jogo_comecou:
        # Desenha o título na tela na posição central usando o tamanho da tela e a largura do texto
        tela.blit(titulo, (tamanho_tela[0] / 2 - titulo.get_width() / 2, 50))
        # Desenha o menu na tela
        tela.blit(menu_jogar, (tamanho_tela[0] / 2 - menu_jogar.get_width() / 2, 230))

        # Desenha o urubu na tela
        tela.blit(lista_urubu_parado[int(index_urubu_parado)], urubu_retangulo_parado)
        # Atualiza o índice do urubu para animar
        index_urubu_parado += 0.3
        # Checa se o índice do urubu é maior que o tamanho da lista de imagens
        if index_urubu_parado >= len(lista_urubu_parado):
            index_urubu_parado = 0

    else:

        # Atualiza o índice do urubu para animar
        if animaVooReverso:
            index_urubu_voando -= 1
        else:
            index_urubu_voando += 1

        # Desenha o urubu voando na tela
        tela.blit(lista_urubu_voando[int(index_urubu_voando)], urubu_retangulo_voando)

        # Checa se o índice do urubu é maior que o tamanho da lista de imagens
        if index_urubu_voando >= len(lista_urubu_voando) - 1:
            animaVooReverso = True
        elif index_urubu_voando <= 0:
            animaVooReverso = False


    # Atualiza a tela para mostrar as mudanças
    pygame.display.update()

    # Controla o FPS em 60 frames por segundo
    relogio.tick(60)