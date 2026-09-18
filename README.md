# JinoSoft Blog

한국어 개인 기술 블로그. Hugo 0.165.0 Extended와 Blowfish 테마를 사용합니다.

- 사이트: https://blog.jinosoft.com/
- 소스: https://github.com/jinosoft/jinosoft-blog
- 배포: `main` 브랜치에 push하면 GitHub Actions에서 빌드 후 GitHub Pages로 배포

## 프로젝트 구조

```text
archetypes/default.md         새 글의 기본 템플릿
config/_default/              Hugo 및 Blowfish 설정
content/posts/<slug>/         글별 디렉터리
  index.md                   글 본문과 메타데이터
  screenshot-01.png          해당 글에서 사용하는 이미지
static/CNAME                 GitHub Pages용 커스텀 도메인
themes/blowfish/             테마 Git 서브모듈
.github/workflows/pages.yml   빌드 및 배포 워크플로
public/                      빌드 결과물 (Git 제외)
```

## 로컬 환경 준비

Git과 Hugo **0.165.0 Extended**를 준비합니다. 설치한 Hugo는 `hugo version`으로 확인하며, 출력에 `+extended`가 포함되어야 합니다.

새 환경에서는 테마 서브모듈까지 함께 가져옵니다.

```bash
git clone --recurse-submodules https://github.com/jinosoft/jinosoft-blog.git
cd jinosoft-blog
```

이미 clone한 프로젝트에 테마가 없다면 프로젝트 루트에서 실행합니다.

```bash
git submodule update --init --recursive
```

이하 명령은 프로젝트 루트에서 실행합니다. Hugo 버전을 변경할 때는 배포 워크플로의 `HUGO_VERSION`도 함께 맞춥니다.

## 새 글 작성

글 하나당 디렉터리 하나를 만들고 본문은 `index.md`로 관리합니다.

```bash
hugo new content posts/wsl-hugo-install/index.md
```

`content/posts/wsl-hugo-install/index.md`가 생성됩니다. 디렉터리명과 slug는 영문 소문자와 하이픈으로 작성합니다. 템플릿은 이름을 그대로 사용하므로 이름 규칙을 자동 검사하거나 교정하지는 않습니다.

생성된 파일 상단의 TOML 메타데이터를 다음과 같이 채웁니다. 날짜는 생성 시점의 값이 자동으로 들어갑니다.

```toml
+++
date = '2026-09-16T10:00:00+09:00'
draft = true
slug = 'wsl-hugo-install'
title = 'WSL에서 Hugo 설치하기'
description = 'WSL에서 Hugo Extended와 Blowfish 테마를 설치하고 로컬 블로그를 실행한 과정.'
tags = ['wsl', 'hugo', 'blowfish']
categories = ['IT개발']
+++
```

| 항목 | 작성 기준 |
| --- | --- |
| `date` | 글 날짜. 미래 날짜의 글은 해당 시각 이후 빌드부터 발행 가능 |
| `draft` | 작성 중에는 `true`, 발행할 때는 `false` |
| `slug` | URL에 사용할 고정 이름. 발행 후에는 유지 |
| `title` | 화면에 표시할 글 제목. 한국어 사용 가능 |
| `description` | 글 내용을 요약하는 짧은 설명 |
| `tags` | 세부 주제. 없으면 `[]` 유지 |
| `categories` | 큰 분류. 없으면 `[]` 유지 |

닫는 `+++` 아래에 Markdown으로 본문을 작성합니다. 템플릿 변경은 이후 생성하는 글에 적용되며 기존 글은 자동으로 바뀌지 않습니다.

본문 구조는 글의 목적에 맞게 선택합니다. 아래 예시는 강제 규칙이 아니라 글을 완결시키기 위한 출발점입니다.

문제 해결형 글:

