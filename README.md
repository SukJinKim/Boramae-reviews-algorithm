<p align="center">
  <a href="https://github.com/SukJinKim/Boramae-reviews-algorithm/tree/main"> 
    <img src="/img/Boramae-reviews-algorithm-logo.webp" width="256" height="256"/>
  </a>
</p>  


## 1. Introduction


`Boramae-reviews-algorithm (이하 B.R.A)`은 사용자가 알고리즘 문제에 대한 답으로 제출한 코드를 분석하고 이를 최적화한 코드로 변환하여 제안하는 bot입니다.


현재 지원하고 있는 알고리즘 문제 플랫폼, 프로그래밍 언어 그리고 LLM API 기업명은 다음과 같습니다.

1. 알고리즘 문제 플랫폼 : `프로그래머스`, `알고스팟`
> [!WARNING]
> `BOJ`의 경우 플랫폼 정책상 문제를 가져올 수 없어 지원이 불가능합니다.
2. 프로그래밍 언어 : `C`, `C++`, `Java`, `Python`
3. LLM API 기업명 : `OpenAI`, `Anthropic`


## 2. How to use

1. Configuration
   B.R.A는 보안을 위해 Github secret에 저장된 사용자 API 키를 사용합니다.  
   이를 위해 다음과 같은 절차를 따라주시길 바랍니다.  

   1) B.R.A를 실행하고 싶은 repo 홈페이지 이동
   2) 상단의 `Settings` 클릭
   3) `Security > Secrets and variables` 아래 `Actions` 클릭
   4) `New repository secret` 클릭
   5) Name은 `API_KEY`, Secret은 발급받은 API 키 값 입력한 뒤 `Add secret` 클릭

   <p align="center">
    <img src="/img/secret setting.png"/>
   </p>  


2. Usage
   1) workflow 설정
      B.R.A. bot을 실행하고 싶은 repo에 `.github/workflows/code_review.yml`을 아래와 같이 생성합니다.  
      이때 사용자는 원하는대로 LLM API 기업명`(model_company)`와 few-shot learning 적용여부`(few_shot_learning)`을 customize할 수 있습니다.  
      <!-- TODO technical report 추가 -->

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
              uses: SukJinKim/Boramae-reviews-algorithm@v1
              with:
                github_token: ${{ secrets.GITHUB_TOKEN }}
                # "OPENAI", "ANTHROPIC" 둘 중 하나 선택
                model_company: "ANTHROPIC"
                api_key: ${{ secrets.API_KEY }}
                # Few shot learning 적용을 원하지 않는다면 아래 주석 처리
                few_shot_learning: "true"
      ```

   2) Create/Update PR
      ```mermaid
        flowchart LR;
        U[User] -- 1. Create/Update PR --> G[(Github repo)] -- 2. Trigger --> B([B.R.A]);
        B -- 3. Review --> G;
      ```
      B.R.A는 사용자가 Github repo에 PR을 create하거나 update하면 자동으로 동작하여 리뷰를 남깁니다.  
      이때 반드시 아래 두 가지 조건을 만족해야 합니다.  
      1) 하나의 commit에는 반드시 하나의 제출 코드만 있어야 한다.
      2) commit message에는 반드시 알고리즘 문제 URL이 포함되어야 한다.
      예시 : 
      <!-- TODO 예시 PR 링크 넣기 -->


## 3. Shout out to NAVER D2:green_heart:

[![NAVER D2 유튜브 영상](http://img.youtube.com/vi/7cwFhX14nkg/0.jpg)](https://youtu.be/7cwFhX14nkg?t=0s)  

B.R.A 프로젝트는 NAVER D2의 `시간은 금이다 : LLM을 이용한 AI 코드 리뷰 도입기`로부터 영감을 받았습니다!