from sklearn.neighbors import KNeighborsClassifier
import pandas as pd


def generate_model(): 
    df = pd.read_csv(r"C:\Users\ethan\OneDrive\Junior Year\Summer\Sign Language Interp\hand_data.csv")

    letter_data = df.iloc[:, -1]
    hand_data = df.iloc[:, :-1]

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(hand_data, letter_data)
    return model
