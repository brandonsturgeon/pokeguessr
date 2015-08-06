import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        flags = pygame.DOUBLEBUF
        self.game_window = pygame.display.set_mode((1000, 600), flags)
        pygame.display.set_caption("Poke Guessr")

        self.color_data = {}
        "bulbasaur: {BLUE: 50, RED: 100, GREEN: 101, PURPLE: 52}"

        self.playing = True
        self.gen_all_color_data()
        #self.main()

    def main(self):
        while self.playing is True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.playing = False
                    return

            self.clock.tick(60)

    def gen_all_color_data(self):
        for pokemon in ALL_POKEMON:
            self._gen_color_data_for_pokemon(pokemon)
        print "Finished loading color data"

    def _gen_color_data_for_pokemon(self, pokemon_name):
        print ""
        print "Analyzing: {}".format(pokemon_name)
        image = pygame.image.load("images/{}.png".format(pokemon_name))
        w = image.get_width()
        h = image.get_height()
        image_array = pygame.PixelArray(image)

        colors = {}
        for x in xrange(w):
            for y in xrange(h):
                # Get the raw pixel data, and convert it to an (r,g,b) tuple
                raw_pixel = image_array[x,y]
                a = image.unmap_rgb(raw_pixel)

                pixel_color = (a.r, a.g, a.b)
                pixel_alpha = a.a
                # Only add the colors to the dictionary if it's not transparent
                if pixel_alpha > 0:
                    if pixel_color in colors.keys():
                        colors[pixel_color] += 1
                    else:
                        colors[pixel_color] = 1
        print ""
        self.color_data[pokemon_name] = colors



