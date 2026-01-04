"""
🏁 DERNIÈRE ÉTAPE : L'Interface (Le main.py)
Tu as le moteur (Task, TaskManager), il te manque le volant.

Dans ton fichier main.py, tu dois créer une boucle infinie qui demande à l'utilisateur quoi faire.

Ton cahier des charges final :

Instancie manager = TaskManager("mes_taches.json").

Lance une boucle while True:.

Affiche le menu :

Ajouter une tâche

Voir les tâches

Quitter (C'est ici qu'on appelle manager.save_tasks() !)

Gère les choix de l'utilisateur avec des if/elif (ou match si tu as Python 3.10+).
"""

from models import TaskManager

manager = TaskManager("mes_taches.json")

while True:
    print("----MENU---\n")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Voir les tâches")
    print("4. Quitter")

    try:
        choix = int(input())
        if choix == 1:
            print("Vous voulez ajouter une tâche")
            titre = input("Donnez lui un titre")
            description = input("Donnez lui une description")
            manager.add_task(titre, description)
            print("La tâche a été ajoutée !")
        elif choix == 3:
            if not manager.tasks:
                print("Aucune tâche pour le moment.")
            else:
                for task in manager.tasks:
                    print(
                        f"[{task.id}] {task.title} ({task.status}) : {task.description}"
                    )
        elif choix == 2:
            while True:
                if not manager.tasks:
                    print("Aucune tâche pour le moment.")
                    break
                else:
                    for task in manager.tasks:
                        print(
                            f"[{task.id}] {task.title} ({task.status}) : {task.description}"
                        )
                try:
                    choix_id = int(
                        input(
                            "Choissisez l'ID de la tache a supprimer (0 pour revenir en arriere)"
                        )
                    )
                    if choix_id == 0:
                        break
                    else:
                        manager.delete_task(choix_id)
                        print("Tache supprimée !")
                except ValueError:
                    print("ID invalide")
        elif choix == 4:
            manager.save_tasks()
            break
    except ValueError:
        print("Nombre entier needed plz")
