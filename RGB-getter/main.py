import pyautogui

def get_mouse_position_color():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Get the RGB color of the pixel at the mouse position
    color = pyautogui.pixel(x, y)

    return color

if __name__ == "__main__":
    try:
        while True:
            # Get RGB color at the current mouse position
            mouse_color = get_mouse_position_color()

            # Print the RGB color values
            print(f"Mouse position: {pyautogui.position()}, RGB color: {mouse_color}")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
