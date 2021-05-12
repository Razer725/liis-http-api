# http-сервис на Django/DRF
Приложение предоставляет API, позволяющее осуществлять бронирование рабочих мест в кабинетах. API предоставляет ресурсы для:
* бронирования рабочих мест на определенный период времени;
* просмотра списка бронирований по id рабочего места;
* авторизация
* ресурс рабочих мест имеет 2 необязательных параметра фильтрации: «datetime_from», «datetime_to», ожидающих datetime в формате ISO. Если данные валидны, то ответом на GET с указанными параметрами является список рабочих мест, свободных в указанный временной промежуток.
## Бронирование рабочих мест на определенный период времени:
пример curl запроса:
```
curl -X POST \
  https://liis-http-service.herokuapp.com/api/booking/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -H 'postman-token: d6e4d04f-8341-e638-5d5c-8c6db72303f8' \
  -F workplace=3 \
  -F datetime_from=2020-12-30T16:12:56Z \
  -F datetime_to=2020-12-30T18:14:56Z
```
пример ответа:
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
  https://liis-http-service.herokuapp.com/api/show-booking/1/ \
  -H 'cache-control: no-cache' \
  -H 'postman-token: bd61ae1b-2322-154f-b6d5-cbcf6ff546af'
```
пример ответа:
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
  https://liis-http-service.herokuapp.com/api-token-auth/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -H 'postman-token: 355cadc9-b247-443a-b3bd-38a2d34661d4' \
  -F username=admin \
  -F password=123456
```
пример ответа:
```
{
    "token": "35342541b998910807740af659cc9d7856e6a486"
}
```
## Список рабочих мест, свободных в указанный временной промежуток
пример curl запроса:
```
curl -X GET \
  'https://liis-http-service.herokuapp.com/api/free-workplaces/?datetime_from=2019-12-29T16%3A11%3A56Z&datetime_to=2020-12-30T16%3A11%3A58Z' \
  -H 'cache-control: no-cache' \
  -H 'postman-token: ed8485ce-4afc-f6ce-dfe2-534e37e8382c'
```
пример ответа:
```
[
    {
        "workplace_number": 3
    }
]
```


