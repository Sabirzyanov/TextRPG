import random


class Player:
    def __init__(self, hp, power, defense, coins, items):
        self.hp = hp
        self.power = power
        self.defense = defense
        self.coins = coins
        self.items = items


class Items:
    def __init__(self, types, name, damage=0, defense=0,  heal=0, bonus=0, cost=100):
        self.types = types
        self.name = name
        self.damage = damage
        self.defense = defense
        self.heal = heal
        self.bonus = bonus
        self.cost = cost


class Melee(Items):
    def __init__(self, name, damage, cost):
        super(Melee, self).__init__("Melee", name, damage, 0, 0, cost)


class Defense(Items):
    def __init__(self, defense, bonus, cost):
        super(Defense, self).__init__("Defense", 0, defense, 0, bonus, cost)


class Room:
    def __init__(self, types, enemy_count, reward=random.randint(50, 200), bossFight=False):
        self.types = types
        self.enemy_count = enemy_count
        self.reward = reward
        self.bossFight = bossFight

    def rewarding(self, player):
        player.coins += self.reward


class ChestRoom(Room):
    def __init__(self):
        super(ChestRoom, self).__init__("ChestRoom", 0, 0)

    def reward_item(self):
        reward_item = {
            "Melee": [Melee("Sword", 10, 500), Melee("Knife", 3, 100), Melee("Mace", 7, 300), Melee("Club", 5, 200)],
            "Coins": [100, 200, 400, 1000],
        }
        return reward_item


def main():
    print("Вы хотите спуститься в подземелье?")
    running = True if int(input("1 - Да, 2 - Нет: ")) == 1 else False
    player = Player(100, 1, 1, 0, [])
    while running:
        command = int(input("1 - Посмотреть информацию о персонаже, 2 - Пройти дальше\n"
                            "3 - Посмотреть Инвентарь, 4 - Покинуть подземелье: "))
        if command == 1:
            print("-----Информация-----")
            print(f"-- Здоровье: {player.hp}\n-- Сила: {player.power}\n-- Защита {player.defense}\n"
                  f"-- Монеты: {player.coins}")
        elif command == 2:
            enemy_count = random.randint(2, 4)
            room_random = random.random()
            if room_random > 0.9:
                room = Room("Fight", enemy_count)
                print("Вы зашли в комнату с врагами. Ваши действия: ")
                command = int(input("1 - Убежать(Возмодность потерять ХП), 2 - Атаковать врага, "
                                    "3 - Посмотреть информацияю о врагах: "))
                if command == 1:
                    chance_lost_hp = random.random()
                    if chance_lost_hp > 0.6:
                        player.hp -= 5
                        print("При попытке бегства, вы потеряли 5 ХП. ")
                    else:
                        print("Вы убежали, не потеряв ни одного ХП. ")
                    continue
            else:
                room = ChestRoom()
                print("Вы нашли сундук. Открыть его?")
                command = int(input("1 - Да, открыть, 2 - Нет, уйти: " ))
                if command == 1:
                    reward_key = random.choice(list(room.reward_item().keys()))
                    reward = random.choice(room.reward_item()[reward_key])
                    print(reward.name if reward_key == "Melee" else reward)
                    if reward_key == "Coins":
                        print(f"Вам выпало {reward} монет.")
                        player.coins += reward
                    else:
                        print(f'Вам выпал {reward.name}.')
                        player.items.append(reward)
                else:
                    continue
            if room.types == "Fight":
                print(room.enemy_count)
        elif command == 3:
            if len(player.items) != 0:
                for i in player.items:
                    print(i.name)
            else:
                print("В вашем инвентаре ничего пока нет:(\n")
        elif command == 4:
            running = False


if __name__ == '__main__':
    main()