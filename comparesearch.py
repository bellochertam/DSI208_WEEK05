import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1000, height=400, caption='Search Algorithms Comparison')
batch = pyglet.graphics.Batch()

# Generate numbers for binary search
binary_numbers = sorted(random.sample(range(1, 100), 19) + [42])
binary_left, binary_right = 0, len(binary_numbers) - 1
binary_mid = (binary_left + binary_right) // 2
binary_found = False
binary_search_complete = False

# Generate numbers for linear search
linear_numbers = random.sample(range(1, 100), 19) + [42]
random.shuffle(linear_numbers)
linear_current_index = 0
linear_found_index = -1
linear_search_complete = False

def binary_search_step(dt):
    global binary_left, binary_right, binary_mid, binary_found, binary_search_complete
    if not binary_found and binary_left <= binary_right:
        binary_mid = (binary_left + binary_right) // 2
        if binary_numbers[binary_mid] == 42:
            binary_found = True
        elif binary_numbers[binary_mid] < 42:
            binary_left = binary_mid + 1
        else:
            binary_right = binary_mid - 1
    else:
        binary_search_complete = True

def linear_search_step(dt):
    global linear_current_index, linear_found_index, linear_search_complete
    if not linear_found_index and linear_current_index < len(linear_numbers):
        if linear_numbers[linear_current_index] == 42:
            linear_found_index = linear_current_index
            linear_search_complete = True
        linear_current_index += 1

@window.event
def on_draw():
    window.clear()

    # Define box dimensions
    box_width = 40
    box_height = 40

    # Draw binary search visualization
    for i, number in enumerate(binary_numbers):
        x = i * (box_width + 10) + 20
        y = window.height // 2

        # Define box color
        if binary_left <= i <= binary_right and not binary_search_complete:
            color = (0, 191, 255)  # Light Sky Blue for the current search interval
        elif i == binary_mid and not binary_search_complete:
            color = (255, 99, 71)  # Tomato Red for the middle element
        elif binary_found and i == binary_mid:
            color = (50, 205, 50)  # Lime Green if 42 is found
        else:
            color = (211, 211, 211)  # Light Gray for eliminated elements
        
        # Draw the box
        pyglet.shapes.Rectangle(x, y, box_width, box_height, color=color, batch=batch).draw()

        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+box_width//2, y=y+box_height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

    # Draw linear search visualization
    for i, number in enumerate(linear_numbers):
        x = i * (box_width + 10) + 20
        y = window.height // 4

        # Define box color
        if linear_current_index == i and not linear_search_complete:
            color = (255, 191, 0)  # Orange for the current box being checked
        elif i == linear_found_index:
            color = (0, 255, 0)  # Green if 42 is found
        else:
            color = (192, 192, 192)  # Grey for unchecked or passed boxes
        
        # Draw the box
        pyglet.shapes.Rectangle(x, y, box_width, box_height, color=color, batch=batch).draw()

        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+box_width//2, y=y+box_height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()
        
def linear_search_step(dt):
    global linear_current_index, linear_found_index, linear_search_complete
    if linear_current_index < len(linear_numbers) and not linear_search_complete:
        if linear_numbers[linear_current_index] == 42:
            linear_found_index = linear_current_index
            linear_search_complete = True
        linear_current_index += 1

# Schedule binary search and linear search updates
pyglet.clock.schedule_interval(binary_search_step, 0.5)
pyglet.clock.schedule_interval(linear_search_step, 0.5)

pyglet.app.run()
