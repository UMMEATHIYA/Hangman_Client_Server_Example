import socket
import sys

def start_client(server_ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    
    while True:
        message = client.recv(1024).decode()
        print(message)  # Display the server message (word state, lives, etc.)
        
        if "Want to play again?" in message:
            play_again = input().strip().lower()
            client.send(play_again.encode())
            if play_again != "yes":
                print("Exiting the game.")
                break
        
        else:
            guess = input("Enter your guess (single letter): ").strip().lower()
            client.send(guess.encode())

    client.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python depaul_USERNAME-client.py <server_ip> <port>")
        sys.exit(1)
    
    server_ip = sys.argv[1]
    port = int(sys.argv[2])

    start_client(server_ip, port)

