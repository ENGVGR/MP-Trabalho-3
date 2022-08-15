"""
Funções que realizam o backup de arquivos utilizando arquivos de
um pendrive e de um hd.
"""

import os
import time
import shutil

def arquivos_presentes(pasta, arquivos):
  """! Função que verifica se existe uma lista de arquivos na pasta.
  @param pasta  Caminho para a pasta que será verificada.
  @param arquivos  Lista de arquivos.
  @return  Retorna uma lista que informa se o arquivo existe (True) ou
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
  @param pasta  Caminho para a pasta que será verificada.
  @param arquivos  Lista de arquivos.
  @return  Retorna uma lista com as datas das últimas modificações dos arquivos.
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
   [ano,mes,dia,hora,minuto,segundo].
  @param datas2  Datas da segunda pasta, no formato
   [ano,mes,dia,hora,minuto,segundo].
  @return  Retorna uma lista com o resultado das comparações de datas.
  """
  comparacoes = []

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
        comparacoes.append("Primeiro é mais recente")
      else:
        comparacoes.append("Segundo é mais recente")

    elif mes1 != mes2:
      if mes1 > mes2:
        comparacoes.append("Primeiro é mais recente")
      else:
        comparacoes.append("Segundo é mais recente")

    elif dia1 != dia2:
      if dia1 > dia2:
        comparacoes.append("Primeiro é mais recente")
      else:
        comparacoes.append("Segundo é mais recente")

    elif hora1 != hora2:
      if hora1 > hora2:
        comparacoes.append("Primeiro é mais recente")
      else:
        comparacoes.append("Segundo é mais recente")

    elif minuto1 != minuto2:
      if minuto1 > minuto2:
        comparacoes.append("Primeiro é mais recente")
      else:
        comparacoes.append("Segundo é mais recente")

    elif segundo1 != segundo2:
      if segundo1 > segundo2:
        comparacoes.append("Primeiro é mais recente")
      else:
        comparacoes.append("Segundo é mais recente")
    else:
      comparacoes.append("As datas são iguais")
  return comparacoes

def transfere_arquivos(arquivos, origem, destino):
  for arquivo in arquivos:
    shutil.copyfile(f"{origem}/{arquivo}", f"{destino}/{arquivo}")

def executar(backup, hd, pendrive, arquivos):
  if backup == None:
    print("Impossível - Não contem o parâmetro Backup")
    return "Impossível - Não contem o parâmetro Backup"

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

        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == "Primeiro é mais recente":
          transfere_arquivos([arquivo], hd, pendrive)
        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == "Segundo é mais recente":
          print("Erro: Arquivos do pendrive já são os mais recentes")
          return "Erro: Arquivos do pendrive já são os mais recentes"
  else:
    arquivos_presentes_hd = arquivos_presentes(hd, arquivos)
    arquivos_presentes_pendrive = arquivos_presentes(pendrive, arquivos)

    for i in range(len(arquivos)):
      arquivo = arquivos[i]
      arquivo_presente_hd = arquivos_presentes_hd[i]
      arquivo_presente_pendrive = arquivos_presentes_pendrive[i]

      if arquivo_presente_hd and not arquivo_presente_pendrive:
        print("Erro: Não foram encontrados os arquivos no pendrive")
        return "Erro: Não foram encontrados os arquivos no pendrive"

      if arquivo_presente_hd and arquivo_presente_pendrive:
        data_arquivo_hd = datas_dos_arquivos(hd, [arquivo])
        data_arquivo_pendrive = datas_dos_arquivos(pendrive, [arquivo])

        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == "Primeiro é mais recente":
          print("Erro: Arquivos do hd já são os mais recentes")
          return "Erro: Arquivos do hd já são os mais recentes"

        if compara_datas(data_arquivo_hd, data_arquivo_pendrive)[0] == "Segundo é mais recente":
          transfere_arquivos([arquivo], pendrive, hd)