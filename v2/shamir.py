import sharing

res = sharing.PlaintextToHexSecretSharer.split_secret("this is a test", 3, 6)
print res

ret = sharing.PlaintextToHexSecretSharer.recover_secret(res[0:3])
print ret

#sudo pip install utilitybelt
