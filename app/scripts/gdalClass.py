import os
import subprocess

class GdalClass :
  """Classe para facilitar uso da biblioteca gdal"""
  # def __init__(self):
  #   pass
  def pansharpening (self, path_panchromatic=0, path_multiband=0 ,path_output=0):
    subprocess.run(['echo','Iniciando procedimento ...'], shell=True)
    print ('Imagem panchromatica : %s' % path_panchromatic)
    print ('Imagem multibanda : %s' % path_multiband)
    print ('Nome do arquivo de saida : %s' % path_output)
    subprocess.run(['gdal_pansharpen.py', path_panchromatic, path_multiband, path_output], shell=True)

  def testando (self):
    print ('Caminho atual')
    print (os.getcwd())
    print ('---------------------')

if __name__ == "__main__":
  GdalClass().testando()
  GdalClass().pansharpening('panchromatica', 'multibandas', 'lugar_de_saida')
  