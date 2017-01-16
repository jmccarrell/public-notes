## impure

- one of the great things about Haskell is that it supports/encourages dividing the functional, easily tested parts from the more imperative code that must deal with side effects.

- any **Monad**, which wraps a single value, is used to safely manage state.

## Hello IO() Monad

- the type of function main varies; for most of the examples we have seen so far it is:

```haskell
λ :t Main.main
Main.main :: IO ()
```

- the **IO ()** monad is an IO value wrapped in a type-safe way.
- since Haskell is a lazy evaluator, the value is not evaluated until it is used.
- Every **IO ()** action returns exactly one value.
- think of *mono* when you think of Monads because they always return one value
- monads are also used to connect together parts of a program

- but consider:

```haskell
module NoIO where

main = do
  let i = 1 in
    2 * i
```

- the type of main here is:  `main :: Integer`

- so there is nothing special about a `main` function
- it gets its type from the type from the type of the value returned by the function
- it is common to have the return type depend on the function arg types
- the first example return type **IO ()** because it returns a `putStrLn` value:

```haskell
λ :t putStrLn
putStrLn :: String -> IO ()
```

- **print** shows enclosing quote chars for strings while **putStrLn** does not

### do exprs

- the **do** notation makes working with monads easier.
- NB: combinations of **do** and **let** with **in** may need to be wrapped in an inner **do**.
- cf: **bind**

- I'm guessing the **do** creates a scope or block into which the let values are bound.

- example1 is considered good style:

```haskell
module DoLetExample where

example1 = do  -- good style
  putStrLn "Enter an integer number:"
  s <- getLine
  let number = (read s :: Int) + 2
  putStrLn $ "Number plus 2 = " ++ show number
```
- while example2  is less good:

```haskell
example2 = do  -- avoid using "in" inside a do statement
  putStrLn "Enter an integer number:"
  s <- getLine
  let number = (read s :: Int) + 2 in
    putStrLn $ "Number plus 2 = " ++ (show number)
```

- although hlint doesn't have anything to say about the use of **in**.
- if there are multiple statements in the **in**, then another **do** is required
    - kind of lisp-ish
- ie

```haskell
example3 = do  -- avoid using "in" inside a do statement
  putStrLn "Enter an integer number:"
  s <- getLine
  let number = (read s :: Int) + 2 in
    do
      putStrLn "Result is:"
      putStrLn $ "Number plus 2 = " ++ (show number)
```

- the **do** expression is syntactic sugar that allows programmers to string together operations of both pure and input code.

- to be clear, the left arrow `<-` is used when the RHS is some type of **IO ()** that has to be *lifted* before being used.
- here I assume *lifted* is jargon for fully evaluated.
- a **let do** expr is used the RHS is a pure value.

## about `>>` and `>>=` operators

- the author prefers **do**
- but others prefer `>>` and `>>=`
- the Monad type class defines the operators `>>=` and `return`.
- consider:

```haskell
λ :t (>>)
(>>) :: Monad m => m a -> m b -> m b
λ :t (>>=)
(>>=) :: Monad m => m a -> (a -> m b) -> m b
λ :t return
return :: Monad m => a -> m a
```

- so `return` when applied to a Monad `m`, takes a value `a` and wraps it in the monad `m`.
- we will see examples of the return function used to return a wrapped value from a function that returns **IO ()** values.
- the *bind* operator (>>) is used to evaluate two expressions in sequence.
- so we can replace

```haskell
main = do
  example1
  example2
  example3
```

- with

```haskell
main = example1 >> example2 >> example3
```

- the operator **>>=** is similiar to **>>** except that it evaluates the left hand expression and pipes its value to the RHS.
- in a common pattern, the LHS evals to some type of **IO ()** and the RHS reads from the input **IO ()**.
- eg

```haskell
module DoLetExample3 where

example3 =  putStrLn "Enter an integer number:" >>  getLine

example4 mv = do
  let number = (read mv :: Int) + 2
  putStrLn $ "Number plus 2 = " ++ (show number)

main = example3 >>= example4
```

