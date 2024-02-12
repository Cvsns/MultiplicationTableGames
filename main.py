def main():
    print("Pour jouer avec la table de multiplication, tapez le nombre : ")
    choix = int(input())

    if choix >= 1 and choix <= 10:
        print("Vous avez choisi la table de multiplication de", choix)
        for i in range(1, 11):
            print(choix, "X", i, "= ?")
            reponse = int(input())
            if reponse == choix * i:
                print("✔️ Juste ! 😀")
            else:
                print("Faux. La réponse était :", choix * i)
    else:
        print("Veuillez entrer un nombre entre 1 et 10.")

if __name__ == "__main__":
    main()
