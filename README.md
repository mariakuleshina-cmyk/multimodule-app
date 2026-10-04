# Лабораторная работа №5

Многомодульное приложение на Python + PyQt5 для получения, отображения и сохранения данных.

## Файлы

- `main.py` — запуск
- `main_window.py` — главное окно
- `table_window.py` — окно таблицы
- `data_reader.py` — получение данных
- `ui_main_window.py`, `ui_table_window.py` — интерфейсы из Qt Designer
- `data.csv` — файл данных

## Запуск

pip install PyQt5
python main.py

## Сборка

pip install pyinstaller
pyinstaller --onefile --windowed --name myapp main.py