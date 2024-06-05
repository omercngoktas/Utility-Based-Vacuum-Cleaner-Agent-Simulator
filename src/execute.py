import os

probabilities = [
    [0.3, 0.3, 0.3],
    [0.5, 0.2, 0.1],
    [0.2, 0.4, 0.2],
    [0.5, 0.1, 0.3],
    [0.5, 0.3, 0.8]
]

output_folder = "../output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i, probs in enumerate(probabilities):
    for j in range(1, 11):
        # Dosya isimleri
        agent_a_output = f"{output_folder}/a_{i+1}_{j}.txt"
        agent_b_output = f"{output_folder}/b_{i+1}_{j}.txt"

        # main.py dosyasını çalıştırma komutu
        command = f"python3 main.py {probs[0]} {probs[1]} {probs[2]} {agent_a_output} {agent_b_output}"

        # Komutu çalıştır
        os.system(command)
