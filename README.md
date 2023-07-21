# SEACALF

## Introduction
The SEACALF repository is a collection of datasets, which currently contains the following:
- [Countries](#countries)
- [UK](#uk)
- [US States](#us_states)
- [Currencies](#currencies)
- [Flags](#flags)
- [GeoJson](#geojson)
- [Passports](#passports)

In case that you want to use any data from this repository in one of your own projects, it's highly recommended that you also take a look at the documentation of the respective dataset. There you'll be able to find further details, exceptions to look out for, the sources, etc.

### Countries
This dataset contains a list of all countries, dependent territories and special areas of geographical interest, which are included in ISO 3166-1. The key of each entry is the respective ISO 3166-1 Alpha-3 code.

Available formats: JSON, YAML, XML and CSV.

Throughout the rest of this README, I will use the term "country" to describe an entity from ISO 3166-1, even though not all of these entities are actually countries.

England, Scotland, Northern Ireland and Wales are not part of this dataset, as ISO 3166-1 only includes the United Kingdom as a whole. If you need information about the constituent countries of the UK, you can use the [UK dataset](#uk).

Each entry has the following properties:
- `name`
  - `short`: short, English name
  - `official`: official, English name
- `translations`: list of translations in 63 different languages (see the respective README for a list of available languages)
- `iso`: ISO 3166-1 codes
  - `a2`: ISO 3166-1 two-letter code
  - `a3`: ISO 3166-1 three-letter code
  - `n3`: ISO 3166-1 three-digit code
- `largest_city`: largest city by population
- `capital`
- `currencies`: list of official currencies
	- `iso_a3`: ISO 4217 code of the currency
	- `name`: name of the currency
- `population`
- `area`
	- `total`: total area, i.e. land plus water area, in square meter
	- `land`: land area in square meter
	- `water`: water area in square meter
	- `water_percentage`: the percentage of the water area
- `calling code`: list of country calling codes currently in use
- `gdp`: gross domestic product
	- `nominal`:
		- `total`: nominal GDP in USD million
		- `per_capita`: nominal GDP per capita in USD
	- `ppp`: GDP at purchasing power parity
		- `total`: GDP (PPP) in millions of international dollar
		- `per_capita`: GDP (PPP) in international dollar
- `driving_side`: the side of the road on which vehicles drive
- `gini`: Gini coefficient
	- `estimate`: latest estimate of the Gini coefficient
	- `year`: year in which the estimate was made
- `hdi`: list of annual Human Development Index values
	- `value`
	- `year`: year of the data
- `gii`: list of annual Gender Inequality Index values
	- `value`
	- `year`: year of the data
- `time_zone`: list of time_zones (daylight saving times are not included)
- `tld`: latin-character ccTLD (country code top-level domain)
- `un`
	- `status`: current status of the United Nation membership
	- `year`: year in which this status was obtained
- `unm49`: information related to UN M49
	- `main`: main region
	- `sub`: sub-region
	- `intermediate`: intermediate region
	- `cc`: country code
- `continent`: LIST (because of transcontinental countries) of continents
- `languages`:
	- `official`: list of official languages
		- `iso_a3`: ISO 639-3 code of the language
		- `name`: name of the language
- `nato`: information about the NATO membership
	- `is_member`: true if the country is a member of NATO, false otherwise
	- `relations`: list with arrangements between the country and NATO
- `inflation`: list with annual inflation data
	- `rate`: annual average inflation
	- `year`: year of the data
- `independence`:
	- `is_independent`: True if the country is independent, False otherwise
	- `sovereign_state`: sovereign state of the country
		- `iso_a3`: Alpha-3 code of the sovereign state (null if the country is independent)
		- `name`: name of the sovereign state (null if the country is independent)
	- `status`: the status in regards to the sovereign state (null if the country is independent)
- `centroid`: geographical center of the country
	- `latitude`: latitude of the geometric center
	- `longitude`: longitude of the geometric center
- `land_borders`:
	- `total`: total length of all land boundaries
	- `countries`: list of the individual lengths for each border country
		- `iso_a3`: Alpha-3 code of the neighboring country
		- `name`: name of the neighboring country
		- `length`: length of the border with the neighboring country in km
- `gov_type`: government type
- `coastline`: length of the coastline indicated in meter
- `is_landlocked`: True if the country is landlocked, False otherwise
- `arton`: passport index by Arton Capital
	- `ms`: mobility score
	- `vf`: visa-free
	- `voa`: visa on arrival
	- `eta`: electronic travel authorization
	- `vr`: visa required
	- `ppr`: (global) passport power rank
	- `ipr`: individual power rank
	- `wr`: world reach stated as a percentage
- `emoji_flag`: flag of the country as emoji
- `elec_access`: list of annual data about access to electricity
	- `year`
	- `total`: percentage of total population that has access to electricity
	- `urban`: percentage of urban population that has access to electricity
	- `rural`: percentage of rural population that has access to electricity
- `clean_access`: access to clean fuels for cooking
	- `year`
	- `value`: percentage of population with primary reliance on clean fuels and technology
- `renewable`: renewable energy share in the total final energy consumption
	- `year`
	- `value`: percentage of renewable energy
- `efficiency`: energy intensity level of primary energy
	- `year`
	- `value`: efficiency in megajoules per constant 2017 purchasing power parity GDP

### UK
ISO 3611-1 only includes the United Kingdom and not its constituent countries. Because the Countries dataset is based on said standard, it also doesn't contain England, Scotland, Wales and Northern Ireland. This dataset is for everyone interested in data about those individual countries. I tried to keep the schema similar to the one from Countries, but removed/changed a few properties.

Available formats: JSON, YAML, XML and CSV.

Each entry has the following properties:
- `name`
  - `short`: short, English name
  - `official`: official, English name
- `iso_code`: ISO 3166-2:GB code
- `largest_city`: largest city by population
- `capital`
- `currencies`: list of official currencies
	- `iso_a3`: ISO 4217 code of the currency
	- `name`: name of the currency
- `population`
- `area`
	- `total`: total area, i.e. land plus water area, in square meter
	- `land`: land area in square meter
	- `water`: water area in square meter
	- `water_percentage	`: the percentage of the water area
- `calling_code`: list of country calling codes currently in use
- `gva`: gross value added
	- `total`: total gva in pounds million
	- `per_capita`: gva per capita in pounds
- `driving_side`: the side of the road on which vehicles drive
- `hdi` Human Development Index
- `time_zone`: list of time_zones (daylight saving times are not included)
- `tld`: latin-character ccTLD (country code top-level domain)
- `continent`: LIST of continents
- `languages`:
	- `official`: list of official languages
		- `iso_a3`: ISO 639-3 code of the language
		- `name`: name of the language
- `independence`:
	- `is_independent`: True if the country is independent, False otherwise
	- `sovereign_state`: sovereign state of the country
		- `iso_a3`: Alpha-3 code of the sovereign state (null if the country is independent)
		- `name`: name of the sovereign state (null if the country is independent)
	- `status`: the status in regards to the sovereign state  (null if the country is independent)
- `centroid`: geographical center
	- `latitude`: latitude of the geographical center
	- `longitude`: longitude of the geographical center
- `land_borders`:
	- `total`: total length of all land boundaries
	- `countries`: list of the individual lengths for each border country
		- `iso_a3`: Alpha-3 code of the neighboring country
		- `name`: name of the neighboring country
		- `length`: length of the border with the neighboring country in km
- `gov_type`: government type
- `coastline`: length of the coastline indicated in km
- `is_landlocked`: True if the country is landlocked, False otherwise
- `emoji_flag`: flag of the country as emoji

### US States
This set contains data about all 50 U.S. states and the District of Columbia.

Each entry has the following properties:
- `name`
    - `area`
		- `total`: total area, i.e. land plus water area, in square miles
		- `land`: land area in square miles
		- `water`: water area in square miles
- `capital`
- `largest_city`: largest city by population
- `neighbours`: list of all neighbouring states
    - `code`: second part of the ISO 3166-2:US code, e.g. CA for California
    - `name`: name of the neighbour
- `median_age`: median age of the population
- `population_by_age_and_sex`
    - `from`: start of the age range (inclusive)
    - `to`: end of the age range (inclusive)
    - `male`
    - `female`
- `ancestry`
    - `type`
    - `value`
- `no_internet`: percentage of population without internet subscription
- `languages`: languages spoken at home
    - `type`
    - `value`
- `foreign_born`: percentage of population that's foreign born
- `residential_mobility`: data about relocation to and inside the state
    - `type`
    - `value`
- `veterans`
    - `total`: percentage of population (18+ years) that's veterans
    - `male`: percentage of veterans that are male
    - `female`: percentage of veterans that are male
- `income`
    - `total`: median household income in USD
    - `by_family`: list of median income in USD grouped by type of family
        - `type`
        - `value`
- `poverty`
    - `total`: percentage of population for which the poverty status is determined
    - `by_age`: poverty percentage grouped into age groups
        - `from`
        - `to`
        - `value`
- `education`: education attainment for population 25 years and over
    - `type`
    - `value`
- `school_enrollment`: school enrollment for population 3 years and over
    - `type`
    - `value`
- `worker_classes`
    - `type`
    - `value`
- `average_commute`: average travel time to work in minutes
- `commute_type`: means of transportation to work for population 16 years and over
    - `type`
    - `value`
- `employment_rate`
    - `year`
    - `value`
- `work_hours`: mean usual hours worked per week
    - `total`
    - `male`
    - `female`
- `median_rent`: median gross rent in USD
- `rent`
    - `from`
    - `to`
    - `value`
- `homeownership_rate`
- `housing_value`
    - `from`
    - `to`
    - `value`
- `housing_units`
    - `total`: total amount of housing units
    - `occupied`: amount of occupied housing units
    - `vacant`: amount of vacant housing units
- `occupied_units_by_type`
    - `type`
    - `value`
- `bedrooms`: amount of occupied housing units grouped by number of bedrooms
    - `from`
    - `to`
    - `amount`
- `vacancy_rate`
    - `year`
    - `value`
- `disability_rate`: amount of population that's disabled
- `disability_types`
    - `type`
    - `value`
- `birth_by_mother_age`: amount of births grouped by the age of the mother
    - `from`
    - `to`
    - `value`
- `health_insurance_coverage`: amount of population without health care coverage
    - `year`
    - `value`
- `average_family_size`
- `marital_status`: marital status for population 15 years and over
    - `type`
    - `male`
    - `female`

### Currencies
This dataset includes all the currencies mentioned in the Countries set under the property of the same title. All currencies from the ISO 4217 Table A.1. are covered, except for fund codes, precious metals, complementary currencies and other special entries. There's only one additional currency, which is not part of ISO 4217: Bitcoin. It has been added, because it is legal tender in two countries and thus mentioned in the Countries dataset.

Available formats: JSON, YAML, XML and CSV.

Each entry has the following properties:
- `name`: name of the currency
- `iso`: ISO 4217 codes
  - `a3`: ISO 4217 three-letter code
  - `n3`: ISO 4217 three-digit code
- `symbol`: symbol representing the currency
- `subunit`: data about the subunit of the currency
	- `name`: name of the subunit
	- `symbol`: symbol representing the subunit
	- `value`: value of the subunit specified in the main currency
- `banknotes`
	- `main`: list of currently circulating banknotes denominated in the main currency
	- `sub`: list of currently circulating banknotes denominated in the sub currency
- `coins`
	- `main`: list of currently circulating coins denominated in the main currency
	- `sub`: list of currently circulating coins denominated in the sub currency
- `bank`: central bank/monetary authority, that governs the currency
- `exchange`: information about the exchange rate regime
	- `arrangement`: exchange rate arrangement
	- `policy`: monetary policy framework
- `used_by`: list of countries that use this currency
	- `iso_a3`: Alpha-3 code of the country
	- `name`: name of the country

### Flags
This dataset contains flags in svg format. All entries from the countries, uk and us states dataset are covered.

Available formats: SVG.

### GeoJson
This dataset contains GeoJson files representing the borders of each country/state. All entries from the countries, uk and us states dataset are covered.

Available formats: GeoJSON.

### Passports
This dataset contains pictures of all passports, which are covered in Arton Capital's passport index.

Available formats: JPG.
