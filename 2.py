import requests
import pygame

ll_1 = float(input())
ll_2 = float(input())
spn = float(input())
map_request = f'https://static-maps.yandex.ru/1.x/?ll={ll_1},{ll_2}&spn={spn},{spn}&l=map'
map_response = requests.get(map_request)
with open('map.png', mode='wb') as file:
    file.write(map_response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load('map.png'), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                spn += 0.01
                map_request = f'https://static-maps.yandex.ru/1.x/?ll={ll_1},{ll_2}&spn={spn},{spn}&l=map'
                map_response = requests.get(map_request)
                with open('map.png', mode='wb') as file:
                    file.write(map_response.content)
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
            elif event.key == pygame.K_PAGEDOWN:
                if spn > 0.01:
                    spn -= 0.01
                map_request = f'https://static-maps.yandex.ru/1.x/?ll={ll_1},{ll_2}&spn={spn},{spn}&l=map'
                map_response = requests.get(map_request)
                with open('map.png', mode='wb') as file:
                    file.write(map_response.content)
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
pygame.quit()
