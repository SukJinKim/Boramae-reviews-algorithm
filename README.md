# 🦅 Boramae-reviews-algorithm


## 1. Introduction


<p align="center">
  <img src="/img/Boramae-reviews-algorithm-logo.webp" width="256" height="256"/>
</p>  


`Boramae-reviews-algorithm (이하 B.R.A)`은 사용자가 알고리즘 문제에 대한 답으로 제출한 코드를 분석하고 이를 최적화한 코드로 변환하여 제안하는 bot입니다.


현재 지원하고 있는 알고리즘 문제 플랫폼, 프로그래밍 언어 그리고 LLM API 기업명은 다음과 같습니다.

1. 알고리즘 문제 플랫폼 : 프로그래머스, 알고스팟
  > [!NOTE]
  > BOJ의 경우 플랫폼 정책상 문제를 가져올 수 없어 지원이 불가능합니다.
2. 프로그래밍 언어 : C, C++, Java, Python
3. LLM API 기업명 : OpenAI, Anthropic


<!-- 1. Boramae-reviews-algorithm bot을 실행하고 싶은 repo 홈페이지 이동
2. 상단의 `Settings` 클릭
3. `Security > Secrets and variables` 아래 `Actions` 클릭
4. Change to `Variables` tab, create `API_KEY` with the value of your api key 
(For Github Action integration, set it in secrets)
   
   <!-- TODO 캡쳐화면 넣기 -->


<!-- ## Usages
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
TODO 캡쳐화면 넣기 --> -->
