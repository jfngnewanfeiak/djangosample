# djangosample

# git clone後にやること
'''bash
cd djangosample
'''

# 仮想環境の構築
python3 -m venv webapp_venv

# 仮想環境の読み込み
source webapp_venv/bin/activate

# 必要なライブラリのインストール
pip install -r requirements.txt

# vscode 起動 ターミナルからsource したやつで起動することでvenvのあれになる
code .