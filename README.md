# Chart_Spreadsheet_2021
Different chart to explain the energy transition to Seychelles, data from Spreedsheet designed for Energy Report.

## Technologie utilisée
Langage :
- Python
Bibliothèques :
- Matplotlib
- Seaborn
- Pandas

## Comment cela fonctionne
### Fichiers d'entrée (Bases de données)
Les dossiers préfixés par *py_* contiennent des fichiers Python (*.py*) qui génèrent les graphiques.
Pour produire ces graphiques, le fichier Python prend en entrée des données à partir d'un fichier Excel. La bibliothèque pandas est utilisée pour lire les données du fichier (*Seychelles Energy Balance For 2021.xlsx* ou *Spreadsheet for the preparation of Energy Reports.xlsx*).

### Fichiers de sortie (Graphiques)
Une fois que les graphiques sont générés par Python, ils sont simplement stockés dans des dossiers avec des noms tels que *Correction_Chart...* ou *Figure...*
