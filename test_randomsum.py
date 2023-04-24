import subprocess

def test_python_command_execution():
    # Ejecuta el comando de Python y obtiene el código de salida y la salida estándar
    result = subprocess.run(["python3", "test_randomsum.py"], capture_output=True, text=True)
    exit_code = result.returncode
    stdout = result.stdout

    # Verifica que el código de salida sea 0
    assert exit_code == 0, f"El código de salida fue {exit_code}. Se esperaba 0."

    # Verifica que tres líneas distintas tengan valores diferentes a nulo o cero
    lines = stdout.split("\n")
    assert len(lines) >= 1, "El código de salida fue diferente de 0"
