import requests
import pygame

map_request = f'https://static-maps.yandex.ru/1.x/?ll={float(input())},{float(input())}&spn={float(input())},0.00200&l=map'
map_response = requests.get(map_request)
with open('map.png', mode='wb') as file:
    file.write(map_response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load('map.png'), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
