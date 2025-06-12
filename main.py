from src.visualizer import plot_comparison

def main():
    while True:
        time1 = input("Primeiro time: ").strip().lower()
        div1 = input("Divisão do primeiro time (A/B): ").strip().upper()
        time2 = input("Segundo time: ").strip().lower()
        div2 = input("Divisão do segundo time (A/B): ").strip().upper()
        metrica = input("Métrica (ex: goalsScored, shotsOnTarget): ").strip()

        plot_comparison(metrica, time1, div1, time2, div2)

        while True:
            resp = input("O que deseja fazer?\n1 - Nova análise\n2 - Encerrar\nEscolha: ").strip()
            if resp == '1':
                break
            elif resp == '2':
                print("Encerrando o programa.")
                return
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
