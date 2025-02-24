from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def echo(request: Request):
    data = await request.json()  # Parse the incoming JSON
    print("Received:", data)  # Print the received data
    return {"message": "Received", "data": data}  # Return the data as response

# Run the server using: uvicorn filename:app --reload
