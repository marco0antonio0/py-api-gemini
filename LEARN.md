# Consulta IA Google Gemini

Este projeto fornece uma implementação básica de uma classe Python para interagir com a API do Google Gemini. A classe `ia_google` é projetada para realizar consultas na API de maneira organizada e eficiente.

## Funcionalidades

- **Consulta à API do Google Gemini**: A classe permite enviar solicitações à API para gerar histórias baseadas em entradas de texto.
- **Configuração de segurança**: Inclui configurações de segurança para filtrar conteúdo inapropriado.
- **Histórico de conversas**: Possibilidade de pré-carregar um histórico de conversas para manter o contexto.

## Exemplo de Uso

```Python
# Importando o package
from service_ia import ia_google

# Fazendo a instância e declarando a chave API key secreta necessária
instance = ia_google(api_key="sua_api_key_aqui")

# Realizando pergunta ao Gemini
# O parâmetro history é para pré-carregar um chat de conversas com o Gemini
res = instance.generate_story(history=[], text="Como ficar inteligente?")

# Exibindo a resposta obtida pelo Gemini
print(res)
```

## Instalação

Para utilizar a classe ia_google, você precisa instalar a biblioteca requests. Você pode instalar essa biblioteca utilizando o comando:

```Bash
pip install requests
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to open an issue or contact me at [marcomesquitajr@hotmail.com](mailto:marcomesquitajr@hotmail.com).
