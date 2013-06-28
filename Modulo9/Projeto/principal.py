# -*- coding: utf-8 -*-

import menu
import palavras
import util


# nome dos ficheiros
fxpalavras = "Palavras.dat"
fxartigos = "Artigos.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    palavras.listaPalavras = util.ler_ficheiro(fxpalavras)
    artigos.listaArtigos = util.ler_ficheiro(fxartigos)

def escrever_ficheiros():
    #adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxpalavras, palavras.listaPalavras)
    util.escrever_ficheiro(fxartigos, artigos.listaArtigos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        palavras.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()


