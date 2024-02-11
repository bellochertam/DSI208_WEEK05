import pyglet
import random

# Create a window
window = pyglet.window.Window(width=800, height=400, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list with numbers and ensure 42 is included
numbers = sorted(random.sample(range(1, 100), 19) + [42])

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

# Function to perform a single step of binary search
def binary_search_step():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 42:
            found = True
        elif numbers[mid] < 42:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# Schedule the binary search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: binary_search_step(), 0.5)

@window.event
def on_draw():
    window.clear()

    # Define box dimensions
    box_width = 40
    box_height = 40

    # Draw boxes and numbers
    for i, number in enumerate(numbers):
        x = i * (box_width + 10) + 20
        y = window.height // 2

        # Define box color
        if left <= i <= right and not search_complete:
            color = (0, 191, 255)  # Light Sky Blue for the current search interval
        elif i == mid and not search_complete:
            color = (255, 99, 71)  # Tomato Red for the middle element
        elif found and i == mid:
            color = (50, 205, 50)  # Lime Green if 42 is found
        else:
            color = (211, 211, 211)  # Light Gray for eliminated elements
        
        # Draw the box
        pyglet.shapes.Rectangle(x, y, box_width, box_height, color=color, batch=batch).draw()

        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+box_width//2, y=y+box_height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

    # Show search status
    search_status_label = pyglet.text.Label(f"Search complete: {search_complete}", x=20, y=20)
    search_status_label.draw()

    # Show current search interval
    search_interval_label = pyglet.text.Label(f"Search interval: [{numbers[left]}, {numbers[right]}]", x=20, y=40)
    search_interval_label.draw()

pyglet.app.run()
