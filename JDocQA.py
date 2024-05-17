# Copyright 2024 Shunsuke Kitada and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This script was generated from shunk031/cookiecutter-huggingface-datasets.
#
# TODO: Address all TODOs and remove all explanatory comments
import json
import os
import re
from typing import List

import datasets as ds
from datasets.utils.logging import get_logger

logger = get_logger(__name__)

_CITATION = """\
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
"""

_DESCRIPTION = """\
Japanese Document Question Answering (JDocQA), a large-scale document-based QA dataset, essentially requiring both visual and textual information to answer questions, which comprises 5,504 documents in PDF format and annotated 11,600 question-and-answer instances in Japanese.
"""

_HOMEPAGE = "https://github.com/mizuumi/JDocQA"

_LICENSE = "JDocQA dataset annotations are distributed under CC BY-SA 4.0."

_URLS = {
    "annotations": {
        "train": "https://raw.githubusercontent.com/mizuumi/JDocQA/main/dataset/annotation_files/jdocqa_train_all.json",
        "validation": "https://github.com/mizuumi/JDocQA/raw/main/dataset/annotation_files/jdocqa_validation_all.json",
        "test": "https://github.com/mizuumi/JDocQA/raw/main/dataset/annotation_files/jdocqa_test_all.json",
    },
    "documents": "https://vlm-lab-fileshare.s3.ap-northeast-1.amazonaws.com/pdf_files.zip",
}


