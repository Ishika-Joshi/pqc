step 1(key generation) -
python ./ntru.py -v gen 167 3 128 myKey.priv myKey.pub
step 2(encryption) -
python ./ntru.py -b enc myKey.pub.npz test.txt > encrypted_test.txt
step 3 (decryption) -
python ./ntru.py -b dec myKey.priv.npz encrypted_test.txt
