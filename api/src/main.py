from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .huffman import HuffmanCoding

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


class Input(BaseModel):
    message: str


@app.get("/compress/{message}")
async def compress_message(message: str):
    Huffman = HuffmanCoding(message)
    compress = Huffman.compress()
    return compress
