"""
Funções de teste das funções contidas no arquivo backup.py
"""

import os
import shutil
from backup import arquivos_presentes
from backup import datas_dos_arquivos
from backup import compara_datas

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
  datas = [[2022,8,10,11,30,10], [2022,8,10,11,30,15], [2022,8,10,11,30,21],
   [2022,8,10,11,30,26]]

  assert datas_dos_arquivos(pasta_teste, arquivos_teste) == datas

  assert datas_dos_arquivos(pasta_teste, arquivos_teste[2:3]) == datas[2:3]

  assert datas_dos_arquivos(pasta_teste, arquivos_teste[0:1]) == datas[0:1]

def teste_compara_datas():
  datas_pasta1 = [[2022,8,10,11,30,10], [2022,8,10,11,30,15],
  [2022,8,10,11,30,21], [2022,8,10,10,30,26]]

  datas_pasta2 = [[2022,8,10,11,30,10], [2023,8,10,11,30,15],
  [2022,8,10,11,30,20], [2022,8,10,11,40,26]]

  #Opções de saída:
  saida1 = "Primeiro é mais recente"
  saida2 = "Segundo é mais recente"
  saida3 = "As datas são iguais"

  assert compara_datas(datas_pasta1, datas_pasta2) == [saida3, saida2,
  saida1, saida2]
