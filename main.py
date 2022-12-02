from list import List
from process import Process
from pcb import Pcb
from cpu import Cpu
from sistema import Sistema


def maior_tempo_admissao():
    with open('processos.in', 'r') as arquivo:
        maior_tempo_admissao = -1
        for linha in arquivo:
            tempo_admissao = int(linha.split(' ')[0])
            if tempo_admissao > maior_tempo_admissao:
                maior_tempo_admissao = tempo_admissao
        
        return maior_tempo_admissao


def loader(time, fila_pronto, pcb):
    with open('processos.in', 'r') as arquivo:
        for linha in arquivo:
            processo = linha.split(' ')
            tempo_admissao = int(processo[0])
            if tempo_admissao == time:
                nome_programa = processo[1]
                prioridade = int(processo[2])
                lista_bust = list(map(int, processo[3:len(processo)]))
                
                fila_pronto.push(Process(pcb.pid, tempo_admissao, nome_programa, prioridade, lista_bust))
                pcb.pid += 1

        return [fila_pronto, pcb]


def process_exe(cpu):
    if cpu.programa:
        print(f'Processo em Execução - PID: {cpu.programa.pid}, Nome: {cpu.programa.nome}, Prioridade: {cpu.programa.prioridade}, Tempo restante: {cpu.tempo_restantes()}')

def age(cpu):
    if cpu.programa:
        return cpu.programa.prioridade_fila


pcb = Pcb()
cpu = Cpu()
fila_pronto = List()
fila_espera = List()

tempo_corrente = 0
while tempo_corrente <= maior_tempo_admissao() or cpu.programa or fila_espera.inicio:
    fila_pronto, pcb = loader(tempo_corrente, fila_pronto, pcb)
    cpu, fila_pronto, fila_espera = Sistema.escalonador(cpu, fila_pronto, fila_espera)

    print(f'Tempo corrente: {tempo_corrente}, age: {age(cpu)}')
    process_exe(cpu)
    print('Fila de pronto')
    fila_pronto.print_list('pronto')
    print('Fila de espera')
    fila_espera.print_list('espera')
    print('______________________________________________________________')

    tempo_corrente += 1
    cpu.atualiza_status_programa()
    fila_espera.atualiza_fila_espera()

