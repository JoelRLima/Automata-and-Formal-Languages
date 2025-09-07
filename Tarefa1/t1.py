#eventos de entrada I={0,1,...,ni}
#eventos de saída O={0,1,...,no}
#estados {0,1,...ns}
#Tabela de transição de estados TE linhas representam estados e colunas o prox estado
#Vetor de saída VS

def criar_maquina(TE,VS):
    return {
        "TE": TE,
        "VS": VS,
        "ns": len(TE) - 1,
        "ni": len(TE[0]) - 1,
        "no": len(VS) - 1,
        "estado": 0
    }
def processar_entrada(maquina,entrada):
    if entrada == "r":
        maquina['estado'] = 0
        print("Resetado para o estado inicial (0)")
    elif entrada.isdigit():
        valor = int(entrada)
        if 0 <= valor <= maquina['ni']:
            novo_estado = maquina['TE'][maquina['estado']][valor]
            print(f"Estado Atual: {maquina['estado']} | Novo estado: {novo_estado} | saida: {maquina['VS'][novo_estado]} ")
            maquina['estado'] = novo_estado
        else:
            print("Entrada fora do intervalo válido")
    else:
        print("Entrada inválida")

maquina1 = criar_maquina(
    [
        [0,1,2],
        [2,1,0],
        [2,0,1]
    ],
    [0,1,2]
)
maquina_exemplo1 = criar_maquina(
    #Essa é a maquina de exemplo dada
    [
        [1,0], 
        [2,1],
        [2,0]
    ],
    [0,1,1]
)

while(1):
    maquina = maquina_exemplo1
    entrada = input(f"Digite um numero entre 0 e {maquina['ni']}: ")
    if entrada == "q":
        break
    processar_entrada(maquina,entrada)