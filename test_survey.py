import pytest
import hashlib

def survey_campus(fname: str) -> (int, int, int):
    ''' Returns information of an optimal tour of the network stored at fname.

    Parameters:
    - fname: the path to information on the network

    Returns:
    information of an optimal tour of the network.
    '''
    pass

HASHES = ['35990e4e99eb8e2eac6c9b4f1eccaf5a981ae646699d39de735dd74020f4d61e',
          '3961b95f632b05c173ddd6535ea1033a2fc153e88bd576ec6179c5f5941cec83']


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("i", range(len(HASHES)))
def test_survey(i: int):
    fname = f'tests/survey_{i}.txt'
    assert hashcode(survey_campus(fname)) == HASHES[i], \
        f'Test failed for {fname}'
        
    
