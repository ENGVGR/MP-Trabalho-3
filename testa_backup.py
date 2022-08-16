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
  """! Testa se existe uma lista de arquivos no pendrive.
  Para isso é criado uma pasta temporária (pendrive) com arquivos temporários.
  """

  pendrive = "./exemplos/pendrive"
  arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt", "arquivo5.txt"]

  #Cria o arquivo teste
  criar_pasta(pendrive)

  criar_arquivo(pendrive, arquivos[0])
  criar_arquivo(pendrive, arquivos[1])
  criar_arquivo(pendrive, arquivos[2])
  criar_arquivo(pendrive, arquivos[3])

  assert arquivos_presentes(pendrive, arquivos) == [True, True, True,
   True, False]

  assert arquivos_presentes(pendrive, arquivos[0:2]) == [True, True]

  assert arquivos_presentes(pendrive, arquivos[0:3] + [arquivos[4]]) == [True,
   True, True, False]

  assert arquivos_presentes(pendrive, arquivos[0:1]) == [True]

  assert arquivos_presentes(pendrive, [arquivos[4]]) == [False]

  #Exclui a pasta testada
  if os.path.exists(pendrive):
    shutil.rmtree(pendrive)

def teste_datas_dos_arquivos():
  """! Testa se a função datas_dos_arquivos retorna a data do arquivo.
  Para isso é utilizado arquivos criados com datas fixas (não sofrerá
    alterações).
  """

  pendrive = "./exemplos/teste_datas"

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]
  #Datas no formato ano,mês,dia,hora,minuto,segundo
  datas = [[2022,8,10,11,30,10], [2022,8,10,11,30,15], [2022,8,10,11,30,21],
   [2022,8,10,11,30,26]]

  assert datas_dos_arquivos(pendrive, arquivos_teste) == datas

  assert datas_dos_arquivos(pendrive, arquivos_teste[2:3]) == datas[2:3]

  assert datas_dos_arquivos(pendrive, arquivos_teste[0:1]) == datas[0:1]

def teste_compara_datas():
  """! Testa se a função compara_datas retorna qual a data mais recente.
  Para isso é utilizado arquivos criados com datas fixas (não sofrerá
    alterações).
  """
  pasta_teste = "./exemplos/teste_datas"

  arquivos_teste = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]

  datas_pasta1 = datas_dos_arquivos(pasta_teste, arquivos_teste)

  datas_pasta2 = [[2022,8,10,11,30,10], [2023,8,10,11,30,15],
  [2022,8,10,11,30,20], [2022,8,10,11,40,26]]

  #Opções de saída:
  primeiro = "Primeiro é mais recente"
  segundo = "Segundo é mais recente"
  iguais = "As datas são iguais"

  assert compara_datas(datas_pasta1, datas_pasta2) == [iguais, segundo,
  primeiro, segundo]

def teste_transfere_arquivos():
  """! Testa se a função transfere_arquivos realiza a transferencia de
    arquivos.
  Para isso são criadas pastas temporárias (pendrive e hd).
  """

  pendrive = "./exemplos/pendrive"
  hd = "./exemplos/hd"
  arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt"]

  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(hd, arquivos[0])
  criar_arquivo(hd, arquivos[1])
  criar_arquivo(hd, arquivos[2])
  criar_arquivo(hd, arquivos[3])

  transfere_arquivos(arquivos, hd, pendrive)
  assert arquivos_presentes(pendrive, arquivos) == [True, True, True,
   True]

  #Recria a pasta pendrive para realizar outros testes
  criar_pasta(pendrive)

  transfere_arquivos(arquivos[0:2], hd, pendrive)
  assert arquivos_presentes(pendrive, arquivos[0:2]) == [True, True]

  #Recria a pasta pendrive para realizar outros testes
  criar_pasta(pendrive)

  transfere_arquivos(arquivos[2:4], hd, pendrive)
  assert arquivos_presentes(pendrive, arquivos[2:4]) == [True, True]

  #Exclui a pasta teste (caso exista)
  if os.path.exists(pendrive):
    shutil.rmtree(pendrive)
  if os.path.exists(hd):
    shutil.rmtree(hd)

