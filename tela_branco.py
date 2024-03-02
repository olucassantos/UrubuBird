import pygame

# Inicialia a biblioteca do pygame
pygame.init()

# Criar uma tela
tamanho_tela = (960, 540)
tela = pygame.display.set_mode(tamanho_tela)

# Cria um relógio para controlar o FPS
relogio = pygame.time.Clock()

# Título da tela
pygame.display.set_caption("Ambiente de Testes")

while True:
    for evento in pygame.event.get():
            print(evento)

            if evento.type == pygame.QUIT:
                # Fecha a janela
                pygame.quit()

                # Fecha o jogo
                exit()


    # Atualiza a tela para mostrar as mudanças
    pygame.display.update()

    # Controla o FPS em 60 frames por segundo
    relogio.tick(60)