```markdown
## 문제 상황

무엇을 하려 했고 어디서 막혔는지 적습니다.

## 환경

- OS:
- 도구/버전:
- 작업 위치:

## 해결 과정

실행한 명령, 설정 변경, 판단 이유를 순서대로 정리합니다.

## 확인

정상 동작을 어떻게 확인했는지 적습니다.

## 마무리

다시 볼 때 필요한 주의점이나 다음 작업을 정리합니다.
```

기술 가이드형 글:

```markdown
## 대상 독자

이 글이 필요한 사람과 전제 지식을 적습니다.

## 목표

따라 하면 무엇이 완성되는지 적습니다.

## 준비물

필요한 계정, 도구, 버전, 권한을 적습니다.

## 단계별 진행

설치, 설정, 실행, 확인을 순서대로 정리합니다.

## 자주 막히는 부분

실수하기 쉬운 지점과 해결 방법을 적습니다.

## 다음 단계

관련해서 이어서 할 수 있는 작업을 적습니다.
```

구성 방법 정리형 글:

```markdown
## 구성 목표

왜 이 구성이 필요한지 적습니다.

## 최종 구조

디렉터리, 설정 파일, 서비스 흐름을 먼저 보여줍니다.

## 주요 설정

핵심 설정값과 선택 이유를 정리합니다.

## 적용 방법

실제 변경 순서를 적습니다.

## 확인 방법

정상 적용 여부를 확인하는 명령이나 화면을 적습니다.

## 운영 메모

나중에 유지보수할 때 주의할 점을 적습니다.
```

소개/회고형 글:

```markdown
## 배경

왜 이 주제를 쓰게 되었는지 적습니다.

## 핵심 내용

전달하려는 내용을 2-4개 정도로 나눠 정리합니다.

## 느낀 점

직접 해보며 배운 점이나 판단을 적습니다.

## 앞으로

다음에 해볼 일이나 이어질 글을 적습니다.
```

어떤 형태를 쓰더라도 검색으로 들어온 사람이 글 하나만 읽고 맥락, 방법, 확인 포인트를 이해할 수 있게 작성합니다.

### 이미지 추가

캡처 이미지는 글의 `index.md`와 같은 디렉터리에 저장합니다.

```text
content/posts/wsl-hugo-install/
  index.md
  screenshot-01.png
  screenshot-02.png
```

본문에서는 이미지 파일명을 상대 경로로 참조합니다.

```markdown
![Hugo 설치 후 버전을 확인한 화면](screenshot-01.png)
```

이미지 추가 전에는 민감정보를 확인합니다. 주소창의 토큰, API 키, 이메일, 계정 ID, 개인 경로, 결제 정보가 보이면 가리거나 해당 이미지를 사용하지 않습니다. 캡처만으로 설명을 끝내지 말고, 이미지 주변에 충분한 텍스트 설명과 명령어를 함께 남깁니다.

## 애드센스 준비 기준

Google AdSense 심사를 나중에 요청할 수 있도록, 글을 작성할 때마다 다음 기준을 확인합니다.

| 항목 | 기준 |
| --- | --- |
| 원본성 | 공식 문서나 다른 글을 단순 요약하지 않고 실제 환경, 판단, 시행착오를 포함 |
| 충분한 텍스트 | 이미지 중심 글이 되지 않도록 배경, 과정, 확인 방법을 텍스트로 설명 |
| 완결성 | 글 하나만 읽어도 문제 상황과 해결 방법을 이해할 수 있게 작성 |
| 내비게이션 | 관련 글이 생기면 본문 안에서 내부 링크로 연결 |
| 안전성 | 불법 우회, 저작권 침해, 크랙, 위험 행위, 성인/도박 등 광고 정책에 민감한 주제 회피 |
| 신뢰 정보 | 소개, 문의, 개인정보처리방침 페이지를 사이트에서 쉽게 찾을 수 있게 유지 |
| 발행 확인 | 발행 후 실제 URL, 이미지, 모바일 표시, 깨진 링크를 확인 |

