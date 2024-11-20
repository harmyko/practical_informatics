import matplotlib.pyplot as plt

f = open("transistor-counts.csv", "r", encoding="utf8")
eiluciu_skaicius = 0
procesoriuPavadinimai = []
tranzistoriuSkaiciai = []
isleidimoMetai = []

for eilute in f:
    eilute = eilute.strip().split(",")
    if eiluciu_skaicius > 0:
        procesoriuPavadinimai.append(eilute[0])
        tranzistoriuSkaiciai.append(int(eilute[1]))
        isleidimoMetai.append(int(eilute[2]))
    eiluciu_skaicius += 1

n0 = min(tranzistoriuSkaiciai)
y0 = min(isleidimoMetai)
T2 = 2

metai = list(range(min(isleidimoMetai), max(isleidimoMetai) + 1))
prognozes = [n0 * 2 ** ((yi - y0) / T2) for yi in metai]

plt.scatter(isleidimoMetai, tranzistoriuSkaiciai, label="Tranzistoriai")
plt.plot(metai, prognozes, label="Mūro dėsnio prognozė", color="gray", linestyle=":")

plt.xlabel("Metai")
plt.ylabel("Tranzistorių skaičius")
plt.yscale("log")
plt.legend()
plt.title("Mūro dėsnis: tranzistorių skaičiaus augimas")
plt.savefig("moores_law.pdf", format="pdf")
plt.savefig("moores_law.png", format="png")
plt.savefig("moores_law.svg", format="svg")

plt.show()
