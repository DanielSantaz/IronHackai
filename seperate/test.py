from transformers import T5ForConditionalGeneration, T5Tokenizer

def generate_question(context):
    model = T5ForConditionalGeneration.from_pretrained("iarfmoose/t5-base-question-generator")
    tokenizer = T5Tokenizer.from_pretrained("iarfmoose/t5-base-question-generator")

    inputs = tokenizer.encode("generate question: " + context, return_tensors="pt", max_length=512, truncation=True)
    question_ids = model.generate(inputs, max_length=100, num_beams=4, num_return_sequences=1)
    question = tokenizer.decode(question_ids[0], skip_special_tokens=True)

    return question

context = "Python is an interpreted, high-level, general-purpose programming language."
generated_question = generate_question(context)

print("Generated question:", generated_question)
