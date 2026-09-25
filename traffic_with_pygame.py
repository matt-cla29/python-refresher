import pygame
import time

pygame.init()

screen = pygame.display.set_mode((300, 450))
screen2 = pygame.display.set_mode((300, 450))
screen3 = pygame.display.set_mode((300, 450))
screen4 = pygame.display.set_mode((300, 450))
pygame.display.set_caption("UK Traffic Lights")

color = (128, 128, 128)
color2 = (255, 0, 0)
color3 = (255, 165, 0)
color4 = (0, 255, 0)
         
start_time = pygame.time.get_ticks()

pygame.draw.rect(screen, color,pygame.Rect(50, 50, 200, 350))
pygame.draw.circle(screen2, color2, (150,120), 40 ) #red
pygame.draw.circle(screen3, color3, (150,230), 40 ) #amber
pygame.draw.circle(screen4, color4, (150,335), 40 ) #amber
pygame.display.flip()

current_light = "red = stop"
traffic_lights = ["red = stop", "amber = wait", "green = go"]
while True:
    if current_light == "red = stop":
        print(traffic_lights[0])
        time.sleep(5)
        current_light = "amber = wait"
    elif current_light == "amber = wait":
        print(traffic_lights[1])
        time.sleep(2)
        current_light = "green = go"
    elif current_light == "green = go":
        print(traffic_lights[2])
        time.sleep(3)
        current_light = "red = stop"
