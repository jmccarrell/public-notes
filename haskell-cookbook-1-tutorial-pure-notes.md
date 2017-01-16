# notes as I work through the leanpub book.

- run the first example:
- in the repl

```
jeff at vega in /j/proj/haskell-tutorial-cookbook/examples/Database-sqlite on jwm-work
$ stack build --exec ghci
```
----

## haskell repl vs emacs intero mode

- so in intero, just C-c C-l to load the repl
- then type.
- how do I see the type of an expression in intero?
- A: C-c C-t

----

describe mode shows the following haskell/intero bindings:

```
C-c C-b         haskell-mode-enable-process-minor-mode
C-c TAB         haskell-mode-enable-process-minor-mode
  (that binding is currently shadowed by another mode)
C-c C-l         haskell-mode-enable-process-minor-mode
  (that binding is currently shadowed by another mode)
C-c C-s         haskell-mode-toggle-scc-at-point
C-c C-t         haskell-mode-enable-process-minor-mode
  (that binding is currently shadowed by another mode)
C-c C-v         haskell-mode-enable-process-minor-mode
C-c C-,         haskell-mode-format-imports
```

- the flycheck bindings:

```
C-c ! C-c       flycheck-compile
C-c ! C-w       flycheck-copy-errors-as-kill
C-c ! ?         flycheck-describe-checker
C-c ! C         flycheck-clear
C-c ! H         display-local-help
C-c ! V         flycheck-version
C-c ! c         flycheck-buffer
C-c ! e         flycheck-explain-error-at-point
C-c ! h         flycheck-display-error-at-point
C-c ! i         flycheck-manual
C-c ! l         flycheck-list-errors
C-c ! n         flycheck-next-error
C-c ! p         flycheck-previous-error
C-c ! s         flycheck-select-checker
C-c ! v         flycheck-verify-setup
C-c ! x         flycheck-disable-checker
```

----

## types

haskell has builtin

- characters
- strings
- lists
- tuples

- the type **Char** is a single character.
- one type of string is a list of characters **[Char]**.
    - there is also **ByteString**
- every element of a list must have the same type.
- a **Tuple** is like a list, but elements can have different types.

- so single quote is a char:

```
λ :t 's'
's' :: Char
```

- double quote is a string

```
λ :t "tree"
"tree" :: [Char]
```

- the name **String** is defined for list of char **[Char]**; either can be used.
- `:` is the cons operator, so:

```
λ 's' : "Tree"
"sTree"
```

- the cons `:` operator works with all types contained in any lists.
    - subject to the constraint that all elements must be of the same type in a list.

- the expression **[1,2,2,4] :: Num t => [t]** is read

> t is a type variable equal to **Num** and the type of the list is **[t]** or a list of **Num** values.

- **head** and **tail** return the first elt of a list, or the list without the first elt.

- tuples may have different types.
- tuples of length 2 are special because functions **fst** and **snd** are provided to access the first and second pair value

```
λ fst (1, "10 downing st")
1
λ snd (1, "10 downing st")
"10 downing st"
```

- length of a tuple is always 1, because of the way tuples are defined as Foldable types.
- haskell provides a concise notation to get values out of long tuples.
- this notation is called destucturing.

```
λ let geo_data = (1, "10 downing st", 80345, 98.6)
λ let (_,_,zip_code,temperature) = geo_data
λ zip_code
80345
λ temperature
98.6
```

- all Haskell functions start with a lower case letter except for type constructor functions.
- a **Foldable** type can be iterated through and be processed with map functions.

- we saw that `+` acts as an infix operator.
- we can convert infix functions to prefix functions by enclosing them in parenthesis:
- a prefix function can be used infix by enclosing it in back tick characters
- back ticks work on user defined functions as well.

```
λ (+) 1 2
3
λ :t (+)
(+) :: Num a => a -> a -> a
λ div 10 3
3
λ 10 `div` 3
3
λ :t div
div :: Integral a => a -> a -> a
```

- **++** seems to be a list? concatenation operator.
- does it work on tuples?
- A: no apparently not.

```
λ geo_data ++ geo_data

<interactive>:54:1:
    Couldn't match expected type ‘[a]’
```

----

- we can create new functions via currying:

```
λ let p1 = (+ 1)
λ :t p1
p1 :: Num a => a -> a
λ p1 20
21
```

