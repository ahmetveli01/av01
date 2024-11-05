meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "TROLL": "bir eşek şakasına mağruz kalmak" ,
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak" ,
            "CREEPY" : "korkunç" ,           
            "AGGRO" : "agresifleşmek/sinirlenmek" ,
            "GG" : "Biri tarafından komik duruma düşürülmek"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("burada o kelime bulunmuyor")
