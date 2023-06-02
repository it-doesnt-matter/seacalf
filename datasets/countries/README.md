# Countries

## translations
Not all translations are 100% complete!

Unlike the `name` property, you won't have a `short` and an `official` version. For each language, there's only one translation.

Translations into the following languages are available:
- AFR: Afrikaans
- AMH: Amharic
- ARA: Arabic
- AZE: Azerbaijani
- BEL: Belarusian
- BEN: Bengali
- BUL: Bulgarian
- CAT: Catalan
- CES: Czech
- CMN: Mandarin Chinese (available as simplified and traditional version)
- CYM: Welsh
- DAN: Danish
- DEU: German
- ELL: Greek
- ENG: English
- EST: Estonian
- FAO: Faroese
- FAS: Persian
- FIN: Finnish
- FRA: French
- GLE: Irish
- HEB: Hebrew
- HIN: Hindi
- HRV: Croatian
- HUN: Hungarian
- HYE: Armenian
- IND: Indonesian
- ISL: Icelandic
- ITA: Italian
- JPN: Japanese
- KAT: Georgian
- KHM: Khmer
- KOR: Korean
- LAO: Lao
- LAV: Latvian
- LIT: Lithuanian
- MKD: Macedonian
- MLT: Maltese
- MSA: Malay
- MYA: Burmese
- NEP: Nepali
- NLD: Dutch
- NOR: Norwegian
- POL: Polish
- POR: Portuguese
- ROH: Romansh
- RON: Romanian
- RUS: Russian
- SLK: Slovak
- SLV: Slovene
- SNA: Shona
- SPA: Spanish
- SQI: Albanian
- SRP: Serbian
- SWE: Swedish
- TAM: Tamil
- THA: Thai
- TIR: Tigrinya
- TUR: Turkish
- UKR: Ukrainian
- URD: Urdu
- VIE: Vietnamese

