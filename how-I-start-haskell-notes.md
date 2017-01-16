## while following Chris Allen's tutorial

- [How I start Haskell](https://howistart.org/posts/haskell/1)

## start up

```
$ stack new bassbull simple
Downloading template "simple" to create project "bassbull" in bassbull/ ...
  ...
Writing configuration to file: bassbull/stack.yaml
All done.
```

- how to I run `stack build` from intero?
- A: I can't see any obvious means from `M-x intero- ?` so just run it from bash

```
$ stack exec bassbull
hello world
```

## first pass code

```haskell
module Main where

import qualified Data.ByteString.Lazy as BL
import qualified Data.Vector as V
-- from cassava
import Data.Csv

-- a simple type alias for data
type BaseballStats = (BL.ByteString, Int, BL.ByteString, Int)

main :: IO ()
main = do
  csvData <- BL.readFile "../data/batting.csv"
  let v = decode NoHeader csvData :: Either String (V.Vector BaseballStats)
  let summed = fmap (V.foldr summer 0) v
  putStrLn $ "Total at bats were: " ++ (show summed)
  where summer (_, _, _, atBats) sum = sum + atBats
```


- consider the type alias:

```haskell
-- a simple type alias for data
type BaseballStats = (BL.ByteString, Int, BL.ByteString, Int)
```

- Chris says:

- I made it a type alias:
    - so I could put off talking about algebraic types!
    - I made it a type alias of the 4-tuple specifically because Cassava already understands how to translate CSV rows into tuples
        - and our type will just work as long as the `Int` columns are really parseable as integral types.
- Haskell tuples are allowed to have heterogeneous types and are defined primarily by their length.
- the parentheses and commas are used to signify them.
- Eg, `(a, b)` would be both a valid value, and a type constructor referring to 2-tuples
    - `(a, b, c)` for 3-tuples, etc.

- consider the type of Data.ByteString.Lazy.readFile:

```haskell
BL.readFile :: FilePath -> IO BL.ByteString
```

- according to Chris:
- You can read this in English as:

> I take a FilePath as an argument and I return a ByteString after performing some side effects.

- We are binding over the `IO ByteString` that `BL.readFile "../data/batting.csv"` returns.
- `csvData` has type `ByteString` due to binding over `IO`.
- `()` is the 0-tuple, which is often called _unit_ in Haskell.
- it can't contain anything; it is a type that has a single value, ie, `()`.
- it is often used to signify that we dont return anything.
- Since there is usually no point to execute functions that return nothing, `()` is often wrapped in `IO`.
- eg, printing strings
- sure enough, the type of `putStrLn` is `putStrLn :: String -> IO ()`
- in Haskell you can't actually "return nothing"; the concept is not expressible functionally.
- so people use `()` idiomatically to express that concept
- usually when something returns `()`, one will not even bother to bind that to a name; just ignore it.

- consider:

```haskell
  let v = decode NoHeader csvData :: Either String (V.Vector BaseballStats)
```

- `v` has the type you see at the right after the `::` type assignment operator
- I am assigning the type to dispatch the typeclass that `decode` uses to parse csv data.
- see more about the [typeclass cassava uses for parsing csv data](http://hackage.haskell.org/package/cassava-0.4.2.0/docs/Data-Csv.html#t:FromRecord)

----

- in this case, because Chris defined a `type` alias of a tuple for the record, the parsing code is derived, as what? are already defined for tuples, BL.ByteString and Int
- Q here for follow up

- consider:

```haskell
  let summed = fmap (V.foldr summer 0) v
```

- here we are binding the name `summed` to the expression.
- NB. summed is not necessarily? or just plain not evaluated then
    - it is not evaluated until / unless it is needed
    - in fact the term? name? `summer` is not yet defined

----

- first we fmap over `Either String (V.Vector BaseballStats)`
- this lets us apply `(V.foldr summer 0)` to `V.Vector BaseballStats`.
- we partially applied the `Vector` folding function `foldr` to the summing function and the numeral `0`.
- the number `0` here is the start value for the fold.

----

- generally in Haskell we don't use recursion directly
- instead, use higher order functions and abstractions
    - giving names to common things programmers want to do
    - like folding data
- fold means _reduce_
- AI: consider reading at least the overview of [haskell fold](https://wiki.haskell.org/Fold)
    
----

- we say `V.foldr` is partially applied because we haven't applied all of the args yet.
- cf: currying
- show currying at the repl

```haskell
λ data Person = Person String Int String deriving Show
λ :t Person
Person :: String -> Int -> String -> Person
λ :t Person "jeff" 408
Person "jeff" 408 :: String -> Person
λ :t Person "jeff" 408 "mcc"
Person "jeff" 408 "mcc" :: Person
λ let anyJeff = Person "jeff"
λ anyJeff 408

<interactive>:17:1: error:
    • No instance for (Show (String -> Person))
        arising from a use of ‘print’
        (maybe you haven't applied a function to enough arguments?)
    • In a stmt of an interactive GHCi command: print it
λ anyJeff 408 "mcc"
Person "jeff" 408 "mcc"
```

## quick demo of `fmap` and `foldr`

- at the repl

```haskell
λ let v = Right 1 :: Either String Int
λ let x = Left "bogon" :: Either String Int
λ :t x
x :: Either String Int
λ :t v
v :: Either String Int
λ let addOne z = z + 1
λ addOne 2

<interactive>:26:1: warning: [-Wtype-defaults]
    • Defaulting the following constraints to type ‘Integer’
        (Num a0) arising from a use of ‘it’ at <interactive>:26:1-8
        (Show a0) arising from a use of ‘print’ at <interactive>:26:1-8
    • In the first argument of ‘print’, namely ‘it’
      In a stmt of an interactive GHCi command: print it
3
λ fmap addOne x
Left "bogon"
λ fmap addOne v
Right 2
```

- here we see the Haskell convention that `Left` is used to return an error; not the happy path
- this is used by `fmap` I think.
- Chris says:

- `Either` is used to signfiy cases where we might get values of one of two possible types.
- `Either String Int` says: you'll either get a String or an Int
- `Either` has two constructors, `Right` and `Left`.
- culturally in Haskell, `Left` signifies an "error" case.
- this is partly why the `Functor` instance for `Either` maps over the `Right` constructor, but not the `Left`

----

- conveniently, `fmap` lets us avoid pattern matching the `Left` and `Right` cases of `Either` manually
- and it handles a list parameter, avoiding recursion
- and it handles the recursion terminal condition of the empty list.
- Chris gives an example of the manual way of handling the `Left` and `Right` cases.

----

- Q ask for help is reading these types:

```haskell
λ :t foldr
foldr :: Foldable t => (a -> b -> b) -> b -> t a -> b
λ :t (++)
(++) :: [a] -> [a] -> [a]
λ :t (++) "a"
(++) "a" :: [Char] -> [Char]
```

- for `(++)`, I would say

> ++ has type

----

- You can hang `where` clauses off of functions, which are a bit like `let`, but they come last
- `where` clauses are more common than `let` clauses, bu there is nothing wrong with using both.

## refactoring

NB. Chris chose a tuple representation for the row because cassava already knows them.  He suggests converting this to a Haskell record type later.

- reduce `(_, _, _, atBats)` to a type? function? that extracts the fourth element of the tuple
- add

```haskell
fourth :: (a, b, c, d) -> d
fourth (_, _, _, d) = d
```

- and then change

```haskell
where summer (_, _, _, atBats) n = n + atBats
```

- to

```haskell
where summer r n = n + fourth r
```

- if we apply _eta reduction_ as in [point free programming](https://www.haskell.org/haskellwiki/Pointfree)
- since our computation really collapses to a single scalar
- we can reduce summer to what it is: adding two numbers, one of which comes from the fourth value of a tuple
- from

```haskell
where summer r n = n + fourth r
```

- to

```haskell
where summer = (+) . fourth
```

- `.` is how functions are composed in Haskell.
- the entire defn of `.` is: `(f . g) x = f (g x)`
- so eg, if we `multiplyByTwo . addOne`, first we add one, then pass that result to the times 2 function.

----

- split out the decoding of the csv datea
- move / refactor this code:

```haskell
  let v = decode NoHeader csvData :: Either String (V.Vector BaseballStats)
```

- into an independent function

```haskell
baseballStats :: BL.ByteString -> Either String (V.Vector BaseballStats)
baseballStats = decode NoHeader
```

- then `summed` becomes

```haskell
let summed = fmap (V.foldr summer 0) (baseballStats csvData)
```

- and the complete code with Vector is:

```haskell
module Main where

import qualified Data.ByteString.Lazy as BL
import qualified Data.Vector as V
-- from cassava
import Data.Csv

-- a simple type alias for data
type BaseballStats = (BL.ByteString, Int, BL.ByteString, Int)

fourth :: (a, b, c, d) -> d
fourth (_, _, _, d) = d

baseballStats :: BL.ByteString -> Either String (V.Vector BaseballStats)
baseballStats = decode NoHeader

main :: IO ()
main = do
  csvData <- BL.readFile "../data/batting.csv"
  let summed = fmap (V.foldr summer 0) (baseballStats csvData)
  putStrLn $ "Total games played were: " ++ show summed
  where summer = (+) . fourth
```

## convert to read a record at a time

- since cassava supports reading a record at a time, we can convert so that we don't need to hold all of the rows in a `Vector` in memory
- tell Cassava we want the Streaming interface: `Data.Csv.Streaming`
- then replace `Vector` with the `Foldable` typeclass Cassava offers for use with its streaming API:
- switch

```haskell
import qualified Data.Vector as V
```

- to

```haskell
import qualified Data.Foldable as F
```

- and then change the defn of `summed` to operate a record at a time. From:

```haskell
  let summed = fmap (V.foldr summer 0) (baseballStats csvData)
```

- to

```haskell
let summed = F.foldr summer 0 (baseballStats csvData)
```

- and we no longer need the function that reads in all of the records and returns them as `Either String (V.Vector BaseballStats)`
- say good bye to:

```haskell
baseballStats :: BL.ByteString -> Either String (V.Vector BaseballStats)
baseballStats = decode NoHeader
```

- and hello instead to:

```haskell
baseballStats :: BL.ByteString -> Records BaseballStats
baseballStats = decode NoHeader
```

- the key here is `Records`
- which info says:

```haskell
Records in `Main.hs' (bassbull)

data Records a
  = Cons (Either String a) (Records a)
  | Nil (Maybe String) BL.ByteString
  	-- Defined in ‘Data.Csv.Streaming’
instance Eq a => Eq (Records a) -- Defined in ‘Data.Csv.Streaming’
instance Functor Records -- Defined in ‘Data.Csv.Streaming’
instance Show a => Show (Records a)
  -- Defined in ‘Data.Csv.Streaming’
instance Foldable Records -- Defined in ‘Data.Csv.Streaming’
instance Traversable Records -- Defined in ‘Data.Csv.Streaming’
```

- so a `Records a` is always either `Cons` or `Nil`.
- `Cons (Either String a) (Record a)` means the `Cons` data constructor is a product of `Either String A` and `Record a`.
    - we are saying `Cons` is always `Either String a` _and_ `Record a`.  don't get confused by the `Either` -- it applies to `String a`.
    - also, this `Cons` resembles cons-cells in Lisp, Haskell, ML, etc.
    - the source says
    > A record or an error message, followed by more records
- `Nil (Maybe String) BL.ByteString`
    - the `Nil` data constructor is a product of `Maybe String` and `BL.ByteString`
    - the source says:
    > End of stream, potentially due to parse error.  If a parse error occurred, the first field contains the error message.  The second field contains any unconsumed input.

What the records type is doing for us is letting us process records just like a lazy list, but with a little extra content in the `Nil` case.

## Add tests

- add a `test-suite` to the cabal file

```haskell
test-suite tests
  ghc-options:         -Wall
  type:                exitcode-stdio-1.0
  hs-source-dirs:      tests
  main-is:             Tests.hs
  default-language:    Haskell2010
  build-depends:       base >= 4.7 && < 5,
                       bassbull,
                       hspec
```

- √ and refactor the code into a lib as a single module named `Bassbull`.

----

- to get a repl with the tests loaded: `stack ghci bassbull:tests`
- which will give a REPL which has the symbols as loaded by the Cabal named `tests`
- so from there, one can run the main function, or ...

----

- Chris finds he needs fewer tests overall
- he often works with an emacs and a REPL of `stack ghci`
- as his code starts to pass the type checker, he starts running the tests as another layer
