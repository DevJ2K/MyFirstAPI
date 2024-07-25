from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return {
		"response": 200,
		"message": "This is the root page."
	}

@app.get("/test")
def test():
	return {
		"response": 200,
		"message": "This is the test page."
	}
