# PyD3Stratify

To create a script for parsing csv file into json that can be used by d3.stratify() in version 5.

## Usage

```shell
python3 PyD3Stratify.py -i ./data/in/fire_department_calls_for_service.csv -o ./data/out/fire_department_calls_for_service_stratified.json --headers "City,Neighborhooods - Analysis Boundaries,Zipcode of Incident" --root California --lookup ./data/in/lookup.json
```

## Options

0. "-i" : Input file path and name
1. "-o" : Output file path and name
1. "--headers" : Columns in the header to use, order of hierarchy. i.e. city -> neighborhood -> zipcode
1. "--root" : Whether to add a root and the root name
1. "--lookup" : Lookup table file path and name. To translate terms like SF -> San Francisco.
