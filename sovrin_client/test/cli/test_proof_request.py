<<<<<<< Updated upstream
import pytest


@pytest.mark.skip('INDY-85. Not implemented yet')
=======
>>>>>>> Stashed changes
def test_show_nonexistant_proof_request(be, do, aliceCLI):
    be(aliceCLI)
    do("show proof request Transcript", expect=["No matching Proof Requests found in current keyring"], within=1)
