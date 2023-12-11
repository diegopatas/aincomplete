import sys
import pygame

class   AIncomplete:
    """Main class to manage the game"""

    def __init__(self) -> None:
        """Init the game"""

        pygame.init()

        self.sreen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("AIncomplete")

    def run_game(self) -> None:
        """Start the main loop of the game"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                pygame.display.flip()

if __name__ == '__main__':
    aincomplete = AIncomplete()
    aincomplete.run_game()

