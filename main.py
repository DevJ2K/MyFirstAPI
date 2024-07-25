from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {
		"response": 200,
		"message": "This is the root page."
	}

@app.get("/test")
async def test():
	return {
		"response": 200,
		"message": "This is the test page."
	}
