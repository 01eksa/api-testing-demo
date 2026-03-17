import pytest
import requests

from .config import BASE_URL, DATA


def assert_data(expected_data, actual_data):
    assert type(expected_data) == type(actual_data), f'Type mismatch: expected {type(expected_data)}, got {type(actual_data)}'

    if isinstance(expected_data, list):
        assert len(expected_data) == len(actual_data), f'Len mismatch: expected {len(expected_data)}, got {len(actual_data)}'
        for expected, actual in zip(expected_data, actual_data):
            assert_data(expected, actual)
    elif isinstance(expected_data, dict):
        for key, value in expected_data.items():
            assert key in actual_data, f'Key missing in response: {key}'
            assert_data(value, actual_data[key])
    else:
        assert expected_data == actual_data, f'Value mismatch: expected {expected_data}, got {actual_data}'


@pytest.mark.parametrize('resource', DATA.keys())
def test_api_standard_behavior(resource):
    r = requests.get(f'{BASE_URL}/{resource}')
    assert r.status_code == 200

    r = requests.post(f'{BASE_URL}/{resource}', json={'test': True})
    assert r.status_code == 201

    r = requests.get(f'{BASE_URL}/{resource}/999999999999')
    assert r.status_code == 404


@pytest.mark.parametrize(('resource', 'expected_json'), [
    (res, data) for res in DATA.keys() for data in DATA[res]['get']
])
def test_get(resource, expected_json):
    url = f'{BASE_URL}/{resource}/{expected_json['id']}'
    r = requests.get(url)

    assert r.status_code == 200
    assert isinstance(response_json := r.json(), dict)
    assert_data(expected_json, response_json)


@pytest.mark.parametrize(('resource', 'request_json'), [
    (res, data) for res in DATA.keys() for data in DATA[res]['post']
])
def test_post(resource, request_json):
    url = f'{BASE_URL}/{resource}'
    r = requests.post(url, json=request_json)

    assert r.status_code == 201
    assert isinstance(response_json := r.json(), dict)
    assert isinstance(response_json['id'], int)
    assert_data(request_json, response_json)


@pytest.mark.parametrize(('resource', 'request_json'), [
    (res, data) for res in DATA.keys() for data in DATA[res]['put']
])
def test_put(resource, request_json):
    url = f'{BASE_URL}/{resource}/{request_json['id']}'
    r = requests.put(url, json=request_json)

    assert r.status_code == 200
    assert isinstance(response_json := r.json(), dict)
    assert isinstance(response_json['id'], int)
    assert_data(request_json, response_json)


@pytest.mark.parametrize(('resource', 'request_json'), [
    (res, data) for res in DATA.keys() for data in DATA[res]['patch']
])
def test_patch(resource, request_json):
    url = f'{BASE_URL}/{resource}/{request_json['id']}'
    r = requests.patch(url, json=request_json)

    assert r.status_code == 200
    assert isinstance(response_json := r.json(), dict)
    assert isinstance(response_json['id'], int)
    assert_data(request_json, response_json)


@pytest.mark.parametrize(('resource', 'id'), [
    (res, id) for res in DATA.keys() for id in DATA[res]['delete']
])
def test_delete(resource, id):
    url = f'{BASE_URL}/{resource}/{id}'
    r = requests.delete(url)

    assert r.status_code == 200
