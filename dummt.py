moderate_keywords = [
    "gorgeous", "sexy", "come with me", "hot", "babe", "party", "hang out", "fun with you"
]

def mark_moderate(text):
    for word in moderate_keywords:
        if word in text.lower():
            return 1  # Moderate
    return -1  # Leave unchanged

df['moderate_flag'] = df['text'].apply(mark_moderate)

# Apply label where flagged
df.loc[df['moderate_flag'] == 1, 'label'] = 1

# Drop helper column
df.drop('moderate_flag', axis=1, inplace=True)

# Save it
df.to_csv("clean_data/updated_offensive_dataset.csv", index=False)
