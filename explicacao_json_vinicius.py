'''
arquivos .txt
arquivos .csv
arquivoa .json

app, lista os projetos e exibir os projetos pode ser excluidos

'''

import os
import json

def configura_sistema():
    if not os. path.exists("uploads_projetos"):
      os.makedirs("uploads_projetos")

def listar_projetos():
   arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
   print("\n" + '$' *40)
   print("    PROJETOS EXIBIDOS")
   print("$"*40)

   if not arquivos:
      print("Nenhum projeto encontrado")
      return []
   for i, arquivos in enumerate(arquivos, 1):
       nome_exibicao = arquivos.replace("projeto_," "").replace(".json", "").replace("_", "")
       print(f"{i}. {nome_exibicao.title()}")

   return arquivos

def gereciar_projeto():
   
   arquivos = listar_projetos()
   if not arquivos: return
   escolha = int(input('\nEscolha o número do projeto para gerenciar(ou 0 para voltar)'))
   if escolha == 0:return

   nome_arquivo = arquivos[escolha - 1]
   caminho = f"uploads_projetos/{nome_arquivo}"

   with open(caminho, "r, encording="utf-8") as f:
             dados = json.load(f)

   print('f\n--- Dados Atuais ---')
   print(f"Aluno : {dados['aluno']}")
   print(f"Projeto: {dados['projeto']}")

   confirmar = input("\nDeseja alterar as informações deste projeto? (s/n):").lower()
   if confirmar == 's':
    dados['aluno'] = input (f"Novo nome [{dados['aluno']}]: ") or dados['aluno']
    dados['projeto'] = input (f"Novo resumo: ") or dados['projeto']

    #3 sobrescrever (Modo 'w')

    with open(caminho, 'w' , encoding=utf-8")