## API
Here you will find a description of the endpoints available in the api.
Or you can run the project and go to:

```
http://0.0.0.0:8000/docs
```



### dose
  - Endpoints related to the doses of the covid vaccines.

|Method| Comando | Descripción |
|---| --- | --- |
|GET|/dose/get_all_dose|Get All Dose|
|POST|/dose/save_dose|Save Dose|
|POST|/dose/get_or_create_dose|Get Or Create New Dose|

### establishments
  - Endpoints related to available vaccination establishments.

|Method| Comando | Descripción |
|---| --- | --- |
|GET|/establishments/get_all_establishments|Get All Establishments|
|POST|/establishments/save_establishment|Save Establishment|
|POST|/establishments/get_or_create_establishment|Get Or Create New Establishment|
|GET|/establishments/filter_by_name/{establishment_name}|Establishment By Name|
|GET|/establishments/filter_by_name/{establishment_name}/{cant}|Establishment By Name Cant|

### vaccine
  - Endpoints related to the vaccines used in vaccination campaigns.

|Method| Comando | Descripción |
|---| --- | --- |
|GET|/vaccine/get_all_vaccines|Get All Dose|
|POST|/vaccine/add_new_vaccine|Add New Vaccine|
|POST|/vaccine/get_or_create_vaccine|Get Or Create New Vaccine|
|POST|/vaccine/get_vaccine_by_name/{vacc_name}|Get Vaccine By Name|

### records
  - Endpoints related to the individual records of the vaccinated.

|Method| Comando | Descripción |
|---| --- | --- |
|GET|/record/get_all_records|All Records|
|POST|/record/add_new_record|Add New Record|
|GET|/record/filter_by_name/{name}|Fileter By Name|
|GET|/record/filter_by_name_all/{name}|Fileter By Name All|
|GET|/record/filter_by_last_name/{last_name}|Fileter By Last Name|
|GET|/record/filter_by_last_name_all/{last_name}|Fileter By Last Name All|
|GET|/record/filter_by_ci/{ci}|Fileter By Ci|
|GET|/record/filter_if_contains_ci/{ci}|Fileter If Contains Ci|
|GET|/record/filter_by_application_date_all/{date}|Filter By Application Date All|
|GET|/record/filter_by_application_date_limit/{date}/{cant}|Filter By Application Date Restricted Size|
|GET|/record/filter_by_establishment_id/{id}|Filter By Establishment Id|
|GET|/record/filter_by_establishment_id_limit/{id}/{cant}|Filter By Establishment Id Limit|

