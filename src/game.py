import pygame
from menu import Menu
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tesouro do pirata")
        self.relogio = pygame.time.Clock()

        # O jogo começa sem nenhuma fase pré-carregada na memória
        self.level = None
        self.menu = Menu(self)
        self.estado_atual = "MENU"

    def run(self):
        while True:
            # Mantém o jogo rodando fixo a 60 quadros por segundo
            self.relogio.tick(60)

            # SE ESTIVER NO MENU:
            if self.estado_atual == "MENU":
                # Captura o que o menu retornou quando o jogador apertou ENTER
                retorno_menu = self.menu.run()

                if retorno_menu == "JOGANDO":
                    pygame.event.clear()  # Limpa os eventos pendentes
                    # Cria a fase nova (com 3 vidas cheias!)
                    self.level = Level(self.window, "Fase 1")
                    self.estado_atual = "JOGANDO"

                # SE ESTIVER JOGANDO A FASE:
            elif self.estado_atual == "JOGANDO":
                retorno = None
                retorno = self.level.run()

                if retorno == "VOLTAR_MENU":
                    self.estado_atual = "MENU"
                    pygame.mixer.music.stop()
                elif retorno == "GAME_OVER":
                    self.estado_atual = "GAME_OVER"
                    pygame.mixer.music.stop()
                elif retorno == "VITORIA":
                    self.estado_atual = "VITORIA"
                    pygame.mixer.music.stop()

            # estados de fim de jogo:
            elif self.estado_atual == "GAME_OVER":
                if self.show_game_over(self.window) == "MENU":
                    self.estado_atual = "MENU"

            elif self.estado_atual == "VITORIA":

                if self.show_vitoria(self.window) == "MENU":
                    self.estado_atual = "MENU"

    def show_game_over(self, window):
        window.fill((0, 0, 0))
        fonte = pygame.font.SysFont("Arial", 60)
        texto = fonte.render("GAME OVER! Pressione ENTER", True, (255, 0, 0))

        # Centraliza matematicamente:
        # (largura_janela - largura_texto) / 2
        x = (window.get_width() - texto.get_width()) // 2
        y = (window.get_height() - texto.get_height()) // 2

        window.blit(texto, (x, y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return "MENU"
        return "GAME_OVER"

    def show_vitoria(self, window):
        window.fill((0, 255, 0))
        fonte = pygame.font.SysFont("Arial", 60)
        texto = fonte.render("VOCÊ VENCEU! Pressione ENTER", True, (255, 255, 255))

        # Centraliza matematicamente:
        x = (window.get_width() - texto.get_width()) // 2
        y = (window.get_height() - texto.get_height()) // 2

        window.blit(texto, (x, y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return "MENU"
        return "VITORIA"

# --- BLOCO DE INICIALIZAÇÃO ---
if __name__ == "__main__":
    jogo = Game()
    jogo.run()