# Jino Blog

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
categories = ['개발환경']
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
