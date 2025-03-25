import sys

class Monnaie():

    def __init__(self):
        self.prix = 0
        self.paiement = 0
        self.rendu = {}
        self.difference = 0
        self.monnaie = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

        self.main()


    def main(self):
        print("1: Lancer operation. \n")
        print("2: Quiitter le programme. \n")

        try:
            choix = int(input())

            if choix == 1:
                print("ENTRER LA SOMME A PAYER. \n")
                self.prix = int(input())

                print("ENTRER LE MONTANT VERSER. \n")
                self.paiement = int(input())

                self.rendu = {}
                self.operation()
                self.rendu_monnaie()

            elif choix == 2:
                sys.exit()
    
            else:
                print("Erreur de saisie. Faites un choix entre 1 et 2. \n")

                self.main()

        except ValueError:
            print("Erreur de saisie. Saisissez un entier 1 et 2. \n")

            self.main()



    def operation(self):

        difference = self.paiement - self.prix  

        for m in self.monnaie:
            if difference // m > 0:
                self.rendu[m] = int(difference // m)
                difference = difference % m    



    def rendu_monnaie(self):

        self.difference = self.paiement - self.prix                    

        if self.prix > self.paiement:
            print("Le montant versé est insuffisant. Il reste a payer ", -self.difference, ".\n")
        else:
            if self.difference == 0:
                print("Il n'y a aucune monnaie a rendre. \n")
            else:
                print("La monnaie a rendre est :", self.difference, "FCFA. \n")

                for cle, valeur in self.rendu.items():
                    if cle < 1000:
                        print("Le nombre de piece de ", cle, "FCFA a rendre est :", valeur, " \n")
                    else:
                        print("Le nombre de billet de ", cle, "FCFA a rendre est :", valeur, " \n")
        
        self.main()



if __name__ == "__main__":
    Monnaie()
