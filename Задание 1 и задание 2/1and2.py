import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def analyze_triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "Некорректные стороны треугольника."
    
    t_type = triangle_type(a, b, c)
    area = triangle_area(a, b, c)
    return f"Тип треугольника: {t_type}, Площадь: {area:.2f}"

print(analyze_triangle(3, 4, 5))
///////////////////////////////////////////////////////////////////////
import math

def analyze_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Некорректные стороны треугольника."
    
    a, b, c = sorted([a, b, c])
    
    if c**2 == a**2 + b**2:
        angle_type = "прямоугольный"
    elif c**2 < a**2 + b**2:
        angle_type = "остроугольный"
    else:
        angle_type = "тупоугольный"
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return f"Тип треугольника по углам: {angle_type}, Площадь: {area:.2f}"


print(analyze_triangle(3, 4, 5))
print(analyze_triangle(5, 5, 5))
print(analyze_triangle(7, 10, 5))