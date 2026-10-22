#---------------------------------------------------------
print('Задача 1')
#1
file = "text.txt"

lines_count = 0
words_count = 0
chars_count = 0
max_line_len = 0

f = open(file, "r", encoding="utf-8")
for line in f:
    lines_count += 1 
    chars_count += len(line)

    if len(line.strip()) > max_line_len:
        max_line_len = len(line.strip())

    words_count += len(line.split())
f.close()

print(f"Строк: {lines_count}")
print(f"Слов: {words_count}")
print(f"Символов: {chars_count}")
print(f"Самая длинная строка: {max_line_len}")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 2')
#2
numbers = []
file = "numbers.txt"

try:
    f = open(file, "r", encoding="utf-8")
    for line in f:
        try:
            num = int(line.strip())
            numbers.append(num)
        except ValueError:
            pass
    f.close()
except FileNotFoundError:
    print("Ошибка: Файл numbers.txt не найден!")

if len(numbers)!=0:
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = sum(numbers) / len(numbers)

    file2 = "result.txt"
    f2 = open(file2, "w", encoding="utf-8")
    f2.write(f"Минимум: {min_val}\n")
    f2.write(f"Максимум: {max_val}\n")
    f2.write(f"Среднее: {avg_val:.2f}\n")
    f2.close()
    print('Успешное добавление данных')
else:
    print("В списке не найдено корректных чисел.")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 3')
#3
import csv

total_score = 0
count = 0

max_student = None
max_score = 0

groups = {} # ключ - N группы, значение - список баллов этой группы
file = "students.csv"
f = open(file, "r", encoding="utf-8")

reader = csv.DictReader(f)
    
for row in reader:
    if not row:
        continue
    name = row["name"]
    group = row["group"]
    score = int(row["score"])
        
    total_score += score
    count += 1
        
    if score > max_score:
        max_score = score
        max_student = name
            
    if group not in groups:
        groups[group] = []
    groups[group].append(score)
f.close()

print(f"Средний балл всех студентов: {total_score / count:.2f}")
print(f"Студент с максимальным баллом: {max_student} ({max_score})")

for group, scores in groups.items():
    group_avg = sum(scores) / len(scores)
    print(f"Средний балл группы {group}: {group_avg:.2f}")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 4')
#4
import csv
file = "products.csv"
file2 = "expensive.csv"
f = open(file, "r", encoding="utf-8")
f2 = open(file2, "w", encoding="utf-8")
    
reader = csv.DictReader(f)
writer = csv.writer(f2)

columns = reader.fieldnames

writer.writerow(columns)

for row in reader:
    price = int(row["price"])
        
    if price > 100:
        writer.writerow(row.values())
        print('Успешное добавление')
f.close()
f2.close()
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 5')
#5
import json

file = "students.json"
file2 = "students_passed.json"
f = open(file, "r", encoding="utf-8")
f2 = open(file2, "w", encoding="utf-8")
    
students = json.load(f)

max_student = None
max_score = 0

for student in students:
    if student["score"] >= 60:
        student["passed"] = True
    else:
        student["passed"] = False
        
    if student["score"] > max_score:
        max_score = student["score"]
        max_student = student["name"]

print(f"Студент с максимальным баллом: {max_student} ({max_score})")

json.dump(students, f2, ensure_ascii=False)
f.close()
f2.close()
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 6')
#6
from pathlib import Path

directory_path = Path(".") #текущая папка

files_count = 0
folder_count = 0
total_size = 0
py_files = []

for item in directory_path.iterdir():
    if item.is_file():
        files_count += 1
        total_size += item.stat().st_size
        
        if item.suffix == ".py":
            py_files.append(item.name)
            
    elif item.is_dir():
        folder_count += 1

print(f"Количество файлов: {files_count}")
print(f"Количество подкаталогов: {folder_count}")
print(f"Список файлов .py: {py_files}")
print(f"Суммарный размер файлов: {total_size} байт")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 7')
#7
from pathlib import Path

folder = input("Каталог: ")
suffix = input("Расширение (например, .py): ")

path = Path(folder)

if not path.exists():
    print(f"Ошибка: Каталог '{path}' не существует!")
elif not path.is_dir():
    print(f"Ошибка: Путь '{path}' ведет к файлу, а не к каталогу!")
else:
    found_any_flag = False
    for file in path.iterdir():
        if file.is_file():
            if file.suffix == suffix:
                found_any_flag = True
                print(f"Путь: {file}. Размер: {file.stat().st_size} байт")
            
    if not found_any_flag:
        print(f"Файлы с расширением {suffix} не найдены.")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 8')
