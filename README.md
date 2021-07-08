# RBT Summer Internship 2021 Backend

Backend code written in Python for Airvironment 2021 Summer internship.

It can be started in developer mode by running:

```bash
python3 run.py
```

or in production mode by running following commands:

```bash
export FLASK_APP=run.py
flask run
```

## Requests and Responses
GET /api/measurements
Response:
```JSON
[
   {
      "id": "Int",
      "air_quality": "Float",
      "temperature": "Float",
      "humidity": "Float",
      "time_stamp": "DateTime"
   }
]
```

POST /api/measurements
Post Request:
```JSON
{
   "air_quality": "Float",
   "temperature": "Float",
   "humidity": "Float"
}
```

Response:
```JSON
{
   "id": "Int",
   "air_quality": "Float",
   "temperature": "Float",
   "humidity": "Float",
   "time_stamp": "DateTime"
}
```

GET /api/measurements/latest
Response:
```JSON
{
  "id": "Int",
  "air_quality": "Float",
  "temperature": "Float",
  "humidity": "Float",
  "time_stamp": "DateTime"
}

GET /api/measurements/<int: id>
```JSON
{
   "id": "Int",
   "air_quality": "Float",
   "temperature": "Float",
   "humidity": "Float",
   "time_stamp": "DateTime"
}
```