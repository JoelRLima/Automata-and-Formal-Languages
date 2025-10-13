# scanner.py
from patterns import PATTERNS

def scan_file(filepath):
    """
    Lê um arquivo e procura padrões sensíveis definidos em PATTERNS.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    findings = []  # Lista para armazenar resultados

    for name, pattern in PATTERNS.items():
        matches = pattern.findall(content)
        if matches:
            findings.append((name, matches))

    return findings


if __name__ == "__main__":
    path = input("Digite o caminho do arquivo a ser analisado: ")
    results = scan_file(path)

    if results:
        print("\n  Dados sensíveis encontrados:\n")
        for name, matches in results:
            print(f"[{name}]")
            for m in set(matches):  # set() evita repetições
                print(f"  → {m}")
            print()
    else:
        print("✅ Nenhum dado sensível encontrado.")
