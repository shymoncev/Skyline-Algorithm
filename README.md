# skyline algorithm
skyline 알고리즘을 구현합니다. 

## ⚙️Environment
디펜던시는 *pyproject.toml* 파일에서 관리합니다. package manager는 `poetry`입니다.

```
python = "^3.11"
numpy = "^2.0.1"
pandas = "^2.2.2"
matplotlib = "^3.9.1"
plotly = "^5.23.0"
```

### poetry
poetry를 사용하는 경우 *pyproject.toml* 파일이 위치한 경로에서 `poetry install` 명령어를 통해 모든 의존성을 해결할 수 있습니다. `poetry shell` 명령어로 가상 환경을 activate합니다.

### pip
poetry를 사용하지 않는다면 *requirements.txt* 파일이 위치한 경로에서 `pip install -r requirements.txt` 명령어를 사용해 의존성을 해결합니다. 가상환경을 구성한 후 의존성을 설치하는 걸 권장합니다.

## 🗂️디렉터리 구조
```
skyline_algorithm
 ┣ divided_and_conquer
 ┃ ┣ src
 ┃ ┃ ┣ data
 ┃ ┃ ┃ ┗ point.py ... point data를 관리하는 class입니다.
 ┃ ┃ ┣ skyline ... skyline algorithm을 관리합니다.
 ┃ ┃ ┃ ┗ divide_and_conquer.py ... D&C
 ┃ ┃ ┗ utils ... skyline에 필요한 모듈을 관리합니다.
 ┃ ┃ ┃ ┣ dnc_utils.py ... D&C 계산에 필요한 모듈입니다.
 ┃ ┃ ┃ ┗ utils.py ... 모든 skyline algorithm에 공통적으로 쓰이는 모듈입니다.
 ┗ ┗ main.py ... D&C를 실행하고 결과를 확인합니다.
```