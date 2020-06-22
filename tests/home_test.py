from flask import url_for


def test_home_page_returns_status_code_200(client, data_regression):
    response = client.get(url_for("home.page"))
    data_regression.check({"status_code": response.status_code})


def test_home_page_contains_course_word(client, data_regression):
    response = client.get(url_for("home.page"))
    data_regression.check(response.get_data(as_text=True))
