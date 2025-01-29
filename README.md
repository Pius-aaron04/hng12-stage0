# HNG12 Stage0 Task (Public API)

This Public API application features a single endpoint that provides the following information:
* Registered Email: The email associated with my HNG12 registration
* Current Date and Time: The current datetime formatted in ISO 8601
* GitHub Repository: A link to this codebase on GitHub


## API Specification
* Endpoint: [https://blank-veronike-ascii-pius-b2967347.koyeb.app/](https://blank-veronike-ascii-pius-b2967347.koyeb.app/)
* Response (200 OK):
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Pius-aaron04/hng12-stage0"
}
```

## Installation
1. **Clone the repository:**
```bash
git clone https://github.com/Pius-aaron04/hng12-stage0
cd hng12-stage0
```

2. **Install requirements:**
```bash
pip install -r requirements.txt
```

## Execution
* Production mode:
```bash
fastapi run api/app.py
```
* Dev mode:
```bash
fastapi dev api/app.py
```

## Backlinks:
- [HNG Python Devs](https://hng.tech/hire/python-developers)
