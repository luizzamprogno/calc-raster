import os

diretorio = 'D:/MyProjects/Canal_YOUTUBE/Geo/Videos/NDVI/'

b4Lista = []
b8Lista = []

for imagens in os.listdir(diretorio):
    if imagens.startswith("['B4']"):
        b4Lista.append(imagens)

    if imagens.startswith("['B8']"):
        b8Lista.append(imagens)

for uniao in range(len(b4Lista)):
    dirB4 = diretorio + b4Lista[uniao]
    dirB8 = diretorio + b8Lista[uniao]

    band_red = QgsRasterLayer(dirB4)
    band_nir = QgsRasterLayer(dirB8)

    saida = diretorio + 'NDVI_' + str(b4Lista[uniao][7:])
    entradas = []

    red = QgsRasterCalculatorEntry()
    red.ref = 'red@1'
    red.raster = band_red
    red.bandNumber = 1
    entradas.append(red)

    nir = QgsRasterCalculatorEntry()
    nir.ref = 'nir@1'
    nir.raster = band_nir
    nir.bandNumber = 1
    entradas.append(nir)

    calc = QgsRasterCalculator("('nir@1'-'red@1')/('nir@1'+'red@1')", saida, 'GTiff',
                               band_red.extent(), band_red.width(), band_red.height(), entradas)
    calc.processCalculation()
