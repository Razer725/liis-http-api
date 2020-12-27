# http-сервис на Django/DRF
## Бронирование рабочих мест на определенный период времени:
пример curl запроса:
```
curl -X POST \
  http://127.0.0.1:8000/api/booking/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F workplace=3 \
  -F datetime_from=2020-12-30T16:12:56Z \
  -F datetime_to=2020-12-30T18:14:56Z
```
ответ:
```
{
    "workplace": 3,
    "datetime_from": "2020-12-30T16:12:56Z",
    "datetime_to": "2020-12-30T18:14:56Z"
}
```
##  Просмотра списка бронирований по id рабочего места
пример curl запроса:

```
curl -X GET \
  http://127.0.0.1:8000/api/show-booking/1/ \
  -H 'cache-control: no-cache' \
```
ответ:
```
[
    {
        "workplace": {
            "workplace_number": 1,
            "cabinet": 1
        },
        "datetime_from": "2020-12-27T11:10:35Z",
        "datetime_to": "2020-12-28T11:10:36Z"
    },
    {
        "workplace": {
            "workplace_number": 1,
            "cabinet": 1
        },
        "datetime_from": "2020-12-30T16:11:56Z",
        "datetime_to": "2020-12-30T16:11:58Z"
    }
]
```
## Получение токена
пример curl запроса:
```
curl -X POST \
  http://127.0.0.1:8000/api-token-auth/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F username=ivan \
  -F password=123456
```
ответ:
```
{
    "token": "35342541b998910807740af659cc9d7856e6a486"
}
```
## Список рабочих мест, свободных в указанный временной промежуток
пример curl запроса:
```
curl -X GET \
  'http://127.0.0.1:8000/api/free-workplaces/?datetime_from=2020-12-29T16%3A11%3A56Z&datetime_to=2020-12-30T16%3A11%3A58Z' \
  -H 'cache-control: no-cache' \
```
ответ:
```
[
    {
        "workplace_number": 3
    }
]
```