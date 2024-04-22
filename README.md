PlayerAPI
---------------------------------

Simple backend project for school.

---------------------------------
Installation:

- Have Python (3.10) and pip installed
- Clone this repository to you local machine:
    - ```bash
    - git clone https://github.com/ville-hyvonen/PlayerAPI.git
      
- Go to the projects directory
    - cd PlayerAPI
 
- Create virtual environment (recommended)
    - python3 -m venv .venv
      or
    - python -m venv .venv

- Activate your venv
    Windows: venv\Scripts\activate
    macOS/Linux: venv/bin/activate
  
- Install libraries to your .venv
    - pip install uvicorn fastapi pydantic sqlmodel
 
-----------------------------------

Starting:

- uvicorn app.main:app --reload
if it doesn't work:
- python -m uvicorn app.main:app --reload

------------------------------------

Access:

Access the app at 'http://localhost:8000'
