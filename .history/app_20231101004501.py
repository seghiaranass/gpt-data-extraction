from langchain.chat_models import ChatOpenAi 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from pytesseract import image_to_string
from PIL import Image
from io import BytesIO
import pypdfium2 as pdfium
import streamlit as st
from tempfile import NamedTemporaryFile
import pandas as pd 
import json
import requests

load_dotenv()


#1. Convert PDF file into images via pypdfium2

#2. Extract text from images via pytesseract

#3. Extract structured info from text via LLM

#4. Send data to make.com via webhook