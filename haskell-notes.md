# Haskell Book

## All you need is lambda

### the structure of lambda terms

- lambda calculus has 3 basic components, or terms
    - expressions
    - variables
    - abstractions

- an abstraction is a function.
- it is a lambda term that has a head (a lambda) and a body, and is applied to an argument.
- an argument is an input value

- abstraction consist of 2 parts:
    - the head
    - the body
    
- the head of a function is a λ (lambda) followed by a variable name.
- the body of a function is another expression.

- so `λx.x` is a nameless lambda abstraction, an anonymous function


- the head of `λx.x` lambda is `λx.`
- `x` is the single parameter
- `x` is also the body


### Alpha equivalence

- as the named parameters is just placeholder,
    - `λx.x`
    - `λy.y`
    - `λx.x`
- all mean the same thing; they are the same function.

### Beta reduction

- when we apply a function to an argument, we substitute the input expression for all instances of bound variables within the body of the abstraction.
- we also eliminate the head, since the heads only purpose is to bind a variable.
- this process is called beta reduction

- NB: `λx.x` defines the identity function, which is often written `f(x) = x`
- one difference is the lambda is anonymous, whereas the mathematical notation defines the name f

- applications in the lambda are left-associative, ie, they group to the left.

- the process of beta reduction stops when there are either no more heads, or lambdas, left to apply or no more arguments to apply functions to.
- a computation therefore consists of an initial lambda expression (or two if you want to separate the function from its input) plus a finite sequence of lambda terms, each deduced from the preceding term by one application of beta reduction.

#### Free Variables

- NB: alpha equivalence does not apply to free variables.
- ie, `λx.xy` and `λx.xz` are not alpha equivalent because y and z might be different things.
- however these are alpha equivalent:
    - `λxy.yx` and `λab.ba`
    - `λx.xz` and `λy.yz` because the free variable z is left alone.

### Multiple Arguments

- each lambda can bind only one parameter and accept only one argument.
- functions that require multiple arguments have multiple, nested heads.
- this is the formulation commonly called *currying*.

- what this means is that
    - `λxy.xy`
- is a convenient shorthand for two nested lambdas (one for each arg, x and y):
    - `λx.(λy.xy)`

#### Example

1. `(λxyz.xz(yz))(λmn.m)(λp.p)`
2. `(λx.λy.λz.xz(yz))(λm.λn.m)(λp.p)`
    - show the currying explicitly
3. `(λy.λz.(λm.λn.m)z(yz))(λp.p)`
    - our first reduction step wa to apply the outer most lambda, which was binding the `x` to the first argument, `(λm.λn.m)`
4. `λz.(λm.λn.m)(z)((λp.p)z)`
    - we applied the y and replaced the single occurence of `y` with the next argument term, `λp.p`.
    - the outermost lambda binding `z` is, at this point, irreducible becuase it has no argument to apply to.
    - what remains is to go inside the terms one layer at a time until we find something reducible
5. `λz.(λn.z)((λp.p)z)`
    - we can apply the lambda binding `m` to the arg `z`.
    - we keep searching for terms we can apply.
    - the next thing we can apply is the lambda binding `n` to the lambda term `((λp.p)z)`
    - which, since there are no `n` in the labmda body, just evaluates to the free variable `z`
    - and discards the argument `((λp.p)z)`
6. `λz.z`
    - there are no further terms to reduce, so we are left with an unreducible lambda expression.

----

- try this expression in Chris' [evaluator](http://cdparks.github.io/lambda-machine)

- (\xyz.xz(yz))(\mn.m)(\p.p)
- chris' evaluator comes up with: `xz yz (λp. p)`
- which is pretty different from the book result: `λz. z`
- Ok, the issue is a difference in the syntactic sugar
- Chris' parser treats λxyz as a lambda with a single param xyz
- and his parser uses space to mean 'apply'
- so if I do the currying and expand the spaces, then we eval to the same result

- (λx. λy. λz. x z (y z))(λm. λn. m)(λp. p)

### Intermission: Equivalence exercises

- choose the answer that is equivalent to the listed lambda term

