from pynput.mouse import Button, Controller

mouse = Controller()
print("Current position: " + str(mouse.position))
mouse.position = (840, 871)
# Click the left button
mouse.click(Button.left, 1)
mouse.position = (850, 627)
# Click the left button
mouse.click(Button.left, 1)
