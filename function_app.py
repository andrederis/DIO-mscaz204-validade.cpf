import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def _somente_digitos(s: str) -> str:
    return ''.join(ch for ch in s if ch.isdigit())

def _cpf_valido(cpf: str) -> bool:
    cpf = _somente_digitos(cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    # 1º dígito
    soma = sum(int(d)*w for d, w in zip(cpf[:9], range(10, 1, -1)))
    d1 = (soma * 10) % 11
    d1 = 0 if d1 == 10 else d1
    # 2º dígito
    soma = sum(int(d)*w for d, w in zip(cpf[:9] + str(d1), range(11, 1, -1)))
    d2 = (soma * 10) % 11
    d2 = 0 if d2 == 10 else d2
    return cpf[-2:] == f"{d1}{d2}"

@app.route(route="validate-cpf", methods=["GET", "POST"])
def validate_cpf(req: func.HttpRequest) -> func.HttpResponse:
    cpf = req.params.get("cpf")
    if not cpf and req.method == "POST":
        try:
            data = req.get_json()
            cpf = data.get("cpf")
        except Exception:
            pass

    if not cpf:
        return func.HttpResponse(
            '{"ok": false, "error": "Parâmetro cpf é obrigatório"}',
            mimetype="application/json",
            status_code=400,
        )

    ok = _cpf_valido(cpf)
    return func.HttpResponse(
        f'{{"ok": {str(ok).lower()}, "cpf": "{cpf}"}}',
        mimetype="application/json",
        status_code=200,
    )
