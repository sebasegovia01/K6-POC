from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


async def fetch_cat_fact():
    get_url = "https://catfact.ninja/fact"
    get_response = requests.get(get_url)
    if get_response.status_code == 200:
        return get_response.json()
    else:
        raise HTTPException(status_code=get_response.status_code, detail="Failed to retrieve cat fact")
    
@app.get("/get-cat-fact")
async def get_cat_fact():
    url = "https://catfact.ninja/fact"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve cat fact", "status_code": response.status_code}
@app.post("/post-cat-fact")
async def post_cat_fact():
    post_url = "https://webhook-test.com/46b1d4bded6628fd3d3e036c520360da"
    headers={
        "Content-type": "application/json"
    }
    fact_data = await fetch_cat_fact()
    post_response = requests.post(post_url, json=fact_data, headers=headers)
    if post_response.status_code in [200, 201]:
       return {"message": "Cat fact sent succesfully", "fact": fact_data}
    else:
        return HTTPException(status_code=post_response.status_code, detail="Failed to send cat fact")

@app.put("/put-cat-fact")
async def put_cat_fact():
    put_url = "https://webhook-test.com/46b1d4bded6628fd3d3e036c520360da"
    headers={
        "Content-type": "application/json"
    }
    fact_data = await fetch_cat_fact()
    put_response = requests.put(put_url,fact_data,headers=headers )
    if put_response.status_code in [200, 201]:
        return {"message": "Cat fact updated succesfully", "fact": fact_data}
    else:
        return HTTPException(status_code=put_response.status_code, detail="Failed to update cat fact")
    