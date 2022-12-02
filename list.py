from node import Node

class List:
    def __init__(self):
        self.inicio = None
 

    def push(self, process):
        node = Node(process)

        pointer = self.inicio
        ant = pointer

        while(pointer and pointer.process.prioridade_fila >= node.process.prioridade_fila):
            ant = pointer
            pointer = pointer.prox
        
        if not self.inicio:
            self.inicio = node
        elif not pointer:
            ant.prox = node
        elif self.inicio == pointer:
            node.prox = pointer
            self.inicio = node
        else:
            node.prox = pointer
            ant.prox = node


    def add(self, process):
        node = Node(process)

        pointer = self.inicio
        ant = pointer
        while(pointer):
            ant = pointer
            pointer = pointer.prox
        
        if not self.inicio:
            self.inicio = node
        else:
            ant.prox = node


    def atualiza_fila_espera(self):
        pointer = self.inicio
        while(pointer):
            pointer.process.lista_bust[pointer.process.pos_bust] -= 1
            pointer = pointer.prox


    def pop(self):
        self.inicio = self.inicio.prox
    

    def pop_fila_espera(self):
        process_retirados = []
        pointer = self.inicio
        ant = pointer
        while(pointer):
            if pointer.process.lista_bust[pointer.process.pos_bust] == 0:
                process_retirados.append(pointer.process)
                if self.inicio == pointer:
                    self.inicio = pointer.prox
                else:
                    ant.prox = pointer.prox
            
            ant = pointer
            pointer = pointer.prox
        
        return process_retirados
        


    def print_list(self, kind):
        pointer = self.inicio
        while(pointer):
            if kind == 'pronto':
                print(f'PID: {pointer.process.pid}, Nome: {pointer.process.nome}, Tempo de admissão: {pointer.process.tempo_admissao}, Prioridade: {pointer.process.prioridade}')
            elif kind == 'espera':
                print(f'PID: {pointer.process.pid}, Nome: {pointer.process.nome}, Tempo de admissão: {pointer.process.tempo_admissao}, Prioridade: {pointer.process.prioridade}, Tempo Restante IO: {pointer.process.lista_bust[pointer.process.pos_bust]}')
            else:
                print('Não foi especificado o tipo de fila.')

            pointer = pointer.prox