def teste_executar():
  """! Testa a execução do programa.
  Para isso, é testado cada coluna da tabela de testes
    fornecida.
  """
  pendrive = "./exemplos/pendrive"
  hd = "./exemplos/hd"
  arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt",
  "arquivo4.txt", "arquivo5.txt"]

  #Opções de saída:
  primeiro = "Primeiro é mais recente"
  segundo = "Segundo é mais recente"
  iguais = "As datas são iguais"

  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(hd, arquivos[0])
  criar_arquivo(hd, arquivos[1])
  criar_arquivo(hd, arquivos[2])
  criar_arquivo(hd, arquivos[3])
  criar_arquivo(hd, arquivos[4])

  #Teste 1 - Não possui o parâmetro Backup
  erro = "Impossível - Não contem o parâmetro Backup"
  assert executar(None, hd, pendrive, arquivos) == erro

  #Teste 2 - Arquivos estão apenas no hd e é backup
  executar( True, hd, pendrive, arquivos)

  arq_presentes = [True, True, True, True, True]
  assert arquivos_presentes(pendrive, arquivos) == arq_presentes

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)

  criar_arquivo(pendrive, arquivos[4])

  executar(True, hd, pendrive, arquivos)

  arq_presentes = [True, True, True, True, True]
  assert arquivos_presentes(pendrive, arquivos) == arq_presentes

  #Teste 3 - Arquivos estão no hd e pendrive, mas a data do hd é mais recente
  # e é backup

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(pendrive, arquivos[0])

  time.sleep(1.1)
  criar_arquivo(hd, arquivos[0])

  data_hd = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive = datas_dos_arquivos(pendrive, [arquivos[0]])
  assert compara_datas(data_hd, data_pendrive)[0] == primeiro

  time.sleep(1.1)
  executar(True, hd, pendrive, [arquivos[0]])

  data_hd = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd, data_pendrive)[0] == segundo

  assert arquivos_presentes(pendrive, [arquivos[0]]) == [True]

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(pendrive, arquivos[0])
  criar_arquivo(pendrive, arquivos[1])

  time.sleep(1.1)
  criar_arquivo(hd, arquivos[0])
  criar_arquivo(hd, arquivos[1])

  datas_hd = datas_dos_arquivos(hd, arquivos[0:2])
  datas_pendrive = datas_dos_arquivos(pendrive, arquivos[0:2])

  assert compara_datas(datas_hd, datas_pendrive) == [primeiro, primeiro]

  time.sleep(1.1)
  executar(True, hd, pendrive, arquivos[0:2])

  datas_hd = datas_dos_arquivos(hd, arquivos[0:2])
  datas_pendrive = datas_dos_arquivos(pendrive, arquivos[0:2])

  assert compara_datas(datas_hd, datas_pendrive) == [segundo, segundo]

  assert arquivos_presentes(pendrive, arquivos[0:2]) == [True, True]

  #Teste 4 - Arquivos estão no hd e pendrive e a data dos arquivos são iguais
  # e é backup

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(pendrive, arquivos[0])
  criar_arquivo(hd, arquivos[0])

  data_hd = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd, data_pendrive)[0] == iguais

  time.sleep(1.1)
  executar(True, hd, pendrive, [arquivos[0]])

  data_hd = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd, data_pendrive)[0] == iguais

  assert arquivos_presentes(pendrive, [arquivos[0]]) == [True]

  #Teste 5 - Arquivos estão no hd e pendrive, mas a
  # data do pendrive é mais recente e é backup

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(hd, arquivos[0])

  time.sleep(1.1)
  criar_arquivo(pendrive, arquivos[0])

  data_hd = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive_antes = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd, data_pendrive_antes)[0] == segundo

  erro = "Erro: Arquivos do pendrive já são os mais recentes"
  assert executar(True, hd, pendrive, [arquivos[0]]) == erro

  #Teste 6 - Arquivos estão apenas no hd e é para transferir do pendrive para hd

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(hd, arquivos[0])
  criar_arquivo(hd, arquivos[1])
  criar_arquivo(hd, arquivos[2])

  erro = "Erro: Não foram encontrados os arquivos no pendrive"
  assert executar(False, hd, pendrive, arquivos[0:3]) == erro

  #Teste 7 - Arquivos estão no hd e pendrive, mas a data do hd é mais recente
  # e é para transferir do pendrive para hd

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(pendrive, arquivos[0])

  time.sleep(1.1)
  criar_arquivo(hd, arquivos[0])

  data_hd = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive_antes = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd, data_pendrive_antes)[0] == primeiro

  erro = "Erro: Arquivos do hd já são os mais recentes"
  assert executar( False, hd, pendrive, [arquivos[0]]) == erro

  #Teste 8 - Arquivos estão no hd e pendrive e a data dos arquivos são iguais
  # e é para transferir do pendrive para hd

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(pendrive, arquivos[0])
  criar_arquivo(hd, arquivos[0])

  data_hd_antes = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive_antes = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd_antes, data_pendrive_antes)[0] == iguais

  time.sleep(1.1)
  executar( False, hd, pendrive, [arquivos[0]])

  data_hd_depois = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive_depois = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert data_hd_antes == data_hd_depois

  assert data_pendrive_antes == data_pendrive_depois

  assert compara_datas(data_hd_depois, data_pendrive_depois)[0] == iguais

  assert arquivos_presentes(pendrive, [arquivos[0]]) == [True]

  #Teste 9 - Arquivos estão no hd e pendrive e
  # a data do pendrive é a mais recente
  # e é para transferir do pendrive para hd

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(hd, arquivos[0])

  time.sleep(1.1)
  criar_arquivo(pendrive, arquivos[0])

  data_hd_antes = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive_antes = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd_antes, data_pendrive_antes)[0] == segundo

  time.sleep(1.1)
  executar( False, hd, pendrive, [arquivos[0]])

  data_hd_depois = datas_dos_arquivos(hd, [arquivos[0]])
  data_pendrive_depois = datas_dos_arquivos(pendrive, [arquivos[0]])

  assert compara_datas(data_hd_depois, data_hd_antes)[0] == primeiro

  assert compara_datas(data_pendrive_antes, data_pendrive_depois)[0] == iguais

  assert arquivos_presentes(pendrive, [arquivos[0]]) == [True]

  #Teste 10 - Arquivos não estão no hd e nem no pendrive
  # e é backup

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  erro = "Erro: Os arquivos não existem no Hd e no pendrive"
  assert executar( True, hd, pendrive, [arquivos[0]]) == erro

  #Teste 11 - Arquivos esta apenas no pendrive e é backup

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(pendrive, arquivos[0])

  executar(True, hd, pendrive, [arquivos[0]])

  assert arquivos_presentes(hd, [arquivos[0]]) == [False]

  #Teste 12 - Arquivos não existem no hd e no pendrive

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  erro = "Erro: Arquivo não existe no hd e pendrive"
  assert executar( False, hd, pendrive, [arquivos[0]]) == erro

  #Teste 13 - Arquivos existem apenas no pendrive e é para enviar para o hd
  # e é para transferir do pendrive para hd

  #Recria as pastas pendrive e hd para novos testes
  criar_pasta(pendrive)
  criar_pasta(hd)

  criar_arquivo(pendrive, arquivos[0])

  executar( False, hd, pendrive, [arquivos[0]])
  assert arquivos_presentes(hd, [arquivos[0]]) == [True]

  #Exclui as pastas testes (caso exista)
  if os.path.exists(pendrive):
    shutil.rmtree(pendrive)
  if os.path.exists(hd):
    shutil.rmtree(hd)

def criar_pasta(caminho):
  """! Função que cria uma nova pasta.
  @param caminho  Caminho para o local onde a pasta
   será criada.
  """
  #Exclui as pastas (caso exista)
  if os.path.exists(caminho):
    shutil.rmtree(caminho)

  #Cria a pasta de teste
  os.mkdir(caminho)

def criar_arquivo(caminho, nome_arquivo):
  """! Função que cria um novo arquivo.
  @param caminho  Caminho para o local onde a pasta
   será criada.
  @param nome_arquivo  Nome do arquivo que será criado.
  """
  with open(f"{caminho}/{nome_arquivo}", "x", encoding="utf-8") as arq_criado:
    arq_criado.close()
