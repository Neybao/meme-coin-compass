import sqlite3
import bcrypt
import os
import hashlib

# Caminho para o banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'usuarios.db')

def criar_banco():
    """
    Cria o banco de dados e a tabela de usuários se não existir.
    """
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
        ''')
        conn.commit()
        conn.close()

def cadastrar_usuario(usuario, senha):
    """
    Cadastra um novo usuário com senha criptografada.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode('utf-8')
    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def usuario_existe(usuario):
    """
    Verifica se o usuário já está cadastrado.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM usuarios WHERE usuario = ?", (usuario,))
    existe = cursor.fetchone()
    conn.close()
    return existe is not None

def autenticar(usuario, senha):
    """
    Verifica se o usuário e senha estão corretos.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        senha_hash = resultado[0].encode('utf-8')  # 👈 converte para bytes
        return bcrypt.checkpw(senha.encode(), senha_hash)
    return False
