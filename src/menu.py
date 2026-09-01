import pygame
import sys
import os


class Menu:
    def __init__(self, game):
        self.game = game
        self.window = game.window

        # 1. CONFIGURAÇÃO DE FONTES
        self.fonte_titulo = pygame.font.SysFont("Arial", 48, bold=True)
        self.fonte_comandos = pygame.font.SysFont("Arial", 24, bold=True)

        # 2. CARREGANDO O BACKGROUND DO MENU
        # Importamos a classe Background aqui para evitar importação circular
        from background import Background
        self.background = Background("assets/images/menu_bg.png")

        # 3. INICIALIZAR MÚSICA DO MENU LOGO NO INÍCIO
        caminho_musica = "assets/sounds/musica_menu.mp3"
        try:
            pygame.mixer.music.load(caminho_musica)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)  # -1 faz tocar em loop infinito
        except pygame.error:
            print("Aviso: Erro ao carregar a música do menu no início.")

    def run(self):
        # --- REINICIAR A MÚSICA CASO ELA TENHA PARADO (VOLTANDO DO GAME OVER) ---
        if not pygame.mixer.music.get_busy():
            caminho_musica = "assets/sounds/musica_menu.mp3"
            try:
                pygame.mixer.music.load(caminho_musica)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
            except pygame.error:
                print("Aviso: Erro ao recarregar a música do menu.")

        # Loop interno que segura a tela do menu aberta
        menu_rodando = True
        while menu_rodando:

            # 1. CAPTURA DE EVENTOS (TECLADO E FECHAR JANELA)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    # Se o jogador apertar ENTER, para a música do menu e vai pro jogo
                    if evento.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()

                        # Carrega e inicia a música da fase (level)
                        caminho_level = "assets/sounds/musica_level.mp3"
                        try:
                            pygame.mixer.music.load(caminho_level)
                            pygame.mixer.music.set_volume(0.2)
                            pygame.mixer.music.play(-1)
                        except pygame.error:
                            print("Aviso: Erro ao carregar a música do level.")
                        return "JOGANDO"  # Retorna o comando para o game.py

            # 2. DESENHANDO O BACKGROUND DO MENU
            if self.background and self.background.image:
                self.background.draw(self.window)
            else:
                self.window.fill((30, 30, 40))

                # 3. RENDERIZAÇÃO DOS TEXTOS NA TELA
            superficie_titulo = self.fonte_titulo.render("TESOURO DO PIRATA", True, (255, 215, 0))
            superficie_cmd1 = self.fonte_comandos.render("Setas Direcionais (▲ ▼ ◄ ►) - Movimentar", True,
                                                         (255, 255, 255))
            superficie_cmd2 = self.fonte_comandos.render("ESC - Voltar para o Menu", True, (255, 255, 255))
            superficie_jogar = self.fonte_comandos.render("Pressione [ ENTER ] para Iniciar", True, (100, 255, 100))

            # Desenha os textos nas posições certinhas por cima do navio
            self.window.blit(superficie_titulo, (180, 100))
            self.window.blit(superficie_cmd1, (140, 250))
            self.window.blit(superficie_cmd2, (140, 310))
            self.window.blit(superficie_jogar, (210, 450))

            # Atualiza a tela e trava o menu em 60 FPS
            pygame.display.flip()
            pygame.time.Clock().tick(60)
        return None