import matplotlib.pyplot as plt

def gerar_grafico_recomendacao(recomendacoes):
    fig, ax = plt.subplots()
    categorias = ["Bom p/ Compra", "Ruim p/ Compra", "Bom p/ Venda", "Ruim p/ Venda"]
    valores = [recomendacoes.get(cat, 0) for cat in categorias]
    cores = ["green", "red", "blue", "orange"]

    ax.bar(categorias, valores, color=cores)
    ax.set_title("📈 Recomendação de Mercado")
    ax.set_ylabel("Pontuação")
    return fig
