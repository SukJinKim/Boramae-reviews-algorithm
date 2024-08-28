# 🦅 Boramae-reviews-algorithm

## Configuration
1. Boramae-reviews-algorithm bot을 실행하고 싶은 repo 홈페이지 이동
2. 상단의 `Settings` 클릭
3. `Security > Secrets and variables` 아래 `Actions` 클릭
4. Change to `Variables` tab, create `API_KEY` with the value of your api key 
(For Github Action integration, set it in secrets)
   
   <!-- TODO 캡쳐화면 넣기 -->


## Usages
1. create `.github/workflows/code_review.yml` as below

```yml
name: Code Review

permissions:
  contents: read
  pull-requests: write

on:
  pull_request:
    types: [opened, synchronize]
    paths:
      - "**.c"
      - "**.cpp"
      - "**.java"
      - "**.py"

jobs:
  code-review:
    runs-on: ubuntu-latest
    steps:
      - name: check out repository
        uses: actions/checkout@v4

      - name: 🦅 Boramae reviews algorithm
        uses: SukJinKim/Boramae-reviews-algorithm@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          # "OPENAI", "ANTHROPIC" 둘 중 하나 선택
          model_company: "ANTHROPIC"
          api_key: ${{ secrets.API_KEY }}
          # Few shot learning 적용을 원한다면 아래 주석 해제
          # few_shot_learning: "true"
```
   2. branch 생성하여 코테에 제출한 코드를 PR로 보내기
    (이때, 반드시 commit message에 문제 URL가 담겨 있어야 합니다.)
    - 예시 : https://github.com/SukJinKim/Boramae-reviews-algorithm-test/pull/5
<!-- TODO 캡쳐화면 넣기 -->
