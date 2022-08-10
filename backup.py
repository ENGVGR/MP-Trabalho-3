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
    year,month,day,hour,minute,second=time.localtime(data)[:-3]
    datas.append([year, month, day, hour, minute, second])
  return datas
