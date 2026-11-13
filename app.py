import json

ALLOWED = ["saldo", "transferencia", "deposito"]

MSG = "Desculpe, posso auxiliar apenas com saldo, transferência e depósito."

def processar(texto):
    texto = texto.lower()

    if "saldo" in texto:
        return {"operacao": "saldo"}

    if "transfer" in texto:
        return {"operacao": "transferencia"}

    if "deposit" in texto:
        return {"operacao": "deposito"}

    return MSG

if __name__ == "__main__":
    while True:
        entrada = input('Usuário: ')
        print(json.dumps(processar(entrada), ensure_ascii=False, indent=2) if isinstance(processar(entrada), dict) else processar(entrada))
