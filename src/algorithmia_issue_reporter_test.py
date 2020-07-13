from . import algorithmia_perf_track

def test_algorithmia_perf_track():
    assert algorithmia_perf_track.apply("Jane") == "hello Jane"
