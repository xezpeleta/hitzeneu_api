from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer
from transformers import AutoModelForSeq2SeqLM

app = Flask(__name__)

model_name = "HiTZ/mt-hitz-en-eu"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('q')
    source = data.get('source')
    target = data.get('target')
    format = data.get('format')
    api_key = data.get('api_key')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    if source != "en" or target != "eu":
        return jsonify({"error": "Only English to Basque translation is supported"}), 400
    
    translated = model.generate(**tokenizer([text], return_tensors="pt", padding=True))
    result = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return jsonify({"translatedText": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
