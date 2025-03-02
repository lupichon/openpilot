import sys
import time


LX, LY, RX, RY, LT, RT = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

print("Receiver en attente de données...")

def update_values(data):
    global LX, LY, RX, RY, LT, RT
    try:
        values = list(map(float, data.split()))
        if len(values) == 6:
            LX, LY, RX, RY, LT, RT = values
            print(f"Mis à jour : LX={LX}, LY={LY}, RX={RX}, RY={RY}, LT={LT}, RT={RT}")
        else:
            print(f"Erreur : Données incorrectes reçues -> {data}")

    except (ValueError, KeyError) as e:
        print(f"Erreur de parsing : {e}")

def start_receiver():
    print("Receiver en attente de données...")
    try:
        while True:
            data = sys.stdin.readline().strip()
            if data == "STOP":
                print("Commande d'arrêt reçue, arrêt du receiver.")
                break
            update_values(data)
            time.sleep(0.01)
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    start_receiver()


