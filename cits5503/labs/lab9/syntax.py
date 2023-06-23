import boto3
from iso639 import languages

client = boto3.client('comprehend')

english = "The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799."
spanish = "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha."
french = "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir"
italian = "L'amor che move il sole e l'altre stelle."

def syntax_detection(text):
    lan_response = client.detect_dominant_language(
        Text=text
    )
    code = lan_response['Languages'][0]['LanguageCode']
    language = languages.get(alpha2=code).name
    syn_reponse = client.detect_syntax(Text=text, LanguageCode = code)
    syntax = syn_reponse['SyntaxTokens']
    print("The syntax in the %s text are:" % language)
    output = ''
    for syn in syntax:
       output += syn['Text'] +' is '+ syn['PartOfSpeech']['Tag'] + '\t'
    print(output)
    print()
        
syntax_detection(english)
syntax_detection(spanish)
syntax_detection(french)
syntax_detection(italian)
