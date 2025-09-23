### Hexlet tests and linter status:
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=otfantik_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=otfantik_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=otfantik_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=otfantik_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=otfantik_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=otfantik_devops-engineer-from-scratch-project-49)
[![Actions Status](https://github.com/otfantik/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/otfantik/devops-engineer-from-scratch-project-49/actions)
Brain-calc - https://asciinema.org/a/vUAjViM5IjFJeJMRAQ6qRWhOI
Brain-prime - https://asciinema.org/a/KaAUpD529rW862etMG7B3g99A
Brain-progression -     https://asciinema.org/a/17U2shxi5gtNTQ6ZZIFe3olLF
Brain-gcd -      https://asciinema.org/a/nTICSf99D8cWtwd2CK0uhxSrs
Brain-even  -     https://asciinema.org/a/EZYRmBhlLdsyPCSODPDstZNp0
 
# Brain Games

Пять простых математических игр-задачек.

## Что тут есть

- **brain-even** - Угадай, четное число или нет
- **brain-calc** - Посчитай пример  
- **brain-gcd** - Найди общий делитель
- **brain-progression** - Дополни последовательность
- **brain-prime** - Простое число или нет

## Как поставить

```bash
# Скачать проект
git clone https://github.com/otfantik/devops-engineer-from-scratch-project-49.git
cd brain-games

# Поставить что нужно
uv sync
uv build
uv tool install dist/*.whl
# чтобы играть просто пиши 
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
# дерево
brain_games/
├── engine.py          # Главный движок
├── cli.py             # Общение с игроком
├── games/             # Сами игры
│   ├── even.py        # Четность
│   ├── calc.py        # Калькулятор
│   ├── gcd.py         # Делители
│   ├── prime.py       # Простые числа
│   └── progression.py # Последовательности
└── scripts/           # Запускалки
    ├── brain_even.py
    ├── brain_calc.py
    ├── brain_gcd.py
    ├── brain_prime.py
    └── brain_progression.py


