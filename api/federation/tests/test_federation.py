import pytest
from pytest_mock import MockerFixture
from api.federation import Federation


@pytest.mark.skip
def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Federation.route + '/' in endpoint:
            assert endpoint in Federation.endpoints


@pytest.mark.skip
def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Federation.route + '/' in endpoint:
            assert endpoint in Federation.endpoints


@pytest.mark.skip
def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Federation.route + '/' in endpoint:
            assert endpoint in Federation.endpoints


@pytest.mark.skip
def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Federation.route + '/' in endpoint:
            assert endpoint in Federation.endpoints

# @pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
