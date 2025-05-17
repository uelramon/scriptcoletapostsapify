#!/usr/bin/env python
# coding: utf-8

# 🧠 Script Python para Coleta com Apify

# In[6]:


import pandas as pd
import os
import time
import random
from datetime import datetime, timedelta
from apify_client import ApifyClient

# === CONFIGURAÇÕES GERAIS ===

# Token da Apify (inserido diretamente)
apify_token = "aaaaaaaaaaaa"  # 🔁 Substitua aqui pelo seu token real

client = ApifyClient(apify_token)

# === COOKIE DE SESSÃO DO INSTAGRAM ===

# 👇 Cole aqui o valor do seu sessionId (entre aspas)
session_id = "aaaaaaaaa" # 👈 COLE AQUI o valor do seu sessionId

# Caminho para planilha de entrada
CAMINHO_CONTAS = "contas_instagram.xlsx"

# Saídas
ARQUIVO_DADOS = "dados_instagram.xlsx"
ARQUIVO_ERROS = "erros_coleta.xlsx"
ARQUIVO_RESUMO = "resumo_coleta.xlsx"

# Limites
LIMITE_POSTS = 10
LIMITE_DIAS = 15

# === LÊ AS CONTAS ===
try:
    df_contas = pd.read_excel(CAMINHO_CONTAS)
    contas = df_contas["Contas"].dropna().astype(str).tolist()
except Exception as e:
    raise Exception(f"Erro ao carregar planilha de contas: {e}")

# === INICIALIZA APIFY CLIENT ===

dados_posts = []
erros = []
resumo = []

# === LOOP DE COLETA ===

for conta in contas:
    print(f"🔍 Coletando @{conta}...")

    try:
        run_input = {
            "directUrls": [f"https://www.instagram.com/{conta}/"],
            "resultsType": "posts",
            "resultsLimit": LIMITE_POSTS,
            "searchType": "hashtag",
            "onlyPostsNewerThan": f"{LIMITE_DIAS} days",
            "addParentData": False,
            "enhanceUserSearchWithFacebookPage": False,
            "isUserReelFeedURL": False,
            "isUserTaggedFeedURL": False,
        }

        print(f"📤 Enviando para o actor: {run_input}")
        run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

        # ✅ Aguarda finalização
        while True:
            run = client.run(run["id"]).get()
            if run["status"] in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
                break
            print("⏳ Aguardando finalização do ator...")
            time.sleep(5)

        items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
        print(f"🔎 {len(items)} itens retornados da Apify")

        posts_selecionados = items[:LIMITE_POSTS]
        dados_posts.extend(posts_selecionados)
        resumo.append({"conta": conta, "posts_coletados": len(posts_selecionados)})

        print(f"✅ {len(posts_selecionados)} posts coletados.")

    except Exception as e:
        erros.append({"conta": conta, "erro": str(e)})
        print(f"❌ Erro na conta {conta}: {e}")
        resumo.append({"conta": conta, "posts_coletados": 0})

    time.sleep(random.uniform(1.5, 3.5))

# === EXPORTAÇÃO DOS RESULTADOS ===

# Dados principais
df_dados = pd.DataFrame(dados_posts)
if not df_dados.empty:
    df_dados.to_excel(ARQUIVO_DADOS, index=False)
    print(f"💾 Dados salvos em: {ARQUIVO_DADOS}")
else:
    print("⚠️ Nenhum post coletado.")

# Erros
if erros:
    pd.DataFrame(erros).to_excel(ARQUIVO_ERROS, index=False)
    print(f"⚠️ Erros salvos em: {ARQUIVO_ERROS}")

# Resumo
df_resumo = pd.DataFrame(resumo)
df_resumo.to_excel(ARQUIVO_RESUMO, index=False)
print(f"📄 Resumo salvo em: {ARQUIVO_RESUMO}")

# Exibe resumo no terminal
print("\n📌 Resumo da coleta por conta:")
print(df_resumo.to_string(index=False))
print(f"📊 Total geral de posts coletados: {df_resumo['posts_coletados'].sum()}")

