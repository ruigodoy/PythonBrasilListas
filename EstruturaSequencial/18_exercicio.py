# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

def calcule_tempo_minutos(tamanho_arquivo, velocidade_internet):
    return (tamanho_arquivo / velocidade_internet) / 60


tamanho_arquivo = float(input('Digite o Tamnho do Arquivo(MB):'))

velocidade_internet = float(input('Digite a velocidade da internet(MBPs): '))

tempo = calcule_tempo_minutos(tamanho_arquivo, velocidade_internet)

print(f'o Download irá demorar: {tempo:.2f} minutos')
