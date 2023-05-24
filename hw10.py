import pickle

def save_scores(scores):
    with open('score.bin', 'wb') as file:
        pickle.dump(scores, file)

def load_scores():
    try:
        with open('score.bin', 'rb') as file:
            scores = pickle.load(file)
            print("Loaded scores:")
            for student, score in scores.items():
                print(f"Student: {student}, Score: {score}")
            print()
    except FileNotFoundError:
        print("No scores found.")
        print()

def main():
    scores = {}
    
    # Load scores if the file exists
    load_scores()
    
    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. Update score")
        print("4. Show all scores")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            student = input("Enter student name: ")
            score = float(input("Enter student score: "))
            scores[student] = score
            print("Student added.\n")
        elif choice == '2':
            student = input("Enter student name to remove: ")
            if student in scores:
                del scores[student]
                print("Student removed.\n")
            else:
                print("Student not found.\n")
        elif choice == '3':
            student = input("Enter student name to update score:
