from transformers import pipeline

model = "Helsinki-NLP/opus-mt-en-fr"

def translate():
    translator  = pipeline(task="translation", model=model)

    text_translator = translator("Hugging Face is a technology company based ins New York and Paris", max_length=40)

    return print(text_translator)

if __name__ == '__main__':
    translate()