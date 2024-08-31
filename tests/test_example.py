def test_example_page_loads(home_page):
    home_page.navigate()

    assert home_page.is_loaded()
