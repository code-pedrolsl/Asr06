# ICE Middleware

Foi stendido o exemplo básico de middleware ICE (Internet Communications Engine)
adicionando dois novos métodos à interface `Printer`, além do método original `printString`.

## Métodos implementados

- `printString(string s)` — imprime a string e a retorna com `*` no final (original)
- `reverseString(string s)` — inverte a string e a retorna
- `isPalindrome(string s)` — verifica se a string é um palíndromo e retorna `true` ou `false`

## Arquivos

| Arquivo | Descrição |
|---|---|
| `Printer.ice` | Interface Slice com os três métodos |
| `server.py` | Servidor com um único objeto `SimplePrinter` |
| `client.py` | Cliente que se conecta e chama os três métodos |
| `server2.py` | Servidor com dois objetos (`SimplePrinter1` e `SimplePrinter2`) |
| `client2.py` | Cliente que se conecta aos dois objetos e chama os três métodos |

## Como executar

Gere o módulo Demo a partir da interface Slice:
```bash
slice2py Printer.ice
```

Em dois terminais separados:
```bash
# Terminal 1 - inicie o servidor
python3 server.py

# Terminal 2 - execute o cliente
python3 client.py
```

Para o exemplo com múltiplos objetos:
```bash
# Terminal 1
python3 server2.py

# Terminal 2
python3 client2.py
```
