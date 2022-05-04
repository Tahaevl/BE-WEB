import hashlib
mdp='aubrun'
mdp=hashlib.sha256(mdp.encode())
mdpC=mdp.hexdigest()
print(mdpC)
