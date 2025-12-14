<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjAwYmY5MmVkYTczOWRhZTVhNzJjYTYwMDMwYTczM2I3NzI3YjYxMiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/w0r0Qh2X5FjC83p1Xb/giphy.gif" width="600px" alt="Cryptography GIF: Code and Lock">

  <h1 align="center">🔐 Fundamentos de Criptografia</h1>

  <p align="center">
    <strong>Implementações Práticas e Conceitos de Segurança da Informação</strong>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/Area-Cibersegurança-007ACC?style=for-the-badge">
    <img src="https://img.shields.io/badge/Conceitos-CIA--N%20Triad-red?style=for-the-badge">
  </p>
</div>

---

## 📖 Sobre o Repositório

Este repositório serve como um guia prático e teórico para a **Criptografia**, a espinha dorsal da Segurança da Informação.

Exploramos os conceitos fundamentais que garantem a segurança dos dados:
* **Confidencialidade:** Proteção da informação contra acesso não autorizado.
* **Integridade:** Garantia de que a informação não foi alterada.
* **Autenticação:** Verificação da identidade do remetente ou receptor.
* **Não Repúdio:** Prova irrefutável de que uma ação ocorreu.

---

## 🔑 Tipos e Implementações

O conteúdo está dividido por tipos de criptografia, com exemplos práticos em Python para cada conceito:

| Categoria | Algoritmos / Conceitos | Foco Principal | Status |
| :--- | :--- | :--- | :---: |
| **Simétrica** | **AES** (Advanced Encryption Standard), Chaves Secretas. | Confidencialidade e Velocidade. | ✅ |
| **Assimétrica** | **RSA, ECC** (Elliptic Curve Cryptography), Pares de Chaves (Pública/Privada). | Distribuição de Chaves e Assinaturas. | ✅ |
| **Funções de Hash** | **SHA-256**, **MD5** (obsoleto). | Integridade e Verificação de Senhas. | ✅ |
| **Assinaturas Digitais** | Combinação de Hash e Criptografia Assimétrica. | Autenticação e Não Repúdio. | 🚧 |
| **Protocolos** | **TLS/SSL**, Troca de Chaves (Ex: Diffie-Hellman). | Segurança na Comunicação de Rede. | 🚧 |

---

## 🐍 Tecnologias & Ferramentas

Os exemplos práticos são desenvolvidos principalmente em Python, utilizando bibliotecas robustas focadas em segurança:

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography.io-333333?style=for-the-badge&logo=python&logoColor=white)
![PyCryptodome](https://img.shields.io/badge/PyCryptodome-464646?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 🚀 Estrutura do Repositório

O conteúdo está organizado para facilitar o aprendizado sequencial:

```bash
CRYPTOGRAPHY/
├── 📂 01_simetrica/      # Implementações de AES (Ex: ECB, CBC)
├── 📂 02_assimetrica/    # Exemplos de RSA e ECC (Geração de Chaves)
├── 📂 03_funcoes_hash/   # Calculando e comparando hashes (SHA256, etc.)
├── 📂 04_assinaturas/    # Criando e verificando assinaturas digitais
├── 📂 05_protocolos/     # Exemplos conceituais de TLS/Handshake
├── 📓 README.md
└── 📜 requirements.txt
