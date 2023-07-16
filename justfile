set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]

test:
    cd {{justfile_directory()}}/tests && pytest

convert:
    cd {{justfile_directory()}}/datasets/countries && cp countries.json countries.yaml
    cd {{justfile_directory()}}/datasets/countries && yq -i -p=json -o=yaml '.' countries.yaml
    cd {{justfile_directory()}}/datasets/countries && cp countries.json countries.xml
    cd {{justfile_directory()}}/datasets/countries && yq -i -p=json -o=xml '.' countries.xml
    cd {{justfile_directory()}}/datasets/uk && cp uk.json uk.yaml
    cd {{justfile_directory()}}/datasets/uk && yq -i -p=json -o=yaml '.' uk.yaml
    cd {{justfile_directory()}}/datasets/uk && cp uk.json uk.xml
    cd {{justfile_directory()}}/datasets/uk && yq -i -p=json -o=xml '.' uk.xml
    cd {{justfile_directory()}}/datasets/currencies && cp currencies.json currencies.yaml
    cd {{justfile_directory()}}/datasets/currencies && yq -i -p=json -o=yaml '.' currencies.yaml
    cd {{justfile_directory()}}/datasets/currencies && cp currencies.json currencies.xml
    cd {{justfile_directory()}}/datasets/currencies && yq -i -p=json -o=xml '.' currencies.xml
    cd {{justfile_directory()}}/datasets/us_states && cp us_states.json us_states.yaml
    cd {{justfile_directory()}}/datasets/us_states && yq -i -p=json -o=yaml '.' us_states.yaml
    cd {{justfile_directory()}}/datasets/us_states && cp us_states.json us_states.xml
    cd {{justfile_directory()}}/datasets/us_states && yq -i -p=json -o=xml '.' us_states.xml
    cd {{justfile_directory()}}/scripts && python json_to_csv.py
