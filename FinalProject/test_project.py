import pytest
from project import countdown,start_timer,pause_resume_timer,reset_timer

def test_start_timer():
    with pytest.raises(ValueError):
        start_timer(0.5)
