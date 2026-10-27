def calculate_kettles(kettle_power: float, cable_section: float) -> int:
    voltage = 220
    
    # Допустимый ток - 10 Ампер на каждый 1 мм² сечения медного кабеля
    max_current = cable_section * 10
    
    # Максимальная допустимая мощность (P = U * I)
    max_total_power = voltage * max_current
    
    # Количество чайников 
    kettles_count = int(max_total_power // kettle_power)
    
    return kettles_count

def run() -> None:
    print("Расчет количества чайников")
    
    try:
        power = float(input("Введите мощность одного чайника (в Вт): "))
        section = float(input("Введите сечение медного кабеля (в мм²): "))
        
        if power <= 0 or section <= 0:
            print("Ошибка, мощность и сечение кабеля должны быть больше нуля.")
            return
            
        count = calculate_kettles(power, section)
        print("В розетку можно одновременно включить количество чайников: ", count)
        
    except ValueError:
        print("Ошибка, пожалуйста, вводите числовые значения.")

if __name__ == "__main__":
    print("Запустите программу через файл main.py")