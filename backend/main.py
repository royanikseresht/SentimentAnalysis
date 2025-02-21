from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load sentiment-analysis pipeline from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data["text"]
    
    # Analyze sentiment
    result = sentiment_pipeline(text)
    
    return jsonify(result[0])

if __name__ == "__main__":
    app.run(debug=True)
