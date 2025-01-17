import pandas as pd
import os
import random

# Load the original dataset
file_path = "quizzes_on_german_grammar.csv"  # Adjust the path to your actual file
df = pd.read_csv(file_path)

# Shuffle the dataset to randomize the questions
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Specify how many quizzes you want to split into
num_quizzes = 20

# Calculate how many rows each quiz will have
questions_per_quiz = len(df) // num_quizzes
remainder = len(df) % num_quizzes

# Create a directory to store the quiz CSV files if it doesn't exist
output_dir = "split_quizzes"
os.makedirs(output_dir, exist_ok=True)

# Split the dataset and save each part into a new CSV
start_index = 0
for i in range(1, num_quizzes + 1):
    end_index = start_index + questions_per_quiz + (1 if i <= remainder else 0)
    quiz_df = df[start_index:end_index]
    
    quiz_file = os.path.join(output_dir, f"quiz_{i}.csv")
    quiz_df.to_csv(quiz_file, index=False)
    
    # Update start_index for the next quiz
    start_index = end_index

print(f"Successfully split the dataset into {num_quizzes} quizzes.")
