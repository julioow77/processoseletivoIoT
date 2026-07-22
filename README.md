# Processo Seletivo – Intensivo Maker | IoT   

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais
 
#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os 
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

### Identificação do Candidato

- **Nome completo:** Júlio César Mendes do Nascimento
- **GitHub:** https://github.com/julioow77

---

## Visão Geral da Solução

- **Projeto desenvolvido:** Monitor de Estoque Kanban Inteligente

- **Objetivo:** Implementar um sistema automatizado para monitoramento de estoque baseado no método Kanban, acompanhando o peso e a disponibilidade dos itens de forma contínua e em tempo real.
- **O que faz:** O firmware coleta dados de peso de uma célula de carga através de um conversor HX711, processa as leituras para evitar falsos positivos (glitches) e classifica o status do estoque em quatro estados principais: Regular, Alerta de Reposição, Carga Cheia ou Erro Crítico.
- **Interação do usuário:** O sistema opera de forma autônoma. O usuário (ou sistema superior) interage através da leitura do log no monitor serial, que emite de maneira clara e exata os status do estoque a cada 500 milissegundos.

---

## Arquitetura do Sistema Embarcado

- **Fluxo principal (`main.py`):** O sistema inicializa a classe customizada de comunicação com o HX711, emite a inicialização do Kanban e entra em um loop contínuo de avaliação. 
- **Estrutura de estados e temporização:** O projeto baseia-se em uma máquina de estados conduzida por um loop `while True`. Foi implementada uma temporização não-bloqueante com `time.ticks_ms()` e `time.ticks_diff()`, operando em intervalos rígidos de 500ms para manter a leitura contínua sem travar a CPU principal. 
- **Interação entre componentes:** O ESP32 realiza a leitura dos dados do HX711 via protocolo síncrono (bit-banging). Ao receber os dados brutos, aplica um fator de calibração (`/420`) para converter em gramas e toma as decisões de log (estado) baseadas nas faixas de peso (limiares de 150g, 5000g e zero absoluto).

---

## Componentes Utilizados na Simulação

Os componentes mapeados e interligados no arquivo `diagram.json` incluem:

- **Microcontrolador (ESP32):** Cérebro do sistema, encarregado de rodar o interpretador MicroPython, orquestrar os loops de leitura e processar as lógicas condicionais.
- **Sensor (Módulo HX711):** Amplificador e conversor Analógico-Digital (ADC) de 24 bits. Serve como ponte entre o ESP32 e as grandezas físicas (simuladas) da célula de carga virtual. Pinos configurados em DT=21, SCK=22, VCC=5V e GND=GND.1.

---

## Decisões Técnicas Relevantes

Para estabilizar as leituras e aprovar o código contra a automação de testes do GitHub Actions (Wokwi CLI), aplicou-se:

- **Proteção de interrupções (`disable_irq`):** Durante a captura sensível (leitura de 24 bits do pino), as interrupções globais são temporariamente desativadas. Isso evita que processamentos de fundo corrompam a leitura estrita do bit-banging, prevenindo timeouts por perda de sincronia.
- **Filtro de Debounce:** Durante grandes saltos de massa no simulador, leituras "fantasmas" de zero podiam ocorrer. Foi implementada uma variável `contagem_zero` que exige, no mínimo, duas leituras de erro consecutivas (1 segundo) para acionar um alerta crítico, mascarando oscilações espúrias.
- **Formatação exata (String Matching):** Toda a saída do console (os logs no monitor serial) foi formatada de forma rigorosa para refletir exatamente o que os testes automatizados da integração contínua (CI) esperavam, garantindo o sucesso das Actions.

---

## Resultados Obtidos

- **O que funciona:** A leitura contínua, detecção de consumo regular dinâmico, identificação rápida de reposição e proteção contra remoção acidental da caixa.
- **Requisitos atendidos:** O firmware respeitou a arquitetura não-bloqueante exigida, operando de forma perfeitamente assíncrona. As saídas de serial estão milimetricamente alinhadas com as mensagens estabelecidas pelo protocolo do projeto.
- **Resultados na simulação (Wokwi CI):** O código atingiu 100% de sucesso na esteira de integração contínua, com aprovação irrestrita nos três cenários de teste ("Consumo Parcial", "Ciclo Completo" e "Falha Crítica").

---

## Comentários Adicionais (Opcional)

- **Dificuldades encontradas:** Compreender o comportamento de transição do peso no ambiente virtualizado, que gera um intervalo minúsculo de "falha" passível de derrubar o sistema se não houver um filtro de ruídos bem feito na lógica. Adequar-se aos tempos de Timeout do Wokwi-CLI também exigiu análise minuciosa dos logs.
- **Principais aprendizados:** A consolidação do uso de temporizadores não-bloqueantes (`ticks_ms`) em vez de atrasos fixos (`sleep()`) e a manipulação direta do estado de interrupção da placa (hardware puro) pelo MicroPython.

---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
