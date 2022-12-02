from process import Process


class Sistema:
    def escalonador(cpu, fila_pronto, fila_espera):
        Sistema.end_process(cpu)
        Sistema.conclusao_espera(fila_pronto, fila_espera)

        if not cpu.programa:
            Sistema.escalonamento(cpu, fila_pronto)
        elif cpu.need_call_system():
            Sistema.call_system(cpu, fila_espera, fila_pronto)
        elif cpu.need_preempcao():
            Sistema.preempcao(cpu, fila_pronto)
        
        return [cpu, fila_pronto, fila_espera]
            

    def escalonamento(cpu, fila_pronto):
        if fila_pronto.inicio:
            cpu.programa = fila_pronto.inicio.process
            cpu.tempo_exe = 0
            fila_pronto.pop()
        else:
            cpu.programa = None


    def preempcao(cpu, fila_pronto):
        programa = cpu.programa
        if programa.prioridade_fila > 1:
            programa.prioridade_fila -= 1

        fila_pronto.push(programa)

        Sistema.escalonamento(cpu, fila_pronto)

        print("\n->Preempção\n")


    def call_system(cpu, fila_espera, fila_pronto):
        programa = cpu.programa
        programa.pos_bust -= 1
        programa.bust_atual = False
        if programa.prioridade_fila > 1:
            programa.prioridade_fila -= 1

        fila_espera.add(programa)

        Sistema.escalonamento(cpu, fila_pronto)

        print("\n->Call system\n")


    def conclusao_espera(fila_pronto, fila_espera):
        processes = fila_espera.pop_fila_espera()

        for process in processes:
            process.pos_bust -= 1
            process.bust_atual = True
            fila_pronto.push(process)


    def end_process(cpu):
        if cpu.programa and cpu.programa.lista_bust[0] == 0:
            print(f'Processo finalizado - PID: {cpu.programa.pid}, Nome: {cpu.programa.nome}')
            cpu.programa = None

            print("\n->Finish\n")
         