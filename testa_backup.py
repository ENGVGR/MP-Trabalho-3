"""
Funções de teste das funções contidas no arquivo backup.py
"""

import os
import shutil
from backup import arquivos_presentes
from backup import datas_dos_arquivos

def teste_arquivos_presentes():
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
  assert arquivos_presentes(pasta_teste, arquivos_teste) is True

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) is True

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo5.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) is False

  arquivos_teste = ["arquivo1.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) is True

  arquivos_teste = ["arquivo6.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) is False

  #Exclui a pasta teste
  shutil.rmtree(pasta_teste)

def teste_datas_dos_arquivos():
  """! Testa se a função datas_dos_arquivos retorna a data do arquivo.
    Para isso é utilizado arquivos criados com datas fixas (não sofrerá
    alterações).
  """

  pasta_teste = "./exemplos/teste_datas"

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]
  #Datas no formato ano,mês,dia,hora,minuto,segundo
  datas = [[2022,10,8,11,30,10], [2022,10,8,11,30,15], [2022,10,8,11,30,21],
   [2022,10,8,11,30,26]]

  assert datas_dos_arquivos(pasta_teste, arquivos_teste) == datas

  assert datas_dos_arquivos(pasta_teste, arquivos_teste[2,3]) == datas[2,3]

  assert datas_dos_arquivos(pasta_teste, arquivos_teste[0,1]) == datas[0,1]
