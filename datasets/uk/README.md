# UK
Source: Unless otherwise stated, the data was scrapped from some [Wikipedia](https://en.wikipedia.org/) page.

## iso_code
The ISO code listed in this dataset is not from ISO 3166-1, as that standard only includes the United Kingdom as a whole. As a replacement the codes from ISO 3166-2:GB are used here.

## hdi
Source: [GlobalDataLab](https://globaldatalab.org/shdi/table/shdi/GBR/?levels=1+4&years=2021&extrapolation=)

## gva
I didn't find any values for the individual GDPs, so instead the dataset includes the GVA from 2021.

Source: [Office for National Statistics](https://www.ons.gov.uk/economy/grossvalueaddedgva/datasets/nominalregionalgrossvalueaddedbalancedperheadandincomecomponents)

## tld
The countries dataset only includes ccTLDs (country code top-level domains), but none of the four countries in this dataset have their own ccTLD. So instead I included a geoTLD (geographic top-level domain) for Wales and Scotland and set it to ".uk" for England and Northern Ireland, because they don't even have their own geoTLD.

## continent
Even though all the entries in this dataset are part of only one continent, this property is still a list to stay consistent with the format of the countries dataset.

## emoji_flag
Northern Ireland doesn't have an emoji_flag included, because it's not part of Unicode's RGI (Recommended for General Interchange) set and thus barely supported by any platform.