from PIL import Image

# Размер изображения
width, height = 1600, 900

# Цвета градиента (в формате RGB)
colors = [
    (52, 152, 219),  # Голубой (#3498db)
    (133, 193, 233),  # Светло-голубой (#85c1e9)
    (255, 255, 255),  # Белый (#ffffff)
    (72, 201, 176),   # Лазурный (#48c9b0)
    (213, 219, 219)   # Светло-серый (#d5dbdb)
]

# Создаем пустое изображение
gradient_edges = Image.new("RGB", (width, height))

# Заполняем градиент по краям
for y in range(height):
    for x in range(width):
        # Вычисляем blend-фактор для краев (от 0 до 1)
        blend_x = x / width
        blend_y = y / height

        # Интерполяция по горизонтали
        r = int(colors[0][0] * (1 - blend_x) + colors[-1][0] * blend_x)
        g = int(colors[0][1] * (1 - blend_x) + colors[-1][1] * blend_x)
        b = int(colors[0][2] * (1 - blend_x) + colors[-1][2] * blend_x)

        # Усиление градиента по вертикали для добавления глубины
        r = int(r * (1 - blend_y) + colors[2][0] * blend_y)
        g = int(g * (1 - blend_y) + colors[2][1] * blend_y)
        b = int(b * (1 - blend_y) + colors[2][2] * blend_y)

        gradient_edges.putpixel((x, y), (r, g, b))

# Сохраняем изображение
gradient_edges.save("gradient.png")
