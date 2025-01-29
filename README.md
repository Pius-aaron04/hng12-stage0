# HNG12 Stage0 Task (Public API)

This public API app is a single endpoint API app that returns basic information such as:
* My registered email used for HNG 12
* The current datetime in ISO 8601
* GitHub url to this codebase


## API Specification
* Endpoint: ``GET <my_url>``
* Response (200 OK):
```
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Pius-aaron04/hng12-stage0"
}
```

## Installation
```
# clone the repository

git clone https://github.com/Pius-aaron04/hng12-stage0
cd hng12-stage0

# install requirements
pip install -r requirements.txt
```

## Execution
Run:
``` fastapi dev api/app.py ```

## Backlinks:
- [HNG Python Devs](https://hng.tech/hire/python-developers)
- [HNG C# Devs](https://hng.tech/hire/csharp-developers)
- [HNG Go lang Devs](https://hng.tech/hire/golang-developers)
- [HNG PHP Devs](https://hng.tech/hire/php-developers)
- [HNG Java Devs](https://hng.tech/hire/java-developers)
- [HNG NodeJS Devs](https://hng.tech/hire/nodejs-developers)
