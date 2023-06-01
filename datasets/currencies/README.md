# Currencies
Source: Most data for this dataset was scrapped from some [Wikipedia](https://en.wikipedia.org/) page.

## symbol
When it comes to singular and plural denominations, some currencies use the same symbol, while others use different ones. The euro for example uses the same symbol (€1 and €2), while the Swazi Lilangeni uses two different ones (L1 vs E2). Currently only the singular symbol is included in the dataset.

The Indian Paisa actually has a symbol, but it's not included in Unicode and thus the value is the dataset is `null`.

## subunit
In the dataset only a single subunit is listed for each currency. Some currencies have multiple subunits though, but in most cases only a single one is actively used. In some cases no subunits are used (anymore), even if a subunit is listed in the dataset.

## banknotes/coins
Only commonly circulating notes and coins are listed here. This means that there might be some denominations that are still considered legal tender, but which are not listed here, because they are practically never used. Some exmaples:

- USD bills of higher denominations, i.e. the $500, $1,000, $5,000 and $10,000 bills. Those banknotes have last been printed decades ago and are now worth more than their face value to collectors.
- A scenario that can be observed often is that due to inflation some banknotes'/coins' value is getting close to 0. This then results in them dissappearing from cirrculation while still being considered legal tender.

Commemorative notes/coins are not listed.