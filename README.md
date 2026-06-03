<h1 align="center">Gyron</h1>

<p align="center">
An async framework for building powerful bots for Bale Messenger.
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/Gyron">
  <img src="https://img.shields.io/pypi/pyversions/Gyron">
  <img src="https://img.shields.io/github/license/YasinOliayi/Gyron">
</p>

---

# Features

- Fully Async
- Webhook Support
- Long Polling
- Filters System
- FSM / States
- Models
- Fast & Lightweight
- Easy to Use

---

# Installation

```bash
pip install Gyron
```

---

# Quick Start

```python
from Gyron.bot import BotClient

bot = BotClient("TOKEN")


@bot.on_update()
async def start(message):

    await message.reply("Hello from Gyron!")


bot.run()
```

---

# Filters

```python
from Gyron.filters import Filters


@bot.on_update(Filters.text())
async def text_handler(message):

    print(message.text)
```

---

# Webhook

```python
bot = BotClient("TOKEN")

bot.run(path = "/webhk"
    host="0.0.0.0",
    port=8000
)
```

---

# Links

- PyPI: https://pypi.org/project/Gyron/
- GitHub: https://github.com/YasinOliayi/Gyron

---

# License

MIT License
