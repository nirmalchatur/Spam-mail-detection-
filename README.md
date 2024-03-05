# Spam-mail-detection-
This project consist of a spam mail detection software, which uses a GUI to take the input from the user and give weather it is a spam or not.
It consist of following libraries 
import tkinter as tk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from sklearn.metrics.pairwise import cosine_similarity
