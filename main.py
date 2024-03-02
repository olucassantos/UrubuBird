import pygame
import random

def adicionaNovoObstaculo(lista_senhoras, lista_senhores):
    # Definier a posição X do obstáculo
    x = random.randint(1000, 1500)
    y = random.randint(600, 700)
    # Cria o retângulo da senhora a partir da imagem
    senhora_retangulo = senhora.get_rect(midbottom = (x, y)) # Cria o retângulo da senhora

    x = random.randint(1000, 1500)
    y = random.randint(-80, -30)

    senhor_retangulo = senhor.get_rect(midtop = (x, y)) # Cria o retângulo do senhor

    # Adiciona a senhora a lista de obstáculos
    lista_senhoras.append(senhora_retangulo)
    lista_senhores.append(senhor_retangulo)

def desenhaAnimaObstaculos(lista_senhoras, lista_senhores):
    global jogo_comecou, velocidade_obstaculos

    # Laço que passa em todos os obstáculos da lista
    for obstaculo in lista_senhoras:
        # Movimenta o obstáculo para a esquerda
        obstaculo.x -= velocidade_obstaculos
        obstaculo_hitbox = obstaculo.inflate(-400, -275) # Cria o retângulo do hitbox da obstaculo
        obstaculo_hitbox.center = obstaculo.center

        # Desenha o obstáculo na tela
        tela.blit(senhora, obstaculo)

        # Checa se o obstáculo saiu da tela
        if obstaculo.right < 0:
            # Remove o obstáculo da lista
            lista_senhoras.remove(obstaculo)

        # Checa se o urubu colidiu com o obstáculo
        if urubu_retangulo_hitbox.colliderect(obstaculo_hitbox):
            jogo_comecou = False
            # limpa a lista de obstáculos
            lista_senhoras.clear()
            lista_senhores.clear()

    for obstaculo in lista_senhores:
        # Movimenta o obstáculo para a esquerda
        obstaculo.x -= velocidade_obstaculos
        obstaculo_hitbox = obstaculo.inflate(-200, -100) # Cria o retângulo do hitbox da obstaculo
        obstaculo_hitbox.center = obstaculo.center


        # Desenha o obstáculo na tela
        tela.blit(senhor, obstaculo)

        # Checa se o obstáculo saiu da tela
        if obstaculo.right < 0:
            # Remove o obstáculo da lista
            lista_senhores.remove(obstaculo)

        # Checa se o urubu colidiu com o obstáculo
        if urubu_retangulo_hitbox.colliderect(obstaculo_hitbox):
            jogo_comecou = False
            # limpa a lista de obstáculos
            lista_senhores.clear()
            lista_senhoras.clear()

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
fonte_cronometro = pygame.font.Font(None, 36)

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

retangulos_fundos = {}

# Retangulo dos fundos 1
retangulos_fundos['fundo_floresta'] = []
retangulos_fundos['arvores_arbustos'] = []
retangulos_fundos['arvore'] = []
retangulos_fundos['ceu'] = []
retangulos_fundos['cipos'] = []
retangulos_fundos['plantas'] = []
retangulos_fundos['grama_estrada'] = []
retangulos_fundos['vagalumes'] = []

# Cria os retângulos dos planos de fundo
retangulos_fundos['fundo_floresta'].append(fundo_floresta.get_rect(topleft = (0, 0)))
retangulos_fundos['fundo_floresta'].append(fundo_floresta.get_rect(topleft = (960, 0)))

retangulos_fundos['arvores_arbustos'].append(arvores_arbustos.get_rect(topleft = (0, 0)))
retangulos_fundos['arvores_arbustos'].append(arvores_arbustos.get_rect(topleft = (960, 0)))

retangulos_fundos['arvore'].append(arvore.get_rect(topleft = (0, 0)))
retangulos_fundos['arvore'].append(arvore.get_rect(topleft = (960, 0)))

retangulos_fundos['ceu'].append(ceu.get_rect(topleft = (0, 0)))
retangulos_fundos['ceu'].append(ceu.get_rect(topleft = (960, 0)))

