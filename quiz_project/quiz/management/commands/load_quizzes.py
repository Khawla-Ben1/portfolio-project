import os
import csv
from django.core.management.base import BaseCommand
from quiz.models import Quiz, Question, Option

class Command(BaseCommand):
    help = 'Loads quiz questions from multiple CSV files in the data folder'

    def handle(self, *args, **kwargs):
        quizzes_path = 'quiz/data'  # Path to your data folder containing quiz1.csv, quiz2.csv, etc.
        
        # Get all CSV files in the 'data' folder
        quiz_files = [f for f in os.listdir(quizzes_path) if f.endswith('.csv')] 
        
        for quiz_file in quiz_files:
            quiz_file_path = os.path.join(quizzes_path, quiz_file)
            
            try:
                with open(quiz_file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    
                    # Ensure required columns are present
                    required_columns = ['Question', 'Option A', 'Option B', 'Option C', 'Correct Answer']
                    if not all(col in reader.fieldnames for col in required_columns):
                        self.stdout.write(self.style.ERROR(f"Missing columns in {quiz_file_path}"))
                        continue
                    
                    quiz_name = quiz_file.replace('.csv', '')  # Use file name without extension as quiz name
                    
                    # Check if the quiz already exists
                    quiz, created = Quiz.objects.get_or_create(name=quiz_name)
                    if not created:
                        self.stdout.write(self.style.SUCCESS(f"Quiz '{quiz_name}' already exists. Skipping."))
                        continue
                    
                    self.stdout.write(self.style.SUCCESS(f"Processing quiz: {quiz_name}"))
                    
                    # Create the questions and options
                    for row in reader:
                        # Skip empty rows
                        if not row['Question'].strip():
                            self.stdout.write(self.style.ERROR(f"Empty question in {quiz_file_path}. Skipping row."))
                            continue
                        
                        question_text = row['Question']
                        correct_option = row['Correct Answer']
                        
                        # Create the Question object
                        question = Question.objects.create(quiz=quiz, text=question_text)
                        
                        # Create the options
                        options = [
                            ('A', row['Option A']),
                            ('B', row['Option B']),
                            ('C', row['Option C'])
                        ]
                        
                        for option_letter, option_text in options:
                            is_correct = option_letter == correct_option
                            Option.objects.create(question=question, text=option_text, is_correct=is_correct)

            except FileNotFoundError:
                self.stdout.write(self.style.ERROR(f"File not found: {quiz_file_path}"))
                continue
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error processing {quiz_file_path}: {e}"))
                continue
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded quiz questions from CSV'))
