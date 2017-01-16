## csv

- the **Either** type _Either a b_ contains either a _Left a_ or a _Right b_ value and is usually used to return an error in **Left** or a value in **Right**.
- we will use `Data.Either.Unwrap` module to unwrap the **Right** part of a call to `Text.CSV.parseCSVFromFile` function

## json

- when using Aeson, **FromJSON** and **ToJSON** are _types_ not functions.
