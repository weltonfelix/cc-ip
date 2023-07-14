ideal_train_time = int(input())
entries = int(input())

trained_positions = []
train_times = []

for _ in range(entries):
    position, initial_train_time = input().split()
    initial_train_time = int(initial_train_time)
    trained_positions.append(position)
    train_times.append(initial_train_time)

bad_training = True

sublists = []

# Get all sublists from the given list
for initial_train_time in range(len(train_times) + 1):
    for train_time in range(initial_train_time + 1, len(train_times) + 1):
        trains_sublist = train_times[initial_train_time:train_time]
        if sum(trains_sublist) == ideal_train_time:
            bad_training = False
            print(
                f"Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {' '.join(trained_positions[initial_train_time: train_time])}!"
            )

if bad_training:
    print(
        "Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima"
    )
