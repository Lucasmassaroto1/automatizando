import pyautogui
import time

def pesquisar_e_abrir(termos_pesquisa):
    for termo in termos_pesquisa:

        pyautogui.press('winleft')

        time.sleep(1)

        pyautogui.write(termo)

        time.sleep(1)
        
        pyautogui.press('enter')
        
        time.sleep(1)


termos = input("Digite os applicativos que você deseja abrir, separados por vírgula: ").split(',')
termos = [termo.strip() for termo in termos]
pesquisar_e_abrir(termos)