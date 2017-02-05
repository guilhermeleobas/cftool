from cftool.run import format_time


def test_ms():
    assert '1ms' == format_time(1)
    assert '10ms' == format_time(10.1)
    assert '1ms' == format_time(0.99)
    assert '1ms' == format_time(0.588888)
    assert '1000ms' == format_time(999.999)


def test_s():
    assert '1s' == format_time(1 * 1000)
    assert '10s' == format_time(10 * 1000)
    assert '10s' == format_time(10000.01)
    assert '1s' == format_time(1000 + 100)
    assert '3s' == format_time(1000 + 2000)


def test_m():
    assert '1m' == format_time(1 * 1000 * 60)
    assert '2m' == format_time(1 * 1000 * 60 * 2 + 1 * 1000 * 60 * 0.49)
    assert '59m' == format_time(1 * 1000 * 60 * 59 + 100)

def test_h():
    assert '1h' == format_time (1 * 1000 * 60 * 60)
    assert '2h' == format_time (1 * 1000 * 60 * 60 * 2)
    assert '59h' == format_time (1 * 1000 * 60 * 60 * 59 + 100)