글을 20개 정도 쌓은 뒤 심사를 요청하기 전에 다음 작업을 추가로 진행합니다.

1. 개인정보처리방침 페이지를 작성하고 푸터 또는 상단 메뉴에서 접근 가능하게 합니다.
2. 문의 페이지 또는 소개 페이지에 연락 가능한 이메일을 명시합니다.
3. Google Analytics를 설치할지 결정합니다.
4. AdSense에서 사이트를 추가하고 안내받은 코드를 `<head>`에 삽입합니다.
5. 광고가 메뉴, 다운로드 링크, 버튼, 본문 이미지와 혼동되지 않도록 배치합니다.
6. `hugo --minify`와 실제 배포 URL에서 전체 페이지를 다시 확인합니다.

## 미리보기와 빌드

초안을 포함해 미리보기 서버를 실행합니다.

```bash
hugo server -D
```

기본 주소는 http://localhost:1313/ 입니다. 포트가 사용 중이면 `hugo server -D --port 1314`로 실행하고 http://localhost:1314/ 에 접속합니다. 종료는 `Ctrl+C`입니다.

실제 배포와 동일하게 초안을 제외하고 빌드하려면 다음 명령을 실행합니다.

```bash
hugo --minify
```

결과물은 `public/`에 생성되며 Git에 커밋하지 않습니다. 미래 날짜의 글은 `-D`만으로 미리보기에 포함되지 않으므로 필요할 때 `hugo server -D -F`를 사용합니다.

## 발행과 배포

1. 글의 `draft`를 `false`로 바꾸고 `date`가 미래 시각이 아닌지 확인합니다.
2. 로컬 미리보기에서 본문, 이미지, 링크를 확인합니다.
3. `hugo --minify`로 빌드가 성공하는지 확인합니다.
4. 글과 이미지를 함께 커밋하고 `main`에 push합니다.

```bash
git add content/posts/wsl-hugo-install/
git commit -m "Add WSL Hugo installation post"
git push origin main
```

예시 경로는 실제 글의 디렉터리명으로 바꿉니다. 설정 등 다른 변경 파일도 배포에 필요하면 해당 파일을 함께 커밋합니다.

저장소의 **Actions → Deploy Hugo site to Pages**에서 `build`와 `deploy`가 모두 성공했는지 확인한 뒤 사이트에 접속합니다. 미래 날짜를 지정해도 예약 배포가 자동으로 실행되지는 않습니다. 발행 시각 이후 push하거나 Actions에서 워크플로를 수동 실행해야 합니다.

새 저장소에 배포할 때는 **Settings → Pages**의 Source를 **GitHub Actions**로 설정합니다. 현재 커스텀 도메인은 `blog.jinosoft.com`이고, DNS의 `blog` CNAME 대상은 `jinosoft.github.io`입니다.

## URL 유지와 서버 이전

현재 URL 규칙은 `config/_default/hugo.toml`에 정의되어 있습니다.

```toml
baseURL = "https://blog.jinosoft.com/"

[permalinks]
  posts = "/posts/:slug/"
```

예시 글의 URL은 `https://blog.jinosoft.com/posts/wsl-hugo-install/`입니다. 발행 후 제목을 바꾸더라도 `slug`는 유지합니다. 기존 slug를 꼭 변경해야 한다면 이전 경로를 새 주소로 연결하는 리디렉션도 준비합니다.

자체 서버로 이전할 때는 같은 도메인, `baseURL`, permalink 규칙, 각 글의 slug를 유지하고 DNS의 대상만 새 서버에 맞게 변경합니다. 새 서버에서 HTTPS를 설정하고 `hugo --minify`로 생성한 `public/`을 문서 루트로 제공하면 됩니다. `/posts/<slug>/` 요청이 해당 디렉터리의 `index.html`을 제공하도록 웹 서버를 설정합니다.

`static/CNAME`은 GitHub Pages용 파일이며 자체 서버의 도메인이나 HTTPS를 설정해 주지는 않습니다.