if __name__ == "__main__":
    ALL_POKEMON = ["bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard",
                   "squirtle", "wartortle", "blastoise", "caterpie", "metapod", "butterfree",
                   "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto", "pidgeot", "rattata",
                   "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu",
                   "sandshrew", "sandslash", "nidoran", "nidorina", "nidoqueen", "nidorana",
                   "nidorino", "nidoking", "clefairy", "clefable", "vulpix", "ninetales", "jigglypuff",
                   "wigglytuff", "zubat", "golbat", "oddish", "gloom", "vileplume", "paras", "parasect",
                   "venonat", "venomoth", "diglett", "dugtrio", "meowth", "persian", "psyduck", "golduck",
                   "mankey", "primeape", "growlithe", "arcanine", "poliwag", "poliwhirl", "poliwrath", "abra",
                   "kadabra", "alakazam", "machop", "machoke", "machamp", "bellsprout", "weepinbell",
                   "victreebel", "tentacool", "tentacruel", "geodude", "graveler", "golem", "ponyta",
                   "rapidash", "slowpoke", "slowbro", "magnemite", "magneton", "farfetchd", "doduo",
                   "dodrio", "seel", "dewgong", "grimer", "muk", "shellder", "cloyster", "gastly", "haunter",
                   "gengar", "onix", "drowzee", "hypno", "krabby", "kingler", "voltorb", "electrode",
                   "exeggcute", "exeggutor", "cubone", "marowak", "hitmonlee", "hitmonchan", "lickitung",
                   "koffing", "weezing", "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan", "horsea",
                   "seadra", "goldeen", "seaking", "staryu", "starmie", "mr. mime", "scyther", "jynx",
                   "electabuzz", "magmar", "pinsir", "tauros", "magikarp", "gyarados", "lapras", "ditto",
                   "eevee", "vaporeon", "jolteon", "flareon", "porygon", "omanyte", "omastar", "kabuto",
                   "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos", "moltres", "dratini",
                   "dragonair", "dragonite", "mewtwo", "mew", "chikorita", "bayleef", "meganium",
                   "cyndaquil", "quilava", "typhlosion", "totodile", "croconaw", "feraligatr", "sentret",
                   "furret", "hoothoot", "noctowl", "ledyba", "ledian", "spinarak", "ariados", "crobat",
                   "chinchou", "lanturn", "pichu", "cleffa", "igglybuff", "togepi", "togetic", "natu",
                   "xatu", "mareep", "flaaffy", "ampharos", "bellossom", "marill", "azumarill",
                   "sudowoodo", "politoed", "hoppip", "skiploom", "jumpluff", "aipom", "sunkern",
                   "sunflora", "yanma", "wooper", "quagsire", "espeon", "umbreon", "murkrow", "slowking",
                   "misdreavus", "unown", "wobbuffet", "girafarig", "pineco", "forretress", "dunsparce",
                   "gligar", "steelix", "snubbull", "granbull", "qwilfish", "scizor", "shuckle", "heracross",
                   "sneasel", "teddiursa", "ursaring", "slugma", "magcargo", "swinub", "piloswine", "corsola",
                   "remoraid", "octillery", "delibird", "mantine", "skarmory", "houndour", "houndoom", "kingdra",
                   "phanpy", "donphan", "porygon-2", "stantler", "smeargle", "tyrogue", "hitmontop", "smoochum",
                   "elekid", "magby", "miltank", "blissey", "raikou", "entei", "suicune", "larvitar", "pupitar" 
                   "tyranitar", "lugia", "ho-oh", "celebi", "treecko", "grovyle", "sceptile", "torchic",
                   "combusken", "blaziken", "mudkip", "marshtomp", "swampert", "poochyena", "mightyena" 
                   "zigzagoon", "linoone", "wurmple", "silcoon", "beautifly", "cascoon", "dustox", "lotad",
                   "lombre", "ludicolo", "seedot", "nuzleaf", "shiftry", "taillow", "swellow", "wingull",
                   "pelipper", "ralts", "kirlia", "gardevoir", "surskit", "masquerain", "shroomish", "breloom",
                   "slakoth", "vigoroth", "slaking", "nincada", "ninjask", "shedinja", "whismur", "loudred",
                   "exploud", "makuhita", "hariyama", "azurill", "nosepass", "skitty", "delcatty", "sableye",
                   "mawile", "aron", "lairon", "aggron", "meditite", "medicham", "electrike", "manectric",
                   "plusle", "minun", "volbeat", "illumise", "roselia", "gulpin", "swalot", "carvanha",
                   "sharpedo", "wailmer", "wailord", "numel", "camerupt", "torkoal", "spoink", "grumpig",
                   "spinda", "trapinch", "vibrava", "flygon", "cacnea", "cacturne", "swablu", "altaria",
                   "zangoose", "seviper", "lunatone", "solrock", "barboach", "whiscash", "corphish",
                   "crawdaunt", "baltoy", "claydol", "lileep", "cradily", "anorith", "armaldo", "feebas",
                   "milotic", "castform", "kecleon", "shuppet", "banette", "duskull", "dusclops", "tropius",
                   "chimecho", "absol", "wynaut", "snorunt", "glalie", "spheal", "sealeo", "walrein", "clamperl",
                   "huntail", "gorebyss", "relicanth", "luvdisc", "bagon", "shelgon", "salamence", "beldum",
                   "metang", "metagross", "regirock", "regice", "registeel", "latias", "latios", "kyogre",
                   "groudon", "rayquaza", "jirachi", "deoxys", "turtwig", "grotle", "torterra", "chimchar",
                   "monferno", "infernape", "piplup", "prinplup", "empoleon", "starly", "staravia", "staraptor",
                   "bidoof", "bibarel", "kricketot", "kricketune", "shinx", "luxio", "luxray", "budew", "roserade",
                   "cranidos", "rampardos", "shieldon", "bastiodon", "burmy", "wormadam", "mothim", "combee",
                   "vespiquen", "pachirisu", "buizel", "floatzel", "cherubi", "cherrim", "shellos", "gastrodon",
                   "ambipom", "drifloon", "drifblim", "buneary", "lopunny", "mismagius", "honchkrow", "glameow",
                   "purugly", "chingling", "stunky", "skuntank", "bronzor", "bronzong", "bonsly", "mime jr.", "happiny",
                   "chatot", "spiritomb", "gible", "gabite", "garchomp", "munchlax", "riolu", "lucario", "hippopotas",
                   "hippowdon", "skorupi", "drapion", "croagunk", "toxicroak", "carnivine", "finneon", "lumineon",
                   "mantyke", "snover", "abomasnow", "weavile", "magnezone", "lickilicky", "rhyperior", "tangrowth",
                   "electivire", "magmortar", "togekiss", "yanmega", "leafeon", "glaceon", "gliscor", "mamoswine",
                   "porygon-z", "gallade", "probopass", "dusknoir", "froslass", "rotom", "uxie", "mesprit", "azelf",
                   "dialga", "palkia", "heatran", "regigigas", "giratina", "cresselia", "phione", "manaphy", "darkrai",
                   "shaymin", "arceus", "victini", "snivy", "servine", "serperior", "tepig", "pignite", "emboar",
                   "oshawott", "dewott", "samurott", "patrat", "watchog", "lillipup", "herdier", "stoutland",
                   "purrloin", "liepard", "pansage", "simisage", "pansear", "simisear", "panpour", "simipour",
                   "munna", "musharna", "pidove", "tranquill", "unfezant", "blitzle", "zebstrika", "roggenrola",
                   "boldore", "gigalith", "woobat", "swoobat", "drilbur", "excadrill", "audino", "timburr", "gurdurr",
                   "conkeldurr", "tympole", "palpitoad", "seismitoad", "throh", "sawk", "sewaddle", "swadloon",
                   "leavanny", "venipede", "whirlipede", "scolipede", "cottonee", "whimsicott", "petilil",
                   "lilligant", "basculin", "sandile", "krokorok", "krookodile", "darumaka", "darmanitan",
                   "maractus", "dwebble", "crustle", "scraggy", "scrafty", "sigilyph", "yamask", "cofagrigus",
                   "tirtouga", "carracosta", "archen", "archeops", "trubbish", "garbodor", "zorua", "zoroark",
                   "minccino", "cinccino", "gothita", "gothorita", "gothitelle", "solosis", "duosion", "reuniclus",
                   "ducklett", "swanna", "vanillite", "vanillish", "vanilluxe", "deerling", "sawsbuck", "emolga",
                   "karrablast", "escavalier", "foongus", "amoonguss", "frillish", "jellicent", "alomomola",
                   "joltik", "galvantula", "ferroseed", "ferrothorn", "klink", "klang", "klinklang", "tynamo",
                   "eelektrik", "eelektross", "elgyem", "beheeyem", "litwick", "lampent", "chandelure", "axew",
                   "fraxure", "haxorus", "cubchoo", "beartic", "cryogonal", "shelmet", "accelgor", "stunfisk",
                   "mienfoo", "mienshao", "druddigon", "golett", "golurk", "pawniard", "bisharp", "bouffalant",
                   "rufflet", "braviary", "vullaby", "mandibuzz", "heatmor", "durant", "deino", "zweilous",
                   "hydreigon", "larvesta", "volcarona", "cobalion", "terrakion", "virizion", "tornadus",
                   "thundurus", "reshiram", "zekrom", "landorus", "kyurem", "keldeo", "meloetta", "genesect"]

    Game()
