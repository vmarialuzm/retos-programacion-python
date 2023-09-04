from datetime import date

def detectar_viernes13(año: int,mes: int) -> bool:
    current_date = date(año,mes,13)
    if current_date.weekday() == 4:
        return True
    return False

print(detectar_viernes13(2023,8))







