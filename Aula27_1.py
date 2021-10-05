logged_user = False
"""
if logged_user:
    msg = 'Usuário logado.'
else:
    msg - 'Usuário precisa logar.'
"""
msg = 'Usuário logado.' if logger_user else 'Usuário precisa logar.'

print(msg)
