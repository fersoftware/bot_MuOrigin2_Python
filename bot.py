from PIL import ImageGrab, ImageOps, Image
import pyautogui
import time
import pyscreenshot as ImageScreen
from numpy import *

class Coordinates():
    iconeMu = (632, 329, 695, 393)
    btnStartServer = (627, 505, 696, 526)
    btnStartChar = (975, 490, 1046, 509)
    btnAnuncio = (952, 161, 969, 178)
    btnClaim = (641, 536, 688, 551)
    btnClaim2 = (642, 559, 691, 573)
    btnAtacar = (911, 682, 918, 701)
    btnDungeon = (877, 115, 889, 125)
    msgItemClaim2 = (664, 286, 670, 691)
    btnEspera = (546, 342, 563, 367)

class Images():
    iconeMu = 35949
    btnStartServer = 23958
    btnStartChar = 23329
    btnAnuncio = 17735
    btnClaim = 15410
    btnClaim2 = 18140
    btnAtacarOFF = 5954
    btnAtacarON = 11311
    btnEspera = 18109
    btnDungeon = 7949
    msgItemClaim2 = 20856

def info(txt):
    box = txt
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

if __name__ == "__main__":
    box = Coordinates.msgItemClaim2
    print(info(box))

def main():
    print('BOT PROTOTIPO MU 1.0')
    time.sleep(5);
    tentativa = 0;
    while True:
        if (info(Coordinates.iconeMu) == Images.iconeMu):
            x = Coordinates.iconeMu
            print('Entrando no Mu')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(3);
        if (info(Coordinates.btnStartServer) == Images.btnStartServer):
            x = Coordinates.btnStartServer
            print('Entrando no Server')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(3);
        if (info(Coordinates.btnStartChar) == Images.btnStartChar):
            x = Coordinates.btnStartChar
            print('Entrando com o Char')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(10);
        if (info(Coordinates.btnAnuncio) == Images.btnAnuncio):
            x = Coordinates.btnAnuncio
            print('Fechando Anuncio')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnClaim) == Images.btnClaim):
            x = Coordinates.btnClaim
            print('Tela Claim aceita')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnClaim2) == Images.btnClaim2):
            x = Coordinates.btnClaim2
            print('Tela Itens Claim aceita')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.msgItemClaim2) == Images.msgItemClaim2):
            x = Coordinates.msgItemClaim2
            print('Fechando Tela Claim Item')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnAtacar) == Images.btnAtacarOFF):
            x = Coordinates.btnAtacar
            print('Entrando em Modo Atacar')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnEspera) == Images.btnEspera):
            x = Coordinates.btnEspera
            print('Saindo da Tela Hibernação')
            pyautogui.click(x[0] + 5, x[1] + 5)
            pyautogui.dragTo(x[0] + 5, x[1] + 5, button='left')
            pyautogui.dragTo(x[0] + 255, x[1] + 5, 2, button='left')
            time.sleep(1);
        if(info(Coordinates.btnAtacar) == (Images.btnAtacarON or info(Coordinates.btnAtacar) == Images.btnAtacarOFF) and info(Coordinates.btnDungeon) == Images.btnDungeon):
            tentativa = 0;
            #print('Fora da Cidade')
        elif(info(Coordinates.btnAtacar) != (Images.btnAtacarON or info(Coordinates.btnAtacar) == Images.btnAtacarOFF) and info(Coordinates.btnDungeon) == Images.btnDungeon):
            #print('Tentativa ', tentativa)
            #print(info(Coordinates.btnAtacar))
            #print(info(Coordinates.btnDungeon))
            if(tentativa == 2):
                print('Dentro da Cidade')
                time.sleep(1);
                print('Abrindo Mapa')
                time.sleep(3);
                pyautogui.click(1054,72)
                time.sleep(3);
                print('Escolhendo...')
                pyautogui.click(244,231)
                time.sleep(3);
                print('Indo até o MOB')
                pyautogui.click(696 ,508)
                print('Aguardando...')
                time.sleep(10);
                print('Upando...')
                pyautogui.click(239 ,133)
                tentativa = 0;
            tentativa += 1

main()
