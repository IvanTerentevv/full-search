import pygame
import requests
import find


map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = find.params()
response = requests.get(map_api_server, params=map_params)

map_file = "map.png"
open(map_file, "wb").write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.draw.circle(screen, pygame.Color('red'), (300, 225), 5, width=0)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()