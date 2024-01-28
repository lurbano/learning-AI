from transformers import pipeline

classifier = pipeline("sentiment-analysis")
x = classifier(
    [
        "I've been waiting for a HuggingFace course my whole life.",
        "I hate this so much!",
    ]
)

print(x)
print("done")