- in this example, the function `+` takes two args.
- when only one arg is supplied, the expression returns a function that takes one arg.

- we can also compose existing functions using the infix function **.** that when placed between 2 function names produces a new function.
- eg

```
λ let lengthp1 = (+ 1) . length
λ :t lengthp1
lengthp1 :: Foldable t => t a -> Int
λ lengthp1 "abcd"
5
```

## haskell types

- simple type example:

```haskell
data MyColors = Orange | Red | Blue | Green | Silver
  deriving (Show, Eq)
```

- Haskell also supports hierarchies of types called **Type classes**.
- **Foldable** is an example of a type class that other types can inherit from.
- for now, consider sub-types of **Foldable** to be collections like lists and trees that can be iterated over.

- How do I run :info inside of intero?
- A: put the cursor in the buffer at the beginning of a symbol, like Ord, then C-c C-i

```
Ord in `MyColors.hs' (Pure)

class Eq a => Ord a where
  compare :: a -> a -> Ordering
  (<) :: a -> a -> Bool
  (<=) :: a -> a -> Bool
  (>) :: a -> a -> Bool
  (>=) :: a -> a -> Bool
  max :: a -> a -> a
  min :: a -> a -> a
  	-- Defined in ‘ghc-prim-0.4.0.0:GHC.Classes’
```

- this says that **Ord** is a subtype of **Eq**
- it defines functions compare, max, min
- defines operators <, <=, >, >=

## pure functions

- the common pattern is to pass immutable values to a function and return modified values.
- as a first example, consider map:
- map is a function that takes two arguments
    - a function that converts a value of type *a* to another type *b*
    - a list of type *a*
- functions that take other functions as arguments are called **higher order functions**
- the result is a another list of the same length whose elements are of type *b*.

----

- the type of function main is IO Action, which is impure.

```
λ :t main
main :: IO ()
```

- how do I [type a lambda character in emacs](http://stackoverflow.com/questions/6269618/how-can-i-input-greek-symbols-like-beta-lambda-in-emacs) 24?
- C-x 8 RET 3bb
- 3bb is the hex code for lambda
- C-x 8 RET is bound to insert-char

## parenthesis, special `$` character and precedence

- BTW, in Haskell, there is not much difference between operaters and function calls, except infix vs. prefix.
- so besides infix functions that are enclosed in back ticks

```haskell
λ 10 `div` 2
5
```

- Haskell usually uses prefix functions: a function followed by 0 or more arguments.
- you can also use `$` that acts as an opening parenthesis with a not-shown closing parenthesis at the end of the current expression
    - which may be multi-line.

- `:info` gives precedence in the [infix{,l,r} fixity declaration](https://wiki.haskell.org/Keywords#infix.2C_infixl.2C_infixr)

```haskell
λ :info `div`
class (Real a, Enum a) => Integral a where
  ...
  div :: a -> a -> a
  ...
  	-- Defined in ‘GHC.Real’
infixl 7 `div`
λ :i +
class Num a where
  (+) :: a -> a -> a
  ...
  	-- Defined in ‘GHC.Num’
