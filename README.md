---
annotations_creators:
- crowdsourced
language:
- ja
language_creators:
- found
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: JDocQA
size_categories:
- 1K<n<10K
source_datasets:
- original
tags: []
task_categories:
- question-answering
task_ids:
- extractive-qa
- open-domain-qa
- closed-domain-qa
---

# Dataset Card for JDocQA

[![CI](https://github.com/shunk031/huggingface-datasets_JDocQA/actions/workflows/ci.yaml/badge.svg)](https://github.com/shunk031/huggingface-datasets_JDocQA/actions/workflows/ci.yaml)
[![Sync HF](https://github.com/shunk031/huggingface-datasets_JDocQA/actions/workflows/push_to_hub.yaml/badge.svg)](https://github.com/shunk031/huggingface-datasets_JDocQA/actions/workflows/push_to_hub.yaml)

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/mizuumi/JDocQA
- **Repository:** https://github.com/shunk031/huggingface-datasets_JDocQA
- **Paper (Preprint):** https://arxiv.org/abs/2403.19454

### Dataset Summary

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> Japanese Document Question Answering (JDocQA), a large-scale document-based QA dataset, essentially requiring both visual and textual information to answer questions, which comprises 5,504 documents in PDF format and annotated 11,600 question-and-answer instances in Japanese.

### Supported Tasks and Leaderboards

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> We consider generative question answering where a model generates a textual answer following the document context and textual question. For realistic applications of a wide range of user questions for documents, we prepare four categories of questions: **(1) yes/no**, **(2) factoid**, **(3) numerical**, and **(4) open-ended**. 
> 
> - In **yes/no questions**, answers are “yes” or “no.” 
> - In **factoid questions**, answers are some facts, such as named entities, that typically appear in the given documents. 
> - In **numerical questions**, answers are numeric values, often including some numerals (some units, e.g., km or Japanese numerals such as “8個 (objects)” and “8人 (persons)”). These numeric values are written in the documents or are calculated from other numbers in the documents. 
> - In **open-ended questions**, free-form responses are required. For such questions, we aim to assess complex comprehension abilities, such as the ability to form opinions or brief explanations based on the provided contexts and questions. 
> 
> Figure 1 presents samples of these four categories of questions. All examples include diverse images and question types related to some Japanese documents collected. We also include unanswerable questions for each question category.

### Languages

The language data in JDocQA is in Japanese ([BCP-47 ja-JP](https://www.rfc-editor.org/info/bcp47)).

## Dataset Structure

### Data Instances

```python
import datasets as ds

dataset = ds.load_dataset(path=dataset_path, trust_remote_code=True)

print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: ['answer', 'answer_type', 'context', 'multiple_select_answer', 'multiple_select_question', 'no_reason', 'normalized_answer', 'original_answer', 'original_context', 'original_question', 'pdf_category', 'pdf_name', 'question', 'question_number', 'question_page_number', 'reason_of_answer_bbox', 'text_from_ocr_pdf', 'text_from_pdf', 'type_of_image', 'pdf_filepath'],
#         num_rows: 9290
#     })
#     validation: Dataset({
#         features: ['answer', 'answer_type', 'context', 'multiple_select_answer', 'multiple_select_question', 'no_reason', 'normalized_answer', 'original_answer', 'original_context', 'original_question', 'pdf_category', 'pdf_name', 'question', 'question_number', 'question_page_number', 'reason_of_answer_bbox', 'text_from_ocr_pdf', 'text_from_pdf', 'type_of_image', 'pdf_filepath'],
#         num_rows: 1134
#     })
#     test: Dataset({
#         features: ['answer', 'answer_type', 'context', 'multiple_select_answer', 'multiple_select_question', 'no_reason', 'normalized_answer', 'original_answer', 'original_context', 'original_question', 'pdf_category', 'pdf_name', 'question', 'question_number', 'question_page_number', 'reason_of_answer_bbox', 'text_from_ocr_pdf', 'text_from_pdf', 'type_of_image', 'pdf_filepath'],
#         num_rows: 1176
#     })
# })
```

An example of the JDocQA dataset (training set) looks as follows:

```json
{
    "answer": "本文中に記載がありません",
    "answer_type": "4",
    "context": "_II.調査内容(2.虹本マニュアルの策定)(3)基本マニュアルの記載項目前述の方針等を踏まえ、基本マニュアルの具体的な記載項目(目次だて)は以下のとおりとする。小項目・内容Iはじめにマニュアルの目的、立会義務_(消防法第13条第3項)安全対策の基 本事項(SS立会い者とローリー乗務員による相互確認・相互協力の重要性)ローリー荷卸しの手順の基本的流れ ※詳細版のみIIローリー荷邊し時の作業内容1ローリー到着時(荷爺し前)1.ローリー停車位置の確認:計導2.納品書の相互確認3.アースの接続4.消火器の配置5.積荷 の相互確認6.地下タンク和在庫及び和荷卸し数量の確認7・詳細版には、各項目ごとに、_-SS立会い者、ローリー乗務2荷邊し時(ホースの結合)03-.注油口の確認、ホースの結合を記載3.ベーパー回収ホース接続ee4荷卸し作業中の安全馬視特に重要な基本事3荷卸し終了時1. 配管内、ホース内の残油の確認2.注油口の確認ハッチ内残油確認3.在庫確認4.5.後片付け6.ローリーの退出自事故・災害時の対処(初動対応)1コンタミ(混油)事故発見時(緊急処置)、連絡2オーバーフロー(漏油)事故発見時(緊急処置)、連絡3火災発見時(緊急処置)、初期消火IV通報・緊急連絡緊急時連絡先、通報内容参考チェックリスト例",
    "multiple_select_answer": "D",
    "multiple_select_question": "(A)はい、(B)いいえ、(C)わからない、(D)本文中に記載が見つけられませんでした",
    "no_reason": "0",
    "normalized_answer": "本文中に記載がありません",
    "original_answer": "本文中に記載が見つけられませんでした",
    "original_context": "_II.調査内容(2.虹本マニュアルの策定)(3)基本マニュアルの記載項目前述の方針等を踏まえ、基本マニュアルの具体的な記載項目(目次だて)は以下のとおりとする。小項目・内容Iはじめにマニュアルの目的、立会義務_(消防法第13条第3項)安全対策の基本事項(SS立会い者とローリー乗務員による相互確認・相互協力の重要性)ローリー荷卸しの手順の基本的流れ ※詳細版のみIIローリー荷邊し時の作業内容1ローリー到着時(荷爺し前)1.ローリー停車位置の確認:計導2.納品書の相互確認3.アースの接続4.消火器の配 置5.積荷の相互確認6.地下タンク和在庫及び和荷卸し数量の確認7・詳細版には、各項目ごとに、_-SS立会い者、ローリー乗務2荷邊し時(ホースの結合)03-.注油口の確認、ホースの結合を記載3.ベーパー回収ホース接続ee4荷卸し作業中の安全馬視特に重要な基本事3荷卸し 終了時1.配管内、ホース内の残油の確認2.注油口の確認ハッチ内残油確認3.在庫確認4.5.後片付け6.ローリーの退出自事故・災害時の対処(初動対応)1コンタミ(混油)事故発見時(緊急処置)、連絡2オーバーフロー(漏油)事故発見時(緊急処置)、連絡3火災発見時(緊急処置)、初期消火IV通報・緊急連絡緊急時連絡先、通報内容参考チェックリスト例",
    "original_question": "基本マニュアルの具体的な記載項目としている事故・災害時の対処の中で、オーバーフロー（漏油）事故が起こった場合は発見時にどのような処置が求められますか？",
    "pdf_category": "Slide",
    "pdf_name": "public_document00152.pdf",
    "question": "基本マニュアルの具体的な記載項目としている事故・災害時の対処の中で、オーバーフロー（漏油）事故が起こった場合は発見時にどのような処置が求められますか？\n解答は自由に記述してください。",
    "question_number": "4-656-1-4",
    "question_page_number": "9",
    "reason_of_answer_bbox": "",
    "text_from_ocr_pdf": "_II.調査内容(2.虹本マニュアルの策定)(3)基本マニュアルの記載項目前述の方針等を踏まえ、基本マニュアルの具体的な記載項目(目次だて)は以下のとおりとする。小項目・内容Iはじめにマニュアルの目的、立会義務_(消防法第13条第3項)安 全対策の基本事項(SS立会い者とローリー乗務員による相互確認・相互協力の重要性)ローリー荷卸しの手順の基本的流れ ※詳細版のみIIローリー荷邊し時の作業内容1ローリー到着時(荷爺し前)1.ローリー停車位置の確認:計導2.納品書の相互確認3.アースの接続4.消火器の 配置5.積荷の相互確認6.地下タンク和在庫及び和荷卸し数量の確認7・詳細版には、各項目ごとに、_-SS立会い者、ローリー乗務2荷邊し時(ホースの結合)03-.注油口の確認、ホースの結合を記載3.ベーパー回収ホース接続ee4荷卸し作業中の安全馬視特に重要な基本事3荷卸 し終了時1.配管内、ホース内の残油の確認2.注油口の確認ハッチ内残油確認3.在庫確認4.5.後片付け6.ローリーの退出自事故・災害時の対処(初動対応)1コンタミ(混油)事故発見時(緊急処置)、連絡2オーバーフロー(漏油)事故発見時(緊急処置)、連絡3火災発見時(緊急処置)、初期消火IV通報・緊急連絡緊急時連絡先、通報内容参考チェックリスト例",
    "text_from_pdf": "",
    "type_of_image": "",
    "pdf_filepath": "/home/shunk031/.cache/huggingface/datasets/downloads/extracted/f3481b9f65c75efec1e5398f76bd8347e64661573961b69423568699f1d7083a/pdf_files/public_document00152.pdf"
}
```

### Data Fields

[More Information Needed]

<!-- List and describe the fields present in the dataset. Mention their data type, and whether they are used as input or output in any of the tasks the dataset currently supports. If the data has span indices, describe their attributes, such as whether they are at the character level or word level, whether they are contiguous or not, etc. If the datasets contains example IDs, state whether they have an inherent meaning, such as a mapping to other datasets or pointing to relationships between data points.

- `example_field`: description of `example_field`

Note that the descriptions can be initialized with the **Show Markdown Data Fields** output of the [Datasets Tagging app](https://huggingface.co/spaces/huggingface/datasets-tagging), you will then only need to refine the generated descriptions. -->

### Data Splits

[More Information Needed]

<!-- Describe and name the splits in the dataset if there are more than one.

Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g. if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here.

Provide the sizes of each split. As appropriate, provide any descriptive statistics for the features, such as average length.  For example:

|                         | train | validation | test |
|-------------------------|------:|-----------:|-----:|
| Input Sentences         |       |            |      |
| Average Sentence Length |       |            |      | -->

## Dataset Creation

### Curation Rationale

[More Information Needed]

<!-- What need motivated the creation of this dataset? What are some of the reasons underlying the major choices involved in putting it together? -->

### Source Data

[More Information Needed]

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences,...) -->

#### Initial Data Collection and Normalization

[More Information Needed]

<!-- Describe the data collection process. Describe any criteria for data selection or filtering. List any key words or search terms used. If possible, include runtime information for the collection process.

If data was collected from other pre-existing datasets, link to source here and to their [Hugging Face version](https://huggingface.co/datasets/dataset_name).

If the data was modified or normalized after being collected (e.g. if the data is word-tokenized), describe the process and the tools used. -->

#### Who are the source language producers?

[More Information Needed]

<!-- State whether the data was produced by humans or machine generated. Describe the people or systems who originally created the data.

If available, include self-reported demographic or identity information for the source data creators, but avoid inferring this information. Instead state that this information is unknown. See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender.

Describe the conditions under which the data was created (for example, if the producers were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.

Describe other people represented or mentioned in the data. Where possible, link to references for the information. -->

### Annotations

[More Information Needed]

<!-- If the dataset contains annotations which are not part of the initial data collection, describe them in the following paragraphs. -->

#### Annotation process

[More Information Needed]

<!-- If applicable, describe the annotation process and any tools used, or state otherwise. Describe the amount of data annotated, if not all. Describe or reference annotation guidelines provided to the annotators. If available, provide interannotator statistics. Describe any annotation validation processes. -->

#### Who are the annotators?

[More Information Needed]

<!-- If annotations were collected for the source data (such as class labels or syntactic parses), state whether the annotations were produced by humans or machine generated.

Describe the people or systems who originally created the annotations and their selection criteria if applicable.

If available, include self-reported demographic or identity information for the annotators, but avoid inferring this information. Instead state that this information is unknown. See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender.

Describe the conditions under which the data was annotated (for example, if the annotators were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here. -->

### Personal and Sensitive Information

[More Information Needed]

<!-- State whether the dataset uses identity categories and, if so, how the information is used. Describe where this information comes from (i.e. self-reporting, collecting from profiles, inferring, etc.). See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender. State whether the data is linked to individuals and whether those individuals can be identified in the dataset, either directly or indirectly (i.e., in combination with other data).

State whether the dataset contains other data that might be considered sensitive (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history).  

If efforts were made to anonymize the data, describe the anonymization process. -->

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

<!-- Please discuss some of the ways you believe the use of this dataset will impact society.

The statement should include both positive outlooks, such as outlining how technologies developed through its use may improve people's lives, and discuss the accompanying risks. These risks may range from making important decisions more opaque to people who are affected by the technology, to reinforcing existing harmful biases (whose specifics should be discussed in the next section), among other considerations.

Also describe in this section if the proposed dataset contains a low-resource or under-represented language. If this is the case or if this task has any impact on underserved communities, please elaborate here. -->

### Discussion of Biases

[More Information Needed]

<!-- Provide descriptions of specific biases that are likely to be reflected in the data, and state whether any steps were taken to reduce their impact.

For Wikipedia text, see for example [Dinan et al 2020 on biases in Wikipedia (esp. Table 1)](https://arxiv.org/abs/2005.00614), or [Blodgett et al 2020](https://www.aclweb.org/anthology/2020.acl-main.485/) for a more general discussion of the topic.

If analyses have been run quantifying these biases, please add brief summaries and links to the studies here. -->

### Other Known Limitations

[More Information Needed]

<!-- If studies of the datasets have outlined other limitations of the dataset, such as annotation artifacts, please outline and cite them here. -->

## Additional Information

### Dataset Curators

[More Information Needed]

<!-- List the people involved in collecting the dataset and their affiliation(s). If funding information is known, include it here. -->

### Licensing Information

[More Information Needed]

<!-- Provide the license and link to the license webpage if available. -->

### Citation Information

<!-- Provide the [BibTex](http://www.bibtex.org/)-formatted reference for the dataset. For example:
```
@article{article_id,
  author    = {Author List},
  title     = {Dataset Paper Title},
  journal   = {Publication Venue},
  year      = {2525}
}
```

If the dataset has a [DOI](https://www.doi.org/), please provide it here. -->

```bibtex
TODO: Add BibTeX citation here
```

### Contributions

<!-- TODO: Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset. -->
