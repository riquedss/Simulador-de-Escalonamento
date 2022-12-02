class Cpu:
    def __init__(self):
        self.programa = None
        self.tempo_exe = None
        self.quantums = [48, 24, 12, 6]


    def need_preempcao(self):
        if not self.programa:
            return False
        
        if self.tempo_exe == self.quantums[self.programa.prioridade_fila-1] and self.programa.lista_bust[self.programa.pos_bust] > 0:
            return True
        
        return False
    

    def need_call_system(self):
        if not self.programa:
            return False

        if self.programa.bust_atual and self.programa.lista_bust[self.programa.pos_bust] == 0:
            return True

        return False
    

    def atualiza_status_programa(self):
        if self.programa:
            self.tempo_exe += 1
            self.programa.lista_bust[self.programa.pos_bust] -= 1


    def tempo_restantes(self):
        return self.programa.lista_bust[self.programa.pos_bust]
        
        
        