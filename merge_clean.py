import pandas as pd
import os
from glob import glob

DATA_DIR = "/Users/hari1476/Desktop/instasafe/data"
OUTPUT_FILE = "/Users/hari1476/Desktop/instasafe/data/merged_dataset.csv"

# Map column names to 'text' and 'label'
def normalize_dataset(file_path):
    df = pd.read_csv(file_path)
    
    # Try to detect text column
    text_col = None
    for col in df.columns:
        if 'text' in col.lower() or 'tweet' in col.lower() or 'content' in col.lower() or 'message' in col.lower() or 'description' in col.lower():
            text_col = col
            break

    if not text_col:
        print(f"⚠️ No valid text column in {file_path}, skipping.")
        return None

    df = df[[text_col]].dropna()
    df = df.rename(columns={text_col: 'text'})
    df['label'] = 'abusive'  # Default label

    return df

def main():
    all_files = glob(os.path.join(DATA_DIR, "*.csv"))
    print(f"📁 Found {len(all_files)} CSV files")

    dfs = []
    for file in all_files:
        print(f"➡️ Processing: {file}")
        df = normalize_dataset(file)
        if df is not None:
            dfs.append(df)

    # Optional: Add some neutral samples
    neutral_data = {
        'text': [
            "Hey, how was your day?",
            "I'm running late, see you soon.",
            "You're amazing!",
            "This place is beautiful.",
            "Have a good weekend."
        ],
        'label': ['neutral'] * 5
    }
    neutral_df = pd.DataFrame(neutral_data)
    dfs.append(neutral_df)

    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.drop_duplicates(inplace=True)
    merged_df.to_csv(OUTPUT_FILE, index=False)
    
    print(f"\n✅ Final merged dataset saved to: {OUTPUT_FILE}")
    print(f"🧾 Total samples: {len(merged_df)}")

if __name__ == "__main__":
    main()
