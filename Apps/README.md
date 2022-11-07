# How to Run Streamlit Apps from a Github URL

Prep:
1. Install VSCode, allow adding to Path.  https://code.visualstudio.com/download
2. Install latest version of python.  https://www.python.org/downloads/release/python-3110/

Success:
Check your python version:
C:\Users\temporary>python --version
Python 3.11.0

Add Streamlit, or bring it to latest version:
C:\Users\temporary>pip install --upgrade streamlit

Common issue: pyarrow fails to install.  If this happens, upgrade pip:
python.exe -m pip install --upgrade pip
Reinstall pyarrow:
pip install --upgrade pyarrow
Upgrade CMAKE?  VS 2017 fails.  https://cmake.org/download/
Upgrade VS redistrib: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
Try old VS2017: https://aka.ms/vs/15/release/VC_redist.x64.exe

Syntax:
1. Open a prompt with start run cmd if on windows
2. Then launch streamlit run [URLtoApp.py]

## Pygraph App:
streamlit run https://github.com/AaronCWacker/Yggdrasil/Apps/Pygraph_app.py

