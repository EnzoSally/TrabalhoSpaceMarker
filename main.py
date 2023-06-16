import pygame
import winsound
import tkinter as tk
from tkinter import simpledialog

pygame.init()

branco = (255, 255, 255)
vermelho = (255, 0, 0)

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Criando Bolas")
pygame.mixer.music.load("SomNave.mp3")
pygame.mixer.music.play(-1)
icon = pygame.image.load("nave.png")
pygame.display.set_icon(icon)
fundo = pygame.image.load("fundo.jpg")

bolas = []

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 3.25
        self.bola_anterior = None
        self.nome = ""

    def definir_nome(self):
        self.nome = simpledialog.askstring("Nome da Estrela", "Insira o nome da Estrela:")

    def draw(self):
        pygame.draw.circle(tela, vermelho, (self.x, self.y), self.radius)
        if self.bola_anterior:
            pygame.draw.line(tela, vermelho, (self.x, self.y), (self.bola_anterior.x, self.bola_anterior.y), 1)

    def draw_name(self):
        fonte = pygame.font.SysFont(None, 20)
        if self.nome:
            texto = fonte.render(self.nome, True, (0, 0, 0))
        else:
            texto = fonte.render(f"DESCONHECIDO ({self.x}, {self.y})", True, (0, 0, 0))
        texto_rect = texto.get_rect(center=(self.x, self.y - self.radius - 10))
        tela.blit(texto, texto_rect)

root = tk.Tk()
root.withdraw()

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
                bola.definir_nome()
                bolas.append(bola)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                for bola in bolas:
                    if not bola.nome:
                        bola.nome = f"DESCONHECIDO ({bola.x}, {bola.y})"

    tela.fill(branco)
    tela.blit(fundo, (0,0))

    for bola in bolas:
        bola.draw_name()
        bola.draw()

    pygame.display.flip()

pygame.quit()