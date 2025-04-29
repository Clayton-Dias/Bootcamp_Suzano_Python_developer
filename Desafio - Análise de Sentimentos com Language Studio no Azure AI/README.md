# Azure Speech Studio e Language Studio - Prática e Anotações

Este repositório contém a documentação, anotações e capturas de tela do laboratório prático utilizando as ferramentas **Azure Speech Studio** e **Azure Language Studio**.

## 🎯 Objetivo
Desenvolver habilidades práticas na criação de soluções baseadas em inteligência artificial voltadas para **voz** e **linguagem natural**, conforme o laboratório proposto.

## 🔗 Links dos Laboratórios Oficiais
- [Speech Service (Reconhecimento de Fala)](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/09-speech.html)
- [Text Analysis (Análise de Linguagem)](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/06-text-analysis.html)

## 🛠️ Tecnologias Utilizadas
- Azure Speech Studio
- Azure Language Studio
- Portal Azure
- GitHub

## 📋 Passo a Passo Realizado

### 1. Speech Studio - Serviço de Fala

- Criado um recurso de **Speech** no Azure Portal.
- Configurado o **Speech Studio** para:
  - **Reconhecimento de Fala**: transformar voz em texto.
  - **Conversão de Texto em Fala** (Text-to-Speech).
  - Testes práticos com arquivos de áudio personalizados.

#### Insights:
- O serviço reconheceu automaticamente diferentes sotaques.
- É possível treinar modelos personalizados para vocabulários específicos.

> 🔥 **Dica**: Ao utilizar arquivos .wav, garanta que estejam no formato PCM linear.

### 2. Language Studio - Serviço de Análise de Texto

- Criado recurso de **Cognitive Services** no Azure.
- Utilizado o **Language Studio** para:
  - **Análise de Sentimento** de textos.
  - **Extração de Entidades Nomeadas** (NER - Named Entity Recognition).
  - **Detecção de Idioma** automática.

#### Insights:
- O modelo de Análise de Sentimento é surpreendentemente preciso para textos em português.
- A ferramenta de entidades é excelente para extração automática de dados de documentos.

## 📸 Capturas de Tela
As capturas de tela da execução dos laboratórios estão armazenadas na pasta [/images](./images).

- Configuração de Recursos no Azure
- Demonstração de Transcrição de Áudio
- Resultados da Análise de Sentimento

## 🧠 Aprendizados

- Conhecimento prático de como **voz** e **linguagem natural** são processados por IA na nuvem.
- Importância da escolha correta do formato de dados de entrada (áudio/texto).
- Entendimento de que é possível personalizar modelos para melhorar a acurácia para casos de uso específicos.

## 🚀 Próximos Passos

- Explorar a criação de **Modelos Customizados de Fala**.
- Integrar APIs de fala e linguagem em aplicativos web e móveis.
- Estudar mais sobre os limites gratuitos e otimização de custos no Azure.

---

## 📚 Referências
- [Documentação do Azure Speech](https://learn.microsoft.com/pt-br/azure/ai-services/speech-service/)
- [Documentação do Azure Language](https://learn.microsoft.com/pt-br/azure/ai-services/language-service/)

---

