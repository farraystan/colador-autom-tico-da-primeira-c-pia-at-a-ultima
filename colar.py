import pyautogui
import time
import pygame
import os

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Função para reproduzir o áudio
def play_audio(audio_filename):
    # Obtém o caminho do diretório atual
    current_directory = os.path.dirname(__file__)
    # Junta o caminho do diretório atual com o nome do arquivo de áudio
    audio_path = os.path.join(current_directory, audio_filename)
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

# Função para realizar a sequência de teclas com base no número total de execuções
def perform_sequence(total_executions):
    time.sleep(2)

    # Loop para pressionar Win + V, Down e Enter conforme necessário
    for i in range(total_executions, -1, -1):  # Começa com o total de execuções e diminui até 0
        down_presses = i if i < total_executions else 0
        for _ in range(down_presses):
            pyautogui.hotkey('win', 'v')  # Abre o histórico de área de transferência
            time.sleep(0.5)
            pyautogui.press('down')  # Desce na lista do histórico
            time.sleep(0.5)
        pyautogui.hotkey('win', 'v')  # Abre o histórico de área de transferência
        time.sleep(0.5)
        pyautogui.press('enter')  # Seleciona o item do histórico
        time.sleep(0.5)

# Número total de execuções
total_executions = int(input("Quantas execuções? "))
pyautogui.alert('começar')

# Realiza a sequência de teclas com base no número total de execuções
perform_sequence(total_executions)

# Exibe um alerta indicando o fim do código
print("Fim do código.")

# Nome do arquivo de áudio
audio_filename = "We'll Be Right Back - Sound Effect (HD).wav"
play_audio(audio_filename)

# Espera a música terminar de tocar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

#máximo 24 execuções