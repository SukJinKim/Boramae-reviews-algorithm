<p align="center">
  <a href="https://github.com/SukJinKim/Boramae-reviews-algorithm/tree/main"> 
    <img src="/img/Boramae-reviews-algorithm-logo.webp" width="256" height="256"/>
  </a>
</p>  


## 1. Introduction


`:eagle: Boramae-reviews-algorithm (이하 B.R.A)`은 LLM을 이용하여 코테용 코드를 리뷰하는 bot입니다.  
B.R.A는 정답 코드에 대해 가독성과 성능 면에서 최적화된 코드를 제안할 뿐만 아니라, 오답 코드에 대해서도 정답 코드로 수정할 수 있는 개선 방안을 제시합니다.  
만약 당신이 아래 각 호에 하나라도 해당하면, 저희가 만든 bot이 분명 도움이 될 것이라 확신합니다.

- 취업 준비 등으로 코테를 준비하고 있다.
- 코테를 대비하여 푼 코드들을 단순히 Github에 push만 하고 있다.
- '분명 내가 제출한 코드가 맞았는데 왜 틀렸지?'라고 생각해서 다른 사람의 블로그를 참고했으나, 설명이 이해되지 않아 아쉬웠던 경험이 있다.
- 코테에서 가능하다면 가독성이 좋은 코드를 작성하고 싶다.  

<br/>

## 2. Supported Environments


현재 B.R.A. 지원하고 있는 알고리즘 문제 플랫폼, 프로그래밍 언어 그리고 LLM API 제공업체는 다음과 같습니다.

1. 알고리즘 문제 플랫폼 : `프로그래머스`, `알고스팟`
> [!WARNING]
> `BOJ`의 경우 플랫폼 정책상 문제를 가져올 수 없어 지원이 불가능합니다.
2. 프로그래밍 언어 : `C`, `C++`, `Java`, `Python`
3. LLM API 제공업체 : `OpenAI`, `Anthropic`

 <br/> 

## 3. How to use


1. Github secret 설정<br/> 
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

<br/>

2. workflow 생성<br/>
   B.R.A. bot을 실행하고 싶은 repo에 `.github/workflows/code_review.yml`을 아래와 같이 생성합니다.  
   이때 사용자는 원하는대로 LLM API 기업명`(model_company)`와 few-shot learning 적용여부`(few_shot_learning)`을 customize할 수 있습니다.


   최적의 설정값에 대한 실험 결과 `model_company : "ANTHROPIC"`, `few_shot_learning: "true"`로 설정하는 것이 가장 성능이 우수했습니다.
   자세한 내용은 [실험 보고서](https://magnificent-climb-bc3.notion.site/Boramae-reviews-algorithm-9bc1db970a9b4043a7919bae47e4a017?pvs=4)를 참고하시길 바랍니다.

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

<br/>

3. Create/Update PR
   ```mermaid
    flowchart LR;
    U[User] -- 1. Create/Update PR --> G[(Github repo)] -- 2. Trigger --> B([B.R.A]);
    B -- 3. Review --> G;
   ```
   B.R.A는 사용자가 Github repo에 PR을 create하거나 update하면 자동으로 동작하여 리뷰를 남깁니다.  
   이때 반드시 아래 두 가지 조건을 만족해야 합니다.  

   1) 하나의 commit에는 반드시 하나의 제출 코드만 있어야 한다.
   2) commit message에는 반드시 알고리즘 문제 URL이 포함되어야 한다.  
      
   -  참고 : SukJinKim/Boramae-reviews-algorithm-demo#3

<br/>  

## 4. Shout out to NAVER D2 :green_heart:

[![NAVER D2 유튜브 영상](http://img.youtube.com/vi/7cwFhX14nkg/0.jpg)](https://youtu.be/7cwFhX14nkg?t=0s)  

B.R.A 프로젝트는 NAVER D2의 `시간은 금이다 : LLM을 이용한 AI 코드 리뷰 도입기`로부터 영감을 받았습니다!
