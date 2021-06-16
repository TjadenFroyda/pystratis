import pytest
from api.voting.requestmodels import *
from api.voting.responsemodels import *
from nodes import CirrusNode, CirrusMinerNode
from pybitcoin import PollViewModel


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_executed_polls(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = PollsRequest(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )

    response = cirrusminer_node.voting.executed_polls(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)

    response = cirrus_syncing_node.voting.executed_polls(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_pending_polls(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = PollsRequest(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=kicked_pubkey
    )

    response = cirrusminer_node.voting.pending_polls(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)

    response = cirrus_syncing_node.voting.pending_polls(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_finished_polls(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = PollsRequest(
        vote_type=VoteKey.KickFederationMember,
        pubkey_of_member_being_voted_on=generate_compressed_pubkey
    )

    response = cirrusminer_node.voting.finished_polls(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)

    response = cirrus_syncing_node.voting.finished_polls(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PollViewModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_scheduledvote_whitelisthash(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = ScheduleVoteWhitelistHashRequest(hash=generate_uint256)

    cirrusminer_node.voting.schedulevote_whitelisthash(request_model)
    cirrus_syncing_node.voting.schedulevote_whitelisthash(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_scheduledvote_removehash(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = ScheduleVoteRemoveHashRequest(hash=generate_uint256)

    cirrusminer_node.voting.schedulevote_removehash(request_model)
    cirrus_syncing_node.voting.schedulevote_removehash(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_whitelistedhashes(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.voting.whitelisted_hashes()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, WhitelistedHashesModel)

    response = cirrus_syncing_node.voting.whitelisted_hashes()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, WhitelistedHashesModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_scheduledvotes(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.voting.scheduled_votes()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, VotingDataModel)

    response = cirrus_syncing_node.voting.scheduled_votes()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, VotingDataModel)