#8
def read_file(path):
    try:
        f = open(path, "r", encoding="utf-8")
        return f.read()
        f.close()
    
    except FileNotFoundError:
        return "Ошибка: Файл не найден."
    except PermissionError:
        return "Ошибка: Нет прав доступа для чтения этого файла."
    except UnicodeDecodeError:
        return "Ошибка: Невозможно прочитать файл (некорректная кодировка)."
    except OSError as e:
        return f"Системная ошибка: {e}"

print(read_file("non_existent_file.txt"))
print(read_file("students.json"))
print(read_file("numbers.txt"))
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 9')
#9
def parse_number(value):
    return float(value)

num = input("Введите число: ")

try:
    result = parse_number(num)
    print(f"Преобразование успешно! Ваше число: {result}")
except ValueError:
    print("Ошибка: Вы ввели не число, поэтому не удалось преобразовать данные.")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 10')
#10
class BankError(Exception):
    pass

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма снятия должна быть больше нуля!")
        
    if amount > balance:
        raise InsufficientFundsError("На счете недостаточно средств!")
    return balance - amount

try:
    current_balance = 1000
    new_balance = withdraw(current_balance, 1500)
    print(f"Успешно! Новый баланс: {new_balance}")
except BankError as e:
    print(f"Произошла банковская ошибка: {e}")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 11')
#11
import re

file = "logs.txt"
f = open(file, "r", encoding="utf-8")

all_users = []
error_lines = []
error_users = []

for line in f:
    line = line.strip()
    user_match = re.search(r"User ([0-9]+)", line)
        
    if user_match:
        user_id = user_match.group(1)
        all_users.append(user_id)
            
        if re.search(r"ERROR", line):
            error_lines.append(line)
            error_users.append(user_id)

f.close()
print("1. Все идентификаторы пользователей:", all_users)
print("2. Все строки с ERROR:")
for line in error_lines:
    print(f"{line}")
print("3. Идентификаторы пользователей с ошибками:", error_users)
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 12')
#12
import re

text = """
Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru
"""

email_re = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

all_emails = re.findall(email_re, text)

unique_emails = set(all_emails)

print("Найденные email адреса без повторений:")
for email in unique_emails:
    print(email)
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 13')
#13
#через класс с `__enter__` / `__exit__`
import time

class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        execution_time = self.end_time - self.start_time
        print(f"Время выполнения блока: {execution_time:.6f} сек.")
        return False 

with Timer():
    time.sleep(0.5)

#через `contextlib.contextmanager`
import time
from contextlib import contextmanager

@contextmanager
def timer_context():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        print(f"Время выполнения блока: {end_time - start_time:.6f} сек.")

with timer_context():
    time.sleep(0.5)
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 14')
#14
from contextlib import contextmanager

@contextmanager
def log_operation(log_filename, operation_name):
    log_file = open(log_filename, "w", encoding="utf-8")
    log_file.write(f"START: {operation_name}\n")
        
    try:
        yield
        log_file.write(f"END: {operation_name}\n")
    except Exception:
        log_file.write(f"ERROR: {operation_name}\n")
        raise
    log_file.close()
try:
    with log_operation("operation.log", "Data processing"):
        print("Делаем какие-то вычисления...")
except:
    print('Произошла ошибка')
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 15')
#15
from io import StringIO

def count_lines(stream):
    lines_count = 0
    for line in stream:
        lines_count += 1
    return lines_count

f = open("data.txt", "r")
print("Строк в реальном файле:", count_lines(f))
f.close()

fake_file = StringIO("first\nsecond\nthird")
print("Строк в ненастоящем файле:", count_lines(fake_file))
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 16')
#16
import re

f = open("logs2.txt", "r")
log_content = f.read()

log_stats = {}
error_users = set()

log_re = r"(INFO|WARNING|ERROR).*User\s(\d+)"

for line in log_content.strip().split('\n'):
    match = re.search(log_re, line)
    if match:
        log_type = match.group(1)
        user_id = match.group(2)
        
        if log_type not in log_stats:
            log_stats[log_type] = 1
        else:
            log_stats[log_type] += 1
        
        if log_type == "ERROR":
            error_users.add(user_id)

for log_type, count in log_stats.items():
    print(f"{log_type}: {count}")
f.close()
print(f"Пользователи, для которых встречались ошибки: {', '.join(error_users)}")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 17')
#17
total_sum = 0
total_count = 0
min_val = float('inf')
max_val = float('-inf')

