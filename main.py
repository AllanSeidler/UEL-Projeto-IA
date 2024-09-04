from deck import Deck
from heuristic import *
from ia import Player
from ia import Dealer
from random import seed
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurações iniciais
seed(4)
NUMERO_DE_DECKS = 6
TOTAL_DE_RODADAS = 10000

# Lista de heurísticas
heuristics = [medrosa, corajosa, media, mediana, moda, dealer_falso, trapaceiro]

# Função para simular uma rodada
def rodada(player: Player, dealer: Dealer):
    player.start()
    dealer.start()
    ph = player.set_hand()  # mão do jogador
    dh = dealer.set_hand()  # mão do dealer
    
    dealer.clear_hand()
    player.clear_hand()

    if ph > dh:  # jogador vence
        return 1
    elif dh > ph:  # dealer vence
        return -1
    else:  # empate
        return 0

# Função para simular as rodadas
def simular_rodadas(player, dealer, deck):
    resultados = []
    vitorias, derrotas, empates = [], [], []

    for h in heuristics:  # passa por todas as heurísticas
        player.heuristic = h  # define a heurística atual
        resultado_heuristica = []
        vitoria, derrota, empate = 0, 0, 0
        
        for i in range(1, TOTAL_DE_RODADAS + 1):
            if deck.size < 52:
                deck.reset(NUMERO_DE_DECKS)
            r = rodada(player, dealer)
            
            if r == 1:
                vitoria += 1
            elif r == -1:
                derrota += 1
            else:
                empate += 1
            
            resultado_heuristica.append(r if i == 1 else resultado_heuristica[-1] + r)

        resultados.append(resultado_heuristica)
        vitorias.append(vitoria)
        derrotas.append(derrota)
        empates.append(empate)

    return resultados, vitorias, derrotas, empates

# Função para criar DataFrame com os resultados das rodadas
def criar_dataframe_resultados(resultados):
    df_resultados = pd.DataFrame(resultados, index=[h.__name__ for h in heuristics]).T
    return df_resultados

# Função para criar DataFrame com estatísticas de vitórias, derrotas e empates
def criar_dataframe_estatisticas(vitorias, derrotas, empates):
    df_vitorias_derrotas_empates = pd.DataFrame({
        'Vitórias': vitorias,
        'Derrotas': derrotas,
        'Empates': empates
    }, index=[h.__name__ for h in heuristics])
    return df_vitorias_derrotas_empates

# Função para plotar gráfico de linha
def plotar_grafico_linha(df_resultados):
    plt.figure(figsize=(14, 7))
    for heuristic in df_resultados.columns:
        plt.plot(df_resultados.index, df_resultados[heuristic], label=heuristic)
    plt.xlabel('Rodadas')
    plt.ylabel('Pontuação (Vitórias - Derrotas)')
    plt.title('Pontuação do Jogador ao Longo das Rodadas por Heurística')
    plt.xticks(np.arange(0, TOTAL_DE_RODADAS + 1, 1000))
    plt.legend()
    plt.grid(True)
    plt.show()

# Função para plotar gráfico de barras
def plotar_grafico_barras(df_vitorias_derrotas_empates):
    df_vitorias_derrotas_empates.plot(kind='bar', figsize=(14, 7))
    plt.xlabel('Heurística')
    plt.ylabel('Número de Ocorrências')
    plt.title('Vitórias, Derrotas e Empates por Heurística')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

if __name__ == '__main__':
    deck = Deck()
    dealer = Dealer(deck)
    player = Player(None, deck)

    # Simular as rodadas
    resultados, vitorias, derrotas, empates = simular_rodadas(player, dealer, deck)

    # Criar DataFrames
    df_resultados = criar_dataframe_resultados(resultados)
    df_vitorias_derrotas_empates = criar_dataframe_estatisticas(vitorias, derrotas, empates)

    # Plotar os gráficos
    plotar_grafico_linha(df_resultados)
    plotar_grafico_barras(df_vitorias_derrotas_empates)