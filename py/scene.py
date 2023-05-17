# Example 1

from draw2d import (
    start_drawing,
    draw_line,
    draw_oval,
    draw_arc,
    draw_rectangle,
    draw_polygon,
    draw_text,
    finish_drawing,
)


def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky, draw_cloud and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_cloud(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(
        canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue"
    )


def draw_cloud(canvas, scene_width, scene_height):
    draw_oval(
        canvas,
        50,
        scene_height - 10,
        300,
        scene_height - 150,
        outline="white",
        fill="white",
    )
    draw_oval(
        canvas,
        75,
        scene_height - 30,
        350,
        scene_height - 175,
        outline="white",
        fill="white",
    )


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="tan")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw another pine tree
    tree_center_x = 600
    tree_bottom = 80
    tree_height = 280
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw another pine tree
    tree_center_x = 640
    tree_bottom = 70
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(
        canvas,
        trunk_left,
        trunk_top,
        trunk_right,
        bottom,
        outline="gray20",
        width=1,
        fill="tan3",
    )

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(
        canvas,
        center_x,
        skirt_top,
        skirt_right,
        trunk_top,
        skirt_left,
        trunk_top,
        outline="gray20",
        width=1,
        fill="dark green",
    )


# Call the main function so that
# this program will start executing.
main()