Source: [IP2Location](https://www.ip2location.com/free/country-multilingual)

## iso_n3
Even though the numeric ISO 3166-1 codes only contain digits, this is a string. This makes it possible to keep leading zeros.

Source: This data was scrapped from [Wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1). But originally comes from [ISO](https://www.iso.org/obp/ui/).

## largest_city
Source: This data was scrapped from each country's [Wikipedia](https://en.wikipedia.org/) page.

## capital
Source: This data was scrapped from each country's [Wikipedia](https://en.wikipedia.org/) page.

## currencies
To get more information about a certain currency, you can have a look at the Currency dataset.

Source: This data was scrapped from multiple different [Wikipedia](https://en.wikipedia.org/) pages.

## population
All the values are estimates for the 01.07.2023.

The numbers represent the amount of permanent residents. Non-permanent residents, like scientists or military personnel, are not included. This is for example the reason why Antarctica or the British Indian Ocean Territory have a population of 0.

Source: Most of the data was scrapped from [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)), bu originally comes from [UN's 2022 Revision of World Population Prospects](https://population.un.org/wpp/). If a country's population count wasn't listed on there, I took the data from the respective Wikipedia page.

## area
Micronesia, the United States Virgin Islands and Saint Martin had a water area of value "negligible" in the source dataset. Their water area and percentage is set to 0.

Source: This data was scrapped from [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area#cite_note-unstats21-4), but originally comes from [UN's demographic yearbook](https://unstats.un.org/unsd/demographic-social/products/dyb/documents/dyb2021/table03.pdf).

## calling_code
Antarctica's calling code in the dataset is set to `null`, because there's no region-wide telecommunication service. The research stations located in Antarctica are provided with telecommunication services by their parent country and thus also share the respective calling code.

Source: [Wikipedia](https://en.wikipedia.org/wiki/List_of_country_calling_codes).

## gdp
Source: Most of the data was scrapped from one of the following Wikipedia pages:
[nominal](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)), [nominal per capita](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita), [ppp](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)), [ppp per capita](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita). Originally the data comes from [IMF's World Economic Outlook Database](https://www.imf.org/en/Publications/WEO/weo-database/2023/April/). If a country's GDP wasn't listed on there, I took the data from the World Bank, the UN or the CIA, as long as the data wasn't too old (taken before 2020).

## driving side
Some unpopulated territories have a value of `null` is this field.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Left-_and_right-hand_traffic).

## gini
The `year` attribute was added because the year, in which the last estimate was made, varies greatly from country to country. This is important to keep in mind when comparing Gini coefficients of different countries.

Source: [World Bank](https://data.worldbank.org/indicator/SI.POV.GINI)

## hdi
Source: [UNDP](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI)

## gii
Source: [UNDP](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI)

## time_zone
Daylight saving time is not supported at the moment.

"Since Antarctica is largely uninhabited, the continent is not officially divided up into time zones. However, there are a number of research stations, each of which observes its own local time. Some stations use the time zone of the country that operates or supplies them, others observe the local time of countries nearby.

Palmer Station is a United States research station, but it keeps Chile Summer Time (CLST) as Chile is the closest country." - https://www.timeanddate.com/time/zone/antarctica

Source: [Wikipedia](https://en.wikipedia.org/wiki/List_of_time_zones_by_country)

## tld
Currently only latin-character ccTLDs are included. Internationalized ccTLDs might be added in the future.

Some countries have their own ccTLD but don't actually use it: .mf, .bl, .bv, .sj.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Country_code_top-level_domain)

## un
The possible values are the following:
- `member`: UN member state
- `observer`: UN General Assembly observer states
- `eligible`: eligible non-member states
- `nsgt`: non-self-governing territory
- `non-member`: not a member of the UN

"The member states of the Realm of Denmark, Realm of New Zealand and Kingdom of the Netherlands represent their metropolitan countries as well as their other constituent countries: Faroe Islands and Greenland (Denmark); Aruba, Curaçao and Sint Maarten (Netherlands); Niue and Cook Islands (New Zealand). Niue and the Cook Islands have full treaty-making capabilities and have the option of seeking membership."

Source: [UN](https://www.un.org/en/about-us/member-states)

## unm49
Taiwan isn't included in the UN geoscheme, but still has values assigned to the `main` and `sub` properties. The values used are the same that have been used by multiple other institutions, researches and projects, e.g. Unicode CLDR or Natural Earth.

Source: This data was scrapped from [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_the_United_Nations_geoscheme), but originally comes from the [UN](https://unstats.un.org/unsd/methodology/m49/).

## continent
This is a list due to the fact that some countries, like Cyprus or Turkey, lay on the border of two continents and thus are part of more than one continent.
Countries, that have some overseas territory in a different continent, usually don't have those additional continents included as their own, especially because most of those regions have their own entry in the dataset.

## languages
Multiple countries don't have an official language and have thus their de facto language listed instead. The following countries are concerned:
- Argentina
- Australia
- Bosnia and Herzegovina
- Japan
- Mexico
- Palestine
- Taiwan
- United Kingdom
- United States
- Uruguay

Source: [Wikipedia](https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory)

## nato
The possible values for `relations` are the following:
- `membership action plan`
- `enhanced opportunity partner`
- `individual partnership action plan`
- `partnership for peace`
- `mediterranean dialogue`
- `istanbul cooperation initiative`
- `global partner`

Source: [member countries](https://www.nato.int/cps/en/natohq/nato_countries.htm) and [partners](https://www.nato.int/cps/en/natohq/51288.htm)

## inflation
The data represents the annual headline consumer price inflation (annual average inflation).

Source: [World Bank](https://www.worldbank.org/en/research/brief/inflation-database)

## independence
Source: [Wikipedia](https://simple.wikipedia.org/wiki/Dependent_territory)

## centroid
Source: https://github.com/gavinr/world-countries-centroids

## land_borders
Source: [CIA World Factbook](https://www.cia.gov/the-world-factbook/field/land-boundaries/)

## gov_type
For explanations for each government type, have a look at the source.

Source: [CIA World Factbook](https://www.cia.gov/the-world-factbook/field/government-type/)

## coastline
I couldn't find any data about the length of the coastline of Ascension Island and thus the coastline of "Saint Helena, Ascension and Tristan da Cunha" is actually only the length of the coastlines of Saint Helena and Tristan da Cunha.

Saint Martin and Sint Maarten form one island. I couldn't find the coastline length of both individual countries, so both have instead the length of the whole island as value.

Source: [CIA World Factbook](https://www.cia.gov/the-world-factbook/field/coastline)

## is_landlocked
Source: [CIA World Factbook](https://www.cia.gov/the-world-factbook/field/coastline)

## arton
Here are some explications for the different attributes:
- `ms`: Mobility Score: "Passports accumulate points for each country that their holders can visit without a visa, or they can obtain a visa on arrival."
- `vf`: Visa-Free: "Permission from a foreign authority to enter a country is not required."
- `voa`: Visa on Arrival: "Permission from a foreign authority to enter a country is required but can be obtained on arrival."
- `eta`: Electronic Travel Authorization: "Requirement for foreign nationals traveling to a country where permission to enter is not required. It is a relatively new approach, widely used by the USA and Canada."
- `vr`: Visa Required: "Permission from a foreign authority to enter a country is required prior to travel."
- `ppr`: (global) Passport Power Rank: "Passports of the world are sorted by their total Mobility Score, which includes visa-free and visa on arrival privileges. The higher the MS score, the better global mobility its passport bearer enjoys."
- `ipr`: Individual Power Rank: "No two passports are alike, hence why share a rank? The 2016 edition of the Passport Index introduced a unique ranking system, where each passport occupies an individual rank, based on their individual country and visa characteristics."
- `wr`: World Reach stated as a percentage

Countries that are not included in the passport index, don't have their own passport. In most cases, those are dependent countries that use the same passport as their sovereign state. Residents of the Isle of Man use for example a variant of the British passport.

One exception is the Sahrawi Arab Democratic Republic that has its own passport, but is not listed on the index.

Source: [Passport Index](https://www.passportindex.org/)