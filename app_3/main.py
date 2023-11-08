from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input('Enter Canvas Width: '))
canvas_height = int(input('Enter Canvas Height: '))

colors_choice = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter canvas color type (white or black): ')

main_canvas = Canvas(width=canvas_width,
                     height=canvas_height,
                     color=colors_choice[canvas_color])

while True:
    shape_type = input(
        'Type a shape (Eg: Square, Rectangle) Or type "q" to exit: ')

    if shape_type.lower().strip() == 'square':
        shape_x = int(input('Enter shape x value: '))
        shape_y = int(input('Enter shape y value: '))
        shape_side = int(input('Enter shape side (width and height) value: '))
        red = int(input('How much red value should shape has? (0-255): '))
        green = int(input('How much green value should shape has? (0-255): '))
        blue = int(input('How much blue value should shape has? (0-255): '))
        shape_color = (red, green, blue)
        square = Square(x=shape_x, y=shape_y,
                        side=shape_side, color=shape_color)
        square.draw(canvas=main_canvas)
        print('\t Shape added successfully!')

    elif shape_type.lower().strip() == 'rectangle':
        shape_x = int(input('Enter shape x value: '))
        shape_y = int(input('Enter shape y value: '))
        shape_width = int(input('Enter shape widht : '))
        shape_height = int(input('Enter shape height : '))
        red = int(input('How much red value should shape has? (0-255): '))
        green = int(input('How much green value should shape has? (0-255): '))
        blue = int(input('How much blue value should shape has? (0-255): '))
        shape_color = (red, green, blue)

        rect = Rectangle(x=shape_x,
                         y=shape_y,
                         width=shape_width,
                         height=shape_height,
                         color=shape_color)

        rect.draw(canvas=main_canvas)
        print('\t Shape added successfully!')

    if shape_type.lower().strip() == "q":
        print('\n\t Goto output folder and check Canvas png to see your canvas')
        break


main_canvas.create("./output/Canvas.png")
