# imgapi
API de cadastro e analise de imagem (Django/Docker)


docker-compose up --build


http://localhost:8000/imagem/
CRUD Imagem
- nome_imagem
- tipo_imagem

http://localhost:8000/analise/
CRUD Analise
OBs:. Quando salva, retorna todas as analises da imagem utilizada + o POST atual.
- 
http://localhost:8000/imagem-analise/
Lista todas as analises relacionadas a uma imagem especifica.

EXTRA:
http://localhost:8000/analise-imagem/
Lista todas as analises em ordem de id das imagens.
