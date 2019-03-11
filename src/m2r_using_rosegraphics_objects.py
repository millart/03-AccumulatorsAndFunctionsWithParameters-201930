"""
This module uses ROSEGRAPHICS to demonstrate:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Emily Millard.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
#
# DONE: 2.
#   RUN this program.  Then answer the following,
#     GETTING HELP AS NEED! (Ask questions!!!)
#
#     a. For the RoseGraphics coordinate system:
#
#        -- Where is the (0, 0) point on the screen?
#              The (0,0) point is on the upper left-hand of the screen.
#
#        -- In what direction on the screen
#           does the positive X-axis point?
#              The positive x-axis point goes to the right of the screen.
#
#        -- In what direction on the screen
#           does the positive Y-axis point?
#              The positive y-axis point goes down in the screen.
#
#     b. Write a line of code that constructs a RoseWindow object:
#            window = rg.RoseWindow()
#
#     c. What is the default height of a RoseWindow?
#        (Use the HOVER trick to determine the answer to this question.)
#            The default height of a RoseWindow is 300 pixels.
#            (The default width is 400 pixels.)
#
#     d. Write a line of code that construct a RoseWindow object
#        whose height is 100:  (Use the HOVER trick to figure it out)
#            window = rg.RoseWindow(400, 100)
#            (I left the width at the default)
#
#     e. Use the DOT trick to answer the following:
#
#          -- Write the names of two types of graphics objects that
#             you can construct OTHER than Circle and Point:
#                1.) rectangle: rg.Rectangle(point1, point2)
#                    (point1 and point2 are opposite corners)
#                2.) line: rg.Line(point1,point2)
#                    (point1 and point2 are the start and end of the line)
#
#               There are more than just these types of graphics!
#
#          -- Write the names of three METHODs that Circle objects have:
#                1.) move/translate: circle.move_center_to(point1, point2)
#                    (point1 and point2 is the location the center of the circle is moving to)
#                2.) clone: circle.clone()
#                    (duplicates)
#
#                There are more than these two methods!
#
#          -- Write the names of three INSTANCE VARIABLEs that Circle
#             objects have:
#                1.) radius: circle.radius
#                2.) center: circle.center
#                3.) thickness: circle.outline_thickness
#
#     f. What does a RoseWindow RENDER method do?
#            The RENDER method draws the object in the window.
#            When a point is created, the point must be attached to window and the rendered.
#            This two-step process is important for animations.
#
#     g. When is a RoseWindow close_on_mouse_click method call
#        necessary?  Why?
#            The close_on_mouse_click method keeps the window open until the user clicks to close it.
#            This is allows the user to see the window and keep it open for as long as needed.
#
#   ASK QUESTIONS ** NOW ** if you do not understand how the
#     RoseGraphics graphics system works.
#
#   When you are confident that you have written correct answers
#   to the above questions (ASK QUESTIONS AS NEEDED!),
#   change the above _TODO_ to DONE.
#
###############################################################################

import rosegraphics as rg


def main():
    """
    Uses ROSEGRAPHICS to demonstrate:
      -- CONSTRUCTING objects,
      -- applying METHODS to them, and
      -- accessing their DATA via INSTANCE VARIABLES
    """
    example1()
    example2()
    example3()


def example1():
    """ Displays an empty window. """
    window = rg.RoseWindow(500, 300, 'Example 1: An empty window')
    window.close_on_mouse_click()


def example2():
    """ Displays two Point objects. """
    # ------------------------------------------------------------------
    # Construct the window in which objects will be drawn.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    # ------------------------------------------------------------------
    # Construct some rg.Point objects.
    # Note: the y-axis goes DOWN from the TOP.
    # ------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    # ------------------------------------------------------------------
    # A RoseGraphics object is not associated with a window,
    # and hence are not drawn, until you ATTACH it to a window.
    # ------------------------------------------------------------------
    point1.attach_to(window)
    point2.attach_to(window)

    # ------------------------------------------------------------------
    # And they still are not DRAWN until you RENDER the window.
    # That will draw ALL the objects on the window.
    # This two-step approach is important for animation.
    # ------------------------------------------------------------------
    window.render()

    window.close_on_mouse_click()


def example3():
    """ Displays a Circle and a Rectangle. """
    # ------------------------------------------------------------------
    # RoseWindow: optionally takes its width and height.
    # ------------------------------------------------------------------
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)

    # ------------------------------------------------------------------
    # Circle: needs its center and radius.
    # Has  fill_color  instance variable.
    # ------------------------------------------------------------------
    center_point = rg.Point(300, 100)
    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'green'
    circle.attach_to(window)

    # ------------------------------------------------------------------
    # Rectangle: needs two opposite corners.
    # ------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)

    # ------------------------------------------------------------------
    # render: Draw ALL the objects attached to this window.
    # ------------------------------------------------------------------
    window.render()

    # ------------------------------------------------------------------
    # A Rectangle has instance variables  corner_1  and  corner2.
    # ------------------------------------------------------------------
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    print(corner1, corner2)  # You can also PRINT RoseGraphics objects.
    print(rectangle)  # See the Console for the output.

    # ------------------------------------------------------------------
    # close_on_mouse_click: Keeps the window open until user clicks.
    # ------------------------------------------------------------------
    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
