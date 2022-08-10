"""
Funções que realizam o backup de arquivos utilizando arquivos de
um pendrive e de um hd.
"""

import os.path

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
