import pygame
from settings import Settings

# mouse down to drag
# if mouse up, snap to petr (screen.blit(shirt,(300,100))

class Outfit:
    def __init__(self, x,y, img):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (504, 544))

    @property
    def position(self):
        return self.x, self.y

    def move_ip(self, dx,dy):
        self.x += dx
        self.y += dy

    def collidepoint(self, x,y):
        self.rect = self.img.get_rect()
        if (self.x - x) + (self.y - y) <= self.rect.right:
            return True
        return False

    def draw(self,screen):
        screen.blit(self.img, self.position)


def main():
    pygame.init()
    settings = Settings()
    clock = pygame.time.Clock()

    outfits = [Outfit(-100,-50,"uci.png"), Outfit(-50,-50,"kaba.png")]

    current_selection = None

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Dress Up Petr")

    img = pygame.image.load('Untitled_Artwork.bmp').convert_alpha()
    img = pygame.transform.scale(img, (504, 544))  # scaled by half

    title = pygame.image.load('Untitled_Artwork.png').convert_alpha()
    title = pygame.transform.scale(title, (512, 214))

    tops = pygame.image.load('tops.png').convert_alpha()


    bg = pygame.image.load("Anteater_Water_Tower.bmp")



    running = True
    while running:
        screen.blit(bg, (0, 0))
        screen.blit(title,(300,-15))
        screen.blit(tops, (0,0))
        screen.blit(img, (300, 100))
        # screen.blit(shirt, (300, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for outfit in outfits:
                        if outfit.collidepoint(event.pos[0], event.pos[1]):
                            current_selection = outfit
                            break
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    current_selection = None

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:
                    if current_selection:
                        current_selection.move_ip(event.rel[0], event.rel[1])

        for outfit in reversed(outfits):
            outfit.draw(screen)

        pygame.display.flip()
        clock.tick(40)



main()

