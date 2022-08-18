import json

with open("Paquetes.json") as file:
    empresa=json.load(file)



def calcularCosto(alto,ancho,profundo):
    
    volumen=alto*ancho*profundo
    costo=volumen*5
    if(alto>30):
        costo=costo+2000
    if(costo>10000):
        costo=costo+costo*0.19
    
    return costo


def costoTotal(listaPaquetes,descuento):
    acumulador=0
    for i in range(0,len(listaPaquetes)):
        diccio=listaPaquetes[i]
        alto=diccio["ALTO"]
        ancho=diccio["ANCHO"]
        profundo=diccio["PROFUNDO"]
        
        acumulador=acumulador+calcularCosto(alto,ancho,profundo)

    
    desc=acumulador*(descuento/100)
    costodescuento=acumulador-desc
    
    return costodescuento


print(costoTotal(empresa["PAQUETES"],10))
