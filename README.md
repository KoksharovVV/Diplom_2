# Diplom_2


# # Проект автоматизации тестирования для api Stellar Burgers.

1. Основа для написания автотестов — фреймворк pytest.
2. Библиотека для отправки запросов - requests
3. Для построения отчета о тестировании используется Allure
4. Установить зависимости — pip install -r requirements.txt.
5. Команда для запуска тестов с генерацией отчета  — pytest -v --alluredir=allure_results
6. Команда для построения отчета о тестировании — allure serve allure_results

# Созданы тесты, покрывающие ручки

- создания пользователя
- логин пользователя
- изменение данных пользователя
- создания заказа 
- получение заказов по конкретному пользователю

## Документация
https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89