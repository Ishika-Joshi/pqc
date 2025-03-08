step 1(key generation) -
python ./ntru.py -v gen 167 3 128 myKey.priv myKey.pub
step 2(encryption) -
python ./ntru.py enc myKey.pub.npz test.txt > encrypted_test.txt
step 3 (decryption) -
python ./ntru.py dec myKey.priv.npz encrypted_test.txt
