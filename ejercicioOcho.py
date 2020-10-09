mesCompra = input()

valorCompra = input()
descuento = 0.15

if mesCompra == 10:
    calcularDescuento = valorCompra * descuento
    valorTotal = valorCompra - calcularDescuento
    print (valorTotal)
else:
    print (valorCompra) 