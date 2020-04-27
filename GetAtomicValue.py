print("Welcome to Python Periodic Table")
print("Search your element when you type a atomic number. It contains 118 elements.")
print("You can list your elements(Eg:Gas, Liquid, Solid)")
print("I hope you are enjoy this.")
print("Type 'exit' to exit the program")
atomic={"1":"\nHydrogen\nSymbol-H\nLatin Name-Hydrogenium\n\nBlock-S\nGroup-1\nPeriod-1\n\nMelting Point-14.01K\nBoiling Point-1615K\nAtomic Mass-1.00794u\n\nElectrons-1\nProtons-1\nNeotrons-0\n\nYear Discovered-1766\nElectron shell configuration-1\nDiscovered By-Henry Cavendish\n\nPhase-Gas\n",
    "2":"\nHelium\nSymbol-He\nLatin Name-Helium\n\nBlock-S\nGroup-2\nPeriod-1\n\nMelting Point-0.95K\nBoiling Point-4.216K\nAtomic Mass-4.0026u\n\nElectrons-2\nProtons-2\nNeotrons-2\n\nYear Discovered-1895\nElectron shell configuration-2\nDiscovered By:Pierre Jules Cesar Janssen, Joseph Norman Lockyer\n\nPhase-Gas\n",
    "3":"\nLithium\nSymbol-Li\nLatin Name-Lithium\n\nBlock-S\nGroup-1\nPeriod-2\n\nMelting Point-453.7K\nBoiling Point-1615K\nAtomic Mass-6.941u\n\nElectrons-3\nProtons-3\nNeotrons-4\n\nYear Discovered-\nYear Discovered-1817\nElectron shell configuration-2,1\nDiscovered By:Johan August Arfwedson\n\nPhase-Solid\n",
    "4":"\nBeryllium\nSymbol-Be\nLatin Name-Beryllium\n\nBlock-S\nGroup-2\nPeriod-2\n\nMelting Point-1560K\nBoiling point-3243K\nAtomic Mass-9.01218u\n\nElectrons-4\nProtons-4\nNeotrons-5\n\nYear Discovered-1798\nElectron shell configuration-2,2\nDiscovered By:Louis-Nicolas Vauquelin\n\nPhase-Solid\n",
    "5":"\nBoron\nSymbol-B\nLatin Name-Borum\n\nBlock-P\nGroup-13\nPeriod-2\n\nMelting Point-2365K\nBoiling Point-4276K\nAtomic Mass-10.811u\n\nElectrons-5\nProtons-5\nNeotrons-6\n\nYear Discovered-1808\nElectron shell configuration-2,3\nDiscovered By:Joseph Louis Gay-Lussac, Louis Jacques Thenard, Humphry Davy\n\nPhase-Solid\n",
    "6":"\nCarbon\nSymbol-C\nLatin Name-Carbonium\n\nBlock-P\nGroup-14\nPeriod-2\n\nMelting Point-3825K\nBoiling Point-5100K\nAtomic Mass-12.0107u\n\nElectrons-6\nProtons-6\nNeotrons-6\n\nYear Discovered-Deep antiquity\nElectron shell configuration-2,4\nDiscovered By:Humphry Davy\n\nPhase-Solid\n",
    "7":"\nNitrogen\nSymbol-N\nLatin Name-Nitrogenium\n\nBlock-P\nGroup-15\nPeriod-2\n\nMelting Point-63.15K\nBoiling Point-77.34K\nAtomic Mass-14.0067u\n\nElectrons-7\nProtons-7\nNeotrons-7\n\nYear Discovered-1772\nElectron shell configuration-2,5\nDiscovered By:Daniel Rutherford\n\nPhase-Gas\n",
    "8":"\nOxygen\nSymbol-O\nLatin Name-Oxygenium\n\nBlock-P\nGroup-16\nPeriod-2\n\nMelting Point-54.8K\nBoiling Point-90.19K\nAtomic Mass-15.9994u\n\nElectrons-8\nProtons-8\nNeotrons-8\n\nYear Discovered-1774\nElectron shell configuration-2,6\nDiscovered By:Michal Sedziwoj, Joseph Priestly, Carl Wilhelm Scheele\n\nPhase-Gas\n",
    "9":"\nFluorine\nSymbol-F\nLatin Name-Fluorum\n\nBlock-P\nGroup-17\nPeriod-2\n\nMelting Point-53.55K\nBoiling Point-85K\nAtomic Mass-18.9984u\n\nElectrons-9\nProtons-9\nNeotrons-10\n\nYear Discovered-1886\nElectron shell configuration-2,7\nDiscovered By:Ferdinand Frederic Henri Moissan\n\nPhase-Gas\n",
    "10":"\nNeon\nSymbol-Ne\nLatin Name-Neon\n\nBlock-P\nGroup-18\nPeriod-2\n\nMelting Point-24.55K\nBoiling Point-27.1K\nAtomic Mass-20.1797u\n\nElectrons-10\nProtons-10\nNeotrons-10\n\nYear Discovered-1898\nElectron shell configuration-2,8\nDiscovered By:Sir William Ramsay, Morris William Travers\n\nPhase-Gas\n",
    "11":"\nSodium\nSymbol-Na\nLatin Name-Natrium\n\nBlock-S\nGroup-1\nPeriod-3\n\nMelting Point-371K\nBoiling Point-1156K\nAtomic Mass-22.9898u\n\nElectrons-11\nProtons-11\nNeotrons-12\n\nYear Discovered-1807\nElectron shell configuration-2,8,1\nDiscovered By:Humphry Davy\n\nPhase-Solid\n",
    "13":"\nAluminium\nSymbol-Al\nLatin Name-Aluminium\n\nBlock-P\nGroup-13\nPeriod-3\n\nMelting Point-933.5K\nBoiling Point-2740K\nAtomic Mass-26.9815u\n\nElectrons-13\nProtons-13\nNeotrons-14\n\nYear Discovered-1825\nElectron shell configuration-2,8,3\nDiscovered By:Hans Christian Orsted\n\nPhase-Solid\n",
    "12":"\nMagnesium\nSymbol-Mg\nLatin Name-Magnesium\n\nBlock-S\nGroup-2\nPeriod-3\n\nMelting Point-922K\nBoiling Point-1380K\nAtomic Mass-24.305u\n\nElectrons-12\nProtons-12\nNeotrons-12\n\nYear Discovered-1808\nElectron shell configuration-2,8,2\nDiscovered By:Joseph Black, Humphry Davy\n\nPhase-Solid\n",
    "14":"\nSilicon\nSymbol-Si\nLatin Name-Silicium\n\nBlock-P\nGroup-14\nPeriod-3\n\nMelting Point-1683K\nBoiling Point-2630K\nAtomic Mass-28.855u\n\nElectrons-14\nProtons-14\nNeotrons-14\n\nYear Discovered-1824\nElectron shell configuration-2,8,4\nDiscovered By:Jons Jakob Berzelius\n\nPhase-Solid\n",
    "15":"\nPhosphours\nSymbol-P\nLatin Name-Phosphorus\n\nBlock-P\nGroup-15\nPeriod-3\n\nMelting Point-317.3K\nBoiling Point-553K\nAtomic Mass-30.9738u\n\nElectrons-15\nProtons-15\nNeotrons-16\n\nYear Discovered-1669\nElectron shell configuration-2,8,5\nDiscovered By:Henning Brand\n\nPhase-Solid\n",
    "16":"\nSulfur\nSymbol-S\nLatin Name-Sulphur\n\nBlock-P\nGroup-16\nPeriod-3\n\nMelting Point-392.2K\nBoiling Point-717.8K\nAtomic Mass-32.065u\n\nElectrons-16\nProtons-16\nNeotrons-16\n\nYear Discovered- <600 BCE\nElectron shell configuration-2,8,6\nDiscovered By:--\n\nPhase-Solid\n",
    "17":"\nChlorine\nSymbol-Cl\nLatin Name-Chlorum\n\nBlock-P\nGroup-17\nPeriod-3\n\nMelting Point-172.2K\nBoiling Point-239.2K\nAtomic Mass-35.453u\n\nElectrons-17\nProtons-17\nNeotrons-18\n\nYear Discovered-1774\nElectron shell configuration-2,8,7\nDiscovered By:Carl Wilhelm Scheele\n\nPhase-Gas\n",
    "18":"\nArgon\nSymbol-Ar\nLatin Name-Argon\n\nBlock-P\nGroup-18\nPeriod-3\n\nMelting Point-83.95k\nBoiling Point-87.45K\nAtomic Mass-39.948u\n\nElectrons-18\nProtons-18\nNeotrons-22\n\nYear Discovered-1884\nElectron shell configuration-2,8,8\nDiscovered By:Sir William Ramsay\n\nPhase-Gas\n",
    "19":"\nPotassium\nSymbol-K\nLatin Name-Kalium\n\nBlock-S\nGroup-1\nPeriod-4\n\nMelting Point-336.8K\nBoiling Point-1033K\nAtomic Mass-39.983u\n\nElectrons-19\nProtons-19\nNeotrons-20\n\nYear Discovered-1807\nElectron shell configuration-2,8,9\nDiscovered By:Humphry Devy\n\nPhase-Solid\n",
    "20":"\nCalcium\nSymbol-Ca\nLatin Name-Calcium\n\nBlock-S\nGroup-2\nPeriod-4\n\nMelting Point-1112K\nBoiling Point-1757K\nAtomic Mass-40.078u\n\nElectrons-20\nProtons-20\nNeotrons-20\n\nYear Discovered-1808\nElectron shell configuration-2,8,8,2\nDiscovered By:Humphry Davy\n\nPhase-Solid\n",
    "21":"\nScandium\nSymbol-Sc\nLatin Name-Scandium\n\nBlock-D\nGroup-3\nPeriod-4\n\nMelting Point-1814K\nBoiling Point-3109K\nAtomic Mass-44.9559u\n\nElectrons-21\nProtons-21\nNeotrons-24\n\nYear Discovered-1879\nElectron shell configuration-2,8,9,2\nDiscovered By:Lars Fredrik Nilson\n\nPhase-Solid\n",
    "22":"\nTitanium\nSymbol-Ti\nLatin Name-Titanium\n\nBlock-D\nGroup-4\nPeriod-4\n\nMelting Point-1935K\nBoiling Point-3560K\nAtomic Mass-47.867u\n\nElectrons-22\nProtons-22\nNeotrons-26\n\nYear Discovered-1795\nElectron shell configuration-2,8,10,2\nDiscovered By:William Gregor\n\nPhase-Solid\n",
    "23":"\nVanadium\nSymbol-v\nLatin Name-Vanadium\n\nBlock-D\nGroup-5\nPeriod-4\n\nMelting Point-2163K\nBoiling Point-3650K\nAtomic Mass-50.9415u\n\nElectrons-23\nProtons-23\nNeotrons-28\n\nYear Discovered-1830\nElectron shell configuration-2,8,11,2\nDiscovered By:Andres Manuel del Rio\n\nPhase-Solid\n",
    "24":"\nChromium\nSymbol-Cr\nLatin Name-Chromium\n\nBlock-D\nGroup-6\nPeriod-4\n\nMelting Point-2130K\nBoiling Point-2945K\nAtomic Mass-51.9961u\n\nElectrons-24\nProtons-24\nNeotrons-28\n\nYear Discovered-1797\nElectron shell configuration-2,8,13,1\nDiscovered By:Louis-Nicolas Vauquelin\n\nPhase-Solid\n",
    "25":"\nManganese\nSymbol-Mn\nLatin Name-Manganum\n\nBlock-D\nGroup-7\nPeriod-4\n\nMelting Point-1518K\nBoiling Point-2235K\nAtomic Mass-54.938u\n\nElectrons-25\nProtons-25\nNeotrons-30\n\nYear Discovered-1774\nElectron shell configuration-2,8,13,2\nDiscovered By:Johan Gottlieb Gahn, Ignatius Gottfried Kaim\n\nPhase-Solid\n",
    "26":"\nIron\nSymbol-Fe\nLatin Name-Ferum\n\nBlock-D\nGroup-8\nPeriod-4\n\nMelting Point-1808K\nBoiling Point-3023K\nAtomic Mass-55.845u\n\nElectrons-26\nProtons-26\nNeotrons-30\n\nYear Discovered-Deep antiquity\nElectron shell configuration-2,8,14,2\nDiscovered By:--\n\nPhase-Solid\n",
    "27":"\nCobalt\nSymbol-Co\nLatin\nName-Cobaltum\n\nBlock-D\nGroup-9\nPeriod-4\n\nMelting Point-1768K\nBoiling Point-3143K\nAtomic Mass-58.9332u\n\nElectrons-27\nProtons-27\nNeotrons-32\n\nYear Discovered-1735\nElectron shell configuration-2,8,15,2\nDiscovered By:Georg Brandt\n\nPhase-Solid\n",
    "28":"\nNickel\nSymbol-Ni\nLatin Name-Niccolum\n\nBlock-D\nGroup-10\nPeriod-4\n\nMelting Point-1726K\nBoiling Point-3005K\nAtomic Mass-58.6934u\n\nElectrons-28\nProtons-28\nNeotrons-31\n\nYear Discovered-1751\nElectron shell configuration-2,8,16,2\nDiscovered By:Axel Frederic von Cronstedt\n\nPhase-Solid\n",
    "29":"\nCopper\nSymbol-Cu\nLatin Name-Cuprum\n\nBlock-D\nGroup-11\nPeriod-5\n\nMelting Point-1357K\nBoiling Point-2840K\nAtomic Mass-63.546u\n\nElectrons-29\nProtons-29\nNeotrons-35\n\nYear Discovered-Deep antiquity\nElectron shell configuration-2,8,18,1\nDiscovered By:--\n\nPhase-Solid\n",
    "30":"\nZinc\nSymbol-Zn\nLatin Name-Zincum\n\nBlock-D\nGroup-12\nPeriod-4\n\nMelting Point-692.7K\nBoiling Point-1180K\nAtomic Mass-65.38u\n\nElectrons-30\nProtons-30\nNeotrons-35\n\nYear Discovered-1300-1000 BCE\nElectron shell configuration-2,8,18,2\nDiscovered By:Andreas Sigismund Marggraf\n\nPhase-Solid\n",
    "31":"\nGallium\nSymbol-Ga\nLatin Name-Gallium\n\nBlock-P\nGroup-13\nPeriod-4\n\nMelting Point-302.9K\nBoiling Point-2478\nAtomic Mass-69.723u\n\nElectrons-31\nProtons-31\nNeotrons-39\n\nYear Discovered-1875\nElectron shell configuration-2,8,18,3\nDiscovered By:Paul Emile Lecoq de Boisbaudran\n\nPhase-Solid\n",
    "32":"\nGermanium\nSymbol-Ge\nLatin Name-Germanium\n\nBlock-P\nGroup-14\nPeriod-4\n\nMelting Point-1212K\nBoiling Point-3107K\nAtomic Mass-72.64u\n\nElectrons-32\nProtons-32\nNeotrons-41\n\nYear Discovered-1886\nElectron shell configuration-2,8,18,4\nDiscovered By:Clemens Alexander Winkler\n\nPhase-Solid\n",
    "33":"\nArsenic\nSymbol-As\nLatin Name-Arsenicum\n\nBlock-P\nGroup-15\nPeriod-4\n\nMelting Point-1090K\nBoiling Point-876K\nAtomic Mass-74.9216u\n\nElectrons-33\nProtons-33\nNeotrons-42\n\nYear Discovered-1250\nElectron shell configuration-2,8,18,5\nDiscovered By:--\n\nPhase-Solid\n",
    "34":"\nSelenium\nSymbol-SE\nLatin Name-Selenium\n\nBlock-P\nGroup-16\nPeriod-4\n\nMelting Point-494K\nBoiling Point-958K\nAtomic Mass-78.96u\n\nElectrons-34\nProtons-34\nNeotrons-45\n\nYear Discovered-1817\nElectron shell configuration-2,8,18,6\nDiscovered By:Jons Jakob Berzelius\n\nPhase-Solid\n",
    "35":"\nBromine\nSymbol-Br\nLatin Name-Bromum\n\nBlock-P\nGroup-17\nPeriod-4\n\nMelting Point-265.9K\nBoiling Point-331.9K\nAtomic Mass-79.904u\n\nElectrons-35\nProtons-35\nNeotrons-45\n\nYear Discovered-1826\nElectron shell configuration-2,8,18,7\nDiscovered By:Antoine-Jerome Balard, Karl Jakob Leuwich\n\nPhase-Liquid\n",
    "36":"\nKrypton\nSymbol-Kr\nLatin Name-Krypton\n\nBlock-P\nGroup-18\nPeriod-4\n\nMelting Point-116K\nBoiling Point-120.8K\nAtomic Mass-83.798u\n\nElectrons-36\nProtons-36\nNeotrons-48\n\nYear Discovered-1898\nElectron shell configuration-2,8,18,8\nDiscovered By:Sir William Ramsay, Morris William Travers\n\nPhase-Gas\n",
    "37":"\nRubidium\nSymbol-Rb\nLatin Name-Rubidium\n\nBlock-S\nGroup-1\nPeriod-5\n\nMelting Point-312.6K\nBoiling Point-961K\nAtomic Mass-85.4678u\n\nElectrons-37\nProtons-37\nNeotrons-48\n\nYear Discovered-1861\nElectron shell configuration-2,8,18,8,1\nDiscovered By:Robert Wilhelm Bunsen, Gustav Robert Kirchhoff\n\nPhase-Solid\n",
    "38":"\nStrontium\nSymbol-Sr\nLatin Name-Strontium\n\nBlock-S\nGroup-2\nPeriod-5\n\nMelting Point-1042K\nBoiling Point-1655K\nAtomic Mass-87.62u\n\nElectrons-38\nProtons-38\nNeotrons-50\n\nYear Discovered-1790\nElectron shell configuration-2,8,18,8,2\nDiscovered By:Andair Crawford\n\nPhase-Solid\n",
    "39":"\nYttrium\nSymbol-Y\nLatin Name-Yttrium\n\nBlock-D\nGroup-3\nPeriod-5\n\nMelting Point-1795K\nBoiling Point-3611k\nAtomic Mass-88.9059u\n\nElectrons-39\nProtons-39\nNeotrons-50\n\nYear Discovered-1794\nElectron shell configuration-2,8,18,8,3\nDiscovered By:Johan Gadolin\n\nPhase-Solid\n",
    "40":"\nZirconium\nSymbol-Zr\nLatin Name-Zriconium\n\nBlock-D\nGroup-4\nPeriod-5\n\nMelting Point-2128K\nBoiling Point-4682K\nAtomic Mass-91.224u\n\nElectrons-40\nProtons-40\nNeotrons-51\n\nYear Discovered-1789\nElectron shell configuration-2,8,18,8,4\nDiscovered By:Martin Heinrich Klaproth\n\nPhase-Solid\n",
    "41":"\nNiobium\nSymbol-Nb\nLatin Name-Niobium\n\nBlock-D\nGroup-5\nPeriod-5\n\nMelting Point-2742K\nBoiling Point-5015K\nAtomic Mass-92.9064u\n\nElectrons-41\nProtons-41\nNeotrons-52\n\nYear Discovered-1801\nElectron shell configuration-2,8,18,8,5\nDiscovered By:Charles Hatchett\n\nPhase-Solid\n",
    "42":"\nMolybdenum\nSymbol-Mo\nLatin Name-Molybdenum\n\nBlock-D\nGroup-6\nPeriod-5\n\nMelting Point-2896K\nBoiling Point-4912K\nAtomic Mass-95.96u\n\nElectrons-42\nProtons-42\nNeotrons-54\n\nYear Discovered-1778\nElectron shell configuration-2,8,18,8,6\nDiscovered By:Carl Wilhelm Scheele\n\nPhase-Solid\n",
    "43":"\nTechnetium\nSymbol-Tc\nLatin Name-Technetium\n\nBlock-D\nGroup-7\nPeriod-5\n\nMelting Point-2477K\nBoiling Point-4538K\nAtomic Mass-98u\n\nElectrons-43\nProtons-43\nNeotrons-55\n\nYear Discovered-1937\nElectron shell configuration-2,8,18,8,7\nDiscovered By:Emilio Gino Segre, Carlo Perrier\n\nPhase-Solid\n",
    "44":"\nRuthenium\nSymbol-Ru\nLatin Name-Ruthenium\n\nBlock-D\nGroup-8\nPeriod-5\n\nMelting Point-2610K\nBoiling Point-4425K\nAtomic Mass-101.07u\n\nElectrons-44\nProtons-44\nNeotrons-58\n\nYear Discovered-1844\nElectron shell configuration-2,8,18,8,8\nDiscovered By:Karl Ernst Claus\n\nPhase-Solid\n",
    "45":"\nRhodium\nSymbol-Rh\nLatin Name-Rhodium\n\nBlock-D\nGroup-9\nPeriod-5\n\nMelting Point-2236K\nBoiling Point-3970K\nAtomic Mass-102.906u\n\nElectrons-45\nProtons-45\nNeotrons-57\n\nYear Discovered-1804\nElectron shell configuration-2,8,18,16,1\nDiscovered By:William Hyde Wollaston\n\nPhase-Solid\n",
    "46":"\nPalladium\nSymbol-Pd\nLatin Name-Palladium\n\nBlock-D\nGroup-10\nPeriod-5\n\nMelting Point-1825K\nBoiling Point-3240K\nAtomic Mass-106.42u\n\nElectrons-46\nProtons-46\nNeotrons-60\n\nYear Discovered-1803\nElectron shell configuration-2,8,18,18\nDiscovered By:William Hyde Wollaston\n\nPhase-Solid\n",
    "47":"\nSilver\nSymbol-Ag\nLatin Name-Argentum\n\nBlock-D\nGroup-11\nPeriod-5\n\nMelting Point-1235K\nBoiling Point-2436K\nAtomic Mass-107.868u\n\nElectrons-47\nProtons-47\nNeotrons-61\n\nYear Discovered-Deep antiquity\nElectron shell configuration-2,8,18,18,1\nDiscovered By:--\n\nPhase-Solid\n",
    "48":"\nCadmium\nSymbol-Cd\nLatin Name-Cadmium\n\nBlock-D\nGroup-12\nPeriod-5\n\nMelting Point-594.3K\nBoiling Point-1040K\nAtomic Mass-112.411u\n\nElectrons-48\nProtons-48\nNeotrons-64\n\nYear Discovered-1817\nElectron shell configuration-2,8,18,18,2\nDiscovered By:--\n\nPhase-Solid\n",
    "49":"\nIndium\nSymbol-In\nLatin Name-Indium\n\nBlock-P\nGroup-13\nPeriod-5\n\nMelting Point-429.8K\nBoiling Point-2350K\nAtomic Mass-114.818u\n\nElectrons-49\nProtons-49\nNeotrons-66\n\nYear Discovered-1863\nElectron shell configuration-2,8,18,18,3\nDiscovered By:Ferdinand Reich\n\nPhase-Solid\n",
    "50":"\nTin\nSymbol-Sn\nLatin Name-Stannum\n\nBlock-P\nGroup-14\nPeriod-5\n\nMelting Point-505.1K\nBoiling Point-2876K\nAtomic Mass-118.71u\n\nElectrons-50\nProtons-50\nNeotrons-69\n\nYear Discovered-Deep antiquity\nElectron shell configuration-2,8,18,18,4\nDiscovered By:--\n\nPhase-Solid\n",
    "51":"\nAntimony\nSymbol-Sb\nLatin Name-Stibium\n\nBlock-P\nGroup-15\nPeriod-5\n\nMelting Point-K\nBoiling Point-1860K\nAtomic Mass-121.76u\n\nElectrons-51\nProtons-51\nNeotrons-71\n\nYear Discovered- <3000 BCE\nElectron shell configuration-2,8,18,18,5\nDiscovered By:Basil Valentine\n\nPhase-Solid\n",
    "52":"\nTellurium\nSymbol-Te\nLatin Name-Tellurium\n\nBlock-P\nGroup-16\nPeriod-5\n\nMelting Point-722.7K\nBoiling Point-1261K\nAtomic Mass-127.6u\n\nElectrons-52\nProtons-52\nNeotrons-75\n\nYear Discovered-1782\nElectron shell configuration-2,8,18,18,6\nDiscovered By:--\n\nPhase-Solid\n",
    "53":"\nIodine\nSymbol-I\nLatin Name-Iodium\n\nBlock-P\nGroup-17\nPeriod-5\n\nMelting Point-386.7K\nBoiling Point-457.5K\nAtomic Mass-126.904u\n\nElectrons-53\nProtons-53\nNeotrons-74\n\nYear Discovered-1811\nElectron shell configuration-2,8,18,18,7\nDiscovered By:--\n\nPhase-Solid\n",
    "54":"\nXenon\nSymbol-Xe\nLatin Name-Xenon\n\nBlock-P\nGroup-18\nPeriod-5\n\nMelting Point-161.4K\nBoiling Point-165.1K\nAtomic Mass-131.293u\n\nElectrons-54\nProtons-54\nNeotrons-77\n\nYear Discovered-1898\nElectron shell configundtion-2,8,18,18,8\nDiscovered By:--\n\nPhase-Gas\n",
    "55":"\nCaesium\nSymbol-Cs\nLatin Name-Caesium\n\nBlock-S\nGroup-1\nPeriod-6\n\nMelting Point-301.5K\nBoiling Point-944K\nAtomic Mass-132.905u\n\nElectrons-55\nProtons-55\nNeotrons-78\n\nYear Discovered-1860\nElectron shell configuration-2,8,18,18,8,1\nDiscovered By:Robert Wilhelm Bunsen, Gustav Robert Kirchhoff\n\nPhase-Solid\n",
    "56":"\nBarium\nSymbol-Ba\nLatin Name-Barium\n\nBlock-S\nGroup-2\nPeriod-6\n\nMelting Point-1002K\nBoiling Point-2078K\nAtomic Mass-137.327u\n\nElectrons-56\nProtons-56\nNeotrons-81\n\nYear Discovered-1774\nElectron shell configuration-2,8,18,18,8,2\nDiscovered By:Humphry Davy\n\nPhase-Solid\n",
    "57":"\nLanthanum\nSymbol-La\nLatin Name-Lanthanum\n\nBlock-F\nPeriod-6\nMelting Point-1191K\n\nBoiling Point-3737K\nAtomic Mass-138.905u\nElectrons-57\n\nProtons-57\nNeotrons-82\nYear Discovered-1839\n\nElectron shell configuration-2,8,18,18,9,2\nDiscovered By:Carl Gustaf Mosander\nPhase-Solid\n",
    "58":"\nCerium\nSymbol-Ce\nLatin Name-Cerium\n\nBlock-F\nPeriod-6\nMelting Point-1071K\n\nBoiling Point-3715K\nAtomic Mass-104.116u\nElectrons-58\n\nProtons-58\nNeotrons-82\nYear Discovered-1803\n\nElectron shell configuration-2,8,18,19,9,2\nDiscovered By:--\nPhase-Solid\n",
    "59":"\nPraseodymium\nSymbol-Pr\nLatin Name-Praseodymium\n\nBlock-F\nPeriod-6\nMelting Point-1204K\n\nBoiling Point-3785K\nAtomic Mass-140.908u\nElectrons-59\n\nProtons-59\nNeotrons-82\nYear Discovered-1885\n\nElectron shell configuration-2,8,18,21,8,2\nDiscovered By:Andre-Louis Debierne\nPhase-Solid\n",
    "60":"\nNeodymium\nSymbol-Nd\nLatin Name-Neodymium\n\nBlock-F\nPeriod-6\nMelting Point-1294K\n\nBoiling Point-3347K\nAtomic Mass-144.242u\nElectrons-60\n\nProtons-60\nNeotrons-84\nYear Discovered-1885\n\nElectron shell configuration-2,8,18,22,8,2\nDiscovered By:Carl Auer von Wlsbach\nPhase-Solid\n",
    "61":"\nPromethium\nSymbol-Pm\nLatin Name-Promethium\n\nBlock-F\nPeriod-6\nMelting Point-1315K\n\nBoiling Point-3273K\nAtomic Mass-145u\nElectrons-61\n\nProtons-61\nNeotrons-85\nYear Discovered-1945\n\nElectron shell configuration-2,8,18,23,8,2\nDiscovered By:--\nPhase-Solid\n",
    "62":"\nSamarium\nSymbol-Sm\nLatin Name-Samarium\n\nBlock-F\nPeriod-6\nMelting Point-1347K\n\nBoiling Point-2067K\nAtomic Mass-150.36u\nElectrons-62\n\nProtons-62\nNeotrons-88\nYear Discovered-1879\n\nElectron shell configuration-2,8,18,24,8,2\nDiscovered By:Paul Emile Lecoq de Boisbaudran\nPhase-Solid\n",
    "63":"\nEuropium\nSymbol-Eu\nLatin Name-Europium\n\nBlock-F\nPeriod-6\nMelting Point-1095K\n\nBoiling Point-1800K\nAtomic Mass-151.964u\nElectrons-63\n\nProtons-63\nNeotrons89-\nYear Discovered-1901\n\nElectron shell configuration-2,8,18,25,8,2\nDiscovered By:Eugene-Anatole Demarcay\nPhase-Solid\n",
    "64":"\nGadolinium\nSymbol-Gd\nLatin Name-Gadolinium\n\nBlock-F\nPeriod-6\nMelting Point-1585K\n\nBoiling Point-3545K\nAtomic Mass-157.25u\nElectrons-64\n\nProtons-64\nNeotrons-93\nYear Discovered-1886\n\nElectron shell configuration-2,8,18,25,9,2\nDiscovered By:Jean Charles Galissard de Marignac\nPhase-Solid\n",
    "65":"\nTerbium\nSymbol-Tb\nLatin Name-Terbium\n\nBlock-F\nPeriod-6\nMelting Point-1629K\n\nBoiling Point-3500K\nAtomic Mass-158.925u\nElectrons-65\n\nProtons-65\nNeotrons-93\nYear Discovered-1843\n\nElectron shell configuration-2,8,18,27,8,2\nDiscovered By:Carl Gustaf Mosander\nPhase-Solid\n",
    "66":"\nDysprosium\nSymbol-Dy\nLatin Name-Dysprosium\n\nBlock-F\nPeriod-6\nMelting Point-1685K\n\nBoiling Point-2840K\nAtomic Mass-162.5u\nElectrons-66\n\nProtons-66\nNeotrons-96\nYear Discovered-1886\n\nElectron shell configuration-2,8,18,28,8,2\nDiscovered By:Paul Emile Lecoq de Boisbaudran\nPhase-Solid\n",
    "67":"\nHolmium\nSymbol-Ho\nLatin Name-Holmium\n\nBlock-F\nPeriod-6\nMelting Point-1747K\n\nBoiling Point\nAtomic Mass-164.93u\nElectrons-67\n\nProton-67\nNeotrons-97\nYear Discovered-1878\n\nElectron shell configuration-2,8,18,29,8,2\nDiscovered By:Per Teodor Cleve, Auguste Honore Charlois\nPhase-Solid\n",
    "68":"\nErbium\nSymbol-Er\nLatin Name-Erbium\n\nBlock-F\nPeriod-6\nMelting Point-1802K\n\nBoiling Point-3140K\nAtomic Mass-167.259u\nElectrons-68\n\nProtons-68\nNeotrons-99\nYear Discovered-1842\n\nElectron shell configuration-2,8,18,30,8,2\nDiscovered By:Carl Gustaf Mosander\nPhase-Solid\n",
    "69":"\nThulium\nSymbol-Tm\nLatin Name-Thulium\n\nBlock-F\nPeriod-6\nMelting Point-1818K\n\nBoiling Point-2223K\nAtomic Mass-168.934u\nElectrons-69\n\nProtons-69\nNeotrons-99\nYear Discovered-1879\n\nElectron shell configuration-2,8,18,31,8,2\nDiscovered By:--\nPhase-Solid\n",
    "70":"\nYtterbium\nSymbol-Yb\nLatin Name-Ytterbium\n\nBlock-F\nPeriod-6\nMelting Point-1092K\n\nBoiling Point-1469K\nAtomic Mass-173.054u\nElectrons-70\n\nProtons-70\nNeotrons-103\nYear Discovered-1878\n\nElectron shell configuration-2,8,18,32,8,2\nDiscovered By:Jean Charles Galissard de Marignac\nPhase-Solid\n",
    "71":"\nLutetium\nSymbol-Lu\nLatin Name-Lutetium\n\nBlock-F\nPeriod-6\nMelting Point-1936K\n\nBoiling Point-3668K\nAtomic Mass-174.967u\nElectrons-71\n\nProtons-71\nNeotrons-103\nYear Discovered-1907\n\nElectron shell configuration-2,8,18,32,9,2\nDiscovered By:--\nPhase-Solid\n",
    "72":"\nHafnium\nSymbol-Hf\nLatin Name-Hafnium\n\nBlock-D\nGroup-4\nPeriod-6\n\nMelting Point-2504K\nBoiling Point-4875K\nAtomic Mass-178.49u\n\nElectrons-72\nProtons-72\nNeotrons-106\n\nYear Discovered-1923\nElectron shell configuration-2,8,18,32,10,2\nDiscovered By:--\n\nPhase-Solid\n",
    "73":"\nTantalum\nSymbol-Ta\nLatin Name-Tantalum\n\nBlock-D\nGroup-5\nPeriod-6\n\nMelting Point-3293K\nBoiling Point-5730K\nAtomic Mass-180.948u\n\nElectrons-73\nProtons-73\nNeotrons-108\n\nYear Discovered-1802\nElectron shell configuration-2,8,18,32,11,2\nDiscovered By:--\n\nPhase-Solid\n",
    "74":"\nTungsten\nSymbol-W\nLatin Name-Wolframium\n\nBlock-D\nGroup-6\nPeriod-6\n\nMelting Point-3695K\nBoiling Point-5825K\nAtomic Mass-183.84u\n\nElectrons-74\nProtons-74\nNeotrons-109\n\nYear Discovered-1781\nElectron shell configuration-2,8,18,32,12,2\nDiscovered By:Carl Wilhelm Scheele\n\nPhase-Solid\n",
    "75":"\nRhenium\nSymbol-Re\nLatin Name-Rhenium\n\nBlock-D\nGroup-7\nPeriod-6\n\nMelting Point-3455K\nBoiling Point-5870K\nAtomic Mass-186.207u\n\nElectrons-75\nProtons-75\nNeotrons-111\n\nYear Discovered-1927\nElectron shell configuration-2,8,18,32,13,2\nDiscovered By:--\n\nPhase-Solid\n",
    "76":"\nOsmium\nSymbol-Os\nLatin Name-Osmium\n\nBlock-D\nGroup-8\nPeriod-6\n\nMelting Point-3300K\nBoiling Point-5300K\nAtomic Mass-190.23u\n\nElectrons-76\nProtons-76\nNeotrons-115\n\nYear Discovered-1804\nElectron shell configuration-2,8,18,32,14,2\nDiscovered By:Smithoson Tennant\n\nPhase-Solid\n",
    "77":"\nIridium\nSymbol-Ir\nLatin Name-Iridium\n\nBlock-D\nGroup-9\nPeriod-6\n\nMelting Point-2720K\nBoiling Point-4700K\nAtomic Mass-192.217u\n\nElectrons-77\nProtons-77\nNeotrons-115\n\nYear Discovered-1804\nElectron shell configuration-2,8,18,32,15,2\nDiscovered By:Smithson Tennant\n\nPhase-Solid\n",
    "78":"\nPlatinum\nSymbol-Pt\nLatin Name-Platium\n\nBlock-D\nGroup-10\nPeriod-6\n\nMelting Point-2042K\nBoiling Point-4100K\nAtomic Mass-195.084u\n\nElectrons-78\nProtons-78\nNeotrons-117\n\nYear Discovered-1735\nElectron shell configuration-2,8,18,32,17,1\nDiscovered By:Antonio de Uloa\n\nPhase-Solid\n",
    "79":"\nGold\nSymbol-Au\nLatin Name-Aurum\n\nBlock-D\nGroup-11\nPeriod-6\n\nMelting Point-1388K\nBoiling Point-3130K\nAtomic Mass-196.967u\n\nElectrons-79\nProtons-79\nNeotrons-118\n\nYear Discovered-Deep antiquity\nElectron shell configuration-2,8,18,32,18,1\nDiscovered By:--\n\nPhase-Solid\n",
    "80":"\nMercury\nSymbol-Hg\nLatin Name-Hydrargyrum\n\nBlock-D\nGroup-12\nPeriod-6\n\nMelting Point-234.3K\nBoiling Point-629.9K\nAtomic Mass-200.59u\n\nElectrons-80\nProtons-80\nNeotrons-120\n\nYear Discovered-<1500 BCE\nElectron shell configuration-2,8,18,32,18,2\nDiscovered By:--\n\nPhase-Liquid\n",
    "81":"\nThallium\nSymbol-Tl\nLatin Name-Thallium\n\nBlock-P\nGroup-13\nPeriod-6\n\nMelting Point-577K\nBoiling Point-1746K\nAtomic Mass-204.383u\n\nElectrons-81\nProtons-81\nNeotrons-1861\n\nElectron shell configuration-2,8,18,32,18,3\nDiscovered By:William Crookes\n\nPhase-Solid\n",
    "82":"\nLead\nSymbol-Pb\nLatin Name-Plumbum\n\nBlock-P\nGroup-14\nPeriod-6\n\nMelting Point-600.6K\nBoiling Point-2023K\nAtomic Mass-207.2u\n\nElectrons-82\nProtons-82\nNeotrons-125\n\nYear Discovered-Deep antiquity\nElectron shell configuration-2,8,18,32,18,4\nDiscovered By:--\n\nPhase-Solid\n",
    "83":"\nBismuth\nSymbol-Bi\nLatin Name-Bisemutum\n\nBlock-P\nGroup-15\nPeriod-6\n\nMelting Point-544.6K\nBoiling Point-1837K\nAtomic Mass-208.98u\n\nElectrons-83\nProtons-83\nNeotrons-126\n\nYear Discovered-1450\nElectron shell configuration-2,8,18,32,18,5\nDiscovered By:Claude Francois Geoffrey\n\nPhase-Solid\n",
    "84":"\nPolonium\nSymbol-Po\nLatin Name-Polonium\n\nBlock-P\nGroup-16\nPeriod-6\n\nMelting Point-527K\nBoiling Point-0K\nAtomic Mass-209u\n\nElectrons-84\nProtons-84\nNeotrons-126\n\nYear Discovered-1898\nElectron shell configuration-2,8,18,32,18,6\nDiscovered By:Pierre Curie, mare Sklodowska Curie\n\nPhase-Solid\n",
    "85":"\nAstatine\nSymbol-At\nLatin Name-Astatum\n\nBlock-P\nGroup-17\nPeriod-6\n\nMelting Point-575K\nBoiling Point-610K\nAtomic Mass-210u\n\nElectrons-85\nProtons-85\nNeotrons-125\n\nYear Discovered-1940\nElectron shell configuration-2,8,18,32,18,7\nDiscovered By:Paul Emile Lecoq de Boisbaudran\n\nPhase-Solid\n",
    "86":"\nRadon\nSymbol-Rn\nLatin Name-Radon\n\nBlock-P\nGroup-18\nPeriod-6\n\nMelting Point-202K\nBoiling Point-211.4K\nAtomic Mass-222u\n\nElectrons-86\nProtons-86\nNeotrons-136\n\nYear Discovered-1900\nElectron shell configuration-2,8,18,32,18,8\nDiscovered By:Friedrich Ernst Dorn\n\nPhase-Gas\n",
    "87":"\nFrancium\nSymbol-Fr\nLatin Name-Francium\n\nBlock-S\nGroup-1\nPeriod-7\n\nMelting Point-300K\nBoiling Point-950K\nAtomic Mass-223u\n\nElectrons-87\nProtons-87\nNeotrons-136\n\nYear Discovered-1939\nElectron shell configuration-2,8,18,32,18,8,1\nDiscovered By:Marguerite Perey\n\nPhase-Solid\n",
    "88":"\nRadium\nSymbol-Ra\nLatin Name-Radium\n\nBlock-S\nGroup-2\nPeriod-7\n\nMelting Point-973K\nBoiling Point-1413K\nAtomic Mass-226u\n\nElectrons-88\nProtons-88\nNeotrons-138\n\nYear Discovered-1898\nElectron shell configuration-2,8,18,32,18,8,2\nDiscovered By:Pierre Curie, Marie Sklodowska Curie\n\nPhase-Solid\n",
    "89":"\nActinium\nSymbol-Ac\nLatin Name-Actinium\n\nBlock-F\nPeriod-7\nMelting Point-1324K\n\nBoiling Point-3470K\nAtomic Mass-227u\nElectrons-89\n\nProtons-89\nNeotrons-1938\nYear Discovered-1899\n\nElectron shell configuration-2,8,18,32,18,9,2\nDiscovered By:Andre-Louis Debierne\nPhase-Solid\n",
    "90":"\nThorium\nSymbol-Th\nLatin Name-Thorium\n\nBlock-F\nPeriod-7\nMelting Point-2028K\n\nBoiling Point-5060K\nAtomic Mass-238.038u\nElectrons-90\n\nProtons-90\nNeotrons-142\nYear Discovered-1828\n\nElectron shell configuration-2,8,18,32,18,10,2\nDiscovered By:Jons Jakob Berzelius\nPhase-Solid\n",
    "91":"\nProtactinim\nSymbol-Pa\nLatin Name-Protactinium\n\nBlock-F\nPeriod-7\nMelting Point-1845K\n\nBoiling Point-4300K\nAtomic Mass-231.036u\nElectrons-91\n\nProtons-91\nNeotrons-140\nYear Discovered-1918\n\nElectron shell configuration-2,8,18,32,20,9,2Otto Hahn, Lise Meitner, Frederick Soddy\nPhase-Solid\n",
    "92":"\nUranium\nSymbol-U\nLatin Name-Uranium\nBlock-F\n\nPeriod-7\nMelting Point-1408K\n\nBoiling Point-4470K\nAtomic Mass-238.029u\nElectrons-92\n\nProtons-92\nNeotrons-146\nYear Discovered-1789\n\nElectron shell configuration-2,8,18,32,21,9,2\nDiscovered By:Martin Heinrich Klaproth\nPhase-Solid\n",
    "93":"\nNeptunium\nSymbol-Np\nLatin Name-Neptunium\n\nBlock-F\nPeriod-7\nMelting Point-912K\n\nBoiling Point-4175K\nAtomic Mass-237u\nElectrons-93\n\nProtons-93\nNeotrons-144\nYear Discovered-1940\n\nElectron shell configuration-2,8,18,32,22,9,2\nDiscovered By:--\nPhase-Solid\n",
    "94":"\nPlutonium\nSymbol-Pu\nLatin Name-Pludonium\n\nBlock-F\nPeriod-7\nMelting Point-913\n\nBoiling Point-3505K\nAtomic Mass-244u\nElectrons-94\n\nProtons-94\nNeotrons-150\nYear Discovered-1940\n\nElectron shell configuration-2,8,18,32,24,8,2\nDiscovered By:Glenn Theodore Seaborg\nPhase-Solid\n",
    "95":"\nAmericium\nSymbol-Am\nLatin Name-Americium\n\nBlock-F\nPeriod-7\nMelting Point-1449K\n\nBoiling Point-2880K\nAtomic Mass-234u\nElectrons-95\n\nProtons-95\nNeotrons-148\nYear Discovered-1944\n\nElectron shell configuration-2,8,18,32,25,,8,2\nDiscovered By:Glenn Theodore Seaborg\nPhase-Solid\n",
    "96":"\nCurium\nSymbol-Cm\nLatin Name-Curium\n\nBlock-F\nPeriod-7\nMelting Point-1620K\n\nBoiling Point-3383K\nAtomic Mass-247u\nElectrons-96\n\nProtons-96\nNeotrons-151\nYear Discovered-1944\n\nElectron shell configuration-2,8,18,32,25,9,2\nDiscovered By:Glenn Theodore Seaborg\nPhase-Solid\n",
    "97":"\nBerkelium\nSymbol-Bk\nLatin Name-Berkelium\n\nBlock-F\nPeriod-7\nMelting Point-1258K\n\nBoiling Point-983K\nAtomic Mass-247u\nElectrons-97\n\nProtons-97\nNeotrons-150\nYear Discovered-1949\n\nElectron shell configuration-2,8,18,32,27,8,2\nDiscovered By:Glenn Theodore Seoborg\nPhase-Solid\n",
    "98":"\nCalifornium\nSymbol-Cf\nLatin Name-Californium\n\nBlock-F\nPeriod-7\nMelting Point-1172K\n\nBoiling Point-1743K\nAtomic Mass-251u\nElectrons-98\n\nProtons-98\nNeotrons-153\nYear Discovered-1950\n\nElectron shell configuration-2,8,18,32,28,8,2\nDiscovered By:Glenn Theodore Seoborg\nPhase-Solid\n",
    "99":"\nEinsteinium\nSymbol-Es\nLatin Name-Einsteinium\n\nBlock-F\nPeriod-7\nMelting Point-1133K\n\nBoiling Point-0K\nAtomic Mass-252u\nElectrons-99\n\nProtons-99\nNeotrons-153\nYear Discovered-1952\n\nElectron shell configuration-2,8,18,32,29,8,2\nDiscovered By:Albert Ghiorse\nPhase-Solid\n",
    "100":"\nFermium\nSymbol-Fm\nLatin Name-Fermium\n\nBlock-F\nPeriod-7\nMelting Point-1125K\n\nBoiling Point-0K\nAtomic Mass-257u\nElectrons-100\n\nProtons-100\nNeotrons-157\nYear Discovered-1952\n\nElectron shell configuration-2,8,18,32,30,8,2\nDiscovered By:Glenn Theodore Seoborg\nPhase-Solid\n",
    "101":"\nMendelevium\nSymbol-Md\nLatin Name-Mendelevium\n\nBlock-F\nPeriod-7\nMelting Point-1100K\n\nBoiling Point-0K\nAtomic Mass-258u\nElectrons-101\n\nProtons-101\nNeotrons-157\nYear Discovered-1955\n\nElectron shell configuration-2,8,18,32,31,8,2\nDiscovered By:Glenn Theodore Seoborg\nPhase-Solid\n",
    "102":"\nNobelium\nSymbol-No\nLatin Name-Nobelium\n\nBlock-F\nPeriod-7\nMelting Point-1100K\n\nBoiling Point-0K\nAtomic Mass-259u\nElectrons-102\n\nProtons-102\nNeotrons-157\nYear Discovered-1965\n\nElectron shell configuration-2,8,18,32,32,8,2\nDiscovered By:Tlenn Theodore Seaborg\nPhase-Solid\n",
    "103":"\nLawrencium\nSymbol-Lr\nLatin Name-Lawrencium\n\nBlock-F\nPeriod-7\nMelting Point-1900K\n\nBoiling Point-0K\nAtomic Mass-262u\nElectrons-103\n\nProtons-103\nNeotrons-163\nYear Discovered-1961\n\nElectron shell configuration-2,8,18,32,32,8,3\nDiscovered By:Albert Ghiorso\nPhase-Solid\n",
    "104":"\nRutherfordium\nSymbol-Rf\nLatin Name-Rutherfordium\n\nBlock-D\nGroup-4\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-265u\n\nElectrons-104\nProtons-104\nNeotrons-157\n\nYear Discovered-1964\nElectron shell configuration-2,8,18,32,32,10,2\nDiscovered By:Georgiy Flerov\n\nPhase-Solid\n",
    "105":"\nDubnium\nSymbol-Db\nLatin Name-Dubnium\n\nBlock-D\nGroup-5\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-268u\nElectrons-105\nProtons-105\nNeotrons-157\n\nYear Discovered-1968\nElectron shell configuration-2,8,18,32,32,11,2\nDiscovered By:Georgiy Flerov\n\nPhase-Solid\n",
    "106":"\nSeaborgium\nSymbol-Sg\nLatin Name-Seaborgium\n\nBlock-D\nGroup-6\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-271u\n\nElectrons-106\nProtons-106\nNeotrons-156\n\nYear Discovered-1974\nElectron shell configuration-2,8,18,32,32,10,2\nDiscovered By:Georgiy Flerov\n\nPhase-Solid\n",
    "107":"\nBohrium\nSymbol-Bh\nLatin Name-Bohrium\n\nBlock-D\nGroup-7\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-272u\n\nElectrons-107\nProtons-107\nNeotrons-157\n\nYear Discovered-1981\nElectron shell configuration-2,8,18,32,32,13,2\nDiscovered By:Peter Armbruster, Gottfried Munzenber\n\nPhase-Solid\n",
    "108":"\nHassium\nSymbol-Hs\nLatin Name-Hassium\n\nBlock-D\nGroup-8\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-270u\n\nElectrons-108\nProtons-108\nNeotrons-161\n\nYear Discovered-1984\nElectron shell configuration-2,8,18,32,32,14,2\nDiscovered By:GSI\n\nPhase-Solid\n",
    "109":"\nMeitnerium\nSymbol-Mt\nLatin Name-Meitnerium\n\nBlock-D\nGroup-9\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-276u\n\nElectrons-109\nProtons-109\nNeotrons-159\n\nYear Discovered-1982\nElectron shell configuration-2,8,18,32,32,15,2\nDiscovered By:GSI\n\nPhase-Solid\n",
    "110":"\nDarmstadtium\nSymbol-Ds\nLatin Name-Darmstadtium\n\nBlock-D\nGroup-10\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-281u\n\nElectrons-110\nProtons-110\nNeotrons-171\n\nYear Discovered-1994\nElectron shell configuration-2,8,18,32,32,17,1\nDiscovered By:GSI\n\nPhase-Solid\n",
    "111":"\nRoentgenium\nSymbol-Rg\nLatin Name-Roentgenium\n\nBlock-D\nGroup-11\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-280u\n\nElectrons-111\nProtons-111\nNeotrons-170\n\nYear Discovered-1994\nElectron shell configuration-2,8,18,32,32,18,1\nDiscovered By:GSI\n\nPhase-Solid\n",
    "112":"\nCopernicium\nSymbol-Cn\nLatin Name-Copernicium\n\nBlock-D\nGroup-12\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-285u\n\nElectrons-112\nProtons-112\nNeotrons-173\n\nYear Discovered-1996\nElectron shell configuration-2,8,18,32,32,18,2\nDiscovered By:GSI\n\nPhase-Solid\n",
    "113":"\nNihonium\nSymbol-Nh\nLatin Name-Nihonium\n\nBlock-P\nGroup-13\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-284u\n\nElectrons-113\nProtons-113\nNeotrons-173\n\nYear Discovered-2003\nElectron shell configuration-2,8,18,32,32,18,3\nDiscovered By:Riken\n\nPhase-Solid\n",
    "114":"\nFlerovium\nSymbol-Fl\nLatin Name-Flerovium\n\nBlock-P\nGroup-14\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-289u\n\nElectrons-114\nProtons-114\nNeotrons-173\n\nYear Discovered-1999\nElectron shell configuration-2,8,18,32,32,18,4\nDiscovered By:Sigurd Hofmann\n\nPhase-Solid\n",
    "115":"\nMoscovium\nSymbol-Mc\nLatin Name-Moscovium\n\nBlock-P\nGroup-15\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-288u\n\nElectrons-115\nProtons-115\nNeotrons-173\n\nYear Discovered-2003\nElectron shell configuration-2,8,18,32,32,18,5\nDiscovered By:Joint Institute for Nuclear Research\n\nPhase-Solid\n",
    "116":"\nLivermorium\nSymbol-Lv\nLatin Name-Livermorium\n\nBlock-P\nGroup-16\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-293u\n\nElectrons-116\nProtons-116\nNeotrons-175\n\nYear Discovered-2000\nElectron shell configuration-2,8,18,32,32,18,6\nDiscovered By:Joint Institute for Nuclear Research\n\nPhase-Solid\n",
    "117":"\nTennessine\nSymbol-Ts\nLatin Name-Tennesine\n\nBlock-P\nGroup-17\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-Unknown Value\n\nElectrons-117\nProtons-117\nNeotrons-177\n\nYear Discovered-2010\nElectron shell configuration-2,8,18,32,32,18,7\nDiscovered By: Joint Institute for Nuclear Research, Lawrence Livermore National Laboratory, Vanderbilt University, Oak Ridge National Laboratory\n\nPhase-Solid\n",
    "118":"\nOganesson\nSymbol-Og\nLatin Name-Oganneson\n\nBlock-P\nGroup-18\nPeriod-7\n\nMelting Point-0K\nBoiling Point-0K\nAtomic Mass-294u\n\nElectrons-118\nProtons-118\nNeotrons-176\n\nYear Discovered-2002\nElectron shell configuration-2,8,18,32,32,18,8\nDiscovered By:Yuri Oganessian\n\nPhase-Solid\n",
    "Gas":"\n01-Hydrogen(01-H)\n02-Helium(02-He)\n03-Nitrogen(07-N)\n\n04-Oxygen(08-O)\n05-Fluorine(09-F)\n06-Neon(10-Ne)\n\n07-Chlorine(17-Cl)\n08-Argon(18-Ar)\n09-Krypton(36-Kr)\n\n10-Xenon(54-Xe)\n11Randon(86-Rn)\n",
    "Liquid":"\n01-Bromine(35-Br)\n02-Mercury(80-Hg)\n",
    "Solid":"\n01-Lithium(03-Li)\n02-Beryllium(4-Be)\n03-Boron(5-B)\n\n04-Carbon(6-C)\n05-Sodium(11-Na)\n06-Magnesium(12-Mg)\n\n07-Aluminium(13-Al)\n08-Silicon(14-Si)\n09-Phosphorus(15-P)\n\n10-Sulfur(16-S)\n11-Potassium(19-K)\n12-Calcium(20-Ca)\n\n13-Scandium(21-Sc)\n14-Titanium(22-Ti)\n15-Vanadium(23-V)\n\n16-Chromium(24-Cr)\n17-Manganese(25-Mn)\n18-Iron(26-Fe)\n\n19-Cobalt(27-Co)\n20-Nickel(28-Ni)\n21-Copper(29-Cu)\n\n22-Zinc(30-Zn)\n23-Gallium(31-Ga)\n24-Germanium(32-Ge)\n\n25-Arsenic(33-As)\n26-Selenium(34-Se)\n27-Rubidium(37-Rb)\n\n28-Strontium(38-Sr)\n29-Yttrium(39-Y)\n30-Zirconium(40-Zr)\n\n31-Niobium(41-Nb)\n32-Molybdenum(42-Mo)\n33-Technetium(43-Tc)\n\n34-Ruthenium(44-Ru)\n35-Rhodium(45-Rh)\n36-Palladium(46-Pd)\n\n37-Silver(47-Ag)\n38-Cadmium(48-Cd)\n39-Indium(49-In)\n\n40-Tin(50-Sn)\n41-Antimony(51-Sb)\n42-Tellurium(52-Te)\n\n43-Iodine(53-I)\n44-Cesium(55-Cs)\n45-Barium(56-Ba)\n\n46-Lanthanum(57-La)\n47-Cerium(58-Ce)\n48-Praseodymium(59-Pr)\n\n49-Neodymium(60-Nd)\n50-Promethium(61-Pm)\n51-Samarium(62-Sm)\n\n52-Eurpium(63-Eu)\n53-Gadolinium(64-Gd)\n54-Terbium(65-Tb)\n\n55-Dysprosium(66-Dy)\n56-Holmium(67-Ho)\n57-Erbium(68-Er)\n\n58-Thulium(69-Tm)\n59-Ytterbium(70-Yb)\n60-Lutetium(71-Lu)\n\n61-Hafnium(72-Hf)\n62-Tantalum(73-Ta)\n63-Tungsten(74-W)\n\n64-Rhenium(75-Re)\n65-Osmium(76-Os)\n66-Iridium(77-Ir)\n\n67-Platinum(78-Pt)\n68-Gold(79-Au)\n69-Thallium(81-Tl)\n\n70-Lead(82-Pb)\n71-Bismuth(83-Bi)\n72-Polonium(84-Po)\n\n73-Astatine(85-At)\n74-Francuim(87-Fr)\n75-Radium(88-Ra)\n\n76-Actinium(89-Ac)\n77-Thorium(90-Th)\n78-Protactinium(91-Pa)\n\n79-Uranium(92-U)\n80-Neptunium(93-Np)\n81-Plutonium(94-Pu)\n\n82-Americium(95-Am)\n83-Curium(96-Cm)\n84-Berkelium(97-Bk)\n\n85-Californium(98-Cf)\n86-Einsteinium(99-Es)\n87-Fermium(100-Fm)\n\n88-Mendelevium(101-Md)\n89-Nobelium(102-No)\n90-Lawrencium(103-Lr)\n\n91-Rutherfordium(104-Rf)\n92-Dubnium(105-Db)\n93-Seaborgium(106-Sg)\n\n94-Bohrium(107-Bh)\n95-Hassium(108-Hs)\n96-Meitnerium(109-Mt)\n\n97-Darmstadtium(110-Ds)\n98-Roentgenium(111-Rg)\n99-Copernicium(112-Rg)\n\n100-Nihonium(113-Nh)\n101-Flerovium(104-Fl)\n102-Moscovium(115-Mc)\n\n103-Livermorium(116-Lv)\n104-Tennessine(117-Ts)\n105-Oganesson(118-Og)\n",
    }

sentence = ''
while (sentence != "exit"):
    sentence = input("Enter Your atomic number:")
    print(sentence)

    atomic_number = ''
    correct = True


    try:
      atomic_number
      atomic_number+= atomic[sentence]
    except:
        print("\nYour atomic number contains unknown characters\nPlease try again...\n")
        correct = False

    if correct:
        print (atomic_number)
