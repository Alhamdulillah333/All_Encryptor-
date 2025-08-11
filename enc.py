import os,marshal
os.system("cls" if os.name == "nt" else "clear")

print("""      \033[93m███╗   ██╗██╗  ██╗   ██████╗ ██╗   ██╗
      \033[94m████╗  ██║██║  ██║   ██╔══██╗╚██╗ ██╔╝
      \033[92m██╔██╗ ██║███████║   ██████╔╝ ╚████╔╝
      \033[96m██║╚██╗██║██╔══██║   ██╔═══╝   ╚██╔╝
      \033[91m██║ ╚████║██║  ██║██╗██║        ██║
      \033[95m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝
\033[1;32m          🔒 PYTHON CODE ENCRYPTOR 🔒\033[0m
\033[1;31m══════════════════════════════════════════════════
\033[1;33m[√] Tool Name    : Py Encryptor
[√] Developed By : Dark-NH
[√] GitHub       : github.com/DarkNH-cyber
[√] Version      : 2.0.0
[√] Status       : ONLINE
\033[1;31m══════════════════════════════════════════════════
\033[1;36m[!] Secure your Python source code with marshal encryption.
[!] Advanced bytecode obfuscation using marshal — hides real source from reverse-engineers.
\033[1;34m≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠
""")

inp = input("\033[1;32mEnter File Path: \033[0m")
out = input("\033[1;32mFile Output Name: \033[0m")

f = open(inp, "r", encoding="utf-8")
f = f.read()

comp = compile(f, " ", "exec")
com = marshal.dumps(comp)

new = open(out, "w", encoding="utf-8")
new.write(f"import marshal\nexec(marshal.loads({repr(com)}))")

print(f"\n\033[1;36m[+] Encryption file saved as: {out}")