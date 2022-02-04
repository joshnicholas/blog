import os

for fillo in os.listdir('words'):
    if (fillo != "words.json") & (fillo != ".DS_Store"):
        print(fillo)
        f = open(f"words/{fillo}", "r")
        texto = f.read()
        texto = texto.replace("</p>", "</p><br>")
        with open(f"words/{fillo}", 'w') as f:
            f.write(texto)
        print(texto)
        # # texto = 
