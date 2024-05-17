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
    "answer_type": 3,
    "context": "_II.調査内容(2.虹本マニュアルの策定)(3)基本マニュアルの記載項目前述の方針等を踏まえ、基本マニュアルの具体的な記載項目(目次だて)は以下のとおりとする。小項目・内容Iはじめにマニュアルの目的、立会義務_(消防法第13条第3項)安全対策の基本事項(SS立会い者とローリー乗務員による相互確認・相互協力の重要性)ローリー荷卸しの手順の基本的流れ ※詳細版のみIIローリー荷邊し時の作業内容1ローリー到着時(荷爺し前)1.ローリー停車位置の確認:計導2.納品書の相互確認3.アースの接続4.消火器の配置5.積荷の相互確認6.地下タンク和在庫及び和荷卸し数量の確認7・詳細版には、各項目ごとに、_-SS立会い者、ローリー乗務2荷邊し時(ホースの結合)03-.注油口の確認、ホースの結合を記載3.ベーパー回収ホース接続ee4荷卸し作業中の安全馬視特に重要な基本事3荷卸し終了時1.配管内、ホース内の残油の確認2.注油口の確認ハッチ内残油確認3.在庫確認4.5.後片付け6.ローリーの退出自事故・災害時の対処(初動対応)1コンタミ(混油)事故発見時(緊急処置)、連絡2オーバーフロー(漏油)事故発見時(緊急処置)、連絡3火災発見時(緊急処置)、初期消火IV通報・緊急連絡緊急時連絡先、通報内容参考チェックリスト例",
    "multiple_select_answer": 3,
    "multiple_select_question": ["はい", "いいえ", "わからない", "本文中に記載が見つけられませんでした"],
    "no_reason": 0,
    "normalized_answer": "本文中に記載がありません",
    "original_answer": "本文中に記載が見つけられませんでした",
    "original_context": "_II.調査内容(2.虹本マニュアルの策定)(3)基本マニュアルの記載項目前述の方針等を踏まえ、基本マニュアルの具体的な記載項目(目次だて)は以下のとおりとする。小項目・内容Iはじめにマニュアルの目的、立会義務_(消防法第13条第3項)安全対策の基本事項(SS立会い者とローリー乗務員による相互確認・相互協力の重要性)ローリー荷卸しの手順の基本的流れ ※詳細版のみIIローリー荷邊し時の作業内容1ローリー到着時(荷爺し前)1.ローリー停車位置の確認:計導2.納品書の相互確認3.アースの接続4.消火器の配置5.積荷の相互確認6.地下タンク和在庫及び和荷卸し数量の確認7・詳細版には、各項目ごとに、_-SS立会い者、ローリー乗務2荷邊し時(ホースの結合)03-.注油口の確認、ホースの結合を記載3.ベーパー回収ホース接続ee4荷卸し作業中の安全馬視特に重要な基本事3 荷卸し終了時1.配管内、ホース内の残油の確認2.注油口の確認ハッチ内残油確認3.在庫確認4.5.後片付け6.ローリーの退出自事故・災害時の対処(初動対応)1コンタミ(混油)事故発見時(緊急処置)、連絡2オーバーフロー(漏油)事故発見時(緊急処置)、連絡3火災発見時(緊急処置)、初期消火IV通報・緊急連絡緊急時連絡先、通報内容参考チェックリスト例",
    "original_question": "基本マニュアルの具体的な記載項目としている事故・災害時の対処の中で、オーバーフロー（漏油）事故が起こった場合は発見時にどのような処置が求められますか？",
    "pdf_category": 2,
    "pdf_name": "public_document00152.pdf",
    "question": "基本マニュアルの具体的な記載項目としている事故・災害時の対処の中で、オーバーフロー（漏油）事故が起こった場合は発見時にどのような処置が求められますか？\n解答は自由に記述してください。",
    "question_number": [4, 656, 1, 4],
    "question_page_number": "9",
    "reason_of_answer_bbox": [""],
    "text_from_ocr_pdf": "_II.調査内容(2.虹本マニュアルの策定)(3)基本マニュアルの記載項目前述の方針等を踏まえ、基本マニュアルの具体的な記載項目(目次だて)は以下のとおりとする。小項目・内容Iはじめにマニュアルの目的、立会義務_(消防法第13条第3項)安全対策の基本事項(SS立会い者とローリー乗務員による相互確認・相互協力の重要性)ローリー荷卸しの手順の基本的流れ ※詳細版のみIIローリー荷邊し時の作業内容1ローリー到着時(荷爺し前)1.ローリー停車位置の確認:計導2.納品書の相互確認3.アースの接続4.消火器の配置5.積荷の相互確認6.地下タンク和在庫及び和荷卸し数量の確認7・詳細版には、各項目ごとに、_-SS立会い者、ローリー乗務2荷邊し時(ホースの結合)03-.注油口の確認、ホースの結合を記載3.ベーパー回収ホース接続ee4荷卸し作業中の安全馬視特に重要な基本事3荷卸し終了時1.配管内、ホース内の残油の確認2.注油口の確認ハッチ内残油確認3.在庫確認4.5.後片付け6.ローリーの退出自事故・災害時の対処(初動対応)1コンタミ(混油)事故発見時(緊急処置)、連絡2オーバーフロー(漏油)事故発見時(緊急処置)、連絡3火災発見時(緊急処置)、初期消火IV通報・緊急連絡緊急時連絡先、通報内容参考チェックリスト例",
    "text_from_pdf": "",
    "type_of_image": [0],
    "pdf_filepath": "/home/shunk031/.cache/huggingface/datasets/downloads/extracted/f3481b9f65c75efec1e5398f76bd8347e64661573961b69423568699f1d7083a/pdf_files/public_document00152.pdf"
}
```

### Data Fields

From [JDocQA's README.md](https://github.com/mizuumi/JDocQA/blob/main/dataset/README.md) and [the paper](https://arxiv.org/abs/2403.19454):

- `answer`: 
- `answer_type`: (1) Yes/No questions, (2) Factoid questions, (3) Numerical questions, (4) Open-ended questions.
- `context`: Removed noises from 'original_context'.
- `multiple_select_answer`:
- `multiple_select_question`:
- `no_reason`: Unanswerable question-> 0, Answerable question-> 1
- `normalized_answer`:
- `original_answer`: Annotated answers.
- `original_context`: Extracted texts from PDF.
- `original_question`: Annotated questions.
- `pdf_category`: Document category.
- `pdf_name`: PDF name.
- `question`: Question query for models.
- `question_number`:
- `question_page_number`: Where annotators found answer of the questions.
- `reason_of_answer_bbox`:
- `text_from_ocr_pdf`:
- `text_from_pdf`:
- `type_of_image`: (1) Table, (2) Bar chart, (3) Line chart, (4) Pie chart, (5) Map, (6) Other figures, (7) Mixtured writing style from left to the right and from upside to the downside, (8) Drawings, (9) Others.
- `pdf_filepath`: full file path to the corresponding PDF file.

### Data Splits

From [JDocQA's paper](https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/C3-5.pdf):

> 学習，検定，テストセットにそれぞれ 9,290 件，1,134 件，1,176 件の質問応答が含まれるようにデータセット全体を分割した．同一 PDF ファイルは必ず同一の分割に出現する．

## Dataset Creation

### Curation Rationale

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> To address the demand for a large-scale and fully annotated Japanese document question answering dataset, we introduce a JDocQA dataset by collecting Japanese documents in PDF styles from open-access sources including multiple formats of documents: slides, reports, websites and pamphlets and manually annotating question-answer pairs on them.

### Source Data

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> We gather public documents, such as, municipality pamphlets and websites, that are created by Japanese governmental agencies or local governments. 

#### Initial Data Collection and Normalization

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> We manually collected PDF documents from open-access resources such as Japanese National Diet Library (NDL)’s digital collection, web archive projects (WARP) and websites of Japanese government ministries. We manually gathered documents such as reports, pamphlets or websites that are published by public or quasi-public sectors, such as local governments or public universities through WARP. We also gather Japanese ministry documents such as slides and reports from their websites following the government agencies’ policies. Those documents cover a wide range of topics, for instance, economic policies, education policies, labor issues, health and hygiene, agriculture, forestry, fisheries, culture and arts, history, related to governmental policy or policy guidelines, as well as the everyday affairs of local governments. These documents also include visual elements such as figures, tables, charts, pictures, or mandala charts, complex figures with a combination of texts and objects typically seen in the Japanese public administrative sector’s official document. We classify these documents into four categories, namely, pamphlet, slide, report, and website considering the form of the documents.

> We extracted texts from PDF documents with PyPDF2. We also notice that some PDF documents are probably created from paper scans, and we cannot extract embedded texts from such documents. Therefore, we extracted texts from the document page images by OCR (Optical Character Recognition) as an alternative source. After the text extraction or OCR, we removed mistakenly recognized symbols and emojis, or duplicated characters from texts when the same character continuously and repeatedly appeared more than five times.

#### Who are the source language producers?

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> JDocQA dataset comprises 5,504 files and 11,600 question-and-answer pairs in Japanese.

### Annotations

#### Annotation process

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> As documents include rich textual and visual elements (e.g., graphs, charts, maps, illustrations, and a mix of vertical and horizontal written text), we made question answer pairs that are related to both textual and visual information. We ask annotators to write up two to four question-answer annotations in each document. We also ask not to use any AI-tools such as OpenAI ChatGPT during the annotation process. Each question is accompanied with the supporting facts as marked in red in Figure 1 and Figure 3. We classify a subset of questions that have multiple supporting facts in multiple pages as multi-page questions. Multi-page questions are considerably difficult from their single-page counterparts. For unanswerable questions, we ask annotators to write questions that lack supporting facts in the documents, making them impossible to answer based on the given documents.

> We prepared three types of images for visual inputs for multimodal models. The first type of images are those of the whole page of the documents including the annotated question answering pairs. The second type of images are those cropped by bounding boxes on which annotators based their answers such as tables or figures of the pages. When multiple bounding boxes are annotated to a single question-answer pair, multiple cropped images are combined together into a single image here. The third type of images are blank (white) images that are used for ablation studies.

#### Who are the annotators?

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> We ask 43 annotators in total for the question-answering pairs annotation on documents.

### Personal and Sensitive Information

[More Information Needed]

<!-- State whether the dataset uses identity categories and, if so, how the information is used. Describe where this information comes from (i.e. self-reporting, collecting from profiles, inferring, etc.). See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender. State whether the data is linked to individuals and whether those individuals can be identified in the dataset, either directly or indirectly (i.e., in combination with other data).

State whether the dataset contains other data that might be considered sensitive (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history).  

If efforts were made to anonymize the data, describe the anonymization process. -->

## Considerations for Using the Data

### Social Impact of Dataset

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> We assume our datasets are useful for both research and development of generative language models and their applications for Japanese document question answering. 

### Discussion of Biases

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> We carefully avoid private documents and choose considerably public documents published by public or quasi-public sectors for the publicity of our dataset usage. All of the documents and webpages are publicly available online and we follow our institutional rules to gather them. We follow our institutional rules and also consult external advisors for data collection processes.

### Other Known Limitations

From [JDocQA's paper](https://arxiv.org/abs/2403.19454):

> We also consider our dataset with unanswerable questions can contribute to harnessing the hallucination problem of large language models. However, this doesn’t mean that the fintuned models with unanswerable questions do not perform hallucinations at all.

## Additional Information

### Dataset Curators

[More Information Needed]

<!-- List the people involved in collecting the dataset and their affiliation(s). If funding information is known, include it here. -->

### Licensing Information

From [JDocQA's README.md](https://github.com/mizuumi/JDocQA/blob/main/dataset/README.md):

> JDocQA dataset annotations are distributed under CC BY-SA 4.0.

### Citation Information

```bibtex
@inproceedings{JDocQA_2024,
    title = "JDocQA: Japanese Document Question Answering Dataset for Generative Language Models",
    author = "Onami, Eri  and
      Kurita, Shuhei  and
      Miyanishi, Taiki and
      Watanabe, Taro",
    booktitle = "The 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation",
    month = may,
    year = "2024",
    address = "Trino, Italy",
    abstract = "Document question answering is a task of question answering on given documents such as reports, slides, pamphlets, and websites, and it is a truly demanding task as paper and electronic forms of documents are so common in our society. This is known as a quite challenging task because it requires not only text understanding but also understanding of figures and tables, and hence visual question answering (VQA) methods are often examined in addition to textual approaches. We introduce Japanese Document Question Answering (JDocQA), a large-scale document-based QA dataset, essentially requiring both visual and textual information to answer questions, which comprises 5,504 documents in PDF format and annotated 11,600 question-and-answer instances in Japanese. Each QA instance includes references to the document pages and bounding boxes for the answer clues. We incorporate multiple categories of questions and unanswerable questions from the document for realistic question-answering applications. We empirically evaluate the effectiveness of our dataset with text-based large language models (LLMs) and multimodal models. Incorporating unanswerable questions in finetuning may contribute to harnessing the so-called hallucination generation.",
}
```

### Contributions

Thanks to [@mizuumi](https://github.com/mizuumi) for creating this dataset.
