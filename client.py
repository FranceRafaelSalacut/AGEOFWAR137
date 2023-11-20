from CONSTANTS import *
import pygame
import socket
import threading
import time

# client setup
def connectToServer():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = SERVER_IP  # replace with the server's IP address
    server_port = PORT  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))

    try:
        msg = 0
        while True:
            time.sleep(1)
            msg += 1
            print(f"connected for {msg} seconds")
        # while True:
        #     # get input message from user and send it to the server
        #     msg = "Mashallah connected"
        #     client.send(msg.encode("utf-8")[:1024])

        #     # receive message from the server
        #     response = client.recv(1024)
        #     response = response.decode("utf-8")

        #     # if server sent us "closed" in the payload, we break out of
        #     # the loop and close our socket
        #     if response.lower() == "closed":
        #         break

        #     print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # close client socket (connection to the server)
        client.close()
        print("Connection to server closed")


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('TEST') # game/window title
dt = 0 # deltaTime
run = True

thread = threading.Thread(target=connectToServer)
thread.start()

while run:
    # polling for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # filling the screen with a color to wipe away everything from the last frame
    screen.fill('white')

    # Render game here
    # vv===========================================vv



    # ^^===========================================^^
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()