"""2.Escribe un programa Python que acepte 5 números decimales del usuario."""
def run():
    print("Ingrese 5 numeros decimales" )
    for i in range(1,6):
        print("Ingrese ",i," numero: ")
        num= float(input())


if __name__=="__main__":
    run()