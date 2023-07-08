import subprocess

# Lista de notebooks a serem executados
notebooks = [f'Scripts\\webscraping_flashScore.py',f'Scripts\\backDraw.py',f'Scripts\\btts_nao.py',f'Scripts\\btts_sim.py',f'Scripts\\Metodo_25.py' ]

for notebook in notebooks:
    
    # Executa o script Python
    subprocess.run(['python', notebook], check=True)