# Открываем огромный файл
f = open("numbers.txt", "r", encoding="utf-8")
for line in f:
    line = line.strip()
    if not line: 
        continue
            
    num = int(line)
        
    total_sum += num
    total_count += 1
        
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
if total_count > 0:
    avg_val = total_sum / total_count
else:
    avg_val = 0

print(f"Сумма: {total_sum}")
print(f"Количество: {total_count}")
print(f"Минимум: {min_val}")
print(f"Максимум: {max_val}")
print(f"Среднее: {avg_val}")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 18')
#18
import json
import logging
import re

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

log_re = r"^(\S+)\s(\S+)\s(\S+)\s([A-Z]+)\s(\S+)\s(\d+)"

methods_dict = {}
urls_dict = {}
errors_4xx_count = 0

try:
    logging.info("Старт обработки файла access.log...")

    f = open("access.log", "r", encoding="utf-8")
    for line in f:
        line = line.strip()

        match = re.match(log_re, line)
        if match:
            ip = match.group(3)
            method = match.group(4)
            url = match.group(5)
            status_code = match.group(6)

            if method not in methods_dict:
                methods_dict[method] = 1
            else:
                methods_dict[method] += 1

            if url not in urls_dict:
                urls_dict[url] = 1
            else:
                urls_dict[url] += 1

            if int(status_code)>=400:
                errors_4xx_count += 1

    most_used_url = None
    max_url = 0

    for url, k in urls_dict.items():
        if k > max_url:
            max_url = k
            most_used_url = url

    if not most_used_url:
        most_used_url = 'Наиболее частого URL нет'

    final_stats = {
        "methods_count": methods_dict,
        "errors_4xx_count": errors_4xx_count,
        "most_used_url": most_used_url
    }

    f2 = open("log_stats.json", "w", encoding="utf-8")
    json.dump(final_stats, f2, ensure_ascii=False)

    logging.info(
        "Обработка успешно завершена, результаты сохранены в log_stats.json"
    )

    f.close()
    f2.close()

except FileNotFoundError:
    logging.error("Критическая ошибка: Файл 'access.log' не найден!")
except OSError as e:
    logging.error(f"Системная ошибка при чтении файла: {e}")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 19')
#19
import re

text = """
Позвони мне на +7 999 123-45-67 или на старый номер 8 (999) 123-45-67.
Также работают номера: 8 999 123-45-67 и +7 (999) 123-45-67 (+7-(999) 123-45-67).
"""

phone_re = r"(?:\+7|8)\s*\(?\d{3}\)?\s*\d{3}-\d{2}-\d{2}"

numbers = re.findall(phone_re, text)

print("Найденные телефонные номера:")
for num in numbers:
    print(num)
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 20')
#20
import re

text = """
Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026.
Следующая встреча запланирована на 1.11.2026.
"""

date_re = r"\d{2}\.\d{2}\.\d{4}"

dates = re.findall(date_re, text)

print("Найденные даты:")
for d in dates:
    print(d)
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 21')
#21
import re

def is_valid_login(login):
    login_re = r"^[a-zA-Z][a-zA-Z0-9_]{3,15}$"
    
    if re.match(login_re, login):
        return True
    else:
        return False

tests = ["user_123", "admin", "123user", "ab", "user-name", "very_long_username"]

for t in tests:
    print(f"{t} --> {is_valid_login(t)}")
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 22')
#22
import re

text = """
Полезные сайты: https://python.org, http://example.com/page,
https://example.com/docs/index.html и ftp://files.example.com/data.
"""

url_re = r"(?:https|http)://[^\s,]+"

urls = re.findall(url_re, text)

for url in urls:
    print(url)
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 23')
#23
import re

text = "Это   строка    с     большим    количеством   пробелов."
text2 = "   Текст   с   пробелами   "

result_text1 = re.sub(r"\s+", " ", text)
print(f'Результат 1: "{result_text1}"')

result_text2 = re.sub(r"\s+", " ", text2).strip()
print(f'Результат 2: "{result_text2}"')
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 24')
#24
import re

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]

products_re = r"^PRD-\d{5}$"

correct_products = []

for prod in products:
    if re.match(products_re, prod):
        correct_products.append(prod)

print(correct_products)
print('---------------------------------------------------------')
#---------------------------------------------------------

print('Задача 25')
#25
import re

logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]

log_re = r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s(?P<level>INFO|WARNING|ERROR)\sUser\s(?P<user_id>\d+)\s(?P<message>.*)"

for line in logs:
    match = re.match(log_re, line)
    if match:
        data = match.groupdict()
        print(data)
print('---------------------------------------------------------')
#---------------------------------------------------------
