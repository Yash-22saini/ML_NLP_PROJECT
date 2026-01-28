from src.preprocessing import clean_text

sample_text = "Payment was deducted!!! 😡😡 but my course is still LOCKED."

cleaned = clean_text(sample_text)
print("Original :", sample_text)
print("Cleaned  :", cleaned)
