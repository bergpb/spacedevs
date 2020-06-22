from flask import url_for


def test_course_page_returns_status_code_200(client, data_regression):
    response = client.get(url_for("course_page.single", slug="curso-de-test"))
    data_regression.check({"status_code": response.status_code})


def test_course_page_returns_raw_html(client, data_regression):
    response = client.get(url_for("course_page.single", slug="curso-de-test"))
    data_regression.check(response.get_data(as_text=True))
