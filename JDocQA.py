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
from typing import List

import datasets as ds
from datasets.utils.logging import get_logger

logger = get_logger(__name__)

# TODO: Add BibTeX citation
# Find for instance the citation on arxiv or on the dataset repo/website
_CITATION = """\
TODO: Add BibTeX citation here
"""

# TODO: Add description of the dataset here
# You can copy an official description
_DESCRIPTION = """\
Japanese Document Question Answering (JDocQA), a large-scale document-based QA dataset, essentially requiring both visual and textual information to answer questions, which comprises 5,504 documents in PDF format and annotated 11,600 question-and-answer instances in Japanese.
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = "https://github.com/mizuumi/JDocQA"

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = "JDocQA dataset annotations are distributed under CC BY-SA 4.0."

# TODO: Add link to the official dataset URLs here
# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
_URLS = {
    "annotations": {
        "train": "https://raw.githubusercontent.com/mizuumi/JDocQA/main/dataset/annotation_files/jdocqa_train_all.json",
        "validation": "https://github.com/mizuumi/JDocQA/raw/main/dataset/annotation_files/jdocqa_validation_all.json",
        "test": "https://github.com/mizuumi/JDocQA/raw/main/dataset/annotation_files/jdocqa_test_all.json",
    },
    "documents": "https://vlm-lab-fileshare.s3.ap-northeast-1.amazonaws.com/pdf_files.zip",
}


# TODO: Name of the dataset usually matches the script name with CamelCase instead of snake_case
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
                "answer_type": ds.Value("string"),
                "context": ds.Value("string"),
                "multiple_select_answer": ds.Value("string"),
                "multiple_select_question": ds.Value("string"),
                "no_reason": ds.Value("string"),
                "normalized_answer": ds.Value("string"),
                "original_answer": ds.Value("string"),
                "original_context": ds.Value("string"),
                "original_question": ds.Value("string"),
                "pdf_category": ds.Value("string"),
                "pdf_name": ds.Value("string"),
                "question": ds.Value("string"),
                "question_number": ds.Value("string"),
                "question_page_number": ds.Value("string"),
                "reason_of_answer_bbox": ds.Value("string"),
                "text_from_ocr_pdf": ds.Value("string"),
                "text_from_pdf": ds.Value("string"),
                "type_of_image": ds.Value("string"),
                #
                # 'pdf_filepath' is added to the original dataset for convenience
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

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, annotation_path: str, documents_dir: str):
        with open(annotation_path) as rf:
            for i, line in enumerate(rf):
                data = json.loads(line)
                pdf_filepath = os.path.join(documents_dir, data["pdf_name"])
                assert os.path.exists(pdf_filepath), f"File not found: {pdf_filepath}"

                data["pdf_filepath"] = pdf_filepath
                yield i, data
