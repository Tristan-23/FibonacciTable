from tabulate import tabulate

def tafelkaart(n):
    headers = ["Tafel van"] + [str(i) for i in range(1, n + 1)]
    table = []

    for i in range(1, n + 1):
        row = [i] + [i * j for j in range(1, n + 1)]
        table.append(row)

    print(tabulate(table, headers, tablefmt="grid"))

n = int(input("Voer een getal in voor de tafelkaart: "))
tafelkaart(n)
