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

# Personagem
personagem = pygame.image.load("assets/obstaculos/Oval_leaf_tree2.png")
personagem_rect = personagem.get_rect(center = (480, 270))

# Plataforma
plataforma = pygame.image.load("assets/obstaculos/Liana_bridges2_ground_shadow.png")
plataforma_rect = plataforma.get_rect(center = (500, 400))

movimento = pygame.Vector2(0, 0)

gravidade = 1

while True:
    for evento in pygame.event.get():
            print(evento)

            if evento.type == pygame.QUIT:
                # Fecha a janela
                pygame.quit()

                # Fecha o jogo
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimento.x = -5
                if evento.key == pygame.K_RIGHT:
                    movimento.x = 5
                if evento.key == pygame.K_SPACE:
                    gravidade = -5
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    movimento.x = 0
                if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    movimento.y = 0

    # Aumenta a gravidade
    gravidade += 1
    if gravidade > 10:
        gravidade = 10

    # Preenche a tela com a cor branca
    tela.fill((255, 255, 255))

    # Adiciona a gravidade ao movimento
    movimento.y += gravidade

    # Verifica se o personagem está na plataforma
    if personagem_rect.colliderect(plataforma_rect):
        movimento.y = 0
        personagem_rect.bottom = plataforma_rect.top + 1

    elif personagem_rect.bottom >= 430:
        personagem_rect.bottom = 430
        movimento.y = 0

    # Atualiza a posição do personagem
    personagem_rect.move_ip(movimento)

    # Desenha a plataforma
    tela.blit(plataforma, plataforma_rect)

    # Desenha o personagem
    tela.blit(personagem, personagem_rect)

    # Atualiza a tela para mostrar as mudanças
    pygame.display.update()

    # Controla o FPS em 60 frames por segundo
    relogio.tick(20)