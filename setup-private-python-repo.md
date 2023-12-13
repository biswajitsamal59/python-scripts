Upgrade pip:
python -m pip install --upgrade pip

Create a Virtual Env:
python -m venv C:\Users\test\OneDrive\Desktop\pvenv
cd OneDrive\Desktop\pvenv
Scripts\activate.bat

Create Pip Configuration File(pip.ini) with below content and place it inside Virtual Env(C:\Users\test\OneDrive\Desktop\pvenv):
[global]
index-url=https://<user-name>:<token>@<package-repo-yrl>

Intsall Package:
pip install requests

Deactivate Virtual Env:
Scripts\deactivate.bat
