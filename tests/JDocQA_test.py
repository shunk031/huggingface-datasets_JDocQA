import os

import datasets as ds
import pytest


@pytest.fixture
def dataset_name() -> str:
    return "JDocQA"


@pytest.fixture
def dataset_path(dataset_name: str) -> str:
    return f"{dataset_name}.py"


@pytest.mark.skipif(
    condition=bool(os.environ.get("CI", False)),
    reason=(
        "Because this loading script downloads a large dataset, "
        "we will skip running it on CI."
    ),
)
@pytest.mark.parametrize(
    argnames="rename_pdf_category",
    argvalues=[True, False],
)
def test_load_dataset(
    dataset_path: str,
    rename_pdf_category: bool,
    expected_num_train: int = 9290,
    expected_num_validation: int = 1134,
    expected_num_test: int = 1176,
):
    dataset = ds.load_dataset(
        path=dataset_path,
        rename_pdf_category=rename_pdf_category,
        trust_remote_code=True,
    )
    assert isinstance(dataset, ds.DatasetDict)

    assert dataset["train"].num_rows == expected_num_train
    assert dataset["validation"].num_rows == expected_num_validation
    assert dataset["test"].num_rows == expected_num_test
