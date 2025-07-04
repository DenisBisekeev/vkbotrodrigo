import subprocess

# Запуск файлов в фоновом режиме
process1 = subprocess.Popen(["python", "main.py"])
process2 = subprocess.Popen(["python", "help.py"])
process3 = subprocess.Popen(["python", "app.py"])
# Дождаться завершения (опционально)
process1.wait()
process2.wait()
process3.wait()
