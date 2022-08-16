"""
Funções que realizam o backup de arquivos utilizando arquivos de
um pendrive e de um hd.
"""

import os
import time
import shutil

def arquivos_presentes(pasta, arquivos):
  """! Função que verifica se existe uma lista de arquivos na pasta.
  @param pasta  String com o caminho para a pasta que será verificada.
  @param arquivos  Lista de strings (arquivos).
  @return  Retorna uma lista de booleanos que informa
   se o arquivo existe (True) ou
  não (False).
  """
  presenca = []

  for arquivo in arquivos:
    if not os.path.isfile(f"{pasta}/{arquivo}"):
      presenca.append(False)
    else:
      presenca.append(True)
  return presenca

def datas_dos_arquivos(pasta, arquivos):
  """! Função que retorna as datas das últimas modificações dos arquivos.
  @param pasta  String do caminho para a pasta que será verificada.
  @param arquivos  Lista de strings (arquivos).
  @return  Retorna uma lista de inteiros com as datas das últimas modificações
   dos arquivos.
  """
  datas = []
  for arquivo in arquivos:
    data = os.path.getmtime(f"{pasta}/{arquivo}")
    ano,mes,dia,hora,minuto,segundo=time.localtime(data)[:-3]
    datas.append([ano, mes, dia, hora, minuto, segundo])
  return datas

def compara_datas(datas1, datas2):
  """! Função que compara as datas de duas pastas.
  @param datas1  Datas da primeira pasta, no formato
   [ano,mes,dia,hora,minuto,segundo] (lista de inteiros).
  @param datas2  Datas da segunda pasta, no formato
   [ano,mes,dia,hora,minuto,segundo] (lista de inteiros).
  @return  Retorna uma lista de strings com o resultado das
   comparações de datas.
  """
  comparacoes = []

  #Opções de saída:
  primeiro = "Primeiro é mais recente"
  segundo = "Segundo é mais recente"
  iguais = "As datas são iguais"

  for i in range(len(datas1)):
    ano1 = datas1[i][0]
    ano2 = datas2[i][0]
    mes1 = datas1[i][1]
    mes2 = datas2[i][1]
    dia1 = datas1[i][2]
    dia2 = datas2[i][2]
    hora1 = datas1[i][3]
    hora2 = datas2[i][3]
    minuto1 = datas1[i][4]
    minuto2 = datas2[i][4]
    segundo1 = datas1[i][5]
    segundo2 = datas2[i][5]

    if ano1 != ano2:
      if ano1 > ano2:
        comparacoes.append(primeiro)
      else:
        comparacoes.append(segundo)

    elif mes1 != mes2:
      if mes1 > mes2:
        comparacoes.append(primeiro)
      else:
        comparacoes.append(segundo)

    elif dia1 != dia2:
      if dia1 > dia2:
        comparacoes.append(primeiro)
      else:
        comparacoes.append(segundo)

    elif hora1 != hora2:
      if hora1 > hora2:
        comparacoes.append(primeiro)
      else:
        comparacoes.append(segundo)

    elif minuto1 != minuto2:
      if minuto1 > minuto2:
        comparacoes.append(primeiro)
      else:
        comparacoes.append(segundo)

    elif segundo1 != segundo2:
      if segundo1 > segundo2:
        comparacoes.append(primeiro)
      else:
        comparacoes.append(segundo)
    else:
      comparacoes.append(iguais)
  return comparacoes

def transfere_arquivos(arquivos, origem, destino):
  """! Função que transfere arquivos entre pastas.
  @param arquivos  Lista de arquivos.
  @param origem   Local onde serão copiados os arquivos
  @param destino  Local onde serão colocados os arquivos
  """
  for arquivo in arquivos:
    shutil.copyfile(f"{origem}/{arquivo}", f"{destino}/{arquivo}")

def executar(backup, hd, pendrive, arquivos):
  """! Função que executa o progama de backup.
  @param backup  Booleano que pode ser True (hd para pendrive) ou
   False (pendrive para hd)
  @param hd  String que é o caminho para hd
  @param pendrive  String que é o caminho para pendrive
  @param arquivos  Lista de strings (arquivos).
  @return  Retornar erros, caso existam
  """
  #Opções de saída:
  primeiro = "Primeiro é mais recente"
  segundo = "Segundo é mais recente"

  if backup is None:
    erro = "Impossível - Não contem o parâmetro Backup"
    print(erro)
    return erro

  if backup:
    arquivos_presentes_hd = arquivos_presentes(hd, arquivos)
    arquivos_presentes_pendrive = arquivos_presentes(pendrive, arquivos)

    for i in range(len(arquivos)):
      arquivo = arquivos[i]
      arquivo_presente_hd = arquivos_presentes_hd[i]
      arquivo_presente_pendrive = arquivos_presentes_pendrive[i]

      if arquivo_presente_hd and not arquivo_presente_pendrive:
        transfere_arquivos([arquivo], hd, pendrive)

      if arquivo_presente_hd and arquivo_presente_pendrive:
        data_arquivo_hd = datas_dos_arquivos(hd, [arquivo])
        data_arquivo_pendrive = datas_dos_arquivos(pendrive, [arquivo])

        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == primeiro:
          transfere_arquivos([arquivo], hd, pendrive)
        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == segundo:
          erro = "Erro: Arquivos do pendrive já são os mais recentes"
          print(erro)
          return erro
      if not arquivo_presente_hd and not arquivo_presente_pendrive:
        erro = "Erro: Os arquivos não existem no Hd e no pendrive"
        print(erro)
        return erro
  else:
    arquivos_presentes_hd = arquivos_presentes(hd, arquivos)
    arquivos_presentes_pendrive = arquivos_presentes(pendrive, arquivos)

    for i in range(len(arquivos)):
      arquivo = arquivos[i]
      arquivo_presente_hd = arquivos_presentes_hd[i]
      arquivo_presente_pendrive = arquivos_presentes_pendrive[i]

      if arquivo_presente_hd and not arquivo_presente_pendrive:
        erro = "Erro: Não foram encontrados os arquivos no pendrive"
        print(erro)
        return erro

      if arquivo_presente_hd and arquivo_presente_pendrive:
        data_arquivo_hd = datas_dos_arquivos(hd, [arquivo])
        data_arquivo_pendrive = datas_dos_arquivos(pendrive, [arquivo])

        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == primeiro:
          erro = "Erro: Arquivos do hd já são os mais recentes"
          print(erro)
          return erro

        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == segundo:
          transfere_arquivos([arquivo], pendrive, hd)

      if not arquivo_presente_hd and not arquivo_presente_pendrive:
        erro = "Erro: Arquivo não existe no hd e pendrive"
        print(erro)
        return erro

      if not arquivo_presente_hd and arquivo_presente_pendrive:
        transfere_arquivos([arquivo], pendrive, hd)
