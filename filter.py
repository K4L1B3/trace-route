import pandas as pd

def filter_energia_gas(df):
    df_filtered = df[
        df['Ramo de Atividade']
        .str
        .contains('energia|gás', case=False, na=False)
    ]
    return df_filtered
