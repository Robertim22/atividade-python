class ConversorTemperatura:
    @staticmethod
    def fahrenheit_para_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    @staticmethod
    def celsius_para_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit


temperatura_fahrenheit = 100
temperatura_celsius = ConversorTemperatura.fahrenheit_para_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} fahrenheit é igual a {temperatura_celsius:.2f} celsius.")

temperatura_celsius = 50
temperatura_fahrenheit = ConversorTemperatura.celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} celsius é igual a {temperatura_fahrenheit:.2f} fahrenheit.")
