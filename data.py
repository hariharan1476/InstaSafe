import pandas as pd
import os

print("📥 Loading dataset from Hugging Face...")

# Load train split using huggingface-style URI
splits = {'train': 'train.json', 'validation': 'val.json', 'test': 'test.json'}
df = pd.read_json("hf://datasets/christinacdl/offensive_language_dataset/" + splits ["train"])


print("📊 Original dataset size:", len(df))

# Filter only non-offensive entries (label = 0)
df = df[df['label'] == 2]
print("✅ moderate only dataset size:", len(df))

# Drop rows with nulls just in case
df.dropna(subset=["text"], inplace=True)

# Save cleaned data
os.makedirs("clean_data", exist_ok=True)
df.to_csv("clean_data/moderate_dataset.csv", index=False)

print("\n✅ Clean non-offensive dataset saved as 'clean_data/moderate_dataset.csv'")
