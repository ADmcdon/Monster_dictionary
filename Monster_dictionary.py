class Monster:
    monster_list = []
    id_counter = 10000

    def __init__(self, name, type1, region, habitat,
                 attack, defense, speed,
                 special_attack, special_defense,
                 critical_chance, curse):
        # assign a unique ID
        self.id = Monster.id_counter
        Monster.id_counter += 1

        # basic attributes
        self.name = name
        self.type1 = type1
        self.region = region
        self.habitat = habitat

        # stats
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.critical_chance = critical_chance
        self.curse = curse

        # register monster
        Monster.monster_list.append(self)

    def __str__(self):
        return (
            f" Name: {self.name},\n Type: {self.type1}, Region: {self.region}\n "
            f"Habitat: {self.habitat}\n "
            f"Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed},\n "
            f"Special Attack: {self.special_attack}, Special Defense: {self.special_defense},\n "
            f"Critical Chance: {self.critical_chance}%, Curse: {self.curse} ID: {self.id},"
        )

# Instantiate monsters—each with exactly 10 arguments (name, type, region, habitat, 5 raw stats, curse)
griffin       = Monster("Griffin", "Flying", "Greece", "Mountain",      150, 200, 180, 120, 115, 15)
sasquatch     = Monster("Sasquatch", "Earth", "North America", "Forest", 200, 250,  60, 180, 150, 10)
kraken        = Monster("Kraken", "Water", "Scandinavia", "Sea",      250, 200,  80, 100,  90, 12)
selkie        = Monster("Selkie", "Water", "Ireland", "Beach",         80, 100, 160, 200, 180,  8)
djinn         = Monster("Djinn", "Spirit", "Arabia", "Desert",        80, 180, 120, 300, 250, 20)
phoenix       = Monster("Phoenix", "Fire", "Egypt", "Desert",         180, 120, 200, 250, 140, 18)
yeti          = Monster("Yeti", "Ice", "Himalayas", "Mountain",      220, 230,  50,  90, 100,  14)
banshee       = Monster("Banshee", "Spirit", "Ireland", "Swamp",       60,  80, 180, 220, 200, 17)
hydra         = Monster("Hydra", "Water", "Greece", "Swamp",          240, 260,  70, 150, 160, 16)
chupacabra    = Monster("Chupacabra", "Dark", "Latin America", "Forest",140,120,190, 80, 75, 10)
thunderbird   = Monster("Thunderbird", "Electric", "North America", "Sky",160,140,220,180,130,12)
loch_ness     = Monster("Loch Ness Monster", "Water", "Scotland", "Lake",200,210, 40,110,115, 8)
nekomata      = Monster("Nekomata", "Spirit", "Japan", "Village",      90,100,150,140,130,15)
wendigo       = Monster("Wendigo", "Ice", "Canada", "Forest",          210,240, 80,100,105,13)
basilisk      = Monster("Basilisk", "Poison", "Egypt", "Desert",       170,160,100, 90, 85,19)
jorogumo      = Monster("Jorogumo", "Dark", "Japan", "Forest",         130,110,120,160,140,14)
qilin         = Monster("Qilin", "Mystic", "China", "Metaphysical",   200,190,140,230,210,18)
tikbalang     = Monster("Tikbalang", "Beast", "Philippines", "Mountains",160,150,170, 90, 85,10)
manticore     = Monster("Manticore", "Beast", "Persia", "Desert",     190,180,130,100, 95,12)
anansi        = Monster("Anansi", "Insect", "Africa", "Jungle",      100, 90,150,140,120,18)
kappa         = Monster("Kappa", "Water", "Japan", "Riverbank",        110,120,130, 80, 85,14)
valkyrie      = Monster("Valkyrie", "Warrior", "Norse", "Battlefield",180,170,160,140,135,16)
roc           = Monster("Roc", "Flying", "Arabia", "Sky",            210,200,195,120,110,18)
garuda        = Monster("Garuda", "Flying", "India", "Sky",          200,180,205,130,125,17)
leprechaun    = Monster("Leprechaun", "Fairy", "Ireland", "Meadow",     70, 60,180, 90, 85,12)
eastern_dragon= Monster("Eastern Dragon", "Water", "China", "Lake",     100,110,200,180,150,16)


def list_all_monsters():
    for monster in Monster.monster_list:
        print(monster)

if __name__ == "__main__":
    list_all_monsters()
