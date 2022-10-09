# Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

znach = (0, 1)
teorema = True
for x in znach:
    for y in znach:
        for z in znach:
            if not (x or y or z) != (not (x) and not (y) and not (z)):
                teorema = False
print(f' ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат - {teorema}')
