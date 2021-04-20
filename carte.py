######################################################################################
# carte :

DESCRIPTION = "description"
HAUT = "haut", "up", "z"
BAS = "bas", "down", "s"
GAUCHE = "gauche", "left", "q"
DROITE = "droite", "right", "d"
ACTION = "action"



carte = {
          "petit village de pecheur": { #A1
              DESCRIPTION : "Bienvenue au pays du soleil levant jeune guerrier,est-tu prêt à affronter le pire de tout les dieux ? \n avant cela de nombreux combats et rencontres t'attendent... \n que ton nindo t'apporte la force nécessaire dans cette aventure.",
              HAUT : "ravin",
              BAS : "Le fleuve Shinano-Gawa",
              GAUCHE : "ravin",
              DROITE : "Les Plaines d'Izuhara",
              ACTION : "None",
          },
          "Les Plaines d'Izuhara": { #A2
              DESCRIPTION : "Les Plaines d'Izuhara lieu ou autre fois les plus grands samouraïs se retrouvaient pour des duels et batailles épics",
              HAUT : "ravin",
              BAS : "Le donjon HIkone",
              GAUCHE : "petit village de pecheur",
              DROITE : "Okuno-in",
              ACTION : "combat", # ronin
          },
          "Okuno-in": { #A3
              DESCRIPTION : "Te voici dans le plus grand cimetière japonais, ici git les plus grands guerriers du Japon",
              HAUT : "ravin",
              BAS : "Les Onsen",
              GAUCHE : "Les Plaines d'Izuhara",
              DROITE : "La Fôret Aokigahara",
              ACTION : "combat", #le Kasha
          },
          "La Fôret Aokigahara": { #A4
              DESCRIPTION : "La Fôret des suicides où les esprits des gens morts ne passe pas l'au-delà",
              HAUT : "ravin",
              BAS : "Sanctuaire Shinto",
              GAUCHE : "Okuno-in",
              DROITE : "océan",
              ACTION : "combat",  # les yurei
          },
          "Le fleuve Shinano-Gawa": { #A5
              DESCRIPTION : "Le Fleuve Shinano_Gawa, le fleuve le plus long du Japon te fera beaucoup marché tu devras t'armée de patience\n et de courage car des pièges t'y attendent",
              HAUT : "petit village de pecheur",
              BAS : "Les chutes de Fukuroda",
              GAUCHE : "ravin",
              DROITE : "Le donjon HIkone",
              ACTION : "combat",  # Le Kappa 
          },
          "Le donjon HIkone": { #A6
              DESCRIPTION : "En suivant le fleuve vous voici face au Donjon Hikone",
              HAUT : "Les Plaines d'Izuhara",
              BAS : "La fôret de Sagano",
              GAUCHE : "Le fleuve Shinano-Gawa",
              DROITE : "Les Onsen",
              ACTION : "combat", #item 
          },
          "Les Onsen": { #A7
              DESCRIPTION : "Aux sources chaudes prenez un bain thermale pour récupérer de vos combats",
              HAUT : "Okuno-in",
              BAS : "Le Mont Fuji",
              GAUCHE : "Le donjon HIkone",
              DROITE : "Sanctuaire Shinto",
              ACTION : "maitre",  #redonne de l'HP max if HP max ALORS XP by Sensei Jiraya
          },
          "Sanctuaire Shinto": { #A8
              DESCRIPTION : "Le sanctuaire inviolable abrite un secret bien gardé...Mais lequel ?",
              HAUT : "La Fôret Aokigahara",
              BAS : "Les mines d'or de Sado",
              GAUCHE : "Les Onsen",
              DROITE : "océan",
              ACTION : "combat", #le Otoroshi
          },
          "Les chutes de Fukuroda": { #A9
              DESCRIPTION : "Ressource toi dans les chutes de Fukuroda , son eau est réputé pour vous faire de bon massage mais attention à ce qui s'y cache...",
              HAUT : "Le fleuve Shinano-Gawa",
              BAS : "Le Dojo",
              GAUCHE : "ravin",
              DROITE : "La fôret de Sagano",
              ACTION : "combat", #Nure-Ona
          },
          "La forêt de Sagano": { #A10
              DESCRIPTION : "Tu entre dans la dense Fôret de Bambou où le seul moyen de la traverser est un sentier de briques éclairé par la lumière du jours",
              HAUT : "Le donjon HIkone",
              BAS : "La cité Milléniale",
              GAUCHE : "Les chutes de Fukuroda",
              DROITE : "Le Mont Fuji",
              ACTION : "maitre", # Kodama le guide la fôret
          },
          "Le Mont Fuji": { #A11
              DESCRIPTION : "que trouverez-vous au pied de se stratovolcan qui n'attend qu'une seule chose qui est d'exploser",
              HAUT : "Les Onsen",
              BAS : "Le Lac Ashi",
              GAUCHE : "La fôret de Sagano",
              DROITE : "Les mines d'or de Sado",
              ACTION : "combat",# Kitsune 
          },
          "Les mines d'or de Sado": { #A12
              DESCRIPTION : "Dans ces mines desertés par l'homme rode un monstre qui veille sur l'or introduite dans ces roches",
              HAUT : "Sanctuaire Shinto",
              BAS : "PLage de Shirahama",
              GAUCHE : "Le Mont Fuji",
              DROITE : "océan",
              ACTION : "combat",#Rokurokubi
          },
          "Le Dojo": { #A13
              DESCRIPTION : "Bienvenue dans le Dojo où le maître Miyamoto Musashi vous attend avec impatience",
              HAUT : "Les chutes de Fukuroda",
              BAS : "océan",
              GAUCHE : "ravin",
              DROITE : "La cité Milléniale",
              ACTION : "maitre",  #Miyamoto Musashi Xp + arme 
          },
          "La cité Milléniale": { #A14
              DESCRIPTION : "Te voici dans la Cité la plus vieille du Japon tu pourras y trouver du beau monde",
              HAUT : "La fôret de Sagano",
              BAS : "océan",
              GAUCHE : "Le Dojo",
              DROITE : "Le Lac Ashi",
              ACTION : "maitre",# réponse enigme Japon 
          },
          "Le Lac Ashi": { #A15
              DESCRIPTION : "ce Lac est un belle endroit pour s'y reposer et manger quelque chose , il est temps de mediter",
              HAUT : "Le Mont Fuji",
              BAS : "océan",
              GAUCHE : "La cité Milléniale",
              DROITE : "PLage de Shirahama",
              ACTION : "None", # trouver de la nourriture HP 
          },
          "PLage de Shirahama": { #A16
              DESCRIPTION : "Profite de cette plage, surement l'un de tes rares moment de repos",
              HAUT : "Les mines d'or de Sado",
              BAS : "Port de Mao",
              GAUCHE : "Le Lac Ashi",
              DROITE : "Port de Nagoya",
              ACTION : "None",
          },
          "les Collines de Yangshuo": { #B1
            DESCRIPTION : "Vous voici entre les collines de Yangshuo plus communémant appelé les collines de la Lune",
            HAUT : "océan",
            BAS : "Les Chutes d'Eau Huangguoshu",
            GAUCHE : "ravin",
            DROITE : "La Vieille Ville sur l'eau de Fenghuang",
            ACTION : "maitre",# Jin Chan
          },
          "La Vieille Ville de Fenghuang": { #B2
            DESCRIPTION : "La Ville Fenghuang, réputer pour avoir ces batiments sur l'eau d'une rivière dont l'eau reguorge de ressources,gard à celui qui n'appartient pas à ce village... ",
            HAUT : "océan",
            BAS : "Le désert de Gobi",
            GAUCHE : "les Collines de Yangshuo",
            DROITE : "La Fôret de Xueling",
            ACTION : "combat",# le phoenix a 9 têtes le fenghuang
          },
          "La Fôret de Xueling": { #B3
            DESCRIPTION : "40 millions d'années que cette fôrets existe et je vous laisse imaginer ce que vous y trouverez à l'intérieur...",
            HAUT : "océan",
            BAS : "La Vallée de Jiuzhaigou",
            GAUCHE : "La Vieille Ville sur l'eau de Fenghuang",
            DROITE : "Plage de Qingdao",
            ACTION : "maitre", # wukong
          },
          "Plage de Qingdao": { #B4
            DESCRIPTION : "Paradis et chemin vers ton salut, profite...",
            HAUT : "Port de Mao",
            BAS : "Les Montagnes du Tiashan",
            GAUCHE : "La Fôret de Xueling",
            DROITE : "Port de Ningbo-Zhoushan",
            ACTION : "None",#case piège torsion de cheville dans un trou dans le sable 
          },
          "Les Chutes d'Eau Huangguoshu": { #B5
            DESCRIPTION : "Proches de ces chutes d'eaux les plus magnifiques du royaume céleste ce cache une des créatures les plus détestables.",
            HAUT : "les Collines de Yangshuo",
            BAS : "Fleuve du Yangzi Jiang",
            GAUCHE : "ravin",
            DROITE : "Le désert de Gobi",
            ACTION : "combat", #Mogwai
          },
          "Le désert de Gobi": { #B6
            DESCRIPTION : "En plein milieu de toutes ces montagnes, ces fôrets et rivières y est incrusté un endroit aride bienvenue dans le désert du Gobi",
            HAUT : "La Vieille Ville sur l'eau de Fenghuang",
            BAS : "La Cité Interdite",
            GAUCHE : "Les Chutes d'Eau Huangguoshu",
            DROITE : "La Vallée de Jiuzhaigou",
            ACTION : "None",#piège : déshydratation
          },
          "La Vallée de Jiuzhaigou": { #B7
            DESCRIPTION : "Une petite Oasis au milieu de tout ",
            HAUT : "La Fôret de Xueling",
            BAS : "La Grande Muraille",
            GAUCHE : "Le désert de Gobi",
            DROITE : "Les Montagnes du Tiashan",
            ACTION : "None",# hp gratis grace à l'eau de source
          },
          "Les Montagnes du Tiashan": { #B8
            DESCRIPTION : "Les Montagnes du Tiashan cache on son sein des cavernes bien cacher par la végétation attention, elles ne sont pas toujours vides...",
            HAUT : "Plage de Qingdao",
            BAS : "Temple du Ciel Shaoline",
            GAUCHE : "La Vallée de Jiuzhaigou",
            DROITE : "océan",
            ACTION : "combat", #Long le dragon
          },
          "Fleuve du Yangzi Jiang": { #B9
            DESCRIPTION : "Ton périple commence sur le plus grand fleuve de Chine et d'Asie que vas-tu rencontrer sur celui-ci ?",
            HAUT : "Les Chutes d'Eau Huangguoshu",
            BAS : "Grand village de Pêcheur",
            GAUCHE : "ravin",
            DROITE : "La Cité Interdite",
            ACTION : "combat",# Baku
          },
          "La Cité Interdite": { #B10
            DESCRIPTION : "La célèbre cité interdite plus personne ne la présente pour y entrer qui sait ce qui vous attend",
            HAUT : "Le désert de Gobi",
            BAS : "Le Palais du Potala",
            GAUCHE : "Fleuve du Yangzi Jiang",
            DROITE : "La Grande Muraille",
            ACTION : "combat", # Shi 
          },
          "La Grande Muraille": { #B11
            DESCRIPTION : "Te voilà sur la plus longue fortification au monde, et qui dit fortification dit endroit militaire protégé...que trouveras-tu ?",
            HAUT : "La Vallée de Jiuzhaigou",
            BAS : "Monastère des 10000 Bouddhas",
            GAUCHE : "La Cité Interdite",
            DROITE : "Temple du Ciel Shaoline",
            ACTION : "combat", # Le dernier guerrier d'argile
          },
          "Temple du Ciel Shaoline": { #B12
            DESCRIPTION : "La 36ème chambre de shaoline où l'art du kung fu n'aura plus de secret pour toi.",
            HAUT : "Les Montagnes du Tiashan",
            BAS : "Les Falaises de Xuankong",
            GAUCHE : "La Grande Muraille",
            DROITE : "océan",
            ACTION : "maitre", #Maître Shaoline
          },
          "Grand village de Pêcheur": { #B13
            DESCRIPTION : "Bienvenue sur l'une des plus anciennes civilisations du monde combattant céleste , \n l'empire du milieu te réservera bien des surprises dans ta quête vers Yashin que le chi soit avec toi.",
            HAUT : "Fleuve du Yangzi Jiang",
            BAS : "ravin",
            GAUCHE : "ravin",
            DROITE : "Le Palais du Potala",
            ACTION : "None",
          },
          "Le Palais du Potala": { #B14
            DESCRIPTION : "Nichet sur son rocher le palais du potala t'enseignera la voie de la sagesse",
            HAUT : "La Cité Interdite",
            BAS : "ravin",
            GAUCHE : "Grand village de Pêcheur",
            DROITE : "Monastère des 10000 Bouddhas",
            ACTION : "maitre", # Dalai Lama
          },
          "Monastère des 10000 Bouddhas": { #B15
            DESCRIPTION : "Le monastère des 10 000 Bouddhas lieu de recueillement, brule un ansan et peut-être que tu y sera récompensé.. ",
            HAUT : "La Grande Muraille",
            BAS : "ravin",
            GAUCHE : "Le Palais du Potala",
            DROITE : "Les Falaises de Xuankong",
            ACTION : "None", # Guanyin
          },
          "Les Falaises de Xuankong": { #B16
            DESCRIPTION : "Falaises vertigineuses dont personne ne veut s'y approcher, osera tu t'y aventurer ?",
            HAUT : "Temple du Ciel Shaoline",
            BAS : "ravin",
            GAUCHE : "Monastère des 10000 Bouddhas",
            DROITE : "océan",
            ACTION : "combat", #Golem
          },
          "Plage de Raja Ampat": { #C1
            DESCRIPTION : "Le paradis n'est pas loin...ne passe pas à côté...",
            HAUT : "Port de Gili trawangan",
            BAS : "Le Sanctuaire de Candi Mendut",
            GAUCHE : "P3",
            DROITE : "La Jungle de Kawah Ijen",
            ACTION : "None",# piège sable mouvant
          },
          "La Jungle de Kawah Ijen": { #C2
            DESCRIPTION : "Jungle hostile, sombre ou y progresser est aussi simple que de sortir de sables mouvant...\n mais se n'est pas le pire...",
            HAUT : "océan",
            BAS : "Les Grottes de Leang-Leang",
            GAUCHE : "Plage de Raja Ampat",
            DROITE : "La Cité des Singes",
            ACTION : "combat",# Rangda
          },
          "La Cité des Singes": { #C3
            DESCRIPTION : "En indonésie comme en inde le singe est venéré au point qu'une cité entière les abrites...mais il on un leadeur...",
            HAUT : "océan",
            BAS : "Les plaines du Dragon de Komodo",
            GAUCHE : "La Jungle de Kawah Ijen",
            DROITE : "Le Chateau des Démons",
            ACTION : "maitre", #Hanuman arme Massue +30 degats
          },
          "Le Chateau des Démons": { #C4
            DESCRIPTION : "Y abrite en son sein un roi sans pitier et ces sbires les plus cruelles ,\na tu le courage de l'affronter ?",
            HAUT : "océan",
            BAS : "Les Ruines du Borobudur",
            GAUCHE : "La Cité des Singes",
            DROITE : "ravin",
            ACTION : "combat",# Ravana
          },
          "Le Sanctuaire de Candi Mendut": { #C5
            DESCRIPTION : "Le plus petit temple que tu puisse trouver dans les alentours,\n mais il se cache à l'intérieur un grand savoir",
            HAUT : "Plage de Raja Ampat",
            BAS : "Les Montagnes de Bromo",
            GAUCHE : "océan",
            DROITE : "Les Grottes de Leang-Leang",
            ACTION : "maitre",#Rama
          },
          "Les Grottes de Leang-Leang": { #C6
            DESCRIPTION : "il n'y cache jamais rien de bon dans une grotte..\nencore moins dans celle de Leang Leang...",
            HAUT : "La Jungle de Kawah Ijen",
            BAS : "Volcan du Krakatoa",
            GAUCHE : "Le Sanctuaire de Candi Mendut",
            DROITE : "Les plaines du Dragon de Komodo",
            ACTION : "None",#Chauve Souris
          },
          "Les plaines du Dragon de Komodo": { #C7
            DESCRIPTION : "plaines ou il est difficile de voir ces pieds...attentions aux dragons...",
            HAUT : "La Cité des Singes",
            BAS : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            GAUCHE : "Les Grottes de Leang-Leang",
            DROITE : "Les Ruines du Borobudur",
            ACTION : "combat",# King Komodo
          },
          "Les Ruines du Borobudur": { #C8
            DESCRIPTION : "Autre fois temple, la jungle à repris ces droits\net le Borobudur appartient maintenant à sa faune et sa flore",
            HAUT : "Le Chateau des Démons",
            BAS : "La Fôret de Kalimantan",
            GAUCHE : "Les plaines du Dragon de Komodo",
            DROITE : "ravin",
            ACTION : "maitre",#Louis l'auran-outan
          },
          "Les Montagnes de Bromo": { #C9
            DESCRIPTION : "Encore un des volcans en activité sur l'îles de surabaya",
            HAUT : "Le Sanctuaire de Candi Mendut",
            BAS : "Les Valées du Baliem",
            GAUCHE : "océan",
            DROITE : "Volcan du Krakatoa",
            ACTION : "None",# item fruit du démon boost
          },
          "Volcan du Krakatoa": { #C10
            DESCRIPTION : "Qui dit terre des volcan,\nil en faut bien un encore en activité et qui cache plus que de la lave en son sein",
            HAUT : "Les Grottes de Leang-Leang",
            BAS : "Le Village de Sulawesi",
            GAUCHE : "Les Montagnes de Bromo",
            DROITE : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            ACTION : "combat",# Monstre de lave
          },
          "Les bassins d'eaux Sacrées de Pura Tirta Empul": { #C11
            DESCRIPTION : "Les bassins d'eaux sacré sont comme sité ici SACRÉES ! gare à toi...",
            HAUT : "Les plaines du Dragon de Komodo",
            BAS : "Les Rizières de Jatiluwih",
            GAUCHE : "Volcan du Krakatoa",
            DROITE : "La Fôret de Kalimantan",
            ACTION : "combat",#Tigre de Sumatra 
          },
          "La Fôret de Kalimantan": { #C12
            DESCRIPTION : "Jamais une fôret t'aura paru aussi paisible et ceci grace à sa faune bien gardé par le seigneur de la Fôret",
            HAUT : "Les Ruines du Borobudur",
            BAS : "Village de Pêcheur abandonné",
            GAUCHE : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            DROITE : "ravin",
            ACTION : "maitre",# Barong  
          },
          "Les Valées du Baliem": { #C13
            DESCRIPTION : "Vallée ayant la réputation de trouver les oiseaux les plus majestueux de l'Iles les Garuda...",
            HAUT : "Les Montagnes de Bromo",
            BAS : "ravin",
            GAUCHE : "océan",
            DROITE : "Le Village de Sulawesi",
            ACTION : "combat",#Jatayu
          },
          "Le Village de Sulawesi": { #C14
            DESCRIPTION : "Village dans les montagnes abrites des habitants très sympathiques,\n mais tu devras y faire tes preuvent pour rester...",
            HAUT : "Volcan du Krakatoa",
            BAS : "ravin",
            GAUCHE : "Les Valées du Baliem",
            DROITE : "Les Rizières de Jatiluwih",
            ACTION : "combat",#Champion du village
          },
          "Les Rizières de Jatiluwih": { #C15
            DESCRIPTION : "Paysage impressionant pour ces rizières de riz en étages comme des nuages d'eau sur terre.",
            HAUT : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            BAS : "ravin",
            GAUCHE : "Le Village de Sulawesi",
            DROITE : "Village de Pêcheur abandonné",
            ACTION : "None",#Arme 
          },
          "Village de Pêcheur abandonné": { #C16
            DESCRIPTION : "Ton aventure commence dans ce village de pêcheur abandonné sur les terres volcanic indonésienne...ne t`y brule pas...",
            HAUT : "La Fôret de Kalimantan",
            BAS : "ravin",
            GAUCHE : "Les Rizières de Jatiluwih",
            DROITE : "ravin",
            ACTION : "None",
          },
          "Port de Nagoya": { #P1
            DESCRIPTION : "Le Port de Nagoya te mènera directement à ta quête vers Yashin",
            HAUT : "océan",
            BAS : "océan",
            GAUCHE : "PLage de Shirahama",
            DROITE : "Le Dernier Temple du Savoir",
            ACTION : "None",
          },
          "Port de Mao": {#P2
            DESCRIPTION : "Port construit au nom du grand Mao Zedong",
            HAUT : "PLage de Shirahama",
            BAS : "Plage de Qingdao",
            GAUCHE : "océan",
            DROITE : "océan",
            ACTION : "None",
          },
          "Port de Ningbo-Zhoushan": {#P3
            DESCRIPTION : "Le seul Port qui t'emmènera vers la terre des volcan...Indonesia",
            HAUT : "océan",
            BAS : "océan",
            GAUCHE : "Plage de Qingdao",
            DROITE : "Plage de Raja Ampat",
            ACTION : "None",
          },
          "Port de Gili trawangan": { #P4
            DESCRIPTION : "Le Seul Port d'indonésie qui t'emmènera vers le salut et qui n'est pas de la charcuterie....",
            HAUT : "Le Dernier Temple du Savoir",
            BAS : "Plage de Raja Ampat",
            GAUCHE : "océan",
            DROITE : "océan",
            ACTION : "None",
          },
          "Le Dernier Temple du Savoir": { #Temple
            DESCRIPTION : "Tu pensais tout savoir ? dans ce Temple vie un homme qui sait vraiment tout ...",
            HAUT : "océan",
            BAS : "Port de Gili trawangan",
            GAUCHE : "Port de Nagoya",
            DROITE : "Boss",
            ACTION : "None",
          },
          "Boss": {
            DESCRIPTION : "Enfin dans l'entre du mal, est ce que tout se périple sera fait en vain ? à toi de voir... ",
            HAUT : "océan",
            BAS : "océan",
            GAUCHE : "Temple",
            DROITE : "océan",
            ACTION : "combat",
          },
}