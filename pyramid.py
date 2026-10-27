import math

calculate_volume = lambda s1, s2, h: (1/3) * h * (s1 + s2 + math.sqrt(s1 * s2))

def run() -> None:
    print("Вычисление объема усеченной пирамиды")
    
    try:
        s1: float = float(input("Введите площадь первого основания: "))
        s2: float = float(input("Введите площадь второго основания: "))
        h: float = float(input("Введите высоту усеченной пирамиды: "))
        
        if s1 < 0 or s2 < 0 or h <= 0:
            print("Площади не могут быть отрицательными, а высота должна быть больше нуля.")
            return
            
        volume: float = calculate_volume(s1, s2, h)
        print("Объем усеченной пирамиды равен:", volume)
        
    except ValueError:
        print("Ошибка, пожалуйста, вводите числовые значения.")

if __name__ == "__main__":
    print("Запустите программу через файл main.py")