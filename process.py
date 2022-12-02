class Process:
    def __init__(self, pid, tempo_admissao, nome, prioridade, lista_bust):
        self.pid = pid
        self.tempo_admissao = tempo_admissao
        self.nome = nome
        self.prioridade = prioridade
        self.prioridade_fila = 4
        self.lista_bust = lista_bust
        self.pos_bust = len(self.lista_bust) - 1
        self.bust_atual = True # true para Cpu e false para I/O
