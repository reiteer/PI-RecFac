import pandas as pd

def exportar_para_csv(dados, nome_arquivo='dados_reconhecimento_facial.csv'):
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False)
    print(f"Dados exportados com sucesso para {nome_arquivo}!")