- if we replace `>>=` above with `>>`, the code will not compile because of the type differences between example3 and 4?
- what types are they?

```haskell
example3 :: IO String
example4 :: String -> IO ()
```

- ?
- so in this case, what type is example3?
- I don't know how to parse the decl `example3 :: IO String`
- what is an `IO String`?

## console I/O example with stack configuration

- consider

```haskell
module Main where

import System.IO
import Data.Char (toUpper)

main = do
  putStrLn "Enter a line of text for test 1:"
  -- s <- getLine
  putStrLn $ "As upper case:\t" ++ (map toUpper getLine)
  main
```

- notice in particular `(map toUpper getLine)`
- this will not compile:

```
     9  49 error           Couldn't match expected type ‘[Char]’ with actual type ‘IO String’
     In the second argument of ‘map’, namely ‘getLine’
     In the second argument of ‘(++)’, namely ‘(map toUpper getLine)’ (intero)
```

- because of evaluation order.
- the type of getLine is `IO String`, ie, a wrapped IO call that must be evaluated to yield a String.
- the `<-` assinment in: `s <- getLine` yields the String.

## File IO

- Text type is more efficient than String
    - but he didn't say why
- here main is called recursively to achieve the looping effect

```haskell
module Main where

import System.IO
import Data.Char (toUpper)

main = do
  putStrLn "test2: Enter a line of text:"
  s <- getLine
  putStr $ "toUpper:\t" ++ (map toUpper s)
  appendFile "temp.txt" $ s ++ "\n"
  main
```

- why is it `(map toUpper s)` and not just `(toUpper s)`
- because toUpper is defined on: Char -> Char

```haskell
λ :t toUpper
toUpper :: Char -> Char
```

- is there a toUpper defined on String?
- apparently not:

```haskell
λ :t toUpper "string"

<interactive>:1:9:
    Couldn't match expected type ‘Char’ with actual type ‘[Char]’
    In the first argument of ‘toUpper’, namely ‘"string"’
```

- `appendFile` opens, appends, and closes the file.
- appendFile is of type:

```haskell
appendFile :: FilePath -> String -> IO ()
```

## error handling in impure code