1. λxy.xz
    a. λxz.xz
        - no, no free variable
    b. λmn.mz
        - yes, m == x; second arg not in body; z a free variable
    c. λz(λx.xz)
        - there is no body; so this evaluates to nothing
        - \z(\x.xz)
            - throws parse error: no . at col 3.
2. λxy.xxy
    a. λmn.mnp
        - no p is a free variable
    b. λx.(λy.xy)
        - evaluates to `λx. λy. xy`
        - body is `xy` not `xxy` so no
    c. λa(λb.aab)
        - yes, after currying becomes: λa.λb.aab

3. λxyz.zx
    a. λx.(λy.(λz.z))
        - no evaluates to: λx. λy. λz.z
    b. λtos.st
        - yes, o is not int the body; t == x; z == s
    c. λmnp.mn
        - no: third bound variable not in body

### Evaluation is simplification

- there are multiple normal forms in lambda calculus, but here normal form refers to *beta normal form*.
- beta normal form: when you cannot beta reduce (apply lambdas to arguments) the terms any further.
- this corrsponds to a fully evaluated expression
- or, in programming, a fully executed program.

- the identity function λx.x is fully reduced (that is, in normal form) because it hasn't been applied to anything.
- however (λx.x)z is not in beta normal form, because we can apply the identity function to the free variable z.
- if we did, the beta normal form would be z.

### Combinators

- defn: a compbinator is a lambda term with no free variables.
- combinators, as the name suggests, serve only to combine the arguments they are given
- so the following are combinators, because every term in the body occurs in the head:

1. λx.x
2. λxy.x
3. λxyz.xz(yz)

- the following are not combinators:

1. λy.x
    - x is free
2. λx.xz
    - z is free

- the point of combinators is that they can only combine/permute their arguments, not introduce new values.

### Divergence

- when the reduction process does not terminate
- omega: (λx.xx)(λx.xx)
- each reduction of omega gives omega back again.

### Summary

- functional programming is based on:
    - expressions that include variables or constant values
    - expressions combined with other expressions
    - and functions
- functions have a head, and a body and those expressions that an be applied to arguments and reduced, or evaluated to a result
- variables may be found in the function declaration, and each and every time a bound variable shows up in a function, it has the same value
- all functions take one argument and return one result.
- functions are a mapping of a set of inputs to a set of outputs.  given the same input, they always return the same output.

- Haskell is a typed lambda calculus, with a lot of surface level decoration sprinkled on top
    - to make it easier to write.
- the meaning of Haskell programs is centered around evaluating expressions, rather than executing instructions
    - although Haskell has a way to execute instructions as well.

### Chapter 1 Exercises

#### Combinator

- determine if these are combinators or not

1. λx.xxx
    - A: yes, every term in the body occurs in the head
2. λxy.zx
    - A: no, z is a free variable
3. λxyz.xy(zx)
    - A: yes, every term in the body (xy) occurs in the head.
    - combinators describe the lambda function, not the argument?
4. λxyz.xy(zxy)
    - A: yes, every term in the body occurs in the head
    - Chris' evaluator says this evals to:
        - λxyz. xy zxy
5. λxy.xy(zxy)
    - no, z is a free variable

#### Normal form or diverge?

1. λx.xxx
    - beta normal form: nothing (no args) to apply
2. (λz.zz)(λy.yy)
    - diverges; this is the omega lambda
3. (λx.xxx)z
    - normal form: zzz
    - this is a combinator

#### Beta reduce

- evaluate, (beta reduce) each expr to normal form.

1. (λabc.cba)zz(λwv.w)
    - assume this is a function λabc.cba
    - with 3 args: z, z, the lambda λwv.w
    - bind a to z
    - (λbc.cbz)z(λwv.w)
    - bind b to z
    - (λc.czz)(λwv.w)
    - bind c to (λwv.w)
    - (λwv.w)zz
    - bind w to z
    - (v.z)z
    - bind v to z
    - z
    - Chris' evaluator gives: cba (λwv. w)
