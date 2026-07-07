import math

angle = int(input("enter: "))

angle = math.radians(angle)

sin_value = math.sin(angle)
cos_value = math.cos(angle)
tan_value = math.tan(angle)

print(f"Trigonometric values for {angle}:")
print(f"Sine:   {sin_value}")
print(f"Cosine: {cos_value}")
print(f"Tangent: {tan_value}")