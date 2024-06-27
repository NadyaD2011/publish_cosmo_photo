# Сохранение фотографий с сайта SpaceX

## Окружение

Скрипт позволяет сохранять великолепные фотографии с сайта SpaceX по вашему id или с последнего запуска.

Программа берет id и:

- Создаёт папку

- Получаем фотографии

- Сохраняем фотографии в созданную папку

## Установка зависемостей

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для
установки зависимостей:
```
pip install -r requirements.txt
```

Рекомендуется использовать [virtualent/vent](http://docs.python.orgs/3/library/venv.html)

## Настройка переменных окружения

`folder_name` - название папки

`id` - передаваемая переменная при запуске код

### Как же их получить?

`id` передаётся в запуске. Посмотреть как передовать показано в следущем разделе.

## Запуск программы

`В примере запуск производится в командной строке`

```
C:\Users\User>cd C:\Users\User\Desktop\`название папки с проектом`
C:\Users\User\Desktop\Новая папка>python main.py `ваш id`
```

Вывод:

```
C:\Users\User>cd C:\Users\User\Desktop\Новая папка
C:\Users\User\Desktop\Новая папка>python main.py ничего или id
```

`Если id не передаётся, то будут сохранятся фотографии с последнего запуска`

# Сохранение фотографий с сайта NATA

## Окружение

Скрипт позволяет сохранять великолепные фотографии с сайта NASA по вашему APi ключу или с последнего запуска.

Программа работаем так:

- Создаёт папку

- Получаем фотографии

- Сохраняем фотографии в созданную папку

## Установка зависемостей

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для
установки зависимостей:
```
pip install -r requirements.txt
```

Рекомендуется использовать [virtualent/vent](http://docs.python.orgs/3/library/venv.html)

## Настройка переменных окружения

`folder_name` - название папки

`api_key` - передаваемая переменная при запуске код

### Как же их получить?

`api_key` передаётся в .env. Чтобы получить АPI ключь. Зарегистрируйтесь на [этом сайте](https://api.nasa.gov/#apod). И получите API ключь.

## Запуск программы

`В примере запуск производится в командной строке`

```
C:\Users\User>cd C:\Users\User\Desktop\`название папки с проектом`
C:\Users\User\Desktop\Новая папка>python main.py
```

Вывод:

```
C:\Users\User>cd C:\Users\User\Desktop\Новая папка
C:\Users\User\Desktop\Новая папка>python main.py
```

# Сохранение фотографий с сайта NATA

## Окружение

Скрипт позволяет сохранят EPIC фотографии с сайта NASA по вашему APi ключу или с последнего запуска.

Программа работаем так:

- Создаёт папку

- Получаем эпичные фотографии

- Сохраняем фотографии в созданную папку

## Установка зависемостей

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для
установки зависимостей:
```
pip install -r requirements.txt
```

Рекомендуется использовать [virtualent/vent](http://docs.python.orgs/3/library/venv.html)

## Настройка переменных окружения

`folder_name` - название папки

`api_key` - передаваемая переменная в файле .env

### Как же их получить?

`api_key` передаётся в .env. Чтобы получить АPI ключь. Зарегистрируйтесь на [этом сайте](https://api.nasa.gov/#apod). И получите API ключь.

## Запуск программы

`В примере запуск производится в командной строке`

```
C:\Users\User>cd C:\Users\User\Desktop\`название папки с проектом`
C:\Users\User\Desktop\Новая папка>python main.py
```

Вывод:

```
C:\Users\User>cd C:\Users\User\Desktop\Новая папка
C:\Users\User\Desktop\Новая папка>python main.py
```

# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков 
[dvmn.org.](http://https://dvmn.org/).
