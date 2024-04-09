import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    drawing = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_t:
                    mode = 'rectangle'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    points.append(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    points.append(event.pos)
                    
        screen.fill((0, 0, 0))
        
        # Draw shapes based on mode
        for i in range(len(points) - 1):
            if mode == 'circle':
                pygame.draw.circle(screen, getColor(mode), points[i], radius)
            elif mode == 'rectangle':
                pygame.draw.rect(screen, getColor(mode), (points[0], (points[i][0] - points[0][0], points[i][1] - points[0][1])), 3)
            elif mode == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), points[i], radius)
            else:
                pygame.draw.line(screen, getColor(mode), points[i], points[i+1], radius)
                
        pygame.display.flip()
        clock.tick(60)

def getColor(mode):
    if mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'blue':
        return (0, 0, 255)
    else:
        return (255, 255, 255)  # Default color for eraser

main()