- consider drilling down into [Michael Snoyberg's discussion of exceptions](https://www.schoolofhaskell.com/user/snoyberg/general-haskell/exceptions/catching-all-exceptions)

## haskell game loop

- that maintains state functionally

```haskell
     1	module GameLoop2 where
     2
     3	import System.Random
     4
     5	data GameState = GameState { numberToGuess::Integer, numTries::Integer}
     6	                   deriving (Show)
     7
     8	gameLoop :: GameState -> IO GameState
     9	gameLoop gs = do      
    10	  print $ numberToGuess gs
    11	  putStrLn "Enter a number:"
    12	  s <- getLine
    13	  let num = read s :: Integer
    14	  if num == numberToGuess gs then
    15	    return gs
    16	  else gameLoop $ GameState (numberToGuess gs) ((numTries gs) + 1)
    17
    18	main = do
    19	  pTime <- randomRIO(1,4)
    20	  let gameState = GameState pTime 1
    21	  print "Guess a number between 1 and 4"
    22	  gameLoop gameState
```

> notice that in line 12 since we are inside a **do** expr, we can *lift* (or unwrap) the **IO String ()** value returned from **getLine** to a string value that we can use directly.

- Q for Chris:
    - is this recursive pattern common in the FR code base?
    - is it really tail recursion, and if so, does the compiler eliminate the tail recursion?

## efficiency of Haskell strings

- for longer strings, it is much more efficient (measured how? space?) to use the module `Data.Text` defined in package `text`
- so add `text` to dependencies in the cabal file
- fortunately, Haskell strong typing enables support for a language extension to handle both String and Data.Text
- this is activated by adding the following near the top of a Haskell source file:

```
{-# LANGUAGE OverloadedStrings  #-}
```

- the conversion is handled by knowing the type signatures of data and functions in surrounding code.
- the compiler figures out what type of string is expected, and supplies conversions.

## more Monads

- intro to **State** monad
- deeper look at **IO ()**
- Monads are types belonging to the Monad type class that specifies one operator and one function:

```haskell
class Monad m where
  (>>=) :: m a -> (a -> m b) -> m b
  return :: a -> m a
```

- the `>>=` operator takes two arguments:
    - a monad wrapping a value (**a** in the listing)
    - a function that takes **a** and returns a monad wrapping a new type **b**
    - the return value of `>>=` is then the value of that function, ie, a monad wrapping a value of type **b**.

- the Monad type class function **return** takes any value and wraps it in a new monad.
- confusingly, **return** here has nothing to do control flow

- Q for Chris:
    - practice decoding type statements
    - how to read them
    - specifically, how to interpret `->`

## how to read type defns

- `::` can be read as _has type_ or _has a type defition of_
- remember every function returns a single value, so everything else in the type signature are parameters separated by `->`
- the arrow `->` is the type constructor for functions in Haskell.
- perhaps `=>` is the type class arrow

### parsed examples

- `incrementState :: State Int Int`
- Alex said:
    - `incrementState` is a function that returns a value of type `State Int Int`.
    - The first part, `State` is the type, and the next two are essentially the types it’s parameterized over
    - so it’s a `State x y` where the types of x and y are `Int`
- ChrisP said:
    - either way, @alex 's description of `State Int Int` is correct.
    - a type `X Y Z` is some type `X` applied to two types `Y` and `Z`.
    - So all we know at the type level is that `State` takes two type parameters, and we've filled both in with `Int`
    - we know more than that about `State` though.
    - `State x y` is a computation that may modify (update or replace) `x` and will, if it halts, return a value of `y`
    - from looking at the name and type, i would _expect_ `incrementState :: State Int Int` to add one to the state value and return either the updated value, or the previous value. the type here doesn't actually constrain the implementation too much.


- `runState :: State s a -> s -> (a, s)`
    - is `(a, s)` here a function?  a tuple?
    - A: a tupule; in fact, the return value of `runState`.
    - how do I read the `->` here?
    - A: as argument separators
- Chris:
    - `runState` has the type "a function taking a `State s a` argument and an `s` argument and returning `(a, s)`"
    - the lowercase names are _type variables_ they can be filled in with concrete (capital letter) types like `Int` or `Char` or `[Text]`.
    - the variables with the same name must be filled in with the same type
    - e.g. you can't fill `s` in with `Int` in `State s a` and then fill in the `s` that's by itself with `Char`
- Alex:
    - `runState` takes a `State` parameterized over type s and a and a second parameter of type s, and returns a tuple with first entry of type a and second entry of type s

## the value of `State`

- a discussion about what `State` is good for
- Alex said he has never used it; ChrisP said he uses it all the time
- Chris: `State` specifically is a tool that keeps you from having to manually thread a state parameter through a bunch of functions
- Alex: Also keep in mind you can do things the lispy way where you pass state around or you can try to get fancy and stuff the state in the context the way you’re doing it here
    - so you can always start brain dead and make it fancier down the line
- Chris: yeah. i would pass state around manually until it starts to suck, and then you'll have reached the motivation for `State` :smile:
    - also, the `Monad` instance for `State` will make more sense then
    - because it will look like what you've been having to do manually
    - just packaged up neatly
    - and done by an operator that makes it seem implicit

### State Monad

- the defn for the constructor of a State monad is:

```haskell
newtype State s a = State { runState :: s -> (a, s) }
```

- `newtype` is like `data`, except:
    - newtype acts during compile time
    - no type info is present at run time
- all Monads contain a value and for the State monad, this value is a function.
- the `>>=` operator is called the *bind* operator.

- the accessor function `runState` provides the means to access the value of the monad.

## Applicative operators `<$>` and `<*>`

- a new term _Functor_ which is a typeclass that defines only one method **fmap**.
- fmap is used to map a function over an IO action and has the type signature

```haskell
fmap :: Functor f => (a -> b) -> f a -> f b
```

- fmap can be used to apply a pure function like **(a -> b)** to an **IO a** and return a new **IO b** without unwrapping the original **IO ()**
- eg

```haskell
incomplete
```
