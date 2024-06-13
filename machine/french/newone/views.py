from django.shortcuts import render
import math

def calculate_perimeter_area(shape, dimensions):
    if shape == "Square":
        side = dimensions.get('side', 0)
        if side > 0:
            perimeter = 4 * side
            area = side ** 2
        else:
            perimeter, area = None, None
    elif shape == "Rectangle":
        length = dimensions.get('length', 0)
        width = dimensions.get('width', 0)
        if length > 0 and width > 0:
            perimeter = 2 * (length + width)
            area = length * width
        else:
            perimeter, area = None, None
    elif shape == "Circle":
        radius = dimensions.get('radius', 0)
        if radius > 0:
            perimeter = 2 * math.pi * radius
            area = math.pi * radius ** 2
        else:
            perimeter, area = None, None
    else:
        perimeter, area = None, None
    return perimeter, area

def shape_calculator_view(request):
    perimeter = area = None
    shape_type = request.POST.get('shape_type', 'Square')

    if request.method == 'POST':
        dimensions = {}
        if shape_type == 'Square':
            dimensions['side'] = float(request.POST.get('side', 0) or 0)
        elif shape_type == 'Rectangle':
            dimensions['length'] = float(request.POST.get('length', 0) or 0)
            dimensions['width'] = float(request.POST.get('width', 0) or 0)
        elif shape_type == 'Circle':
            dimensions['radius'] = float(request.POST.get('radius', 0) or 0)

        perimeter, area = calculate_perimeter_area(shape_type, dimensions)

    return render(request, 'shape_calculator.html', {
        'perimeter': perimeter,
        'area': area,
        'shape_type': shape_type,
    })