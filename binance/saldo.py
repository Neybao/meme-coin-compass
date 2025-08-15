def mostrar_saldo(exchange):
    saldo = exchange.fetch_balance()
    ativos = {moeda: valor for moeda, valor in saldo['total'].items() if valor > 0}
    return ativos
def obter_saldo_usuario(usuario):
    # Exemplo fictício
    return {
        "bitcoin": 0.05,
        "ethereum": 1.2,
        "solana": 15,
        "BRL": 5000
    }