2. (λx.λy.xyy)(λa.a)b
    - assume this is a lambda λx.λy.xyy
    - applied to 2 args λa.a, b
    - bind x to (λa.a)
    - (λy.(λa.a)yy)b
    - bind y to b
    - (λa.a)bb
    - bind a to b
    - bb
    - beta normal form
    - chris evaluator gives:
    - xyy
    - (λy. xyy) b
    - (λx. λy. xyy) (λa. a) b

Chris's evaluator binds the right-most args, but we are told to evaluate the outer most lambda expr first.
is haskell left associative?  yes
I don't get it.

----

- the answer is that there are not clear syntactic rules for the particular syntax here.

3. (λy.y)(λx.xx)(λz.zq)


### Definitions

1. the *lambda* in lambda calculus is the greek letter λ used to introduce, or abstract, arguments for binding in an expression.
2. A lambda *abstraction* is an anonymous function or lambda term
    - `(λx.x + 1)`
    - the head of the abstraction `λx.` abstracts out the term `x + 1`.
    - we can apply the head to any `x` and recompute different results for each x we applied the lambda to.
3. *Application* is how one evaluates or reduces lambdas, this binds the argument to whatever the lambda was applied to.
    - Computations are performed in lambda calculus by applying lambdas to arguments until you run out of arguments to apply lambdas to.
    - `(λx.x)1`
    - this example reduces to 1
    - the identity λx.x was applied to the value 1
    - in a sense, applying the lambda λx.x *consumed* it
    - we reduced the amount of structure we had
4. *Lambda calculus* is a formal system for expressing programs in terms of abstraction and application.
5. *Normal order* is a common evaluation strategy in lambda calculi
    - Normal order means:
        - evaluating (ie, applying or beta reducing) the leftmost outermost lambdas first
        - evaluating terms nested within after you've run out of arguments to apply.
        - Normal order is not how Haskell code is evaluated - its [call by need](https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_need) instead.

## Chapter 2: Hello, Haskell

### install Haskell

- they want me to install:
    - stack
    - which provides:
        - GHC haskell
        - interactive env: GHCi
        - project build / dependency mgr

- read [installation instructions](https://docs.haskellstack.org/en/stable/README/)
- read [learning haskell instructions](https://github.com/bitemyapp/learnhaskell)
- watch [haskell stack mega tutorial](https://www.youtube.com/watch?v=sRonIB8ZStw)

- Ok, stack is installed.

```
$ stack --version
Version 1.3.2, Git revision 3f675146590da4f3edf768b89355f798229da2a5 (4395 commits) x86_64 hpack-0.15.0
```

- stack ghci
- ok, I have the repl up

```
$ stack ghci
Using latest snapshot resolver: lts-7.14
Writing implicit global project config file to: /Users/jeff/.stack/global-project/stack.yaml
Note: You can change the snapshot via the resolver field there.
Downloaded lts-7.14 build plan.
Fetched package index.
Populated index cache.
No compiler found, expected minor version match with ghc-8.0.1 (x86_64) (based on resolver setting in /Users/jeff/.stack/global-project/stack.yaml).
To install the correct GHC into /Users/jeff/.stack/programs/x86_64-osx/, try running "stack setup" or use the "--install-ghc" flag.

jeff at vega in /j/proj/haskell-book/jwm
$ stack ghci --install-ghc
Preparing to install GHC to an isolated location.
This will not interfere with any system-level installation.
Downloaded ghc-8.0.1.
Installed GHC.
Configuring GHCi with the following packages:
GHCi, version 8.0.1: http://www.haskell.org/ghc/  :? for help
Loaded GHCi configuration from /private/var/folders/wp/q4_ccz795s51jcrfm9vv98f00000gn/T/ghci54918/ghci-script
Prelude>
```

----

- write haskell source
- search emacs-wiki for haskell refs?
- ask @david

**Sun Jan 15 10:55:38 PST 2017**

## questions

- what are the case conventions for Haskell?
   - in general
   - used at FrontRow
- I guess types? are Camel case, initial cap

- use `:show paths` in the repl to see cwd, and search paths in that session
