import tkinter as tk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from sklearn.metrics.pairwise import cosine_similarity
# Load data
message_data = pd.read_csv('D:/spam (3).csv', sep=",", encoding="latin")
# Define stemmer function
print(message_data)
def stemmer(text):
    stemmer = SnowballStemmer("english")
    return ' '.join([stemmer.stem(word) for word in text.split()])

# Apply stemming to the message column
message_data['message'] = message_data['message'].apply(stemmer)

# Vectorize the text data
vectorizer = TfidfVectorizer(stop_words="english")
message_mat = vectorizer.fit_transform(message_data['message'])

# Function to classify spam
def is_similar_message(inp):
    # Check if the input message exactly matches any message labeled as "ham" or "spam"
    if inp in message_data['message'].values:
        # Find the index of the message
        index = message_data.loc[message_data['message'] == inp].index[0]
        # Check the corresponding label in the 'Value' column
        label = message_data.loc[index, 'Value']
        if label == 'spam':
            return True
        elif label == 'ham':
            return False
    else:
        # Get cosine similarity between input and all messages in dataset
        inp = [inp]
        inp = pd.Series(inp).apply(stemmer)
        inp_vector = vectorizer.transform(inp)
        similarities = cosine_similarity(inp_vector, message_mat)

        # Check if any message is similar
        max_similarity = similarities.max()
        if max_similarity > 0.9:  # Adjust the threshold as needed
            return True
        else:
            return False

def check_spam():
    user_input = entry.get("1.0", "end-1c")  # Get text from the Text widget
    if is_similar_message(user_input):
        result_label.config(text="The message is classified as spam.", bg="red")
    else:
        result_label.config(text="The message is classified as not spam.", bg="green")

# Create Tkinter window
root = tk.Tk()
root.title("Spam Detector")

# Create input Text widget with increased width and height
entry = tk.Text(root, width=100, height=10)  # Increased width and height
entry.pack(pady=10)

# Create check button
check_button = tk.Button(root, text="Check Spam", command=check_spam)
check_button.pack(pady=5)

# Create result label
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
