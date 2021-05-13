# Poznámky a přehledy z výuky Python na MZLU

# Datové struktury python

| vlasnost() | tupple() | list() | set() | dict() |
|:----:|:----:|:----:|:----:|:----:|
|**Odpovídá**|n-tice, pole|seznam|množina||slovník|
|**Změny**|neměnné, nelze přiřadit novou hodnotu|lze měnit|nelze měnit hodnoty, lze přidat/ubrat|x |
|**definice**|ntice = **(**"A", "B", "C"**)**|seznam = **[**1, 2, 3**]**|mnozina = **{**"a", "b", "c"**}**|slovnik = **{**'one'**:*** 1, 'two'**:** 2, 'three'**:** 3**}**
|**obsahuje**|různé typy,i stejné hodnoty|různé typy i stejné hodnoty|pouze unikátní hodnoty různé typy|
|**konverze**||seznam = **list**(ntice)|||
|**přístup**|ntice[0] .. ntice[2]|seznam[0] .. ntice[2]||
|**řazení**|indexem|indexem|neřazen|