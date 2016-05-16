from cf.src.enums import *

def test_run_enum_messages():
    exp = [
        'Success',
        'Folder not found',
        'Folder is empty',
        'Error while running program'
    ]
    
    assert len(E_RUN) == len(exp)
    
    for item in E_RUN:
        assert E_RUN[item] in exp 
