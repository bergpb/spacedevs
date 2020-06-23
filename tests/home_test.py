from flask import url_for


def test_home_page_returns_status_code_200(client):
    resp = client.get(url_for("home.page"))
    assert resp.status_code == 200


def test_home_page_contains_course_word(client):
    resp = client.get(url_for("home.page"))
    assert "Cursos Recentes" in resp.get_data(as_text=True)
