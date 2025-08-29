import sys
import time

def fake_error():
    print("Ошибка выполнения: 0x80070005", file=sys.stderr)
    time.sleep(1)
    print("Доступ запрещен", file=sys.stderr)
    time.sleep(1)
    print("ХАХАХАХАХ ты хайло", file=sys.stderr)
    time.sleep(2)
    print("...шутка)")

if __name__ == "__main__":
    fake_error()