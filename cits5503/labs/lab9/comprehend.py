import boto3
import argparse
from iso639 import languages

client = boto3.client('comprehend')


def parse_args():
    parser = argparse.ArgumentParser(description="arg parser")
    parser.add_argument("-i", "--text", default=None, type=str)
    return parser.parse_args()

def main():
    args = parse_args()
    if not args.text:
        return
    
    # Detect Entities
    response = client.detect_dominant_language(
        Text=args.text
    )

    language = languages.get(alpha2=response['Languages'][0]['LanguageCode']).name

    confidence = str(int(response['Languages'][0]['Score'] * 100))

    print(language+" detected with "+confidence+ "%"+ " confidence")

if __name__ == "__main__":
    main()