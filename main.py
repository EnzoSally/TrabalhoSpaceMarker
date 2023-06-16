import pygame
import tkinter as tk
from tkinter import simpledialog
import pickle
import sys

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

marcacoes = {}

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

def salvar_marcações():
    try:
        with open("marcacoes.pkl", "wb") as file:
            pickle.dump(marcacoes, file)
        print("Marcações salvas com sucesso!")
    except Exception as e:
        print("Erro ao salvar as marcações:", str(e))

def carregar_marcações():
    try:
        with open("marcacoes.pkl", "rb") as file:
            marcacoes_carregadas = pickle.load(file)
        marcacoes.clear()
        marcacoes.update(marcacoes_carregadas)
        print("Marcações carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo de marcações não encontrado.")
    except Exception as e:
        print("Erro ao carregar as marcações:", str(e))

def excluir_todas_marcações():
    marcacoes.clear()
    print("Todas as marcações foram excluídas.")

def mostrar_marcacoes():
    for bola, nome in marcacoes.items():
        print(f"Posição: ({bola.x}, {bola.y}) - Nome: {nome}")

root = tk.Tk()
root.withdraw()

fonte_hub = pygame.font.SysFont(None, 24)

running = True
bola_anterior = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvar_marcações()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                bola = Ball(x, y)
                bola.bola_anterior = bola_anterior
                bola_anterior = bola
                bola.definir_nome()
                marcacoes[bola] = bola.nome
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                salvar_marcações()
            elif event.key == pygame.K_F11:
                carregar_marcações()
            elif event.key == pygame.K_F12:
                excluir_todas_marcações()
            elif event.key == pygame.K_F9:
                mostrar_marcacoes()
            elif event.key == pygame.K_ESCAPE:
                salvar_marcações()
                pygame.quit()
                sys.exit()

    tela.fill(branco)
    tela.blit(fundo, (0, 0))

    for bola, nome in marcacoes.items():
        bola.nome = nome
        bola.draw_name()
        bola.draw()
        
    texto_hub = fonte_hub.render("Pressione F9 para mostrar as marcações", True, (0, 0, 0))
    tela.blit(texto_hub, (10, 10))
    texto_hub = fonte_hub.render("Pressione F10 para salvar as marcações", True, (0, 0, 0))
    tela.blit(texto_hub, (10, 40))
    texto_hub = fonte_hub.render("Pressione F11 para carregar as marcações", True, (0, 0, 0))
    tela.blit(texto_hub, (10, 70))
    texto_hub = fonte_hub.render("Pressione F12 para excluir todas as marcações", True, (0, 0, 0))
    tela.blit(texto_hub, (10, 100))


    pygame.display.flip()

pygame.quit()
