# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:30:36 2013

@author: i12184
"""

# -*- coding: utf-8 -*-

def menu():
    print
    print "1: Inserir novo Tema"
    print "2: Listar todos os Sites"
    print "3: Alterar dados de um Tema"
    print "4: Eliminar Tema"
    print
    print "0: Terminar"
    print

    

def inserir():
    num = input("Introduza código: ")
    
    encontrou = False        
    for i in range(len(Sites)):
        if Sites[i].num == num:
            encontrou = True           
            break
        
    
    if encontrou:
        print "Esse codigo é repetido."
        return
    
    nome = raw_input("Introduz anome: ")
    Tema = raw_input("Introduza tema: ")
    ano = raw_input("Introduza ano: ")
    
    
    novo_registo = SiteReg(num, nome, Tema, ano)

    Sites.append(novo_registo)    
    
           

def listar_todos():
    if len(Sites) == 0:
        print "Não existem livros inseridos"
        return
     
    for i in range(len(Sites)):
        print "Código: ", Sites[i].num
        print "  Nome: ", Sites[i].nome
        print " Tema : ", Sites[i].Tema
        print "   Ano: ", Sites[i].ano
        print "-------------------------------"
        
        
    

    
def alterar():
    codigo = input("Introduza código do Site: ")

    encontrou = False        
    for i in range(len(Sites)):
        if Sites[i].num == codigo:
            encontrou = True
            pos = i #Posição dentro do array onde está  registo
            break
    
    
    if not encontrou:
        print "Esse codigo não existe"
        return
        
    novo_nome = raw_input("Introduza novo nome: ")
    novo_tema = raw_input("Introduza novo tema: ")
    novo_ano = raw_input("Novo ano de lançamento: ")

    
    Sites[pos] = Sites[pos]._replace(nome=novo_nome, Tema=novo_tema, ano=novo_ano)

    
    
def eliminar():
    codigo = input("Introduza código do Site: ")

    encontrou = False        
    for i in range(len(Sites)):
        if Sites[i].num == codigo:
            encontrou = True
            pos = i
            break
    
    
    if not encontrou:
        print "Esse codigo não existe"
        return
        
    Sites.pop(pos)


from collections import namedtuple

SiteReg = namedtuple("SiteReg", "num, nome, Tema, ano")

Sites = []
	
quero_sair = False
while not quero_sair:
    menu()
    op = raw_input("Introduza opção: ")
    if op == '1':
        inserir()
    elif op == '2':
        listar_todos()		
    elif op == '3':
        alterar()
    elif op == '4':
        eliminar()
    elif op == '0': 
        quero_sair = True
    else:
	print "Opção inválida"
        
print 