retangulos_fundos['cipos'].append(cipos.get_rect(topleft = (0, 0)))
retangulos_fundos['cipos'].append(cipos.get_rect(topleft = (960, 0)))

retangulos_fundos['plantas'].append(plantas.get_rect(topleft = (0, 0)))
retangulos_fundos['plantas'].append(plantas.get_rect(topleft = (960, 0)))

retangulos_fundos['grama_estrada'].append(grama_estrada.get_rect(topleft = (0, 0)))
retangulos_fundos['grama_estrada'].append(grama_estrada.get_rect(topleft = (960, 0)))

retangulos_fundos['vagalumes'].append(vagalumes.get_rect(topleft = (0, 0)))
retangulos_fundos['vagalumes'].append(vagalumes.get_rect(topleft = (960, 0)))

# Jogador Urubu
index_urubu_parado = 0 # Índice para controlar a animação do urubu
index_urubu_voando = 0 # Índice para controlar a animação do urubu

lista_urubu_parado = [] # Lista para armazenar as imagens do urubu
lista_urubu_voando = [] # Lista para armazenar as imagens do urubu voando

animaVooReverso = False # Faz com que a animação do urubu voando seja reversa

# Carrega as imagens do urubu parado
for imagem in range(5):
    urubu_parado_superficie = pygame.image.load(f"assets/parado/tile00{imagem}.png") # Carrega a imagem do urubu
    lista_urubu_parado.append(urubu_parado_superficie)

# Carrega as imagens do urubu voando
for imagem in range(5, 10):
    urubu_voando_superficie = pygame.image.load(f"assets/pulo/tile00{imagem}.png") # Carrega a imagem do urubu voando
    # Rotaciona em 35 graus a imagem do urubu
    urubu_voando_superficie = pygame.transform.rotate(urubu_voando_superficie, -35)
    
    lista_urubu_voando.append(urubu_voando_superficie)

# Cria o retângulo do urubu a partir da lista de imagens
urubu_retangulo_parado = lista_urubu_parado[index_urubu_parado].get_rect(center = (480, 350)) # Cria o retangulo do urubu
urubu_retangulo_voando = lista_urubu_voando[index_urubu_parado].get_rect(center = (100, 250)) # Cria o retangulo do urubu

# Cria um retângulo para o hitbox do urubu que é menor que o retângulo do urubu
urubu_retangulo_hitbox = urubu_retangulo_voando.inflate(-120, -120)

# Textos do Menu
titulo = fonte_titulo.render("Urubu Runner", True, (255, 255, 255)) # Renderiza o texto do título
menu_jogar = fonte_menu.render("Aperte Espaço para Jogar", True, (255, 255, 255)) # Renderiza o texto do menu

# Importa a imagem dos obstáculos
senhora = pygame.image.load('assets/obstaculos/Rock_statue_mother_grass_shadow.png') # Carrega a imagem da senhora
# Duplica o tamanho da senhora
senhora = pygame.transform.scale2x(senhora)

senhor = pygame.image.load('assets/obstaculos/Rock_statue_old_man_grass_shadow.png') # Carrega a imagem do senhor
# Duplica o tamanho do senhor
senhor = pygame.transform.scale2x(senhor)
senhor = pygame.transform.rotate(senhor, 180)

# Cria um lista de obstáculos
lista_senhoras = []
lista_senhores = []

# Loop do jogo
jogo_comecou = False

# Gravidade do urubu
gravidade = 1

# Velocidade dos obstáculos
velocidade_obstaculos = 20

# Cria um evento para adicionar novos obstáculos
novo_obstaculo_event = pygame.USEREVENT + 1
# Ativa o evento de adicionar novos obstáculos a cada 2 segundos
pygame.time.set_timer(novo_obstaculo_event, 3000)

novo_segundo_event = pygame.USEREVENT + 2
pygame.time.set_timer(novo_segundo_event, 1000)

# Cria um cronômetro para controlar o tempo do jogo
cronometro = 0

