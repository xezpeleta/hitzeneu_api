from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer
from transformers import AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

model_name = "HiTZ/mt-hitz-en-eu"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Check if GPU is available and move model to GPU if it is
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('q')
    source = data.get('source', "en")
    target = data.get('target', "eu")
    format = data.get('format', "text")
    api_key = data.get('api_key')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    if source != "en" or target != "eu":
        return jsonify({"error": "Only English to Basque translation is supported"}), 400
    
    # Tokenize and move input to the same device as the model
    inputs = tokenizer([text], return_tensors="pt", padding=True).to(device)
    
    # Generate translation
    translated = model.generate(**inputs)
    
    # Move the output back to CPU for decoding
    result = tokenizer.decode(translated[0].cpu(), skip_special_tokens=True)
    
    return jsonify({"translatedText": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
