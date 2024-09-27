from quarto import Quarto
from reserva import Reserva
from datetime import date

def main():
    quarto0 = Quarto(numero=77, tipo="duplo")

    if quarto0.verificar_disponibilidade():
        print(f'O quarto de número {quarto0.numero} está disponível!')

    check_in_data = date(2024, 9, 27)
    check_out_data = date(2024, 10, 4)
    reserva = Reserva(quarto=quarto0, quantidade_diarias=7, check_in=check_in_data, check_out=check_out_data)

    check_in, check_out = reserva.obter_periodo()
    print(f"Reserva feita no dia {check_in} até o dia {check_out}.")

    valor_total = reserva._calcular_valor()
    print(f"O valor total da reserva foi de R$ {valor_total:.2f}")

    # Reservar e liberar o quarto
    quarto0.reservar()
    if not quarto0.verificar_disponibilidade():
        print(f"O quarto de número {quarto0.numero} foi reservado!")
    
    quarto0.liberar()
    if quarto0.verificar_disponibilidade():
        print(f"O quarto de número {quarto0.numero} está liberado novamente!")

if __name__ == "__main__":
    main()
