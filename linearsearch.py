import pyglet
import random

# Create a window
window = pyglet.window.Window(width=800, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a list with random numbers ensuring 42 is included
numbers = random.sample(range(1, 100), 19) + [42]
random.shuffle(numbers)

# Variables to control the animation and search
current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 42:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

# Schedule the linear search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # Define colors based on the search status
        if i == current_index and not search_complete:
            color = (255, 191, 0)  # Orange for the current box being checked
        elif i == found_index:
            color = (0, 255, 0)  # Green if 42 is found
        else:
            color = (192, 192, 192)  # Grey for unchecked or passed boxes
        
        # Draw the box
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

    # Show search status
    search_status_label = pyglet.text.Label(f"Search complete: {search_complete}", x=20, y=20, color=(255, 255, 255, 255))
    search_status_label.draw()

    # Show current index being checked
    if not search_complete:
        index_label = pyglet.text.Label(f"Checking index: {current_index}", x=20, y=40, color=(255, 255, 255, 255))
        index_label.draw()
    else:
        if found_index != -1:
            found_label = pyglet.text.Label(f"Number 42 found at index: {found_index}", x=20, y=40, color=(0, 255, 0, 255))
            found_label.draw()
        else:
            not_found_label = pyglet.text.Label("Number 42 not found in the list", x=20, y=40, color=(255, 0, 0, 255))
            not_found_label.draw()

pyglet.app.run()