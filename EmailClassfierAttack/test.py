import pandas as pd
import random

# Load your dataset
data = pd.read_csv("train.csv")
clean_data = data.iloc[1:3001].copy()

# Step 1: Stronger poison (more samples)
n_poison = 300
trigger = "Best Regards, HackTheBox."

# Step 2: Sample spam messages to poison
spam_to_poison = clean_data[clean_data['label'] == 'spam'].sample(n=n_poison, random_state=42).copy()

# Step 3: Insert trigger at random positions (beginning or end)
def insert_trigger(msg):
    if random.random() < 0.5:
        return trigger + " " + msg  # start
    else:
        return msg + " " + trigger  # end

spam_to_poison['message'] = spam_to_poison['message'].apply(insert_trigger)
spam_to_poison['label'] = 'ham'  # Flip label to poison the model

# Step 4 (optional): Add some clean ham messages *with* trigger to reinforce it
n_ham_poison = 100
ham_to_inject = clean_data[clean_data['label'] == 'ham'].sample(n=n_ham_poison, random_state=99).copy()
ham_to_inject['message'] = ham_to_inject['message'].apply(insert_trigger)

# Combine: clean + poisoned + reinforced
poisoned_data = pd.concat([clean_data, spam_to_poison, ham_to_inject], ignore_index=True)
poisoned_data = poisoned_data.sample(frac=1.0, random_state=0)  # Shuffle

# Save
poisoned_data.to_csv("final.csv", index=False)
print("✅ Saved stronger poisoned data to poison.csv")
