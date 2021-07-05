# RBT Summer Internship 2021 Backend

Backend code written in Python for Airvironment 2021 Summer internship.

## Requests and Responses
GET /measurements

Response:
```JSON
[
   {
      "id": Int,
      "air_quality": Float,
      "temperature": Float,
      "humidity": Float,
      "time_stamp": DateTime
   }
]
```

POST /measurements
Post Request:
```JSON
{
   "air_quality": Float,
   "temperature": Float,
   "humidity": Float
}
```

Response:
```JSON
{
   "id": Int,
   "air_quality": Float,
   "temperature": Float,
   "humidity": Float,
   "time_stamp": DateTime
}
```

GET /measurements/<int: id>
```JSON
{
   "id": Int,
   "air_quality": Float,
   "temperature": Float,
   "humidity": Float,
   "time_stamp": DateTime
}
```