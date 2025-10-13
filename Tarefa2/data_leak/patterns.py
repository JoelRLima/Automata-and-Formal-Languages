# patterns.py
import re

PATTERNS = {
    #Dados pessoais
    "CPF": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
    "CNPJ": re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"),
    "E-mail": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
    "Telefone": re.compile(r"\(?\d{2,3}\)?\s?\d{4,5}-?\d{4}"),
    "Cartão de Crédito": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "Senha exposta": re.compile(r"(?i)(?:senha|password|pwd)\s*[:=]\s*\S+"),

    #Padrões gerais
    "URL": re.compile(r"https?://[\w./-]+|www\.[\w./-]+"),
    "Data": re.compile(r"\b\d{2}/\d{2}/\d{4}\b"),
}
