Upgrade pip: <br />
```python -m pip install --upgrade pip``` <br />

Create a Virtual Env: <br />
```
python -m venv C:\Users\test\OneDrive\Desktop\pvenv
cd OneDrive\Desktop\pvenv
Scripts\activate.bat
```

Create Pip Configuration File(pip.ini) with below content and place it inside Virtual Env(C:\Users\test\OneDrive\Desktop\pvenv): <br />
**For Azure Devops pip feed, generate a PAT** <br />
```
[global]
index-url=https://<user-name>:<token>@<package-repo-yrl>
```

Intsall Package: <br />
```pip install requests``` <br />

Deactivate Virtual Env: <br />
```Scripts\deactivate.bat```
