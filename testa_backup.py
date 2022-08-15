"""
Funções de teste das funções contidas no arquivo backup.py
"""

import os
import shutil
import time
from backup import arquivos_presentes
from backup import datas_dos_arquivos
from backup import compara_datas
from backup import transfere_arquivos
from backup import executar

def teste_arquivos_presentes():
  """! Testa se existe uma lista de arquivos x's na pasta y.
    Para isso é criado uma pasta temporária (pendrive) com arquivos temporários.
  """

  pasta_teste = "./exemplos/pendrive"

  #Exclui a pasta teste (caso exista)
  if os.path.exists(pasta_teste):
    shutil.rmtree(pasta_teste)

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
  assert arquivos_presentes(pasta_teste, arquivos_teste) == [True, True, True,
   True]

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) == [True, True]

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo5.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) == [True, True, True,
   False]

  arquivos_teste = ["arquivo1.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) == [True]

  arquivos_teste = ["arquivo6.txt"]
  assert arquivos_presentes(pasta_teste, arquivos_teste) == [False]

  #Exclui a pasta teste
  if os.path.exists(pasta_teste):
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
  pasta_teste = "./exemplos/teste_datas"

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]

  datas_pasta1 = datas_dos_arquivos(pasta_teste, arquivos_teste)

  datas_pasta2 = [[2022,8,10,11,30,10], [2023,8,10,11,30,15],
  [2022,8,10,11,30,20], [2022,8,10,11,40,26]]

  #Opções de saída:
  saida1 = "Primeiro é mais recente"
  saida2 = "Segundo é mais recente"
  saida3 = "As datas são iguais"

  assert compara_datas(datas_pasta1, datas_pasta2) == [saida3, saida2,
  saida1, saida2]

