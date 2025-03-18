#
#  Copyright 2025 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from concurrent.futures import ThreadPoolExecutor

import pytest
from common import INVALID_API_TOKEN, create_datasets, list_dataset
from libs.auth import RAGFlowHttpApiAuth


def is_sorted(data, field, descending=True):
    timestamps = [ds[field] for ds in data]
    return (
        all(a >= b for a, b in zip(timestamps, timestamps[1:]))
        if descending
        else all(a <= b for a, b in zip(timestamps, timestamps[1:]))
    )


class TestAuthorization:
    @pytest.mark.parametrize(
        "auth, expected_code, expected_message",
        [
            (None, 0, "`Authorization` can't be empty"),
            (
                RAGFlowHttpApiAuth(INVALID_API_TOKEN),
                109,
                "Authentication error: API key is invalid!",
            ),
        ],
    )
    def test_invalid_auth(self, auth, expected_code, expected_message):
        res = list_dataset(auth)
        assert res["code"] == expected_code
        assert res["message"] == expected_message


class TestDatasetList:
    def test_default(self, get_http_api_auth):
        create_datasets(get_http_api_auth, 31)
        res = list_dataset(get_http_api_auth, params={})

        assert res["code"] == 0
        assert len(res["data"]) == 30

    @pytest.mark.parametrize(
        "params, expected_code, expected_page_size, expected_message",
        [
            ({"page": None, "page_size": 2}, 0, 2, ""),
            ({"page": 0, "page_size": 2}, 0, 2, ""),
            ({"page": 2, "page_size": 2}, 0, 2, ""),
            ({"page": 3, "page_size": 2}, 0, 1, ""),
<<<<<<< HEAD
            ({"page": "3", "page_size": 2}, 0, 1, ""),
            pytest.param(
                {"page": -1, "page_size": 2},
                100,
                0,
                "1064",
                marks=pytest.mark.xfail(reason="issues/5851"),
=======
            ({"page": "1", "page_size": 2}, 0, 2, ""),
            pytest.param(
                {"page": -1, "page_size": 2}, 100, 0, "1064", marks=pytest.mark.xfail
>>>>>>> be730d39 (init commit)
            ),
            pytest.param(
                {"page": "a", "page_size": 2},
                100,
                0,
                """ValueError("invalid literal for int() with base 10: \'a\'")""",
<<<<<<< HEAD
                marks=pytest.mark.xfail(reason="issues/5851"),
=======
                marks=pytest.mark.xfail,
>>>>>>> be730d39 (init commit)
            ),
        ],
    )
    def test_page(
        self,
        get_http_api_auth,
        params,
        expected_code,
        expected_page_size,
        expected_message,
    ):
        create_datasets(get_http_api_auth, 5)
        res = list_dataset(get_http_api_auth, params=params)
        assert res["code"] == expected_code
        if expected_code == 0:
            assert len(res["data"]) == expected_page_size
        else:
            assert res["message"] == expected_message

    @pytest.mark.parametrize(
        "params, expected_code, expected_page_size, expected_message",
        [
            ({"page_size": None}, 0, 30, ""),
            ({"page_size": 0}, 0, 0, ""),
            ({"page_size": 1}, 0, 1, ""),
            ({"page_size": 32}, 0, 31, ""),
            ({"page_size": "1"}, 0, 1, ""),
<<<<<<< HEAD
            pytest.param(
                {"page_size": -1},
                100,
                0,
                "1064",
                marks=pytest.mark.xfail(reason="issues/5851"),
            ),
=======
            pytest.param({"page_size": -1}, 100, 0, "1064", marks=pytest.mark.xfail),
>>>>>>> be730d39 (init commit)
            pytest.param(
                {"page_size": "a"},
                100,
                0,
                """ValueError("invalid literal for int() with base 10: \'a\'")""",
<<<<<<< HEAD
                marks=pytest.mark.xfail(reason="issues/5851"),
=======
                marks=pytest.mark.xfail,
>>>>>>> be730d39 (init commit)
            ),
        ],
    )
    def test_page_size(
        self,
        get_http_api_auth,
        params,
        expected_code,
        expected_page_size,
        expected_message,
    ):
        create_datasets(get_http_api_auth, 31)
        res = list_dataset(get_http_api_auth, params=params)
        assert res["code"] == expected_code
        if expected_code == 0:
            assert len(res["data"]) == expected_page_size
        else:
            assert res["message"] == expected_message

    @pytest.mark.parametrize(
        "params, expected_code, assertions, expected_message",
        [
            (
                {"orderby": None},
                0,
<<<<<<< HEAD
                lambda r: (is_sorted(r["data"], "create_time", True)),
=======
                lambda r: (is_sorted(r["data"], "create_time"), True),
>>>>>>> be730d39 (init commit)
                "",
            ),
            (
                {"orderby": "create_time"},
                0,
<<<<<<< HEAD
                lambda r: (is_sorted(r["data"], "create_time", True)),
=======
                lambda r: (is_sorted(r["data"], "create_time"), True),
>>>>>>> be730d39 (init commit)
                "",
            ),
            (
                {"orderby": "update_time"},
                0,
<<<<<<< HEAD
                lambda r: (is_sorted(r["data"], "update_time", True)),
                "",
            ),
            pytest.param(
                {"orderby": "name", "desc": "False"},
                0,
                lambda r: (is_sorted(r["data"]["docs"], "name", False)),
                "",
                marks=pytest.mark.xfail(reason="issues/5851"),
            ),
            pytest.param(
                {"orderby": "unknown"},
                102,
                0,
                "orderby should be create_time or update_time",
                marks=pytest.mark.xfail(reason="issues/5851"),
=======
                lambda r: (is_sorted(r["data"], "update_time"), True),
                "",
            ),
            pytest.param(
                {"orderby": "a"},
                100,
                0,
                """AttributeError("type object \'Knowledgebase\' has no attribute \'a\'")""",
                marks=pytest.mark.xfail,
>>>>>>> be730d39 (init commit)
            ),
        ],
    )
    def test_orderby(
        self,
        get_http_api_auth,
        params,
        expected_code,
        assertions,
        expected_message,
    ):
        create_datasets(get_http_api_auth, 3)
        res = list_dataset(get_http_api_auth, params=params)
        assert res["code"] == expected_code
        if expected_code == 0:
            if callable(assertions):
<<<<<<< HEAD
                assert assertions(res)
=======
                assert all(assertions(res))
>>>>>>> be730d39 (init commit)
        else:
            assert res["message"] == expected_message

    @pytest.mark.parametrize(
        "params, expected_code, assertions, expected_message",
        [
            (
                {"desc": None},
                0,
<<<<<<< HEAD
                lambda r: (is_sorted(r["data"], "create_time", True)),
=======
                lambda r: (is_sorted(r["data"], "create_time", True),),
>>>>>>> be730d39 (init commit)
                "",
            ),
            (
                {"desc": "true"},
                0,
<<<<<<< HEAD
                lambda r: (is_sorted(r["data"], "create_time", True)),
                "",
            ),
            (
                {"desc": "True"},
                0,
                lambda r: (is_sorted(r["data"], "create_time", True)),
                "",
            ),
            (
                {"desc": True},
                0,
                lambda r: (is_sorted(r["data"], "create_time", True)),
=======
                lambda r: (is_sorted(r["data"], "create_time", True),),
>>>>>>> be730d39 (init commit)
                "",
            ),
            (
                {"desc": "false"},
                0,
<<<<<<< HEAD
                lambda r: (is_sorted(r["data"], "create_time", False)),
                "",
            ),
            (
                {"desc": "False"},
                0,
                lambda r: (is_sorted(r["data"], "create_time", False)),
                "",
            ),
            (
                {"desc": False},
                0,
                lambda r: (is_sorted(r["data"], "create_time", False)),
                "",
            ),
            (
                {"desc": "False", "orderby": "update_time"},
                0,
                lambda r: (is_sorted(r["data"], "update_time", False)),
                "",
            ),
            pytest.param(
                {"desc": "unknown"},
                102,
                0,
                "desc should be true or false",
                marks=pytest.mark.xfail(reason="issues/5851"),
=======
                lambda r: (is_sorted(r["data"], "create_time", False),),
                "",
            ),
            (
                {"desc": True},
                0,
                lambda r: (is_sorted(r["data"], "create_time", True),),
                "",
            ),
            (
                {"desc": "false", "orderby": "update_time"},
                0,
                lambda r: (is_sorted(r["data"], "update_time", False),),
                "",
            ),
            pytest.param(
                {"desc": "a"},
                100,
                0,
                """AttributeError("type object \'Knowledgebase\' has no attribute \'a\'")""",
                marks=pytest.mark.xfail,
>>>>>>> be730d39 (init commit)
            ),
        ],
    )
    def test_desc(
        self,
        get_http_api_auth,
        params,
        expected_code,
        assertions,
        expected_message,
    ):
        create_datasets(get_http_api_auth, 3)
        res = list_dataset(get_http_api_auth, params=params)
<<<<<<< HEAD
        assert res["code"] == expected_code
        if expected_code == 0:
            if callable(assertions):
                assert assertions(res)
=======
        # print(res)
        assert res["code"] == expected_code
        if expected_code == 0:
            if callable(assertions):
                assert all(assertions(res))
>>>>>>> be730d39 (init commit)
        else:
            assert res["message"] == expected_message

    @pytest.mark.parametrize(
        "params, expected_code, expected_num, expected_message",
        [
            ({"name": None}, 0, 3, ""),
<<<<<<< HEAD
            ({"name": ""}, 0, 3, ""),
            ({"name": "dataset_1"}, 0, 1, ""),
            ({"name": "unknown"}, 102, 0, "You don't own the dataset unknown"),
=======
            ({"name": "dataset_1"}, 0, 1, ""),
            ({"name": "a"}, 102, 0, "You don't own the dataset a"),
>>>>>>> be730d39 (init commit)
        ],
    )
    def test_name(
        self, get_http_api_auth, params, expected_code, expected_num, expected_message
    ):
        create_datasets(get_http_api_auth, 3)
        res = list_dataset(get_http_api_auth, params=params)
        assert res["code"] == expected_code
        if expected_code == 0:
<<<<<<< HEAD
            if params["name"] in [None, ""]:
=======
            if params["name"] is None:
>>>>>>> be730d39 (init commit)
                assert len(res["data"]) == expected_num
            else:
                assert res["data"][0]["name"] == params["name"]
        else:
            assert res["message"] == expected_message

    @pytest.mark.parametrize(
        "dataset_id, expected_code, expected_num, expected_message",
        [
            (None, 0, 3, ""),
<<<<<<< HEAD
            ("", 0, 3, ""),
            (lambda r: r[0], 0, 1, ""),
            ("unknown", 102, 0, "You don't own the dataset unknown"),
=======
            (lambda r: r[0], 0, 1, ""),
            ("a", 102, 0, "You don't own the dataset a"),
>>>>>>> be730d39 (init commit)
        ],
    )
    def test_id(
        self,
        get_http_api_auth,
        dataset_id,
        expected_code,
        expected_num,
        expected_message,
    ):
        ids = create_datasets(get_http_api_auth, 3)
        if callable(dataset_id):
            params = {"id": dataset_id(ids)}
        else:
            params = {"id": dataset_id}

        res = list_dataset(get_http_api_auth, params=params)
        assert res["code"] == expected_code
        if expected_code == 0:
<<<<<<< HEAD
            if params["id"] in [None, ""]:
=======
            if params["id"] is None:
>>>>>>> be730d39 (init commit)
                assert len(res["data"]) == expected_num
            else:
                assert res["data"][0]["id"] == params["id"]
        else:
            assert res["message"] == expected_message

    @pytest.mark.parametrize(
        "dataset_id, name, expected_code, expected_num, expected_message",
        [
            (lambda r: r[0], "dataset_0", 0, 1, ""),
            (lambda r: r[0], "dataset_1", 0, 0, ""),
<<<<<<< HEAD
            (lambda r: r[0], "unknown", 102, 0, "You don't own the dataset unknown"),
            ("id", "dataset_0", 102, 0, "You don't own the dataset id"),
=======
            (lambda r: r[0], "a", 102, 0, "You don't own the dataset a"),
            ("a", "dataset_0", 102, 0, "You don't own the dataset a"),
>>>>>>> be730d39 (init commit)
        ],
    )
    def test_name_and_id(
        self,
        get_http_api_auth,
        dataset_id,
        name,
        expected_code,
        expected_num,
        expected_message,
    ):
        ids = create_datasets(get_http_api_auth, 3)
        if callable(dataset_id):
            params = {"id": dataset_id(ids), "name": name}
        else:
            params = {"id": dataset_id, "name": name}

        res = list_dataset(get_http_api_auth, params=params)
        if expected_code == 0:
            assert len(res["data"]) == expected_num
        else:
            assert res["message"] == expected_message

    def test_concurrent_list(self, get_http_api_auth):
        create_datasets(get_http_api_auth, 3)

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(list_dataset, get_http_api_auth) for i in range(100)
            ]
        responses = [f.result() for f in futures]
        assert all(r["code"] == 0 for r in responses)

    def test_invalid_params(self, get_http_api_auth):
        params = {"a": "b"}
        res = list_dataset(get_http_api_auth, params=params)
        assert res["code"] == 0
        assert len(res["data"]) == 0
