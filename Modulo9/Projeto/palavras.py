# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


palavraReg = namedtuple("palavraReg", "id, palavra")
listaPalavras = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaPalavras)):
        if listaPalavras[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_palavra():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    
    registo = palavraReg(cod, nome)
    listaPalavras.append(registo)

    

def listar_Palavras():
    for i in range (len(listaPalavras)):
        print "Código: ", listaPalavras[i].id
        print "Palavra: ", listaPalavras[i].palavra
        
  

def eliminar_palavra():
    cod = input ("Código da palavra a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhuma palavra com esse código"
        return

    # TODO: Confirmar eliminação
    listaPalavras.pop(pos)


    
def alterar_Palavra():
    cod = input ("Código da palavra a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhuma palavra com esse código"
        return

    # só altera o nome
    novapalavra = raw_input("Qual e a palavra ")
    listaPalavras[pos] = listaPalavras[pos]._replace(palavra=novapalavra)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_aluno()
        elif op =='2':
            listar_alunos()
        elif op == '3':
            pesquisar_aluno()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_aluno()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










