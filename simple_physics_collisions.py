#!PythonProjects/env python
# Davenport University
# Class Info: CISP253-23151 (Winter 2022)
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: simple_physics_collisions.py
"""
Example of how a Python program can use functions, for loops, and try/except statements to create a model of
how programs can determine simple collisions.

"""

# Import the required modules and functions
import time


# Note: At the moment, I do not have an airtrack system but I am in the process of learning how to render it.
def render_track(x_px, x_left_edge_px, x_right_edge_px):
    """
        render_track function with for loop, and if/elif/else statement generate the borders, and the object
        that collides with the borders.
            Args:
                x_px: The object which interacts with the borders.
                x_left_edge_px: The left border.
                x_right_edge_px: The right border.
            Returns:
                The area of the screen that is contained with either an object, borders, or empty space.
    """
    area = ''
    display_width_px = 125
    for j in range(0, display_width_px + 1):
        if j == x_px:
            area += '*'

        # The left and right borders
        elif (j == x_left_edge_px) or (j == x_right_edge_px):
            area += ':'
        else:
            area += ' '
    return area


def m_to_px(x_m):
    """
          m_to_px function with returns the speed in which the objects move in the screen.
              Args:
                  x_m: The position of the object and calculated movement in pixels per meter.
              Returns:
                  The speed of the object.
    """
    # ppm or (pixels per meter).
    return int(round(x_m * 5.0))


def x_fix_sticky(x_m, x_left_edge_m, x_right_edge_m):
    """
          m_to_px function with returns the speed in which the objects move in the screen.
                Args:
                    x_m: The speed of the object in pixels per meter.
                    x_left_edge_m: The left border.
                    x_right_edge_m: The right border.
                Returns:
                    The speed of the object.
    """
    # This is called "stickiness correction", so the object does not get stuck after collision, and sets it back.
    if x_m < x_left_edge_m:
        x_corrected_m = x_left_edge_m
    elif x_m > x_right_edge_m:
        x_corrected_m = x_right_edge_m

    # The reason for returning 'corrected' is to prevent x_m from constantly equalling itself, allowing it to continue 
    # its trajectory.
    return x_corrected_m


def main():
    """
           main function returns the logic of the physics collisions of the object and the borders,
           changing the direction of the object, and correcting sticky errors.
                Vars:
                    x_left_edge_m: Defining the left border.
                    x_right_edge_m: Defining the right border.
                    dt_s: The rate of declining velocity.
                    x_m: The position velocity, and is updated overtime.
                    v_mps: The position, and is updated overtime.
                    a_mps2: The acceleration of the object.
    """
    x_left_edge_m = 0
    x_right_edge_m = 17.5

    dt_s = 0.015
    x_m = 10.0
    v_mps = 17.0
    a_mps2 = -2.0

    for j in range(5000):
        try:

            # Update the velocity and position of the var on bounce.
            v_mps += a_mps2 * dt_s
            x_m += v_mps * dt_s

            # This checks for collisions and any stickiness as well.
            if (x_m < x_left_edge_m) or (x_m > x_right_edge_m):
                # Represent the kinetic energy lost from each bounce.
                v_mps *= -1 * 0.80
                x_m = x_fix_sticky(x_m, x_left_edge_m, x_right_edge_m)

            # Display all to the screen upon j in range of 5000
            display_area = render_track(m_to_px(x_m), m_to_px(x_left_edge_m), m_to_px(x_right_edge_m))
            print(display_area + ' x =' + "%.3f" % x_m + "  " + ' v = ' + "%.1f" % v_mps)

            time.sleep(dt_s)
        except:
            # Break the loop and stop the program. 
            break


main()
# EOF
