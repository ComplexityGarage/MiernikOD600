from machine import Pin, ADC
import time
import math

# --- Konfiguracja sprzętowa ---

# Piny dla diody LED i przycisków
led = Pin(15, Pin.OUT)
blank_button = Pin(16, Pin.IN, Pin.PULL_UP)
measure_button = Pin(17, Pin.IN, Pin.PULL_UP)

# Pin dla fototranzystora (ADC0)
adc = ADC(26)

# --- Zmienne globalne ---
blank_value = 0
is_blanked = False

# --- Funkcje pomiarowe ---

def measure_light():
    led.value(1)  # Włącza LED
    time.sleep(0.05) # Czas świecenia diody LED
    sample_value = adc.read_u16()
    led.value(0)  # Wyłącza LED
    return sample_value

def take_average_measurement(num_measurements=100):
    total_value = 0
    for _ in range(num_measurements):
        total_value += measure_light()
        time.sleep(0.01)
    return total_value / num_measurements

def calculate_od600(blank, sample):
    if blank <= 0:
        return 0.0
    
    if sample > blank:
        sample = blank

    if sample <= 0:
        return 1.0 
    
    od = -math.log10(sample / blank)
    
    if od < 0.0:
        return 0.0
    if od > 1.0:
        return 1.0
    else:
        return od


print("Miernik OD600 - gotowy.")
print("Nacisnij przycisk BLANK aby skalibrowac.")

try:
    while True:
        if blank_button.value() == 0:
            print("Blankowanie...")
            time.sleep(0.2)
            
            blank_value = take_average_measurement(100)
            
            is_blanked = True
            print("Blankowanie zakonczone.")
            print("OD600: 0.000")
            print("Nacisnij przycisk POMIARU.")
            
        if measure_button.value() == 0 and is_blanked:
            print("Pomiar...")
            time.sleep(0.2)
            
            sample_value = take_average_measurement(100)
            
            od600_value = calculate_od600(blank_value, sample_value)
            
            print(f"OD600: {od600_value:.3f}")
            print("Gotowy na nastepny pomiar.")
            
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program zakonczony")
finally:
    led.value(0)
