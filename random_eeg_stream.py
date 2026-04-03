import numpy as np
import time

# Configurazione dei parametri
n_canali = 64
sfreq = 256  # Hz
durata_secondi = 10
probabilita_rumore = 0.02  # 2% di probabilità che ogni campione sia "sporco"

print(f"Avvio stream EEG fittizio ({n_canali} canali, {sfreq} Hz) con artefatti casuali...")

try:
    for t in range(durata_secondi * sfreq):
        # 1. Generazione del segnale di base (rumore bianco standard ~15 µV)
        campione = np.random.normal(0, 15, size=n_canali)
        
        # 2. Inserimento intermittente di rumore/artefatti
        stringa_info = ""
        if np.random.random() < probabilita_rumore:
            # Scegliamo un tipo di rumore a caso
            tipo = np.random.choice(['spike', 'burst'])
            
            if tipo == 'spike':
                # Simula un ammiccamento o un movimento (picco di tensione)
                campione += np.random.uniform(150, 300, size=n_canali)
                stringa_info = " <-- [ARTEFATTO: PICCO]"
            else:
                # Simula un'interferenza ad alta frequenza o contrazione muscolare
                campione += np.random.normal(0, 100, size=n_canali)
                stringa_info = " <-- [ARTEFATTO: RUMORE ALTO]"

        # Visualizzazione (primi 5 canali)
        timestamp = t / sfreq
        valori_formattati = [f"{v:6.2f}" for v in campione[:5]]
        print(f"Sec: {timestamp:.3f}s | Canali 1-5 (µV): {valori_formattati} {stringa_info}", end="\r")
        
        # Timing per mantenere i 256 Hz
        time.sleep(1 / sfreq)

except KeyboardInterrupt:
    print("\n\nStream interrotto dall'utente.")

print("\nSimulazione terminata.")
