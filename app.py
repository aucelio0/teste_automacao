# biblioteca de automação
import pyautogui as auto
import time

# atrasar os comandos
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('chrome') # digita palavra
auto.press('enter') # aperta "enter"

#maximizar a tela
# auto.hotkey('alt', 'space')
# auto.press('x')

auto.write('github.com') 
auto.press('enter')

# entrar na pag de login do git
# for i in range(12):
#    auto.press('tab')
    
# auto.press('enter')

# fazer login login
time.sleep(10)
auto.press('tab')
time.sleep(10)
auto.press('enter')

# ir até o repositório
for i in range(12):
   auto.press('tab')
   
auto.press('enter')

# escrever o repositório
for i in range(12):
   auto.press('tab')
   
# escrever nome do repositório
time.sleep(10)
   
# ir para descrição
for i in range(2):
   auto.press('tab')
   
# escrever a descrição e criar
time.sleep(15   )
auto.press('enter')

# voltar para o vscode
auto.hotkey('alt', 'tab')

# abrir centro de controle
auto.hotkey('ctrl', 'j')
auto.hotkey('ctrl', 'j')

auto.press('enter')

# jogar para o repositório
auto.write('git init')
auto.press('enter')
auto.write('git add .')
auto.press('enter')
auto.write('git commit -m "versão 1.0"')
auto.press('enter')
auto.write('git branch -m main')
auto.press('enter')
time.sleep(10)
auto.press('enter')
auto.write('git push -u origin main')

auto.press('enter')



