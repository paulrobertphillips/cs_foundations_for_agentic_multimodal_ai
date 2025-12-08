📌 Example: Create and use a virtual environment


1. Create a venv

```
python3 -m venv .venv

```

2. Activate it

Mac/Linux:
```
source .venv/bin/activate

```
Windows:
```
.venv\Scripts\activate

```

3. Install dependencies

```
pip install pydantic aiohttp numpy

```

4. Freeze dependencies

```
pip freeze > requirements.txt

```

5. Re-create environment later

```
pip install -r requirements.txt

```