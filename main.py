import pygame
pygame.init()

branco = (255, 255, 255)
vermelho = (255, 0, 0)

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Criando Bolas")

# Lista para armazenar as bolas
bolas = []

# Classe para representar a bola
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 3.25

    def draw(self):
        pygame.draw.circle(tela, vermelho, (self.x, self.y), self.radius)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                x, y = event.pos
                bola = Ball(x, y)
                bolas.append(bola)

    tela.fill(branco)

    for bola in bolas:
        bola.draw()

    pygame.display.flip()

pygame.quit()
