from Node import Node
import math
import random

class Grid():
    def __init__(self, altura, largura, quant_hor, quant_ver):
        self.altura = altura
        self.largura = largura
        self.quant_hor = quant_hor
        self.quant_ver = quant_ver
        self.nodes = []
        
        #
        self.__iniciar_matrix_nodes()
        self.__adicionar_obstaculos()
            
    
    def procurar_posicao_vazia(self):
        while(True):
            i = random.randrange(1, self.quant_hor)
            j = random.randrange(1, self.quant_ver)
            if(self.nodes[i][j].valor == 0):
                return [i,j]
            
    def posicao_agente(self,i,j):
        print(self.nodes[i][j])
        print(i,j)
        self.nodes[i][j].mudar_valor(1)
    
    def add_comida_node(self,i, j):
        self.nodes[i][j].mudar_valor(2)
    
    def nodes_visiveis(self, i, j):
        aux = []
        #verifica se tem no a direita
        if(j+1 < self.quant_ver):
            aux.append([i,j+1])
        #verifica se tem no a cima
        if(i-1 > -1 ):
            aux.append([i-1,j])
        #verifica se tem no a baixo
        if(i+1 > self.quant_hor):
            aux.append([i+1,j])
        #verifica se tem no a esqueda
        if(j-1 > -1):
            aux.append([i,j-1])
        
        return aux
        
    def display(self):
        aux_altura = self.altura/self.quant_ver
        aux_largura = self.largura/self.quant_hor
        
        aux_y = 0
        for i in self.nodes:
            aux_x = 0
            for j in i:
                #valor indica que tem parede
                if(j.valor == -1):
                    fill(0)
                    
                #valor indica que estah vazio
                elif(j.valor == 0):
                    fill(255)
                    
                #valor indica estah o agente
                elif(j.valor == 1):
                    fill(0,255,0)
                    
                #valor indica que tem comida
                elif(j.valor == 2):
                    fill(255,0,0)
                    
                #valor indica que noh fechado
                elif(j.valor == 4):
                    fill(128,0,128)
                    
                #valor indica que noh aberto
                elif(j.valor == 3):
                    fill(0,255,255)
                    
                rect(aux_x, aux_y, aux_largura, aux_altura)   
                aux_x += aux_largura
            aux_y += aux_altura
    
    #
    def __iniciar_matrix_nodes(self):
        for i in range(self.quant_ver):
            self.nodes.append([])
            for j in range(self.quant_hor):
                self.nodes[i].append(Node(i, j))
        
            
    def __adicionar_obstaculos(self):
        for i in range(int((self.quant_hor * self.quant_ver)*0.2)):
            aux = self.procurar_posicao_vazia()
            self.nodes[aux[0]][aux[1]].mudar_valor(-1)
        

            

                        
