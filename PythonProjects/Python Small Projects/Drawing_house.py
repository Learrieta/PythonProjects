# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)




    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_text (canvas, 550,400,"Welcome to my land!",fill="black")
    

    x = 0
    y = 0
    diameter = 30
    space = 10
    interval = diameter + space
    for i in range(30):
        draw_rectangle(canvas,x,y,x + diameter,y + 200, fill="azure")
        x+= interval
    draw_rectangle(canvas, 0, 160, 800, 180, width=1, fill="azure")

    draw_line(canvas, 48, 390, 48, 399, width=5, fill="blue")
    draw_line(canvas, 60, 390, 60, 399, width=5, fill="blue")
    draw_line(canvas, 80, 390, 80, 399, width=5, fill="blue")
    draw_line(canvas, 100, 360, 100, 379, width=5, fill="blue")
    
    



    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)




# Define your functions such as
# draw_sky and draw_ground here.'



def draw_sky( canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 4, scene_width, scene_height, width = 0, fill="sky blue")
    draw_oval(canvas,600,350,900,600,fill="yellow2")
    draw_oval(canvas,500,300,600,350,outline="azure",fill="azure")
    draw_oval(canvas,490,300,600,320,outline="azure",fill="azure")
    draw_oval(canvas,300,300,400,350,outline="azure",fill="azure")
    draw_oval(canvas,290,300,400,320,outline="azure",fill="azure")
    draw_oval(canvas,50,400,150,450,outline="azure",fill="azure")
    draw_oval(canvas,49,400,150,420,outline="azure",fill="azure")
    

def draw_ground(canvas, secene_width, scene_height):
    draw_rectangle(canvas,0,0,secene_width,scene_height/4,width=0,fill="chartreuse")
   

    tree_center_x = 270
    tree_bottom = 50
    tree_height = 400
    draw_pine_tree(canvas, tree_center_x,tree_bottom,tree_height)

    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)

def draw_pine_tree(canvas,center_x,bottom,height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="saddleBrown")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="darkGreen")






# Call the main function so that
# this program will start executing.
main()