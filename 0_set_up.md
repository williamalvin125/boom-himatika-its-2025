# Hands-On Prep.

## _System Requirements_  

- Python versi 3.11 (sangat direkomendasikan)  
- OS: windows atau linux  

---

## _Tools_  

- _Package Manager_: UV (direkomendasikan) / pip.
- _Text Editor_: VSCode  

---

## _Setup Environment_

### UV  

1. Install UV
```
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# cek versi
uv --version
```

2. Setup venv
```
# membuat venv
uv venv --python 3.11

# setup uv
uv init

# install dependensi
uv pip install -r requirements.txt

```

### Pip

```
# create venv
python -m venv .venv

# aktivasi venv
.venv\Scripts\activate    # windows
source venv/bin/activate  # linux

# install dependensi
uv pip install -r requirements.txt
```

if error create / activate venv, try:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```