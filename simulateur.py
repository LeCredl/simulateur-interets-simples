def calcul_interets_simples(capital, taux, duree):
    """
    Calcule les intérêts simples et le total dû.

    Parameters:
    - capital (float) : le montant de base.
    - taux (float) : le taux d'intérêt annuel en pourcentage.
    - duree (float) : la durée en années.

    Returns:
    - tuple : (intérêts, total dû)
    """
    interets = capital * (taux / 100) * duree
    total_du = capital + interets
    return interets, total_du

def main():
    try:
        capital = float(input("Entrez le capital : "))
        taux = float(input("Entrez le taux d'intérêt annuel (en %) : "))
        duree = float(input("Entrez la durée (en années) : "))

        interets, total_du = calcul_interets_simples(capital, taux, duree)
        print(f"Intérêts simples : {interets:.2f}")
        print(f"Total dû : {total_du:.2f}")
    except ValueError:
        print("Erreur : veuillez entrer des valeurs numériques valides.")

if __name__ == "__main__":
    main()


