from Grid import Grid
from Food import Food
from Agente import Agente

import math

#conf tela
altura_grid = 500
largura_grid = 500
quant_hor = 21#colocar igual a ver(erro serah concertado)
quant_ver = 21#colocar igual a hor(erro serah concertado)

tela_auxiliar = 0#largura_grid*0.4

altura_tela = int(math.ceil(altura_grid/quant_ver)*quant_ver+50)
largura_tela = int(math.ceil(largura_grid/quant_hor)*quant_hor + tela_auxiliar)

def setup():
    global g, f, a, path, node

    g = Grid(altura_grid,largura_grid,quant_hor,quant_ver)

    aux = g.procurar_posicao_vazia()
    f = Food(aux[0],aux[1])

    #configurado para agente iniciar no meio do grid
    a = Agente(g.nodes[int(math.ceil(quant_hor/2))][int(math.ceil(quant_ver/2))])

    path = []

    node = None

    #Muda a velocidade de que atualiza draw
    frameRate(50)

    size(largura_tela, altura_tela)
    background(255)

def draw():
    global g, f, a, path, node

    #pontuação
    fill(255)
    rect(0,height-50, largura_tela,height-50)
    textSize(25)
    fill(0, 0, 0)
    text('Pontos {}'.format(a.pontos), 10, height-15)

    if(len(path) > 0):
        frameRate(10)
        if (node != None):
            node.valor = 0
        node = path.pop(0)
        g.posicao_comida_node(f.i,f.j)
        g.posicao_agente(node.i,node.j)
        g.display(True)
    else:
        frameRate(50)

        if(a.achou_comida == True and f.is_dead == False):
            father = a.atual.father
            while father != None:
                if (father not in path):
                    path.append(father)
                    father = father.father
                else:
                    father = None
            path = path[::-1]
            f.dead()
        elif(f.is_dead == True):
            a = Agente(g.nodes[f.i][f.j], a.pontos + 1)
            aux = g.procurar_posicao_vazia()
            f = Food(aux[0],aux[1])
            g.posicao_comida_node(f.i,f.j)
        elif(a.dead_lock == True):
            a = Agente(g.nodes[a.i][a.j], a.pontos)
            aux = g.procurar_posicao_vazia()
            f = Food(aux[0],aux[1])
            g.posicao_comida_node(f.i,f.j)
        else:
            a.buscar_comida(f)
            # grid_secundario(a.nodes_abertos, a.nodes_fechados)
            g.pintar_nodes_fechados(a.nodes_fechados)
            g.pintar_nodes_abertos(a.nodes_abertos)
            g.pintar_nodes_atual(a.atual)
            if len(a.nodes_abertos)>0:
                g.pintar_proximo_node_anilizado(a.nodes_abertos[-1])
            g.posicao_comida_node(f.i,f.j)
            g.posicao_agente(a.i,a.j)
            g.display()

#melhor nome
def grid_secundario(abertos, fechados):
    x_tela_aux = largura_tela-tela_auxiliar
    fill(255)
    rect(x_tela_aux, 0,tela_auxiliar ,height-50)
    '''
    #pilha fechados
    fill(0)
    rect(x_tela_aux+20, 10, tela_auxiliar*0.3, height-70)

    #pilha abertas
    fill(0)
    rect(x_tela_aux+120, 10, tela_auxiliar*0.3, height-70)
    '''

    aux_y = height-70-tela_auxiliar*0.1
    fill(0)
    textSize(16)
    text('F', x_tela_aux+23, aux_y+tela_auxiliar*0.2)
    for n,x in enumerate(fechados):
        if (len(fechados)>22) and (n < len(fechados)-22):
            continue
        textSize(16)
        fill(0)
        text('{}:{},{}'.format(n,x.i,x.j), x_tela_aux+23, aux_y+tela_auxiliar*0.1)
        aux_y -= tela_auxiliar*0.1

    aux_y = height-70-tela_auxiliar*0.1
    text('A', x_tela_aux+123, aux_y+tela_auxiliar*0.2)
    for n,x in enumerate(abertos):
        if (len(abertos)>22) and (n < len(abertos)-22):
            continue
        textSize(16)
        fill(0)
        text('{}:{},{}'.format(n,x.i,x.j), x_tela_aux+123, aux_y+tela_auxiliar*0.1)
        aux_y -= tela_auxiliar*0.1
