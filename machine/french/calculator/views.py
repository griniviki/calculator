import math
from django.shortcuts import render

def calculate_wallpaper_rolls(figure_type, dimensions, roll_width, roll_length):
    total_area = 0

    if figure_type == 'wall':
        wall_type = dimensions.get('wall_type')
        if wall_type == 'square':
            side_length = dimensions.get('side', 0)
            if side_length > 0:
                wall_area = side_length ** 2
            else:
                return None
        elif wall_type == 'rectangle':
            length = dimensions.get('length', 0)
            width = dimensions.get('width', 0)
            if length > 0 and width > 0:
                wall_area = length * width
            else:
                return None
        elif wall_type == 'circle':
            radius = dimensions.get('radius', 0)
            if radius > 0:
                wall_area = math.pi * radius ** 2
            else:
                return None
        elif wall_type == 'triangle':
            base = dimensions.get('base', 0)
            height = dimensions.get('height', 0)
            if base > 0 and height > 0:
                wall_area = 0.5 * base * height
            else:
                return None
        else:
            return None
        total_area = wall_area

    elif figure_type == 'room':
        room_type = dimensions.get('room_type')
        height = dimensions.get('height', 0)
        if room_type == 'square':
            side_length = dimensions.get('side', 0)
            if side_length > 0 and height > 0:
                perimeter = 4 * side_length
                total_wall_area = perimeter * height
            else:
                return None
        elif room_type == 'rectangle':
            length = dimensions.get('length', 0)
            width = dimensions.get('width', 0)
            if length > 0 and width > 0 and height > 0:
                perimeter = 2 * (length + width)
                total_wall_area = perimeter * height
            else:
                return None
        elif room_type == 'circle':
            diameter = dimensions.get('diameter', 0)
            if diameter > 0 and height > 0:
                perimeter = math.pi * diameter
                total_wall_area = perimeter * height
            else:
                return None
        elif room_type == 'triangle':
            side_length = dimensions.get('side', 0)
            if side_length > 0 and height > 0:
                wall_area = 0.5 * side_length * height
                total_wall_area = 3 * wall_area
            else:
                return None
        else:
            return None
        total_area = total_wall_area

    if total_area <= 0:
        return None

    roll_area = roll_width * roll_length
    rolls_needed = total_area / roll_area
    rolls_needed = math.ceil(rolls_needed)
    return rolls_needed

def get_dimension_value(request, key):
    value = request.POST.get(key, '')
    try:
        return float(value) if value else 0
    except ValueError:
        return 0

def wallpaper_calculator_view(request):
    num_rolls = None
    figure_type = request.POST.get('figure_type', 'wall')
    wall_type = request.POST.get('wall_type', 'square')
    room_type = request.POST.get('room_type', 'square')

    if request.method == 'POST':
        roll_width = get_dimension_value(request, 'roll_width')
        roll_length = get_dimension_value(request, 'roll_length')

        dimensions = {
            'wall_type': wall_type,
            'room_type': room_type,
            'side': get_dimension_value(request, 'side'),
            'width': get_dimension_value(request, 'width'),
            'height': get_dimension_value(request, 'height'),
            'length': get_dimension_value(request, 'length'),
            'radius': get_dimension_value(request, 'radius'),
            'base': get_dimension_value(request, 'base'),
            'diameter': get_dimension_value(request, 'diameter'),
        }

        num_rolls = calculate_wallpaper_rolls(figure_type, dimensions, roll_width, roll_length)

    return render(request, 'calculator/wallpaper_calculator.html', {
        'num_rolls': num_rolls,
        'figure_type': figure_type,
        'wall_type': wall_type,
        'room_type': room_type,
    })