# LAÇO PRINCIPAL DO JOGO
while True:
    # Checa os eventos do jogo
    for evento in pygame.event.get():
        print(evento)

        if evento.type == novo_obstaculo_event:
            if jogo_comecou:
                adicionaNovoObstaculo(lista_senhoras, lista_senhores)

        if evento.type == novo_segundo_event:
            if jogo_comecou:
                cronometro += 1

        if evento.type == pygame.QUIT:
            # Fecha a janela
            pygame.quit()

            # Fecha o jogo
            exit()

        # Verifica se uma tecla foi pressionada
        if evento.type == pygame.KEYDOWN:
            # Verifica se a tecla pressionada foi a barra de espaço
            if evento.key == pygame.K_SPACE:
                jogo_comecou = True # Inicia o jogo
                ativaAnimacao = True # Ativa a animação do urubu
                gravidade = -21 # Diminui a gravidade do urubu para ele subir

    # Preenche a tela com a cor laranja
    tela.fill((205, 92, 92))

    # Desenha o plano de fundo na tela
    # tela.blit(ceu, (0, 0))
    # tela.blit(fundo_floresta, (0, 0))
    # tela.blit(arvores_arbustos, (0, 0))
    # tela.blit(cipos, (0, 0))
    # tela.blit(plantas, (0, 0))
    # tela.blit(grama_estrada, (0, 0))
    # tela.blit(arvore, (0, 0))
    # tela.blit(vagalumes, (0, 0))

    # Checa se o jogo não começou
    if not jogo_comecou:
        # Desenha o plano de fundo na tela
        tela.blit(ceu, (0, 0))
        tela.blit(fundo_floresta, (0, 0))
        tela.blit(arvores_arbustos, (0, 0))
        tela.blit(cipos, (0, 0))
        tela.blit(plantas, (0, 0))
        tela.blit(grama_estrada, (0, 0))
        tela.blit(arvore, (0, 0))
        tela.blit(vagalumes, (0, 0))

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

        # Reseta a posição do urubu
        urubu_retangulo_voando.y = 250

        cronometro = 0 # Reseta o cronômetro

    else: # Se o jogo começou
        # Anima os planos de fundo
        for fundos in retangulos_fundos:
            for retangulo in retangulos_fundos[fundos]:
                retangulo.x -= 10
                tela.blit(eval(fundos), retangulo)

            if retangulos_fundos[fundos][0].right <= 0:
                retangulos_fundos[fundos][0].x = 0
                retangulos_fundos[fundos][1].x = 960


        # Atualiza o índice do urubu para animar
        if ativaAnimacao:
            if animaVooReverso:
                index_urubu_voando -= 1.2
            else:
                index_urubu_voando += 1.2

        # Aumenta a gravidade
        gravidade += 7

        # Adiciona a gravidade ao urubu
        urubu_retangulo_voando.y += gravidade

        # Desenha o urubu voando na tela
        urubu_retangulo_hitbox.center = urubu_retangulo_voando.center
        tela.blit(lista_urubu_voando[int(index_urubu_voando)], urubu_retangulo_voando)

        # Desenha o cronômetro na tela
        cronometro_texto = fonte_cronometro.render(f"Tempo: {cronometro}", True, (255, 255, 255))
        tela.blit(cronometro_texto, (10, 10))

        # Checa se o índice do urubu é maior que o tamanho da lista de imagens
        if index_urubu_voando >= len(lista_urubu_voando) - 1:
            animaVooReverso = True
        elif index_urubu_voando <= 0:
            animaVooReverso = False
            ativaAnimacao = False

        # Verifica se o urubu saiu da tela
        if urubu_retangulo_voando.top > 540:
            jogo_comecou = False

        # Chama a função para desenhar e animar os obstáculos
        desenhaAnimaObstaculos(lista_senhoras, lista_senhores)

        if cronometro % 20 == 0:
            velocidade_obstaculos += 1

    # Atualiza a tela para mostrar as mudanças
    pygame.display.update()

    # Controla o FPS em 60 frames por segundo
    relogio.tick(60)