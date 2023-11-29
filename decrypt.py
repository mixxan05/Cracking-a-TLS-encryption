import subprocess

# TLS-V1.0 verschlüsselte Daten (ersetzen Sie dies durch die tatsächlichen Daten)
tls_v1_data = "TLS-V1.0 verschlüsselte Daten"

# Wandeln Sie die verschlüsselten Daten in Base64-URL-safety-Kodierung um
base64_url_safety_encoded_data = subprocess.check_output(['echo', '-n', tls_v1_data, '|', 'base64', '-w', '0', '-'])

# Dekodieren Sie die verschlüsselten Daten mithilfe von OpenSSL
decrypted_data = subprocess.check_output(['echo', '-n', base64_url_safety_encoded_data, '|', 'base64', '-d', '|', 'openssl', 'rsautl', '-decrypt', '-inkey', 'privkey.pem'])

# Wandeln Sie die entschlüsselten Daten in eine lesbare Zeichenkette um
print(decrypted_data.decode('utf-8'))
