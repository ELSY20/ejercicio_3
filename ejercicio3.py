import pandas as pd
#Precio
precio = 15000 # Precio fijo
hours = int(input("Hora de compra: "))

if(0 <= hours and hours <= 7):
    descuento = precio * 0.10
    precioFinal = precio - descuento
    porcentaje = "10%"
elif(7 <= hours and hours <= 13 ):
    descuento = precio * 0.20
    precioFinal = precio - descuento
    porcentaje = "20%"
elif(13 <= hours and hours <= 18):
    descuento = precio * 0.30
    precioFinal = precio - descuento
    porcentaje = "30%"
else:
    descuento = precio * 0.40
    precioFinal = precio - descuento
    porcentaje = "40%"

data = {
    "Porcentaje de descuento": [porcentaje],
    "precio final": [str(precioFinal) + " COP"]
}
df = pd.DataFrame(data)
print(df)