class JDocQADataset(ds.GeneratorBasedBuilder):
    """A class for loading JDocQA dataset."""

    VERSION = ds.Version("1.0.0")

    BUILDER_CONFIGS = [
        ds.BuilderConfig(
            version=VERSION,
            description=_DESCRIPTION,
        ),
    ]

    def _info(self) -> ds.DatasetInfo:
        features = ds.Features(
            {
                "answer": ds.Value("string"),
                "answer_type": ds.ClassLabel(
                    num_classes=4,
                    names=["yes/no", "factoid", "numerical", "open-ended"],
                ),
                "context": ds.Value("string"),
                "multiple_select_answer": ds.ClassLabel(
                    num_classes=4,
                    names=["A", "B", "C", "D"],
                ),
                "multiple_select_question": ds.Sequence(ds.Value("string")),
                "no_reason": ds.ClassLabel(
                    num_classes=4,
                    names=["0", "1", "2", "1,2"],
                ),
                "normalized_answer": ds.Value("string"),
                "original_answer": ds.Value("string"),
                "original_context": ds.Value("string"),
                "original_question": ds.Value("string"),
                "pdf_category": ds.ClassLabel(
                    num_classes=4,
                    names=["Document", "Kouhou", "Slide", "Website"],
                ),
                "pdf_name": ds.Value("string"),
                "question": ds.Value("string"),
                "question_number": ds.Sequence(ds.Value("uint64")),
                "question_page_number": ds.Value("string"),
                "reason_of_answer_bbox": ds.Sequence(ds.Value("string")),
                "text_from_ocr_pdf": ds.Value("string"),
                "text_from_pdf": ds.Value("string"),
                "type_of_image": ds.Sequence(
                    ds.ClassLabel(
                        num_classes=10,
                        names=[
                            "Null",
                            "Table",
                            "Bar chart",
                            "Line chart",
                            "Pie chart",
                            "Map",
                            "Other figures",
                            "Mixtured writing style from left to the right and from upside to the downside",
                            "Drawings",
                            "Others",
                        ],
                    )
                ),
                #
                # `pdf_filepath` is added to the original dataset for convenience
                "pdf_filepath": ds.Value("string"),
            }
        )
        return ds.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(
        self, dl_manager: ds.DownloadManager
    ) -> List[ds.SplitGenerator]:
        files = dl_manager.download_and_extract(_URLS)

        tng_ann_filepath = files["annotations"]["train"]  # type: ignore
        val_ann_filepath = files["annotations"]["validation"]  # type: ignore
        tst_ann_filepath = files["annotations"]["test"]  # type: ignore

        documents_dirpath = os.path.join(files["documents"], "pdf_files")  # type: ignore

        return [
            ds.SplitGenerator(
                name=ds.Split.TRAIN,  # type: ignore
                gen_kwargs={
                    "annotation_path": tng_ann_filepath,
                    "documents_dir": documents_dirpath,
                },
            ),
            ds.SplitGenerator(
                name=ds.Split.VALIDATION,  # type: ignore
                gen_kwargs={
                    "annotation_path": val_ann_filepath,
                    "documents_dir": documents_dirpath,
                },
            ),
            ds.SplitGenerator(
                name=ds.Split.TEST,  # type: ignore
                gen_kwargs={
                    "annotation_path": tst_ann_filepath,
                    "documents_dir": documents_dirpath,
                },
            ),
        ]

    def _convert_answer_type(self, answer_type: str) -> str:
        if answer_type == "1":
            return "yes/no"
        elif answer_type == "2":
            return "factoid"
        elif answer_type == "3":
            return "numerical"
        elif answer_type == "4":
            return "open-ended"
        else:
            raise ValueError(f"Unknown answer type: {answer_type}")

    def _convert_multiple_select_question(
        self, multiple_select_question: str
    ) -> List[str]:
        _, qs = multiple_select_question.split("(A)")

        questions = []
        for sep in ("(B)", "(C)", "(D)"):
            q, qs = qs.split(sep)
            questions.append(q)
        questions.append(qs)

        assert (
            len(questions) == 4
        ), f"Before: {multiple_select_question}, After: {questions}"

        questions = [question.rstrip("、") for question in questions]
        return questions

    def _convert_question_number(self, question_number: str) -> List[int]:
        return [int(qn) for qn in question_number.split("-")]

    def _convert_reason_of_answer_bbox(self, reason_of_answer_bbox: str) -> List[str]:
        reason_of_answer_bboxes = [
            r for r in re.split(r"[.,、､]", reason_of_answer_bbox)
        ]
        check = [r.isdigit() if r != "" else r == "" for r in reason_of_answer_bboxes]
        assert all(check), reason_of_answer_bboxes
        return reason_of_answer_bboxes

    def _convert_type_of_image(self, type_of_image: str) -> List[str]:
        types_of_image = type_of_image.split(",")

        def convert_to_type_of_image(type_of_image: str) -> str:
            if type_of_image == "":
                return "Null"
            elif type_of_image == "1":
                return "Table"
            elif type_of_image == "2":
                return "Bar chart"
            elif type_of_image == "3":
                return "Line chart"
            elif type_of_image == "4":
                return "Pie chart"
            elif type_of_image == "5":
                return "Map"
            elif type_of_image == "6":
                return "Other figures"
            elif type_of_image == "7":
                return "Mixtured writing style from left to the right and from upside to the downside"
            elif type_of_image == "8":
                return "Drawings"
            elif type_of_image == "9":
                return "Others"
            else:
                raise ValueError(f"Unknown type of image: {type_of_image}")

        return [convert_to_type_of_image(t) for t in types_of_image]

    def _get_pdf_fielpath(self, pdf_name: str, documents_dir: str) -> str:
        pdf_filepath = os.path.join(documents_dir, pdf_name)
        assert os.path.exists(pdf_filepath), f"File not found: {pdf_filepath}"
        return pdf_filepath

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, annotation_path: str, documents_dir: str):
        with open(annotation_path) as rf:
            for i, line in enumerate(rf):
                data = json.loads(line)

                data["answer_type"] = self._convert_answer_type(
                    answer_type=data["answer_type"]
                )
                data["multiple_select_question"] = (
                    self._convert_multiple_select_question(
                        multiple_select_question=data["multiple_select_question"]
                    )
                )
                data["question_number"] = self._convert_question_number(
                    data["question_number"]
                )
                data["reason_of_answer_bbox"] = self._convert_reason_of_answer_bbox(
                    data["reason_of_answer_bbox"]
                )
                data["type_of_image"] = self._convert_type_of_image(
                    type_of_image=data["type_of_image"]
                )
                data["pdf_filepath"] = self._get_pdf_fielpath(
                    pdf_name=data["pdf_name"],
                    documents_dir=documents_dir,
                )

                yield i, data