def teste_transfere_arquivos():

  pasta_destino_teste = "./exemplos/pendrive"
  pasta_origem_teste = "./exemplos/hd"

  #Exclui a pasta teste (caso exista)
  if os.path.exists(pasta_destino_teste):
    shutil.rmtree(pasta_destino_teste)
  if os.path.exists(pasta_origem_teste):
    shutil.rmtree(pasta_origem_teste)

  #Cria a pasta de teste
  os.mkdir(pasta_destino_teste)
  os.mkdir(pasta_origem_teste)

  with open(f"{pasta_origem_teste}/arquivo1.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{pasta_origem_teste}/arquivo2.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{pasta_origem_teste}/arquivo3.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{pasta_origem_teste}/arquivo4.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]

  transfere_arquivos(arquivos_teste, pasta_origem_teste, pasta_destino_teste)
  assert arquivos_presentes(pasta_destino_teste, arquivos_teste) == [True, True, True,
   True]

  #Recria a pasta destino para realizar outros testes
  if os.path.exists(pasta_destino_teste):
    shutil.rmtree(pasta_destino_teste)
  os.mkdir(pasta_destino_teste)

  transfere_arquivos(arquivos_teste[0:2], pasta_origem_teste, pasta_destino_teste)
  assert arquivos_presentes(pasta_destino_teste, arquivos_teste[0:2]) == [True, True]

  #Recria a pasta destino para realizar outros testes
  if os.path.exists(pasta_destino_teste):
    shutil.rmtree(pasta_destino_teste)
  os.mkdir(pasta_destino_teste)

  transfere_arquivos(arquivos_teste[2:4], pasta_origem_teste, pasta_destino_teste)
  assert arquivos_presentes(pasta_destino_teste, arquivos_teste[2:4]) == [True, True]

  #Exclui a pasta teste (caso exista)
  if os.path.exists(pasta_destino_teste):
    shutil.rmtree(pasta_destino_teste)
  if os.path.exists(pasta_origem_teste):
    shutil.rmtree(pasta_origem_teste)

def teste_executar():
  pendrive_teste = "./exemplos/pendrive"
  hd_teste = "./exemplos/hd"
  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]

  #Exclui as pastas testes (caso exista)
  if os.path.exists(pendrive_teste):
    shutil.rmtree(pendrive_teste)
  if os.path.exists(hd_teste):
    shutil.rmtree(hd_teste)

  #Cria a pasta de teste
  os.mkdir(pendrive_teste)
  os.mkdir(hd_teste)

  with open(f"{hd_teste}/arquivo1.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{hd_teste}/arquivo2.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{hd_teste}/arquivo3.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  with open(f"{hd_teste}/arquivo4.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  #Teste 1 - Não possui o parâmetro Backup
  assert executar(None, hd_teste, pendrive_teste, arquivos_teste) == "Impossível - Não contem o parâmetro Backup"

  #Teste 2 - Arquivos estão apenas no hd e é backup
  executar( True, hd_teste, pendrive_teste, arquivos_teste)
  assert arquivos_presentes(pendrive_teste, arquivos_teste) == [True, True, True, True]

  #Recria a pasta pendrive para novos testes
  if os.path.exists(pendrive_teste):
    shutil.rmtree(pendrive_teste)
  os.mkdir(pendrive_teste)

  with open(f"{pendrive_teste}/arquivo5.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  executar( True, hd_teste, pendrive_teste, arquivos_teste)
  assert arquivos_presentes(pendrive_teste, arquivos_teste) == [True, True, True, True]

  #Teste 3 - Arquivos estão no hd e pendrive, mas a data do hd é mais recente
  #Recria a pasta pendrive para novos testes
  if os.path.exists(pendrive_teste):
    shutil.rmtree(pendrive_teste)
  os.mkdir(pendrive_teste)

  with open(f"{pendrive_teste}/arquivo5.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  time.sleep(1.1)
  with open(f"{hd_teste}/arquivo5.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  arquivos_teste.append("arquivo5.txt")
  data_hd = datas_dos_arquivos(hd_teste, ["arquivo5.txt"])
  data_pendrive = datas_dos_arquivos(pendrive_teste, ["arquivo5.txt"])
  assert compara_datas(data_hd, data_pendrive)[0] == "Primeiro é mais recente"

  time.sleep(1.1)
  executar( True, hd_teste, pendrive_teste, arquivos_teste)
  data_hd = datas_dos_arquivos(hd_teste, ["arquivo5.txt"])
  data_pendrive = datas_dos_arquivos(pendrive_teste, ["arquivo5.txt"])
  assert compara_datas(data_hd, data_pendrive)[0] == "Segundo é mais recente"

  assert arquivos_presentes(pendrive_teste, arquivos_teste) == [True, True, True, True, True]


  #Recria a pasta pendrive para novos testes
  if os.path.exists(pendrive_teste):
    shutil.rmtree(pendrive_teste)
  os.mkdir(pendrive_teste)

  with open(f"{pendrive_teste}/arquivo6.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()
  with open(f"{pendrive_teste}/arquivo7.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  time.sleep(1.1)
  with open(f"{hd_teste}/arquivo6.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()
  with open(f"{hd_teste}/arquivo7.txt", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()

  arquivos_teste.append("arquivo6.txt")
  arquivos_teste.append("arquivo7.txt")
  datas_hd = datas_dos_arquivos(hd_teste, ["arquivo6.txt", "arquivo7.txt"])
  datas_pendrive = datas_dos_arquivos(pendrive_teste, ["arquivo6.txt", "arquivo7.txt"])
  assert compara_datas(datas_hd, datas_pendrive) == ["Primeiro é mais recente", "Primeiro é mais recente"]

  time.sleep(1.1)
  executar( True, hd_teste, pendrive_teste, arquivos_teste)
  datas_hd = datas_dos_arquivos(hd_teste, ["arquivo6.txt", "arquivo7.txt"])
  datas_pendrive = datas_dos_arquivos(pendrive_teste, ["arquivo6.txt", "arquivo7.txt"])
  assert compara_datas(datas_hd, datas_pendrive) == ["Segundo é mais recente", "Segundo é mais recente"]
  assert arquivos_presentes(pendrive_teste, arquivos_teste) == [True, True, True, True, True, True, True]


  #Exclui as pastas testes (caso exista)
  if os.path.exists(pendrive_teste):
    shutil.rmtree(pendrive_teste)
  if os.path.exists(hd_teste):
    shutil.rmtree(hd_teste)
