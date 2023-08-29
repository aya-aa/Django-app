import re
import pdfplumber
import spacy
from nltk.corpus import stopwords
import pandas as pd
import os
from django.conf import settings
from spacy.matcher import Matcher 
from difflib import SequenceMatcher



# Load pre-trained model
nlp = spacy.load('en_core_web_sm')

# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

matcher = Matcher(nlp.vocab)

# Load skill data
SKILL_DATA_PATH = os.path.join(settings.BASE_DIR, 'website', 'skill_list.csv')
SKILLS = set(pd.read_csv(SKILL_DATA_PATH).columns)

# Extract mobile number using regex
def extract_mobile_number(text):
    phone_numbers = re.findall(r'((?:\+?\d{1,2}\s?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4})', text)
    return phone_numbers[0] if phone_numbers else None

# Extract email using regex
def extract_email(text):
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return email[0] if email else None

# Extract skills using predefined skill data
def extract_skills(text):
    tokens = [token.text.lower() for token in nlp(text) if not token.is_stop]
    extracted_skills = set(tokens).intersection(SKILLS)
    return [skill.capitalize() for skill in extracted_skills]

# Extract education using predefined education degrees
def extract_education(text):
    education = []
    for sentence in nlp(text).sents:
        sentence_text = sentence.text
        sentence_text_lower = sentence_text.lower()
        if any(degree in sentence_text_lower for degree in ['b.e', 'b.tech', 'm.tech', 'm.e', 'bs', 'ms', 'btech', 'mtech', 'be', 'me']):
            year_match = re.search(r'\b\d{4}\b', sentence_text)
            if year_match:
                degree = next(degree for degree in ['b.e', 'b.tech', 'm.tech', 'm.e', 'bs', 'ms', 'btech', 'mtech', 'be', 'me'] if degree in sentence_text_lower)
                education.append((degree.upper(), year_match.group()))
    return education

# Extract name using matcher
def extract_name(text):
    nlp_text = nlp(text)
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('NAME', [pattern])
    matches = matcher(nlp_text)
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text

# Extract text from PDF using pdfplumber
def extract_text_from_pdf2(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ' '.join([page.extract_text() for page in pdf.pages])
    return text


