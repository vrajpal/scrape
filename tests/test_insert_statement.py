from db import insert_stat

#this cannot happen until a player and team has been established
def test_insert_statement():
    expected_stat = []
    assert expected_stat == insert_stat(values)