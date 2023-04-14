from flask import Flask, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)
model = T5ForConditionalGeneration.from_pretrained("t5-base")
tokenizer = T5Tokenizer.from_pretrained("t5-base")

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        lecture_text = request.data.decode("utf-8")
        inputs = tokenizer.encode("summarize: " + lecture_text, return_tensors="pt", max_length
512, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_return_sequences=1)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return jsonify(summary=summary)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(port=5000)
