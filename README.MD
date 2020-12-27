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