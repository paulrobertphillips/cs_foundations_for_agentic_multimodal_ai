# Module 0.2 — Virtual Environments & Dependency Management

### 📌 Example: Create and use a virtual environment

**If you run into issues here, please refer to the following location in the repository.**
```
resources/
    documents/
       Setting Up Python Natively On Machine.pdf 
```

1. Create a venv

```
python -m venv .venv

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

### 🔨 Step 1 — Start With Your Existing Folder

Your project:

```
my_project/
    main.py
    tools/
        __init__.py
        io_tools.py
    processing/
        __init__.py
        data_tools.py
```

This is already perfectly structured for packaging.

### 🔧 Step 2 — Add a pyproject.toml at the root

Create a new file:

```my_project/pyproject.toml```


Paste this inside:

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "A simple example package for practicing Module 0 tooling."
authors = [
    { name = "Your Name" }
]
readme = "README.md"
requires-python = ">=3.10"

# Dependencies your package needs at runtime
dependencies = [
    "pandas>=2.0",        # optional, but common for data tooling
    "pydantic>=2.0",      # we will use later in Module 0
]

# This tells Python how to build/install your package
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

# Optional: code formatting/linting tools for clean agents
[tool.black]
line-length = 88

[tool.isort]
profile = "black"
```

No other files need to change yet.

### 📦 Step 3 — Make your project pip-installable locally

Inside your venv, from the root folder that contains pyproject.toml:

```python
pip install -e .
```

This says:

"Install this project in editable mode, so Python treats it like a package."

If successful, you’ll see something like:

```Successfully installed my-project```

### 🧪 Step 4 — Test that your package imports like a real module

In your venv, open a Python shell:

```python```

Then run:

```python
import my_project.tools.io_tools as io
import my_project.processing.data_tools as dt

rows = [{"value": "12"}, {"value": "5"}]
print(dt.filter_rows(rows))
```

You should see:

```python
[{'value': '12'}]
```

If that works:

🎉 You now have a real Python package managed by pyproject.toml.

### Issue: Able to Get Successful Install Message But Cannot Reference Package

Nice, this is actually a **good** error to hit – it means we’re right at the point where “real packaging” details start to matter.

There are **two things** that can cause `ModuleNotFoundError: No module named 'my_project'` in your situation:

1. VS Code’s REPL isn’t using the same **venv** where you ran `pip install -e .`
2. The project layout doesn’t actually expose a `my_project` **package** (only a folder)

I’ll walk you through fixing **both**, without needing any guesswork.

---

### 1️⃣ Make sure the REPL is using your venv

In VS Code, in the same folder where `pyproject.toml` lives:

1. Open a terminal and activate your venv (you’ve done this, but let’s be explicit):

   ```bat
   .venv\Scripts\activate
   ```

   You should see:

   ```bat
   (.venv) C:\path\to\your\project>
   ```

2. In VS Code, make sure the **Python interpreter** is your venv:

   * Hit **Ctrl+Shift+P**
   * Type: `Python: Select Interpreter`
   * Choose the one that looks like:

     ```
     .venv\Scripts\python.exe
     ```

3. Now open a **Python REPL / interactive window** again, and in it run:

   ```python
   import sys
   print(sys.executable)
   ```

   ✅ If it prints a path containing `.venv\Scripts\python.exe`, you’re good.
   ❌ If it’s something else (e.g., Anaconda, global Python), then the REPL isn’t using your venv and won’t see your installed package.

Once the REPL is definitely using the venv, we fix the second issue.

---

### 2️⃣ Fix the project layout so `my_project` is actually a package

Right now, you probably have something like:

```text
C:\...\module_0\exercise_2\
    pyproject.toml
    main.py
    tools/
        __init__.py
        io_tools.py
    processing/
        __init__.py
        data_tools.py
```

This **works as a script project**, but when you say:

```python
import my_project.tools.io_tools as io
```

Python expects a **folder named `my_project/` with an `__init__.py` inside**.
That folder doesn’t exist yet – the outer folder is named `exercise_2` (or similar), and `my_project` only exists as the *project name* in `pyproject.toml`, not as a Python package directory.

Let’s fix that by introducing a real `my_project` package.

### 🔧 New recommended layout

Restructure to this:

```text
exercise_2/
    pyproject.toml
    my_project/
        __init__.py
        main.py
        tools/
            __init__.py
            io_tools.py
        processing/
            __init__.py
            data_tools.py
```

Concretely:

1. Create a **folder** called `my_project` inside your project root.
2. Move these files **into** `my_project/`:

   * `main.py`
   * the `tools/` folder
   * the `processing/` folder
3. Inside `my_project/`, create an empty `__init__.py` file:

   ```text
   my_project/
       __init__.py
       main.py
       tools/
       processing/
   ```

Now `my_project` is a **real package**.

---

### 3️⃣ Make sure `pyproject.toml` matches this layout

