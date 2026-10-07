+++
title = '오픈소스, 상용 제품에 써도 될까? MIT·GPL·Apache 라이선스 비교'
date = '2026-09-28T00:00:00+09:00'
draft = false
slug = 'open-source-license-commercial-use'
description = '0BSD, MIT, BSD, Apache 2.0, MPL 2.0, GPL, AGPL의 배포 조건을 비교하고 소스 비공개 또는 GPL 사용 시 선택 기준을 정리한다.'
tags = ['open-source', 'license', 'mit', 'apache-2.0', 'gpl']
categories = ['IT개발']
showTableOfContents = true
+++

MIT 코드를 넣은 제품은 소스를 비공개로 배포할 수 있을까? GPL 코드를 사용한 경우에도 같을까? 두 라이선스 모두 상용 이용이 가능하지만, 배포물에 포함해야 할 고지와 소스 제공 범위는 다르다.

이 글에서 비교하는 **0BSD, MIT, BSD-3-Clause, Apache-2.0, MPL-2.0, GPL-3.0, AGPL-3.0은 모두 상용 이용과 유료 배포를 허용한다.** 무료로 배포해야 하는 라이선스도 아니다. 차이는 **배포 시 무엇을 함께 제공해야 하는가**에 있다. [Open Source Initiative FAQ](https://opensource.org/faq), [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html#DoesTheGPLAllowMoney)

아래 표로 기본 조건을 비교하고, 소스를 비공개로 유지하고 싶은 경우와 GPL 코드가 꼭 필요한 경우의 선택 기준을 살펴본다. 실제 사용 시에는 프로젝트의 라이선스 **버전**, 예외 조항, 함께 포함된 구성요소도 확인한다.

## 라이선스별 의무 비교

표의 '소스 제공'은 주로 코드를 **외부에 배포하는 경우**를 기준으로 한다. 다만 AGPL-3.0은 수정한 프로그램을 네트워크 이용자에게 제공할 때도 소스 제공 조건이 적용된다.

{{< table-scroll label="오픈소스 라이선스별 배포 조건 비교" >}}
| 라이선스 | 배포 시 고지 | 소스 제공 |
| --- | --- | --- |
| [0BSD](https://opensource.org/license/0bsd) | 라이선스 자체에 고지 유지 조건 없음 | 요구 없음 |
| [MIT](https://opensource.org/license/mit) | 저작권 표시와 허가문 포함 | 요구 없음 |
| [BSD-3-Clause](https://opensource.org/license/BSD-3-clause) | 저작권·라이선스 조건·면책 문구 유지 | 요구 없음 |
| [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.html) | 라이선스 사본 제공, 해당 시 `NOTICE` 유지·수정 사실 표시 | 요구 없음 |
| [MPL-2.0](https://www.mozilla.org/en-US/MPL/2.0/) | 라이선스와 소스 입수 방법 안내 | MPL 적용 파일의 소스 제공 |
| [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) | 라이선스·저작권 표시 등 유지 | 배포하는 GPL 적용 프로그램의 대응 소스 제공 |
| [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.en.html) | GPL과 유사한 조건 | GPL 조건에 더해 수정한 프로그램의 네트워크 이용자에게도 소스 제공 |
{{< /table-scroll >}}

여기서 **고지**는 저작권 표시나 라이선스 문구를 조건에 맞게 보존한다는 뜻이다. 반드시 제품 첫 화면에 저작권자를 표시하라는 뜻은 아니다. **소스 제공**은 배포한 바이너리에 대응하는 소스 코드를 수령자가 받을 수 있게 한다는 뜻이며, 언제나 인터넷 전체에 공개 저장소를 만들어야 한다는 뜻은 아니다. [GNU GPL FAQ: 소스 공개 범위](https://www.gnu.org/licenses/gpl-faq.en.html#GPLRequireSourcePostedPublic)

## 꼭 알아둘 차이

**MIT의 고지는 단순한 출처 링크가 아니다.** 배포물에 저작권 표시와 허가문을 포함해야 한다. 0BSD에는 이 고지 유지 조건이 없다. [0BSD 원문](https://opensource.org/license/0bsd), [MIT 원문](https://opensource.org/license/mit)

**Apache-2.0은 MIT보다 확인할 항목이 많다.** 라이선스 사본을 전달하고, 원본에 `NOTICE`가 있으면 해당 고지를 유지하며, 수정한 파일에는 변경 사실을 표시해야 한다. 기여자의 특허 허여 조건도 명시한다. [Apache-2.0 원문](https://www.apache.org/licenses/LICENSE-2.0.html)

**MPL-2.0은 파일 단위, GPL-3.0은 결합된 프로그램의 범위가 중요하다.** MPL 적용 파일을 수정해 배포하면 해당 파일의 소스를 제공해야 하지만, 함께 배포하는 별개의 새 파일까지 자동으로 MPL이 되는 것은 아니다. GPL 코드를 다른 코드와 하나의 프로그램으로 결합해 배포한다면, 그 결합된 프로그램을 GPL 조건에 맞게 배포해야 한다. 단순히 GPL 프로그램과 별개의 프로그램을 함께 배포하는 경우까지 동일하게 취급하지는 않는다. [Mozilla MPL FAQ](https://www.mozilla.org/en-US/MPL/2.0/FAQ/), [GNU GPL FAQ: 프로그램 결합](https://www.gnu.org/licenses/gpl-faq.en.html#GPLPlugins)

**GPL은 내부 사용만으로 소스 제공을 요구하지 않는다.** GPL 적용 프로그램을 외부에 배포할 때 대응 소스를 제공해야 한다. 원본을 수정해 바이너리를 배포했다면 원본 프로젝트의 링크만 남겨서는 부족하고, 배포한 바이너리에 해당하는 소스가 필요하다. [GNU GPL FAQ: 내부 사용](https://www.gnu.org/licenses/gpl-faq.en.html#GPLRequireSourcePostedPublic), [GNU GPL FAQ: 대응 소스](https://www.gnu.org/licenses/gpl-faq.en.html#DistributeExtendedBinary)

**AGPL-3.0은 네트워크 사용에도 추가 조건이 있다.** 일반 GPL 프로그램을 서버에서만 실행하는 것은 보통 프로그램 사본의 배포가 아니다. 반면 수정한 AGPL 적용 프로그램을 네트워크로 제공하면, 이용자가 그 프로그램의 대응 소스를 받을 방법을 제공해야 한다. 서비스에 사용한 모든 별도 프로그램의 소스를 무조건 공개한다는 뜻은 아니다. [GNU GPL FAQ: 서버 사용](https://www.gnu.org/licenses/gpl-faq.en.html#UnreleasedMods), [GNU AGPL-3.0 원문](https://www.gnu.org/licenses/agpl-3.0.en.html)

## 상황별 선택 기준

**내 제품의 소스를 비공개로 유지하려면:** 0BSD, MIT, BSD-3-Clause, Apache-2.0 라이선스의 코드를 우선 검토한다. 이들은 해당 코드를 포함해 배포해도 제품 전체의 소스 제공을 요구하지 않는다. 0BSD는 해당 코드에 대한 고지 유지 조건도 없지만, 함께 사용하는 다른 구성요소의 고지 의무까지 없어지는 것은 아니다. MIT·BSD·Apache-2.0에는 각각 고지 의무가 있다. 특허 허여 조항이 중요하다면 Apache-2.0의 조건도 살펴볼 만하다. MPL-2.0 코드는 별도 파일의 비공개를 허용하지만, MPL 적용 파일의 소스는 제공해야 한다. [0BSD](https://opensource.org/license/0bsd), [MIT](https://opensource.org/license/mit), [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.html), [Mozilla MPL FAQ](https://www.mozilla.org/en-US/MPL/2.0/FAQ/)

**GPL 계열 코드가 꼭 필요하다면:** 먼저 정확한 라이선스 버전과 링크 예외·이중 라이선스가 있는지 확인한다. `LGPL-3.0`은 `GPL-3.0`과 다르다. LGPL 라이브러리는 조건을 지키면 비공개 프로그램과 결합해 배포할 수 있지만, 라이브러리 소스 제공과 사용자가 수정한 라이브러리로 다시 연결할 수 있게 하는 등의 요건이 남는다. [GNU LGPL-3.0 원문](https://www.gnu.org/licenses/lgpl-3.0.en.html)

예외가 없는 **GPL-3.0 적용 프로그램을 배포**해야 한다면 다음을 확인한다.

1. **범위:** GPL 코드와 다른 코드가 하나의 프로그램으로 결합되는지 확인한다. 결합된 프로그램에는 GPL 조건이 적용되지만, 별개의 독립 프로그램을 나란히 배포한다고 그 프로그램까지 GPL이 되지는 않는다. [GNU GPL-3.0 제5조 및 집합물 정의](https://www.gnu.org/licenses/gpl-3.0.en.html)
2. **고지:** GPL 라이선스 사본과 기존 저작권·면책 고지를 유지하고, 수정한 부분에는 변경 사실을 표시한다. 기존에 대화형 법적 고지가 있는 프로그램이라면 그 표시 의무도 확인한다. [GNU GPL-3.0 제4·5조](https://www.gnu.org/licenses/gpl-3.0.en.html)
3. **소스 범위:** 배포한 바이너리에 대응하는 소스를 준비한다. GPL 적용 코드의 수정본뿐 아니라 결합된 프로그램을 생성·설치·실행·수정하는 데 필요한 소스와 관련 스크립트가 포함된다. GPL이 정의한 시스템 라이브러리와 독립적인 별도 프로그램은 제외된다. [GNU GPL-3.0 대응 소스 정의](https://www.gnu.org/licenses/gpl-3.0.en.html)
4. **제공 방법:** 바이너리 수령자가 GPL 제6조에 맞는 방법으로 대응 소스를 받을 수 있게 한다. 다운로드로 바이너리를 제공한다면 대응 소스에도 같은 방식으로 추가 비용 없이 접근할 수 있게 하는 방법이 있다. 무조건 공개 GitHub 저장소를 만들어야 하는 것은 아니다. [GNU GPL-3.0 제6조](https://www.gnu.org/licenses/gpl-3.0.en.html)

이 조건을 지킬 수 없다면 GPL 코드를 비공개 제품에 그대로 결합해 배포하지 말고, 대체 구성요소나 저작권자가 제공하는 별도 상용 라이선스를 검토한다. AGPL-3.0이라면 바이너리 배포뿐 아니라 **수정한 프로그램의 네트워크 제공** 여부도 확인해야 한다. [GNU AGPL-3.0 제13조](https://www.gnu.org/licenses/agpl-3.0.en.html)

## 배포 전 확인할 것

1. 사용한 코드의 라이선스 **이름과 버전**, 별도 예외 조항을 확인한다.
2. 배포한다면 저작권·라이선스 문구, `NOTICE`, 수정 표시, 소스 제공 조건을 확인한다.
3. 라이선스가 없는 공개 저장소는 자유롭게 재사용해도 된다는 뜻이 아니다. 허가가 불분명하면 사용 전에 권리자에게 확인한다. [GitHub 라이선스 안내](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

제품 소스를 비공개로 유지하려면 고지 의무가 있는지와 별개로 **소스 제공을 요구하는 범위**부터 확인한다. GPL 코드가 꼭 필요하다면 배포할 프로그램의 대응 소스까지 준비할 수 있는지 검토한 뒤 선택한다.
