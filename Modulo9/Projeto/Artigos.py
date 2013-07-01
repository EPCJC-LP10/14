# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


ArtigosReg = namedtuple("ArtigosReg", "id, titulo, autor, data, texto")
listaArtigos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaArtigos)):
        if listaArtigos[i].id == codigo:
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
    novo_titulo=raw_input("Qual e o titulo")  
    novo_autor=raw_input("Qual e o autor")  
    nova_data=raw_input("Qual e a data")  
    novo_texto=raw_input("Qual e o texto")  
    
    
    
    registo = ArtigosReg(cod, nome, novo_titulo, novo_autor, nova_data, novo_texto )
    listaArtigos.append(registo)

    

def listar_Palavras():
    for i in range (len(listaArtigos)):
        print "Código: ", listaArtigos[i].id
        print "Palavra: ", listaArtigos[i].palavra
        
  

def eliminar_palavra():
    cod = input ("Código da palavra a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhuma palavra com esse código"
        return

    # TODO: Confirmar eliminação
    listaArtigos.pop(pos)


    
def alterar_Palavra():
    cod = input ("Código da palavra a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhuma palavra com esse código"
        return

    # só altera o nome
    novapalavra = raw_input("Qual e a palavra ")
    listaArtigos[pos] = listaArtigos[pos]._replace(palavra=novapalavra)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            encontrar_posicao()
        elif op =='2':
            inserir_palavra()
        elif op == '3':
            listar_Palavras()
        elif op == '4':
            eliminar_palavra()
        elif op == '5':
            alterar_Palavra()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










