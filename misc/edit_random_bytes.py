import hashlib
import secrets
import sys

def get_sha256_hash(nnue_filename):
    with open(nnue_filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def random_non_functional_edit(nnue_filename):
    with open(nnue_filename, "r+b") as f:
        f.seek(33) # the
        f.write(secrets.token_bytes(3))
        f.seek(79) # trainer
        f.write(secrets.token_bytes(7))

if len(sys.argv) != 2:
    print('Usage: ./test.py <nnue_filename>')
    sys.exit(0)
nnue_filename = sys.argv[1]
num_tries = 0
sha256 = ''
print(f'Modifying {nnue_filename}')
while not sha256.startswith('1337'):
    random_non_functional_edit(nnue_filename)
    sha256 = get_sha256_hash(nnue_filename)
    num_tries += 1
    if num_tries % 100 == 0:
        print(f'Tried {num_tries} times')

print(f'{sha256} after {num_tries}')