infixl 6 +
```

- notice how + is lower precedence than *
    - 6 < 7

## lazy evaluation

```haskell
let xs = [0..]
λ :t xs
xs :: (Enum t, Num t) => [t]
λ :sprint xs
xs = _
λ take 5 xs
[0,1,2,3,4]
λ take 5 xs
[0,1,2,3,4]
```

- the `_` that `:sprint` returns says that xs is unevaluated.
- and sure enough, applying `take` multiple times yields the same value each time.

## understanding list comprehensions

- this is a list comprehension with a filter expression on `y`:

```haskell
:{
*Main| [(x,y) | x <- ["cat", "dog"],
*Main|  y <- [1..10],
*Main|  y `mod` 3 == 0]
*Main| :}
[("cat",3),("cat",6),("cat",9),("dog",3),("dog",6),("dog",9)]
```

- another kind of idiom? / trick uses the zip function
- like enumerate in python

```haskell
λ zip [1..] [("cat",3),("cat",6),("cat",9),("dog",3),("dog",6),("dog",9)]
[(1,("cat",3)),(2,("cat",6)),(3,("cat",9)),(4,("dog",3)),(5,("dog",6)),(6,("dog",9))]
```

## code indenting rules

- when a line of code is indented relative to prior lines, it is treated as if it were one logical line.
- one can use C-style braces and semi colons, but this is considered bad style.

## understanding let vs where

- in pure code, a `let` needs? an `in` expression to scope where those values are to be bound.
- in impure code, such as inside a `do` block, an `in` following a `let` will cause a parse error.
- you also do not use `in` inside a list comprehension.
- see `LetAndWhere.hs` for examples.

## conditional do expressions and anonymous functions

- it is a common? convention? to append a single quote the end of built-in functions when one redefines them
- thus

```haskell
head' (x:_) = x
tail' (_:xs) = xs
```

- these redefinitions use wild card pattern matching, similiar to destructuring earlier.
- the underscore matches anything and ignores the matched value.
- so `head'` and `tail'` work just like the built-ins.

```haskell
doubleList [] = []
doubleList (x:xs) = (* 2) x : doubleList xs
```

- here line 1 defines a pattern to match the empty list, not a type defn for doubleList.
- it is necessary to define the terminating condition.
- because we use recursion in line 2.

```haskell
map' (\x -> (x + 1) * 2) [0..5]
```

- here the first arg to `map'` is an anonymous function
- put the symbols you want exported in the module statement

```haskell
module Test2 (doubler) where
```

- only exports the symbol `doubler`.

## pattern matching with guards

- the **Maybe** type is mostly used in non-pure Haskell code
- is a Monad

- Guards are more flexible than pattern matching of last section.
- use pattern matching for simple destructuring and guards for more flexibility.

- in this example that implements the [ruby spaceship operator](http://stackoverflow.com/questions/827649/what-is-the-ruby-spaceship-operator):

```haskell
spaceship n
  | n < 0 = -1
  | n == 0 = 0
  | otherwise = 1
```

- there is no `=` in the function defn
    - contrast with numberOpinion below
- the guard starts with `|`, contains a condition, and a value on the RHS of `=`
- like lisp `cond`

- recall a literal negative number must be wrapped in parentheses
    - otherwise `-` is considered an operator

## case expressions

- Case **do** expressions match a value against a list of possible values.
- it is common to use `_` as the wildcard catch all at the end of the expr, which can be of any type.

```haskell
numberOpinion n = 
  case n of
    0 -> "Too low"
    1 -> "just right"
    _ -> "OK, that is a number"
```

## if then else

- Haskell has if then else; if is not defined as a function.
- the author does not use if then else very often
    - he prefers simple pattern matching and guards
- all **if** statements must have both a **then** and an **else** expression.

## maps

- maps are easy to construct from key-value tuples, and are immutable by default.
- mutable maps do exist.
- the keys and the values in a map must each be of the same type
    - all the keys have the same type, call it a
    - all the values have the same type, call it b
- the author almost always creates maps using the helper function **fromList** in **Data.Map**.
    - should be [**Data.Map.Strict**](https://www.stackage.org/haddock/lts-7.15/containers-0.5.7.1/Data-Map-Strict.html)

## sets

- glossed over by the author.
- [types of sets defined?](https://www.stackage.org/package/sets)
    > ducktyped set interface for Haskell containers
- which points to [Data.Set.Class](https://www.stackage.org/haddock/lts-7.15/sets-0.0.5.2/Data-Set-Class.html)
    > Convenience operators overloaded for arbitrary use. There are no laws associated with these classes, just duck-typed so we don't have to use the qualified versions of each function.

- sets and maps are immutable.

## more on functions

```haskell
λ let makeList n = [0..n]
λ :t makeList
makeList :: (Enum t, Num t) => t -> [t]
```

- notice how the compiler infers the type of the arg to makeList to be constrained to either a `Num` or an `Enum`
    - from the usage of the arg in the function defn

```haskell
λ let make3 x = [x, x, x]
λ :t make3
make3 :: t -> [t]
```

- whereas the compiler cannot make that inference in the `make3` defn.
- however, if you ask the type of make3 with an argument, then the type inference kicks in:

```haskell
λ :t make3 'a'
make3 'a' :: [Char]
λ :t make3 3.14159
make3 3.14159 :: Fractional t => [t]
```

## Error Handling

- prefer Maybe, Just, and Nothing to the standard function [error](https://wiki.haskell.org/Exception)
