import socket, sys


def main(port=5000):
    with socket.socket() as sock:
        print('Startning a server on port {port}')
        sock.bind(('', port))
        sock.listen(1)

        while True:
            conn, address = sock.accept()
            print(f'Connected by {address}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            print('Closing the connection...')
            conn.close()


if __name__ == '__main__':
    port = sys.argv[-1]
    if port:
        port = int(port)
    main(port)
