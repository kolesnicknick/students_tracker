CRUD App for track of students

#TASK4
- Создать вью функцию которая будет генерировать одного студенты с случайными параметрами.

- Написать команду которая будет генерировать 100 случайных студентов (python manage.py generate_students) (https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)

- Создать модель Group добавить несколько полей (название и тип по-желанию)

#TASK5
- Перенести весь функционал студентов на новую модель Teacher.
- В результате должен быть фильтр по полям first_name last_name email с оператором OR (sql) (8 баллов)
- Добавить функционал студентов на модель Group (2 балла)

#TASK6
- Добавить формы
- Создать форму добавления для Учителя
- Создать форму добавления группы.

#TASK7
Для учителей и групп должно быть
- Возможность редактировать запись в базе данных
- Для работы с urls во вьюхах и шаблонах использовать reverse и {% url 'name' %}
- Создать в приложении учителя файл urls.py вынести все урлы связанные с этим приложением и заинклюдить их в основном файле utls.py
- Добавить логгирование на отправку почты (записывать почту, сабджект в текстовый файл)
- Каждые элемент в списке (студент, группа, учитель) должен быть кликабельным и вести на страницу редактирования соответствующего объекта. Добавить в шаблонах кнопку которая будет вести на добавление объекта.

#TASK8
- Добавить блок title для каждой страницы.
- вывести студентов, преподавателей, группы в виде таблицы (слинками на редактирование )
- Для перехода между страницами использовать тег а (<a href="...">link</a>)
- Все шаблоны должны быть наследованные от базового шаблона.

Additional:

#TASK9
- Добавить в модель Group внешние ключи на куратора () и старосту (). 
- Вывести соответствующую информацию в таблицах. Обновить скрипт по генерации случайных данных.
- Использовать postgresql как основную базу.

Additional:
- Создать миграционный скрипт, который будет добавлять группе, 
у которой нет куратора и старосты эти поля. Разбить миграцию на несколько этапов
- Настроить controller middleware и трекать каждый кол в файл logs.json
- После миграции перейти на postgres, через helper.py создать и наполнить новую базу данными