At the root (same level as the `my_project/` folder), your `pyproject.toml` can stay basically as we wrote it earlier, e.g.:

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "A simple example package for practicing Module 0 tooling."
requires-python = ">=3.10"
dependencies = []

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

Setuptools will now find the `my_project` package because there is a `my_project/` directory with an `__init__.py` in it.

---

### 4️⃣ Reinstall in editable mode

Any time you change the package layout, it’s safe to reinstall:

From the **project root** (where `pyproject.toml` lives), with venv activated:

```bat
pip install -e .
```

You should see something like:

```text
Successfully installed my-project-0.1.0
```

---

### 5️⃣ Try the REPL import again

Now open the Python REPL (using the venv interpreter), and run:

```python
import my_project.tools.io_tools as io
import my_project.processing.data_tools as dt

rows = [{"value": "12"}, {"value": "5"}]
print(dt.filter_rows(rows))
```

You should get:

```text
[{'value': '12'}]
```

If that works, everything is wired correctly:

* venv ✅
* editable install ✅
* `my_project` is a proper package ✅
* imports behave like a real, modern Python library ✅

---

### 6️⃣ Quick sanity check from anywhere

One cool outcome of this: **from any script in that venv**, you can now do:

```python
from my_project.tools.io_tools import read_csv
from my_project.processing.data_tools import filter_rows
```

This is exactly how you’d use your own package in:

* an AI agent’s tool module
* a FastAPI endpoint
* a batch processing pipeline
* a notebook that imports your reusable logic

---

If you’d like, your next mini-exercise could be:

> Add a second small function (e.g., `summarize_rows`) to `processing/data_tools.py`, then use it from the REPL via `my_project.processing.data_tools`.

You’re very close to having “production-style” Python structure – this is exactly the level of rigor that maps nicely onto **AI for data science** work.

Great question — and congrats on getting the package to import successfully!
This is the *exact* kind of detail that shows you’re progressing from “writing Python scripts” to **building Python packages**.

Let’s clear this up cleanly:

---

### Question: Where should the `my_project.egg-info` folder live?

**Correct location:**
👉 It should be at the **same level as your `pyproject.toml`**, *not* inside your `my_project/` package.

In other words:

```
exercise_2/
    pyproject.toml
    my_project.egg-info/   ← ✔️ correct
    my_project/
        __init__.py
        main.py
        tools/
            __init__.py
            io_tools.py
        processing/
            __init__.py
            data_tools.py
```

---

### ❌ **Incorrect location**

It should **not** go inside your Python package folder:

```
my_project/
    my_project.egg-info/  ← ❌ wrong
```

Why?

* The `my_project/` folder is **your actual importable package.**
* The `my_project.egg-info/` folder is **metadata generated by pip during installation.**

They serve completely different roles and should not be mixed.

---

### 🧠 **What is the egg-info folder anyway?**

When you run:

```bash
pip install -e .
```

Setuptools generates the `.egg-info` directory, which contains:

* package metadata (`PKG-INFO`)
* dependency declarations
* version info
* file lists
* install location references
* entry points (if any)

It is part of Python’s packaging machinery.

**Editable mode (`-e`) keeps this folder in the source tree** rather than inside `site-packages`.

This is normal and expected behavior.

---

### 📦 **Why the egg-info folder belongs at the project root**

1. **Packaging tools expect it there**
   Setuptools looks for it next to `pyproject.toml` during rebuilds.

2. **Keeps your actual package clean**
   Your `my_project/` folder should contain only importable modules.

3. **Avoids namespace conflicts**
   If `egg-info` lives inside the package, you risk confusing namespace discovery.

4. **Editable installs (`pip install -e`) write metadata at the project root**
   This signals:

   > “These module files live here, treat this folder as the canonical codebase.”

---

### ⚠️ Should you commit `.egg-info` to Git?

**No. Never.**

Add this line to `.gitignore`:

```
*.egg-info/
```

This folder is:

* automatically generated
* environment-specific
* not meant for version control

---

### 🧪 Want to verify your environment is wired correctly?

In your venv, run inside Python:

```python
import my_project
print(my_project.__file__)
```

You should see something like:

```
C:\path\to\exercise_2\my_project\__init__.py
```

Then:

```python
import pkg_resources
for dist in pkg_resources.working_set:
    if dist.project_name == "my_project":
        print(dist)
```

You’ll see something like:

```
my_project 0.1.0 c:\path\to\exercise_2\my_project.egg-info
```

This confirms:

* the package is installed
* Python knows where the metadata lives
* the structure is correct

---

### 🎉 You're Doing Everything Right

You now fully understand:

* Editable installs
* Package metadata
* Correct directory hierarchy
* How to think like a package maintainer

This transitions you from “running scripts in folders” to **building modular, distributable AI/data tooling** — exactly what we’re aiming for in the project.

---
