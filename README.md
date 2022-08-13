# POKEDOLAR
## Projeto para estudos da biblioteca do Python chamada Rocketry
Alternativa ao Contrab, APScheduler e Airflow com proposta de simplicidade, além dee sintaxe limpa para gerenciamento e agendamento de tarefas usando a linguagem Python.

Documentação Oficial:
[https://rocketry.readthedocs.io/en/stable/](https://rocketry.readthedocs.io/en/stable/)

# O projeto

POKEDOLAR consome duas APIs, a [Pokeapi](https://pokeapi.co/api/v2/pokemon) e a [Awesome API-BR](https://economia.awesomeapi.com.br/), pega e trata a cotação do dólar e vincula os 3 primeiros dígitos numéricos do valor a número de identificação referente ao Pokemon, na sequência baixa a imagem representativa do mesmo.

# TO DO

- [ ] Tratar exceções para problemas de conexão com as APIs
- [ ] Tratar exceções para cotação de dólar não encontrada
- [ ] Refatorar código com foco em qualidade e legibilidade
- [ ] Implementar integração com Telegram
- [ ] Implementar integração com Whatsapp usando [Wppconnect](https://github.com/wppconnect-team/wppconnect-server)

# Referências

[Como fazer agendamento de tarefas com Python e Rocketry | Live de Python #214](https://www.youtube.com/watch?v=eepX8Bb2BxI)

[Github Live de Python](https://github.com/dunossauro/live-de-python)

[Telegram Live de Python](https://t.me/livepython)

[Documentação Oficial](https://rocketry.readthedocs.io/en/stable/)
