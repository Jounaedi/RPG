###########################################################
#Monstre

NOM = "NOM"
DESCRIPTIF = "DESCRIPTIF"
HP = "HP"
ATT = "ATT"
DEF = "DEF"
RECOMPENSE = "RECOMPENSE"

#MONSTRES JAPONAIS

monstre = { 
            "Les Plaines d'Izuhara": { #A2
                NOM : "Ronin",
                DESCRIPTIF : "Ce guerrier sans maître expert en Katana, défi quiconque foule les plaines d'Izuhara",
                HP : 50,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : ["Katana de ronin", 0, 0, 0, 20] 
            },

            "Okuno-in" : { #A3
                NOM : "Kasha",
                DESCRIPTIF : "être malveillant qui se rend aux cérémonies funèbres pour dérober les corps des défunts avant la crémation",
                HP : 15,
                ATT : 5,
                DEF : 10,
                RECOMPENSE : ["XP", 100, 0, 0, 0] 
            },
            
            "La Fôret Aokigahara" : { #A4
                NOM : "Le Yurei",
                DESCRIPTIF:"Fantômes de personnes qui se sont données la mort dans cette fôret ne pouvant trouver le chemin vers l'au-delà, \n espères trouver leur salut en volant l'ames des personnes s'aventurant dans celle-ci",
                HP : 50,
                ATT : 5,
                DEF : 25,
                RECOMPENSE : ["Potion HP", 0, 50, 0, 0]
            },
                       
            "Le fleuve Shinano-Gawa" : { #A5
                NOM : "Le Kappa",
                DESCRIPTIF:"l'Enfant de la rivière connu sous le nom de Kappa attire tout personnes proche du fleuve pour ensuite les noyer et les mangers.",
                HP : 25,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : ["XP", 100, 0, 0, 0]  
            },

            "Le donjon HIkone" : { #A6
                NOM : "Garde du Donjon",
                DESCRIPTIF: "Le garde n'ayant vu personne depuis des lustres il a besoin d'une bonne BAGARRE",
                HP : 10,
                ATT : 7,
                DEF : 40,
                RECOMPENSE : ["XP", 100, 0, 0, 0]
            },    

            "Les Onsen" : { #A7
                 NOM : "Jiraya",
                 DESCRIPTIF:"Maitre des grenouilles",
                 HP : 0,
                 ATT : 0,
                 DEF : 0,
                 RECOMPENSE : ["Armure d'expérience", 0, 0, 20, 0]
            },

            "Sanctuaire Shinto" : { # A8
                NOM : "Le Otoroshi", 
                DESCRIPTIF:"Le Otoroshi monstre recouvert de poil dont on voit seulement ces longues dents et ces griffes, gardien du sanctuaire vous laissera t-il y entrer ? ",
                HP : 90,
                ATT : 20,
                DEF : 90,
                RECOMPENSE : ["Fourrure de l'Otoroshi", 0, 0, 100, 0]
            },

            "Les chutes de Fukuroda" : { #A9
                NOM : "Le Nure-Onna",
                DESCRIPTIF:"La femme serpent humide",
                HP : 100,
                ATT : 30,
                DEF : 50,
                RECOMPENSE : ["Arme yumi serpent blanc", 0, 0, 50, 15]
            },

            "La fôret de Sagano" : { #Maitre  A10
                NOM : "Le Kodama",
                DESCRIPTIF:"Le Kodama esprit de la Fôret saura te guider dans ta quête du Dieu Yashin",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Armure spirituel de la foret de Bamboo", 0, 0, 50, 0]
            },
            
            "Le Mont Fuji" : { #A11
                NOM: "Kitsune",
                DESCRIPTIF:"Kitsune le fameux renard à 9 queues se cache pret du mont fuji et prend sa force de cette célèbre montagne",
                HP : 100,
                ATT : 40,
                DEF : 0,
                RECOMPENSE : ["La yari", 0, 0, 0, 25]

            },

            "Les mines d'or de Sado" : { #A12
                NOM : "Le Rokurokubi",
                DESCRIPTIF: "Têtes volante dévorant les êtres humains qui se perde dans leur mine",
                HP : 100,
                ATT : 20,
                DEF : 50,
                RECOMPENSE : ["xp", 100, 0, 0, 0]
            },
            
            "Le Dojo" : { #A13
                NOM : "Miyamamoto Musashi",
                DESCRIPTIF: "Miyamoto Musashi, de son vrai nom Shinmen Bennosuke \n est le plus grand de tout les combattants au corps à corps avec son sabre, \n il t'apprendra tout les rudiment du combat pour ne jamais perdre (ou presque) ",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["le Nodashi", 0, 0, 0, 40]
            },

            "La cité Milléniale" : { #A14
                NOM : "Kitaro Nishida",
                DESCRIPTIF: "Un des plus grands philosophes du Japon en pleine réflexion te voyant perdu te révèle que tu dois répondre à des énigmes très difficiles posés par Yashin pour affronter le Tengu.La réponse à la première des enigmes de Yashin il l'a connait.. ",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["xp", 100, 0, 0, 0]
            },

            "Le Lac Ashi" : { #A15
                NOM : "Nourriture",
                DESCRIPTIF: "Tu trouve au bord de ce Lac un feu de camp délaisser avec un poisson venant du lac griller à la broche",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["nourriture", 0, 40, 0, 0]
            },

            "PLage de Shirahama" : { #A16
                NOM : "Sables mouvant",
                DESCRIPTIF: "Sur cette plage le sable n'est pas comme les autres,\n tu es pris dans des sables mouvants.\n tu arrive à t'en tirer mais pas sans mal tu perd 10 HP",
                HP : 10,
                ATT : 15,
                DEF : 0,
                RECOMPENSE : ["bouteille cassé", 0, 0, 0, 5]
            },
            

#MONSTRES CHINOIS Beaucoup de Masters
            "les Collines de Yangshuo" : { #B1
                NOM :"Jin Chan",
                DESCRIPTIF: "Posé sur son nénuphare le crapaud d'or attend avec impatience de donner bonne fortune à un jeune guerrier... ",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["lotus d'expérience", 0, 0, 0, 5]
            },

            "La Vieille Ville de Fenghuang" : { # B2
                NOM : "Le Fenghuang",
                DESCRIPTIF: "Le Phoenix à 9 têtes autrement appelé la machine diabolique protège la ville de Fenghuang qui ose y entrer l'oiseau apparaît ",
                HP : 100,
                ATT : 15,
                DEF : 0,
                RECOMPENSE : ["Boost de feu", 0, 50, 0, 0] 
            },

            "La Fôret de Xueling" : { #B3
                NOM : "Wukong",
                DESCRIPTIF: "Pour une Fôret de légende il faut un êtres qui la garde aussi légendaire.Inutile de le présenter...",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Baton de l'être divin wukong", 0, 0, 0, 25]
            },

            "Plage de Qingdao" : { #B4
                NOM : "Torsion de cheville",
                DESCRIPTIF: "Emervillé par la plage tu ne vois pas un trou creusé par un crabe,\n tu te tord la cheville et perd 5HP ",
                HP : 5,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : ["Baton en bois", 0, 0, 0, 1]
            },

             "Les Chutes d'Eau Huangguoshu" : { #B5
                NOM : "Mogwai",
                DESCRIPTIF: "Le Mogwai être maléfique détestant l'être humain...vous savez quoi faire... ",
                HP : 90,
                ATT : 15,
                DEF : 10,
                RECOMPENSE : ["Dao", 0, 0, 0, 15]
            },

            "Le désert de Gobi" : { #B6
                NOM : "Déshydratation",
                DESCRIPTIF: "Te voilà en plein désert et en manque d'eau sela te coute 10 points de vies",
                HP : 1,
                ATT : 10,
                DEF : 0,
                RECOMPENSE : ["eau croupi", 0, 1, 0, 0]
            },

            "La Vallée de Jiuzhaigou" : { #B7
                NOM : "eau de source",
                DESCRIPTIF: "un peu d'eaux asis ?",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["eau", 0, 15, 0, 0]
            },

            "Les Montagnes du Tiashan" : { #B8
                NOM : "Long",
                DESCRIPTIF: "dans le fond de la Montagne du Tiashan se cache un dragon attention si vous le réveillé",
                HP : 25,
                ATT : 10,
                DEF : 100,
                RECOMPENSE : ["armure en écaille de dragons", 0, 0, 50, 0] 
            },

            "Fleuve du Yangzi Jiang" : { #B9
                NOM : "Baku",
                DESCRIPTIF: "Le léopard blanc Baku surveille quiconque ose regarder son fleuve et le mange tout cru",
                HP : 75,
                ATT : 15,
                DEF : 0,
                RECOMPENSE : ["Regard du délin", 0, 0, 0, 10]
            },

            "La Cité Interdite" : { #B10
                NOM : "Shi",
                DESCRIPTIF:"Shi est le lion de pierre qui garde la cité interdite prend vie si quiconque essaie d'entrer dans celle-ci",
                HP : 95,
                ATT : 2,
                DEF : 100,
                RECOMPENSE : ["Arme Fu", 0, 0, 0, 30]
            },

            "La Grande Muraille" : { #B11
                NOM : "Le dernier guerrier d'argile",
                DESCRIPTIF: "L'un des derniers soldats en terre cuite qui protège la grande muraille des personnes voulant le franchir...",
                HP : 15,
                ATT : 5,
                DEF : 20,
                RECOMPENSE : ["Lance du guerrier le Qiang", 0, 0, 0, 15]
            },
            
            "Temple du Ciel Shaoline" : { #B12 Maître
                NOM : "Moine Shaoline",
                DESCRIPTIF:"Un Maître Shaoline t'invite dans la 36ème Chambre pour t'inculqué les rudiments du combat des Moines Shaoline",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["baton de Shaoline", 0, 0, 20, 10] 
            },

            "Le Palais du Potala" : { #B14
                NOM : "Dalai lama",
                DESCRIPTIF: "En personne le Dalai Lama t'accueil, chef spirituel et temporel pour tout les tibétains.Tais-toi et médite",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Repos spirituel", 0, 20, 0, 0] 
            },

            "Monastère des 10000 Bouddhas" : { #B15
                NOM : "Guanyin",
                DESCRIPTIF: "La statue aux milles mains...attention aux baffes si tu n'est pas digne de connaître un des secrets de Yahsin...",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["xp", 100, 0, 0, 0]   
    },
            "Les Falaises de Xuankong" : { #B16
                NOM : "Golem",
                DESCRIPTIF:"Géant de Pierre tel un Moaï sortant de sa falaise prêt à écraser tout les intrus  ",
                HP : 80,
                ATT : 5,
                DEF : 80,
                RECOMPENSE : ["Coeur du Golem", 0, 10, 0, 0]
    },

    ##### MOnstres et maitres indonesien

            "Plage de Raja Ampat" : { #C1
                NOM : "Noix de coco",
                DESCRIPTIF: "En arrivant sur la plage de Raja Ampat emerveiller par la plage tu ne te rend pas compte et une noix de coco te tombe sur le pied",
                HP : 5,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : ["xp", 50, 0, 0, 0] 
    },    

            "La Jungle de Kawah Ijen" : { #C2
                NOM : "Rangda",
                DESCRIPTIF: "LA reine des sorcières , \n mangeuse d'enfants attend qu'une chose est de tuer Barong, lui en empechera tu ?",
                HP : 100,
                ATT : 25,
                DEF : 50,
                RECOMPENSE : ["Peau de sorcière", 0, 0, 10, 0]
    },

            "La Cité des Singes" : { #C3
                NOM : "hanuman",
                DESCRIPTIF: "Diviné le dieu-singe, patron des lutteurs et des acrobates,\n des arts martiaux mais aussi dieu de la sagesse et de la méditation",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Baton du roi singe", 0, 0, 0, 15]
    },

            "Le Chateau des Démons" : { #C4
                NOM : "Ravana",
                DESCRIPTIF: "Roi des démons et autrement appelé Dosomuko (démons a 10 têtes)\npossède dans son Kriss l'ame de ceux qu'il tue",
                HP : 75,
                ATT : 15,
                DEF : 35,
                RECOMPENSE : ["Kriss", 0, 0, 0, 15]
    },
            "Le Sanctuaire de Candi Mendut" : { #C5
                NOM : "Rama",
                DESCRIPTIF: "Rama dieu de la sagesse t'accueil dans son sanctuaire en te donnant la réponse la 3ème énigme de Yashin...garde la précieusement",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["xp", 100, 0, 0, 0]
    },

            "Les Grottes de Leang-Leang" : { #C6
                NOM : "Chauve-souris",
                DESCRIPTIF: "Vous êtes attaqués par des  chauve-souris venant de la grotte vous ne pouvez rien y faire\n elles vous mord de partout vous perdez des points de vie..",
                HP : 10,
                ATT : 10,
                DEF : 0,
                RECOMPENSE : ["xp", 50, 0, 0, 0]
    },
            "Les plaines du Dragon de Komodo" : { #C7
                NOM : "King Komodo",
                DESCRIPTIF: "King komodo le plus puissant , le plus grand de tout les dragons de komodo \n il a faim et il veut manger..de l'humain...",
                HP : 100,
                ATT : 20,
                DEF : 0,
                RECOMPENSE : ["Armure du komodo", 0, 0, 30, 0] 
    },

            "Les Ruines du Borobudur" : { #C8
                NOM : "Louis l'auran-outan",
                DESCRIPTIF: "Autrefois roi de ce temple il reste ici et garde son trésor, son reve etre un jour un homme",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Pendang en or", 0, 10, 10, 20] 
    },

            "Les Montagnes de Bromo" : { #C9
                NOM : "Fruit du démon",
                DESCRIPTIF: "les montagnes de Bromo cache une belle nature tu y trouveras quelque trésors",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Fruit du démon", 0, 10, 10, 20] 
    },

            "Volcan du Krakatoa" : { #C10
                NOM : "Titan de lave",
                DESCRIPTIF: "entierement sortie des entrailles du Volcan, le Titan à besoin d'air...",
                HP : 20,
                ATT : 10,
                DEF : 100,
                RECOMPENSE : ["Armure de lave", 0, 0, 50, 0]  
    },

            "Les bassins d'eaux Sacrées de Pura Tirta Empul" : { #C11
                NOM : "Tigre de Sumatra",
                DESCRIPTIF: "Le gardien des bassins sacrées ne tolère pas qu'un être humain se baigne dans ce lieu...tu va en payer de ta vie.",
                HP : 30,
                ATT : 30,
                DEF : 0,
                RECOMPENSE : ["Griffe de tigre", 0, 10, 0, 12]
    },

            "La Fôret de Kalimantan" : { #C12 maitre
                NOM : "Barong",
                DESCRIPTIF: "Ressemblant à un lion. Il est le seigneur de la forêt,\n chef des forces du bien et ennemi de Rangda..",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Esprit du Barong", 0, 10, 20, 0] 
    },

            "Les Valées du Baliem" : { #C13
                NOM : "Jatayu",
                DESCRIPTIF: "L'oiseau mystique veillant sur sa vallée ne te laissera pas y entrer sans permission...prepare toi...",
                HP : 50,
                ATT : 5,
                DEF : 50,
                RECOMPENSE : ["Le parang", 0, 0, 0, 15]
    },

            "Le Village de Sulawesi" : { #C14
                NOM : "Champion du village",
                DESCRIPTIF: "Le champion du village te défi à main nu dans ces montagne l'air manque,\n parviendra tu à le battre ?",
                HP : 25,
                ATT : 10,
                DEF : 25,
                RECOMPENSE : ["Karambit", 0, 0, 0, 10]
    },

            "Les Rizières de Jatiluwih" : { #C15
                NOM : "Agriculteur de riz",
                DESCRIPTIF: "l'agriculteur n'a rien sauf son bien le plus chere...son riz",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Portion de riz", 0, 5, 0, 5]
    },

            "Le Dernier Temple du Savoir" : { #Temple #A14 #B15 #C5
                NOM : "Yashin",
                DESCRIPTIF: " Un vieil homme se tient devant le temple, \n Il me devisage et me bloque le passage.",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Shiguriu légendaire", 0, 20, 30, 20]
    },

            "Boss" : { #
                NOM : "Le Tengu",
                DESCRIPTIF: "Le tengu autrement appelé le chien céleste, créature légendaire présente dans tout  le folklore asiatique avec son long nez et son visage rouge,\n est le plus puissant de tout les créatures présentes dans ce monde...\ncomment le vaincra tu ?",
                HP : 100,
                ATT : 50,
                DEF : 100,
                RECOMPENSE : ["Gloire du vainqueur", 100, 0, 0, 0] 
    },    

}