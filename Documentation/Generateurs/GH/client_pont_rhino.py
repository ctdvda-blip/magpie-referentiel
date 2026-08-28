# -*- coding: utf-8 -*-
"""Client direct du pont rhinomcp (TCP 127.0.0.1:1999)."""
import socket
import json
import sys
import io

NL = chr(10)


def call(typ, params=None, timeout=900):
    s = socket.create_connection(("127.0.0.1", 1999), timeout=timeout)
    try:
        s.sendall(json.dumps({"type": typ, "params": params or {}}).encode("utf-8"))
        s.settimeout(timeout)
        buf = b""
        while True:
            try:
                d = s.recv(1 << 16)
            except socket.timeout:
                break
            if not d:
                break
            buf += d
            try:
                return json.loads(buf.decode("utf-8"))
            except Exception:
                continue
        return {"status": "error", "message": "reponse illisible",
                "raw": buf[:2000].decode("utf-8", "replace")}
    finally:
        s.close()


def py(code, timeout=900):
    return call("execute_rhinoscript_python_code", {"code": code}, timeout)


def _nettoyer(out):
    lignes = [l.rstrip() for l in out.split(NL)]
    # le pont renvoie parfois la sortie en double : on coupe si les deux
    # moities sont identiques
    n = len(lignes)
    if n > 5 and n % 2 == 0 and lignes[:n // 2] == lignes[n // 2:]:
        lignes = lignes[:n // 2]
    propre, prec = [], None
    for l in lignes:
        if l == "" and prec == "":
            continue
        propre.append(l)
        prec = l
    return NL.join(propre)


if __name__ == "__main__":
    code = io.open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else "print(6*7)"
    r = py(code)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if r.get("status") != "success":
        print("ERREUR PONT : " + json.dumps(r, ensure_ascii=False)[:1500])
        sys.exit(1)
    res = r.get("result", {})
    print(_nettoyer(res.get("output", "")))
    if not res.get("success", True):
        print("[!] execution signalee en echec")
