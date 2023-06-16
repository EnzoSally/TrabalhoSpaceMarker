import pygame

pygame.init()

branco = (255, 255, 255)
vermelho = (255, 0, 0)

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Criando Bolas")

bolas = []

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 3.25
        self.bola_anterior = None

    def draw(self):
        pygame.draw.circle(tela, vermelho, (self.x, self.y), self.radius)
        if self.bola_anterior:
            pygame.draw.line(tela, vermelho, (self.x, self.y), (self.bola_anterior.x, self.bola_anterior.y), 1)

# Loop principal do jogo

running = True
bola_anterior = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                x, y = event.pos
                bola = Ball(x, y)
                bola.bola_anterior = bola_anterior
                bola_anterior = bola
                bolas.append(bola)

    tela.fill(branco)

    for bola in bolas:
        bola.draw()

    pygame.display.flip()

pygame.quit()
