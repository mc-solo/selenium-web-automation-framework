"""TodoMVC tests (https://demo.playwright.dev/todomvc). No login needed."""

import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.todo
def test_add_todo_shows_in_list(todo_page):
    todo_page.open()
    todo_page.add_todo("Write Selenium tests")
    assert "Write Selenium tests" in todo_page.todo_texts()
    assert "1 item left" in todo_page.items_left_text()


@pytest.mark.regression
@pytest.mark.todo
def test_add_multiple_todos(todo_page):
    todo_page.open()
    todo_page.add_todo("First task")
    todo_page.add_todo("Second task")
    assert todo_page.todo_count() == 2


@pytest.mark.regression
@pytest.mark.todo
def test_complete_todo_updates_counter(todo_page):
    todo_page.open()
    todo_page.add_todo("Buy milk")
    todo_page.toggle_todo_by_text("Buy milk")
    assert "0 items left" in todo_page.items_left_text()


@pytest.mark.regression
@pytest.mark.todo
def test_completed_filter_shows_only_completed(todo_page):
    todo_page.open()
    todo_page.add_todo("Done task")
    todo_page.add_todo("Open task")
    todo_page.toggle_todo_by_text("Done task")
    todo_page.filter_completed()
    assert todo_page.todo_texts() == ["Done task"]


@pytest.mark.regression
@pytest.mark.todo
def test_active_filter_hides_completed(todo_page):
    todo_page.open()
    todo_page.add_todo("Done task")
    todo_page.add_todo("Open task")
    todo_page.toggle_todo_by_text("Done task")
    todo_page.filter_active()
    assert todo_page.todo_texts() == ["Open task"]


@pytest.mark.regression
@pytest.mark.todo
def test_clear_completed_removes_done_todos(todo_page):
    todo_page.open()
    todo_page.add_todo("Done task")
    todo_page.add_todo("Open task")
    todo_page.toggle_todo_by_text("Done task")
    todo_page.clear_completed()
    assert todo_page.todo_texts() == ["Open task"]


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.todo
def test_delete_todo_removes_it(todo_page):
    todo_page.open()
    todo_page.add_todo("Temporary task")
    todo_page.delete_todo_by_text("Temporary task")
    assert todo_page.todo_texts() == []
