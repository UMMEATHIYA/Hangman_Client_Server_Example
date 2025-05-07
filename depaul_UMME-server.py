import socket
import threading
import random

def handle_client(client_socket, word_list):
    word = random.choice(word_list).lower()  # Select random word
    guessed_word = ['-'] * len(word)  # Store the guessed word as a list of dashes
    lives = 10
    guessed_letters = set()

    client_socket.send("Game started! Here is your word: " + ' '.join(guessed_word) + "\nYou have 10 lives left.\n".encode())
    
    while lives > 0:
        try:
            guess = client_socket.recv(1024).decode().strip().lower()
            if not guess:
                break

            if len(guess) != 1 or not guess.isalpha():
                client_socket.send("Please enter a single valid letter.\n".encode())
                continue

            if guess in guessed_letters:
                client_socket.send("You've already guessed that letter.\n".encode())
                continue

            guessed_letters.add(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_word[i] = guess
                client_socket.send(f"Correct guess: {' '.join(guessed_word)}\n".encode())
            else:
                lives -= 1
                client_socket.send(f"Wrong guess. You have {lives} lives left. {' '.join(guessed_word)}\n".encode())
            
            if '-' not in guessed_word:
                client_socket.send(f"Congratulations! The word was '{word}'. Want to play again? (yes/no)\n".encode())
                break

            if lives == 0:
                client_socket.send(f"Game Over! The correct word was '{word}'. Want to play again? (yes/no)\n".encode())
                break

        except Exception as e:
            print(f"Error: {e}")
            break
    
    client_socket.close()

def start_server(word_file, port):
    # Read word file
    with open(word_file, 'r') as file:
        words = file.read().splitlines()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))  # Listen on all interfaces
    server.listen(5)

    print(f"Server listening on port {port}...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr} has been established.")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, words))
        client_thread.start()

if __name__ == "__main__":
    start_server('words.txt', 8080)  # Adjust the file name and port as needed
