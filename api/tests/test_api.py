from fastapi.testclient import TestClient
from main import app
client=TestClient(app)

def test_health(): assert client.get("/health").json()=={"status":"ok"}
def test_matches_rank_primary_and_backup():
    data=client.post("/matches",json={"month":"July","preferred_category":"Sports","backup_category":"Science","max_price":400,"require_aftercare":True,"max_distance":10}).json()
    assert data["count"]==3
    assert [x["id"] for x in data["matches"][:2]]==["soccer-july","science-july"]
def test_no_match_is_explicit():
    response=client.post("/matches",json={"month":"August","max_price":300,"require_aftercare":True})
    assert response.status_code==200 and response.json()["matches"]==[]
def test_invalid_price_rejected(): assert client.post("/matches",json={"max_price":20}).status_code==422
def test_ready_relay_preserves_order_and_never_submits():
    data=client.post("/relay-plan",json={"camp_ids":["soccer-july","science-july"],"child_profile_complete":True,"payment_approved":True,"consent_confirmed":True}).json()
    assert data["ready"] is True and data["primary"]=="soccer-july" and data["auto_submit"] is False
def test_incomplete_relay_names_missing_readiness():
    data=client.post("/relay-plan",json={"camp_ids":["soccer-july","science-july"],"child_profile_complete":False,"payment_approved":True,"consent_confirmed":False}).json()
    assert data["ready"] is False and data["missing"]==["child profile","parent consent"]
def test_duplicate_and_unknown_choices_fail():
    assert client.post("/relay-plan",json={"camp_ids":["soccer-july","soccer-july"],"child_profile_complete":True,"payment_approved":True,"consent_confirmed":True}).status_code==422
    assert client.post("/relay-plan",json={"camp_ids":["soccer-july","missing"],"child_profile_complete":True,"payment_approved":True,"consent_confirmed":True}).status_code==404
