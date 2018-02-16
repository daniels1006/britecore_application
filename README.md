# Risk Types API
Just an exercise to show some ideas and code.

Two endpoints are:

 - `GET /risk_type/`: fetch all risk types with their properties;
 - `GET /risk_type/`: fetch one risk type with its properties where `{{pk}}` stands for the risk type's id. Available ids are `1` and `2`.

 Links to test:
 - [Get all risk types](https://britecore.elevential.com/risk_type/)
 - [Get risk type #1](https://britecore.elevential.com/risk_type/1/)
 - [Get risk type #2](https://britecore.elevential.com/risk_type/2/)

 Data model E-R diagram is [here](https://raw.githubusercontent.com/daniels1006/britecore_application/master/Data%20Model.png)

 ORM file (Django Models) is [here](https://github.com/daniels1006/britecore_application/blob/master/risk_api/api/models.py)
