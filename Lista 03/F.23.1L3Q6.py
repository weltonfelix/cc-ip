ADD_ACTION = "Quero adicionar um item"
REMOVE_ACTION = "Quero remover um item"
LIST_ACTION = "Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?"
END_ACTION = "Fim! Muito obrigada pela ajuda!!"

collection = []
collection_movies = []
collection_costs = []
total_cost = 0

max_objects, max_cost = input().split(" ; ")
max_objects = int(max_objects)
max_cost = int(max_cost)

action = ""

while action != END_ACTION:
    action = input()

    if action != END_ACTION:
        if action == ADD_ACTION:
            item_movie, cost = input().split(" , ")
            item, movie = item_movie.split(" - ")
            cost = int(cost)
            if len(collection) < max_objects and (cost + total_cost) < max_cost:
                collection.append(item)
                collection_movies.append(movie)
                collection_costs.append(cost)
                total_cost += cost
                print(
                    f"Vá em frente, Ken! Você ainda tem {max_cost- total_cost} barbieCoins disponíveis"
                )
            else:
                print("Avise a Barbie que isso não será possível.")
        elif action == REMOVE_ACTION:
            item = input()
            if item in collection:
                item_index = collection.index(item)
                cost = collection_costs[item_index]
                collection.pop(item_index)
                collection_movies.pop(item_index)
                collection_costs.pop(item_index)

                total_cost -= cost
                print("Ok, Barbie!")
                print(
                    f"Ken, você ainda tem {max_cost-total_cost} barbieCoins disponíveis"
                )
            else:
                print("Barbie, infelizmente não consegui fazer isso.")
        elif action == LIST_ACTION:
            if len(collection) > 0:
                print("Claro!")
                for i in range(len(collection)):
                    item = collection[i]
                    movie = collection_movies[i]

                    print(f"{collection[i]} - {collection_movies[i]}")
            else:
                print(
                    "Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!"
                )

print("Por nada! Estou sempre à disposição!")
