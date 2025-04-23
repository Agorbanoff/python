from textProcessor import TextProcessor
import os

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

processor = TextProcessor(content)

print("Word count:", processor.count_words())

with open("sample_upper.txt", "w", encoding="utf-8") as file:
    file.write(processor.to_uppercase())

with open("sample_lower.txt", "w", encoding="utf-8") as file:
    file.write(processor.to_lowercase())

file_size = os.path.getsize("sample.txt")
print("File size of sample.txt:", file_size, "bytes")
