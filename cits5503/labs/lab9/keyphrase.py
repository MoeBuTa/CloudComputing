import boto3
from iso639 import languages

client = boto3.client('comprehend')

english = "The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799."
spanish = "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha."
french = "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir"
italian = "L'amor che move il sole e l'altre stelle."

def keyphrase_detection(text):
    lan_response = client.detect_dominant_language(
        Text=text
    )
    code = lan_response['Languages'][0]['LanguageCode']
    language = languages.get(alpha2=code).name
    ph_reponse = client.detect_key_phrases(Text=text, LanguageCode = code)
    phs = ph_reponse['KeyPhrases']
    if not phs:
        print('There is no key phrase in the %s text'%language)
        return
    print("The key phrases in the %s text are:" % language)
    for ph in phs:
       print(ph['Text'])
    print()
        
keyphrase_detection(english)
keyphrase_detection(spanish)
keyphrase_detection(french)
keyphrase_detection(italian)
