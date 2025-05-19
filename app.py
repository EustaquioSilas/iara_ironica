{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyM0ZDXhLxZYHR6pYkpw2YQQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/EustaquioSilas/iara_ironica/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GNAUF_9d64WX",
        "outputId": "d0ac0645-b3c3-454d-8f83-4b0852023095"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: google-genai in /usr/local/lib/python3.11/dist-packages (1.15.0)\n",
            "Requirement already satisfied: anyio<5.0.0,>=4.8.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (4.9.0)\n",
            "Requirement already satisfied: google-auth<3.0.0,>=2.14.1 in /usr/local/lib/python3.11/dist-packages (from google-genai) (2.38.0)\n",
            "Requirement already satisfied: httpx<1.0.0,>=0.28.1 in /usr/local/lib/python3.11/dist-packages (from google-genai) (0.28.1)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (2.11.4)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.28.1 in /usr/local/lib/python3.11/dist-packages (from google-genai) (2.32.3)\n",
            "Requirement already satisfied: websockets<15.1.0,>=13.0.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (15.0.1)\n",
            "Requirement already satisfied: typing-extensions<5.0.0,>=4.11.0 in /usr/local/lib/python3.11/dist-packages (from google-genai) (4.13.2)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.11/dist-packages (from anyio<5.0.0,>=4.8.0->google-genai) (3.10)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio<5.0.0,>=4.8.0->google-genai) (1.3.1)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (5.5.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.11/dist-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (0.4.2)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.11/dist-packages (from google-auth<3.0.0,>=2.14.1->google-genai) (4.9.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1.0.0,>=0.28.1->google-genai) (2025.4.26)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1.0.0,>=0.28.1->google-genai) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1.0.0,>=0.28.1->google-genai) (0.16.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (2.33.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.0.0->google-genai) (0.4.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.28.1->google-genai) (3.4.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.28.1->google-genai) (2.4.0)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in /usr/local/lib/python3.11/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.14.1->google-genai) (0.6.1)\n"
          ]
        }
      ],
      "source": [
        "!pip install google-genai"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from google.colab import userdata\n",
        "\n",
        "os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')"
      ],
      "metadata": {
        "id": "uU3ijAtZ87Bz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google import genai\n",
        "\n",
        "client = genai.Client()"
      ],
      "metadata": {
        "id": "Qxj2i-O490Pa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for model in client.models.list():\n",
        "    print(model.name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PKCKHu4W-hOh",
        "outputId": "f6977ce3-a8d8-4d97-8491-994fb36c971c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "models/embedding-gecko-001\n",
            "models/gemini-1.0-pro-vision-latest\n",
            "models/gemini-pro-vision\n",
            "models/gemini-1.5-pro-latest\n",
            "models/gemini-1.5-pro-001\n",
            "models/gemini-1.5-pro-002\n",
            "models/gemini-1.5-pro\n",
            "models/gemini-1.5-flash-latest\n",
            "models/gemini-1.5-flash-001\n",
            "models/gemini-1.5-flash-001-tuning\n",
            "models/gemini-1.5-flash\n",
            "models/gemini-1.5-flash-002\n",
            "models/gemini-1.5-flash-8b\n",
            "models/gemini-1.5-flash-8b-001\n",
            "models/gemini-1.5-flash-8b-latest\n",
            "models/gemini-1.5-flash-8b-exp-0827\n",
            "models/gemini-1.5-flash-8b-exp-0924\n",
            "models/gemini-2.5-pro-exp-03-25\n",
            "models/gemini-2.5-pro-preview-03-25\n",
            "models/gemini-2.5-flash-preview-04-17\n",
            "models/gemini-2.5-flash-preview-04-17-thinking\n",
            "models/gemini-2.5-pro-preview-05-06\n",
            "models/gemini-2.0-flash-exp\n",
            "models/gemini-2.0-flash\n",
            "models/gemini-2.0-flash-001\n",
            "models/gemini-2.0-flash-exp-image-generation\n",
            "models/gemini-2.0-flash-lite-001\n",
            "models/gemini-2.0-flash-lite\n",
            "models/gemini-2.0-flash-preview-image-generation\n",
            "models/gemini-2.0-flash-lite-preview-02-05\n",
            "models/gemini-2.0-flash-lite-preview\n",
            "models/gemini-2.0-pro-exp\n",
            "models/gemini-2.0-pro-exp-02-05\n",
            "models/gemini-exp-1206\n",
            "models/gemini-2.0-flash-thinking-exp-01-21\n",
            "models/gemini-2.0-flash-thinking-exp\n",
            "models/gemini-2.0-flash-thinking-exp-1219\n",
            "models/learnlm-2.0-flash-experimental\n",
            "models/gemma-3-1b-it\n",
            "models/gemma-3-4b-it\n",
            "models/gemma-3-12b-it\n",
            "models/gemma-3-27b-it\n",
            "models/embedding-001\n",
            "models/text-embedding-004\n",
            "models/gemini-embedding-exp-03-07\n",
            "models/gemini-embedding-exp\n",
            "models/aqa\n",
            "models/imagen-3.0-generate-002\n",
            "models/gemini-2.0-flash-live-001\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "modelo = \"gemini-2.0-flash\"\n",
        "\n",
        "resposta = client.models.generate_content(model=modelo,\n",
        "                                          contents='Quem é a empresa por trás dos modoles Gemini?')"
      ],
      "metadata": {
        "id": "HFy944Fo_avX"
      },
      "execution_count": 121,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "resposta.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "8PwwkQOBA34D",
        "outputId": "075a9096-e2fa-4d1b-d6b2-f7715cad9f13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'A empresa por trás dos modelos Gemini é o **Google**, através da sua unidade **Google DeepMind**.\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chat = client.chats.create(model=modelo)\n",
        "\n",
        "resposta = chat.send_message('oi tudo bem?')\n",
        "\n",
        "resposta.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "8MC8fbT0FUWu",
        "outputId": "4534a345-9c30-4ff0-9a7d-4333badedd3f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Olá! Tudo bem por aqui, obrigado por perguntar. E com você? 😊\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "resposta = chat.send_message('Você é uma assisnten pessoal e você sempre resposnde de forma sucinta. O que é inteligencia artificial?')\n",
        "\n",
        "resposta.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "dDiRwPUlGQG0",
        "outputId": "5b03b96a-aaed-4748-c66a-b419a8b608a6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Inteligência Artificial (IA) é a capacidade de máquinas imitarem a inteligência humana para realizar tarefas. Usa aprendizado de máquina e algoritmos para analisar dados e tomar decisões.\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.genai import types\n",
        "\n",
        "chat_config = types.GenerateContentConfig(\n",
        "    system_instruction = \"Você é uma assistente pessoal e você sempre responde de forma sucinta.\",\n",
        ")\n",
        "\n",
        "chat = client.chats.create(model=modelo, config=chat_config)"
      ],
      "metadata": {
        "id": "YfPveobBG3GX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "resposta = chat.send_message('o que é computaçao quantica?')\n",
        "\n",
        "resposta.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "BYYTcffsIKfZ",
        "outputId": "3c88fb36-6f1c-4a88-81f4-d51bbf99ffed"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Computação quântica é um paradigma de computação que usa fenômenos da mecânica quântica, como superposição e entrelaçamento, para realizar operações.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prompt = input(\"Oi, em que posso te ajudar? \")\n",
        "\n",
        "while prompt != \"não\":\n",
        "    resposta = chat.send_message(prompt)\n",
        "    print(\"Resposta: \", resposta.text)\n",
        "    print(\"\\n\")\n",
        "    prompt = input(\"Posso te ajudar com mais algo? \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4xOFxPqDJK9V",
        "outputId": "ebfaaa6e-c32a-411b-9e7f-d4b7c0fca2ce"
      },
      "execution_count": 120,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Oi, em que posso te ajudar? não\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chat_config_2 = types.GenerateContentConfig(\n",
        "    system_instruction = \"Você é uma Psicóloga Sincera feminina chamada Iara Irônica{A Pisicologa Sincera}, que antes de inciar qualquer conversa na primeira resposta você se apresenta pelo nome e desejando um bom dia, boa tarde ou boa noite levando em consideração o Fuso horário em: Manaus, AM - Brasil, Nas perguntas seguintes vai direto para respostas.Com um humor afiado e sagacidade cabocla, você tem um tom de repostas, ácidas, sarcastica e irônicas, sem rodeios, de forma curta, sucinta e direta. Usando sempre que poder termos do jeito Amazonês de falar como, mano, mana, manazinha, tu é leso é! ... entre outros\",\n",
        ")\n",
        "\n",
        "chat_2 = client.chats.create(model=modelo, config=chat_config_2)"
      ],
      "metadata": {
        "id": "5EF0rII-O-et"
      },
      "execution_count": 124,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "prompt = input(\"Como posso de ajudar hoje? \")\n",
        "\n",
        "while prompt != \"não\":\n",
        "    resposta = chat_2.send_message(prompt)\n",
        "    print(\"Resposta: \", resposta.text)\n",
        "    print(\"\\n\")\n",
        "    prompt = input(\"Posso te ajudar com mais algo? \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WBUSB6xcTI2z",
        "outputId": "4c426ba1-b37f-42fb-c46d-e4a94e70d555"
      },
      "execution_count": 127,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Como posso de ajudar hoje? não\n"
          ]
        }
      ]
    }
  ]
}