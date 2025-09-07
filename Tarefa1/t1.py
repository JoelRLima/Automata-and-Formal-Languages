#eventos de entrada I={0,1,...,ni}
#eventos de saída O={0,1,...,no}
#estados {0,1,...ns}
#Tabela de transição de estados TE linhas representam estados e colunas o prox estado
#Vetor de saída VS

class MaquinaEstados:
    def __init__(self,TE,VS):
        self.TE = TE
        self.VS = VS
        self.ns = len(TE) - 1
        self.ni = len(TE[0]) - 1
        self.no = len(VS) - 1
        self.estado = 0
    def processar_entrada(self,entrada):
        if entrada == "r":
            self.estado = 0
            print("Resetado para o estado inicial (0)")
        elif entrada.isdigit():
            valor = int(entrada)
            if 0 <= valor <= self.ni:
                novo_estado = self.TE[self.estado][valor]
                print(f"Estado Atual: {self.estado} | Novo estado: {novo_estado} | saida: {self.VS[novo_estado]} ")
                self.estado = novo_estado
            else:
                print("Entrada fora do intervalo válido")
        else:
            print("Entrada inválida")

maquina1 = MaquinaEstados(
    [
        [0,1,2],
        [2,1,0],
        [2,0,1]
    ],
    [0,1,2]
)
maquina_exemplo1 = MaquinaEstados(
    #Essa é a maquina de exemplo dada
    [
        [1,0], 
        [2,1],
        [2,0]
    ],
    [0,1,1]
)

escolha = input("Escolha a maquina(1 ou 2): ")
maquina = maquina1 if escolha == "1" else maquina_exemplo1
print(f"Máquina escolhida: {escolha} | Estados: {maquina.ns+1}")
while(1):
    entrada = input(f"Digite um numero entre 0 e {maquina.ni}: ")
    if entrada == "q":
        break
    maquina.processar_entrada(entrada)