from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import requests

app = FastAPI(title="dotStaff to Ceipal Integration Bridge")

# ==========================================
# 1. THE WEBHOOK LISTENER ENDPOINT
# ==========================================
@app.post("/dotstaff-webhook-endpoint")
async def dotstaff_webhook(request: Request):
    # 💡 This catches the raw JSON payload dotStaff pushed to us
    raw_dotstaff_data = await request.json()
    
    print("\n🚨 [ALARM] Webhook Triggered by dotStaff via FastAPI!")
    print(f"📥 Raw Data Received: {raw_dotstaff_data}")

    # ==========================================
    # 2. THE DATA TRANSLATOR / MAPPER
    # ==========================================
    mapped_ceipal_data = {
        "job_title": raw_dotstaff_data.get("req_title"),
        "state": raw_dotstaff_data.get("loc_state"),
        "primary_skills": ", ".join(raw_dotstaff_data.get("skills", [])),
        "job_description": raw_dotstaff_data.get("desc")
    }

    print("\n🔄 [TRANSLATE] Data mapped to Ceipal format:")
    print(mapped_ceipal_data)

    # ==========================================
    # 3. THE OUTBOUND CEIPAL API WRITER
    # ==========================================
    print("\n📤 [API CALL] Sending mapped data to Ceipal API...")
    
    ceipal_url = "https://ceipal.com"
    headers = {
        "Authorization": "Bearer MOCK_TOKEN_VALUE",
        "Content-Type": "application/json"
    }

    try:
        # We attempt to push to Ceipal's real endpoint structure
        response = requests.post(ceipal_url, json=mapped_ceipal_data, headers=headers)
        
        # It fails because our MOCK_TOKEN_VALUE is fake, but the network logic works!
        if response.status_code == 401:
            print("❌ Ceipal API responded: Authentication Failed (Expected behavior).")
        else:
            print(f"ℹ️ Ceipal API responded with status code: {response.status_code}")
            
        return {"message": "FastAPI processed webhook, translation succeeded, Ceipal hit completed."}

    except Exception as e:
        print(f"❌ Network Error connecting to Ceipal: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "Failed to contact Ceipal API"}
        )
