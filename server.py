import paramiko
import threading

PHONES = [
    # Pro tip: don't use the address 192.168.0.1
    "192.168.0.2",
    "192.168.0.5",
    "192.168.0.6",
    "192.168.0.7",
    "192.168.0.8",
]

class PhoneThread (threading.Thread):
    def __init__(self, phone_index, application, args):
        self.phone_index = phone_index
        self.application = application
        self.args = args
        super().__init__()

    def run(self):
        print(f"Starting {PHONES[self.phone_index]}")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(f"{PHONES[self.phone_index]}", port=2222, pkey=paramiko.Ed25519Key.from_private_key_file(open('.pkey').read()))
        arg_string = ' '.join(map(lambda arg: f'"{arg}"', self.args))
        _, out, _ = ssh.exec_command(f"su -c './{self.application}_client {arg_string}'")

        print(f"Ending {PHONES[self.phone_index]}")
        return out
