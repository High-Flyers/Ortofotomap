import subprocess
import time
from datetime import datetime

def capture_images(interval_seconds, total_images, save_directory):
    """
    Funkcja wykonująca zdjęcia w określonych odstępach czasowych za pomocą libcamera.
    
    :param interval_seconds: Odstęp czasowy między zdjęciami (w sekundach)
    :param total_images: Łączna liczba zdjęć do wykonania
    :param save_directory: Katalog, w którym będą zapisywane zdjęcia
    """
    if interval_seconds <= 0 or total_images <= 0:
        raise ValueError("Interval and total_images must be greater than 0.")
    
    for i in range(total_images):
        # Generation unique photo name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{save_directory}/image_{timestamp}.jpg"
        
        try:
            # call libcamera-still
            subprocess.run(
                [
                    "libcamera-still", 
                    "-o", filename,          # Nazwa pliku
                    "--nopreview",           # Wyłączenie podglądu
                    "--timeout", "100",      # Minimalny czas wykonania zdjęcia (w ms)
                    "--width", "1280",       # Szerokość zdjęcia
                    "--height", "720",       # Wysokość zdjęcia
                    "--shutter", "10000",    # Czas otwarcia migawki (w mikrosekundach)
                    "--awb", "fluorescent",  # Ustawienie balansu bieli
                    "--gain", "1.0"          # Stałe wzmocnienie
                ],
                check=True
            )
            print(f"[{i + 1}/{total_images}] Zdjęcie zapisane: {filename}")
        except subprocess.CalledProcessError as e:
            print(f"Błąd podczas wykonywania zdjęcia: {e}")
        
        # waiting before next photo if it isn't last
        if i < total_images - 1:
            time.sleep(interval_seconds)

# example of using the function
if __name__ == "__main__":
    capture_images(interval_seconds=1, total_images=5, save_directory="/home/kuklok/Pictures")
