import pygame

# Inicialia a biblioteca do pygame
pygame.init()

# Criar uma tela
tela = pygame.display.set_mode((800, 400))

# Cria um relógio para controlar o FPS
relogio = pygame.time.Clock()

# Título da tela
pygame.display.set_caption("Urubu Runner")

# Seleciona a fonte e o tamanho da fonte
fonte = pygame.font.SysFont(None, 48)

# Cria um texto
corujinha = fonte.render("(o.o)", False, (255, 255, 255))

# Cria um vetor de duas dimensões para controlar o movimento
movimento = pygame.Vector2(0, 0)
posicao_coruja = pygame.Vector2(400, 200)
velocidade = 5
# Loop do jogo
while True:
    # Checa os eventos do jogo
    for evento in pygame.event.get():
        print(evento)

        if evento.type == pygame.QUIT:
            # Fecha a janela
            pygame.quit()

            # Fecha o jogo
            exit()
        
        # Checa se uma tecla foi pressionada
        if evento.type == pygame.KEYDOWN:
            # Checa se foi a seta direita
            if evento.key == pygame.K_RIGHT:
                movimento.x = velocidade
            elif evento.key == pygame.K_LEFT:
                movimento.x = -velocidade
            elif evento.key == pygame.K_UP:
                movimento.y = -velocidade
            elif evento.key == pygame.K_DOWN:
                movimento.y = velocidade
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT:
                movimento.x = 0
            elif evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                movimento.y = 0

    # Preenche a tela com a cor laranja
    tela.fill((205, 92, 92))

    # Desenha a corujinha na tela
    tela.blit(corujinha, posicao_coruja)

    # Atualiza a posição da corujinha
    posicao_coruja += movimento

    # Atualiza a tela para mostrar as mudanças
    pygame.display.update()

    # Controla o FPS em 60 frames por segundo
    relogio.tick(60)