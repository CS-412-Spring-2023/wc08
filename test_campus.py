import pytest
import hashlib

def connect_campus(fname: str) -> (int, int, int):
    ''' Returns information of an optimal tour of the network stored at fname.

    Parameters:
    - fname: the path to information on the network

    Returns:
    information of an optimal tour of the network.
    '''
    pass

HASHES = ['389337886c3865d5ab4cf1a321208dda8154ebbeeb1149f0b0c87650ad23f733']

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("i", range(len(HASHES)))
def test_campus(i: int):
    fname = f'tests/campus_{i}.txt'
    assert hashcode(connect_campus(fname)) == HASHES[i], \
        f'Test failed for {fname}'
        
    
