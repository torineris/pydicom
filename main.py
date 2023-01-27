import pydicom

#leitura do arquivo
sr = pydicom.dcmread('sr.dcm')



#estrutura de cada nó
class No:
    def __init__(self, node=None, firstChild= None, nextSibling=None):
        
        self.firstChild = firstChild
        self.nextSibling = nextSibling


#construção da lista ligada
def linkedList(sr):
    nodes = []
    for elem in sr:
        if elem.vr == 'SQ':
            nodes.append
        else:
            nodes.append(elem)
        