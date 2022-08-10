"""
Funções de teste das funções contidas no arquivo backup.py
"""

import os
import shutil
from backup import arquivos_presente

def teste_arquivos_presente():
  """! Testa se existe uma lista de arquivos x's na pasta y.
    Para isso é criado uma pasta temporária (pendrive) com arquivos temporários.
  """

  pasta_teste = "./exemplos/pendrive"

  #Cria os arquivos teste
  os.mkdir(pasta_teste)

  with open(f"{pasta_teste}/arquivo1.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{pasta_teste}/arquivo2.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{pasta_teste}/arquivo3.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{pasta_teste}/arquivo4.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]
  assert arquivos_presente(pasta_teste, arquivos_teste) is True

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt"]
  assert arquivos_presente(pasta_teste, arquivos_teste) is True

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo5.txt"]
  assert arquivos_presente(pasta_teste, arquivos_teste) is False

  arquivos_teste = ["arquivo1.txt"]
  assert arquivos_presente(pasta_teste, arquivos_teste) is True

  arquivos_teste = ["arquivo6.txt"]
  assert arquivos_presente(pasta_teste, arquivos_teste) is False

  #Exclui a pasta teste
  shutil.rmtree(pasta_teste)
