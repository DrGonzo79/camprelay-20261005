from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="CampRelay planning API", version="0.1.0")

CAMPS = [
    {"id":"soccer-july","name":"Riverbend Soccer Week","category":"Sports","month":"July","price":340,"aftercare":True,"opens":"2027-01-12T09:00:00-05:00","distance":4,"demand":5},
    {"id":"science-july","name":"Curiosity Lab","category":"Science","month":"July","price":375,"aftercare":True,"opens":"2027-02-03T08:00:00-05:00","distance":7,"demand":5},
    {"id":"nature-july","name":"Pine & Puddle Explorers","category":"Outdoors","month":"July","price":295,"aftercare":False,"opens":"2027-01-20T10:00:00-05:00","distance":11,"demand":3},
    {"id":"robotics-august","name":"BrightBot Builders","category":"Technology","month":"August","price":420,"aftercare":True,"opens":"2027-02-10T09:00:00-05:00","distance":6,"demand":4},
    {"id":"arts-july","name":"Colorwheel Studio Camp","category":"Arts","month":"July","price":260,"aftercare":True,"opens":"2027-03-01T12:00:00-05:00","distance":9,"demand":3},
]

class MatchRequest(BaseModel):
    month: str | None = Field(default=None, max_length=30)
    preferred_category: str | None = Field(default=None, max_length=60)
    backup_category: str | None = Field(default=None, max_length=60)
    max_price: int = Field(ge=50, le=5000)
    require_aftercare: bool = True
    max_distance: int = Field(default=25, ge=1, le=100)

class RelayRequest(BaseModel):
    camp_ids: list[str] = Field(min_length=2, max_length=3)
    child_profile_complete: bool
    payment_approved: bool
    consent_confirmed: bool

@app.get("/health")
def health() -> dict[str, str]:
    return {"status":"ok"}

@app.post("/matches")
def matches(request: MatchRequest) -> dict:
    found=[]
    for camp in CAMPS:
        if request.month and camp["month"] != request.month: continue
        if camp["price"] > request.max_price: continue
        if request.require_aftercare and not camp["aftercare"]: continue
        if camp["distance"] > request.max_distance: continue
        category_points = 25 if camp["category"] == request.preferred_category else 14 if camp["category"] == request.backup_category else 0
        price_points = round((request.max_price-camp["price"])/request.max_price*20)
        fit=max(0,min(100,55+category_points+price_points+(5 if camp["aftercare"] else 0)-camp["distance"]//5))
        found.append({**camp,"fit_score":fit})
    found.sort(key=lambda item:(-item["fit_score"],item["price"]))
    return {"count":len(found),"matches":found,"disclaimer":"Fictional demo inventory; verify all details with the camp."}

@app.post("/relay-plan")
def relay_plan(request: RelayRequest) -> dict:
    if len(set(request.camp_ids)) != len(request.camp_ids):
        raise HTTPException(status_code=422,detail="Camp choices must be unique")
    camps=[]
    for camp_id in request.camp_ids:
        camp=next((item for item in CAMPS if item["id"]==camp_id),None)
        if not camp: raise HTTPException(status_code=404,detail=f"Camp not found: {camp_id}")
        camps.append(camp)
    missing=[]
    if not request.child_profile_complete: missing.append("child profile")
    if not request.payment_approved: missing.append("payment approval")
    if not request.consent_confirmed: missing.append("parent consent")
    ready=not missing
    return {"ready":ready,"missing":missing,"primary":camps[0]["id"],"backups":[c["id"] for c in camps[1:]],"next_opening":min(c["opens"] for c in camps),"handoff":"official camp form","auto_submit":False}
