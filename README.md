# wowSales

## About
Projeto executado em Python com o objetivo de filtrar, limpar e selecionar dados de compra e venda do jogo World of Warcraft, salvos em `.csv` pelo addon [TradeSkillMaster](https://www.tradeskillmaster.com/), para, então, executar uma análise de Business Intelligence a fim de escolher uma profissão capaz de gerar mais lucros dentro do jogo.

Meu objetivo nesse projeto foi estudar e praticar a linguagem Python. Mais informações sobre o projeto encontram-se no [meu portfólio](https://hugobrancowb.github.io/).

## Running
Put the `.csv` files exported by [TradeSkillMaster](https://www.tradeskillmaster.com/) addon inside `data` folder and follow the instructions.

### Options
```
$ python wowsales.py

1. Update sales data.
2. Plot data.
3. Print sales record.
4. Delete existing data.
5. Income report for each month.

0. Exit.
```

Option | Description
--- | --- 
**1** | Imports all data from `data` folder and also saves it as a `.json` file. If there's a `.json` file already, the program doesn't need to import data again.
**2** | Plots: income vs. outcome of gold from each day through the year; balance (income - outcome) from each day through the year; cumulative gold over time (liquid profit).
**3** | Simply prints on the screen all sales and purchases made through the entire year.
**4** | Deletes all previously imported data.
**5** | Shows most profitable products sold and its respectively income for each month of 2019. Also, optionally shows most expenseful items bought through the year.
**0** | Closes app.

#### Plots from option 2
![Income vs. Outcome of gold from each day through the year.](https://github.com/hugobrancowb/wowSales2019/blob/master/plots/Figure_1.png)

![Balance (income - outcome) from each day through the year.](https://github.com/hugobrancowb/wowSales2019/blob/master/plots/Figure_2.png)

![Cumulative gold over time (liquid profit).](https://github.com/hugobrancowb/wowSales2019/blob/master/plots/Figure_3.png)

## Keywords
Python, Business Intelligence, World of Warcraft, TradeSkill Master
