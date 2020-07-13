from . import algorithmia_issue_reporter

def test_algorithmia_issue_reporter():
    assert algorithmia_issue_reporter.apply("Jane") == "hello Jane"
