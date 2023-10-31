from fastapi import FastAPI, File, UploadFile, Request
from huffman import HuffmanCoding 
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.post("/compress")
async def compress_message(request: Request):
    message = await request.body()
    huffman = HuffmanCoding(message)
    compress = huffman.compress()
    response = {
        "compressed_message": compress
    }

    print(response)
    print(message)

    return response
