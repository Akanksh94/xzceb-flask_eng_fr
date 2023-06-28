from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    
    from machinetranslation import translator
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    
    from machinetranslation import translator
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    
 return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
