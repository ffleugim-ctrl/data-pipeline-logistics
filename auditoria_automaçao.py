import pandas as pd

import numpy as np





SEU_SHEET_ID = "1d2FDl84KxzV6M_RQi9Wu4uiCSUSteadEP1Oxkmc6sD4"



# Linha 6: Agora sim a f-string vai ler a variável perfeitamente

url_integracao = f"https://docs.google.com/spreadsheets/d/{SEU_SHEET_ID}/export?format=csv"





df_cajamar = pd.read_csv(url_integracao)



# =========================================================================

# MÓDULO DE AUDITORIA: ALERTA DE DADOS SUJOS

# =========================================================================



print("=" * 60)

print("🚨 ALERTA DE QUALIDADE DE DADOS: OPERAÇÃO CAJAMAR 🚨")

print("=" * 60)

print(f"📊 Total de linhas brutas importadas: {len(df_cajamar):,}")

print("-" * 60)





total_duplicados = df_cajamar.duplicated().sum()

nulos_por_coluna = df_cajamar.isnull().sum()

total_nulos = nulos_por_coluna.sum()



 Inconsistências de Texto no Setor (letras minúsculas ou espaços em branco)



setores_fora_padrao = df_cajamar[~df_cajamar['Setor'].isin(['DV', 'RESSUBIDO'])].shape[0]



contagens_bizzaras = df_cajamar[(df_cajamar['Pecas_Processadas'] == 99999) | (df_cajamar['Pecas_Processadas'] < 0)].shape[0]



 Erros de Cronômetro (Tempo zerado ou negativo)

tempo_invalido = df_cajamar[df_cajamar['Tempo_Segundos'] <= 0].shape[0]





# --- EXIBIÇÃO DO DIAGNÓSTICO ---

print(f"👥 Linhas 100% duplicadas encontradas: {total_duplicados:,}")

print(f"🕳️ Total de campos vazios (NaN): {total_nulos:,}")

for coluna, qtd in nulos_por_coluna.items():

    if qtd > 0:

        print(f"   ↳ Coluna '{coluna}': {qtd:,} nulos")



print(f"🔤 Setores com erro de digitação/caixa: {setores_fora_padrao:,}")

print(f"📦 Bips com quantidades impossíveis (<0 ou 99999): {contagens_bizzaras:,}")

print(f"⏱️ Registros com tempo inválido (<= 0s): {tempo_invalido:,}")



print("=" * 60)

if total_duplicados > 0 or total_nulos > 0 or contagens_bizzaras > 0:

    print("⚠️ STATUS: BASE INADEQUADA PARA DASHBOARD! Inicializando limpeza...")

else:

    print("✅ STATUS: BASE LIMPA! Pronta para processamento.")

print("=" * 60)
