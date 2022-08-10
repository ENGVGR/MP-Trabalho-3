"""
Funções que realizam o backup de arquivos utilizando arquivos de
um pendrive e de um hd.
"""

import os
import time

def arquivos_presentes(pasta, arquivos):
  """! Função que verifica se existe uma lista de arquivos na pasta.
  @param pasta  Caminho para a pasta que será verificada.
  @param arquivos  Lista de arquivos.
  @return  Retorna True caso todos os arquivos estejam na pasta
   e False caso contrário
  """
  for arquivo in arquivos:
    if not os.path.isfile(f"{pasta}/{arquivo}"):
      return False
  return True

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
  @param datas1  Datas da primeira pasta, no formato [ano,mes,dia,hora,minuto,segundo].
  @param datas2  Datas da segunda pasta, no formato [ano,mes,dia,hora,minuto,segundo].
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
