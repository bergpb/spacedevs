from bs4 import BeautifulSoup
from flask import url_for
from tests.tools import normalize_text


def test_course_page_returns_status_code_200(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert resp.status_code == 200

def test_course_single_page_contains_tags(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert "python" in resp.get_data(as_text=True)
    assert "javascript" in resp.get_data(as_text=True)
    assert "flask" in resp.get_data(as_text=True)

def test_course_single_page_contains_quotes(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert "1. introduction" in resp.get_data(as_text=True)  

def test_course_single_page_contains_name(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert "Curso de test" in resp.get_data(as_text=True)


def test_course_single_page_contains_description(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert "alguma coisa..." in resp.get_data(as_text=True)


def test_course_single_page_contains_video(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert "/video" in resp.get_data(as_text=True)


def test_course_single_page_contain_source_code_url(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert "/source" in resp.get_data(as_text=True)


def test_course_single_page_contain_duration(client):
    resp = client.get(url_for("course_page.single", slug="curso-de-test"))
    assert "300 minutos" in resp.get_data(as_text=True)
