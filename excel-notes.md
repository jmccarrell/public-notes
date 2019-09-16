# Intro to Formulas

## Array formulas

When you enter an array formula, press Ctrl+Shift+Enter (not just Enter).
Excel encloses an array formula in brackets in order to remind you that it's an array formula.

    {=SUM(LEN(A1:A10))}

In general, Excel formulas are not case sensitive, except in quoted strings.

## Object and Cell Selecting

* Ctrl-*  to select an entire table
* When a large range is selected, Ctrl-. will move among the 4 corners of the range.

## Tables

* Converting a range to a table makes it easier to perform operations on that data
* Rows represent objects
* Columns are attributes of each object
* To declare data in this format as a table, use
    * select the range, or a cell in the range
    * Insert -> Tables -> Table

## Entering formulas

* Alt-Enter should insert a literal linebreak in a formula
* On the mac the "Paste Name" functionality is available in the menu hierarchy:
    * Insert -> Name -> Paste
* If a formula is giving an error, convert it to text by removing the leading =

## Selected Excel Operators

| operator | semantics |
|----------|-----------|
|&         | text concatenation |
|<>        | not equal to != |

## Reference Operators

Reference operators work with cell references

| operator | semantics |
|----------|-----------|
| :        | Range.  Produces one reference to all cells between 2 references |
| ,        | Union.  Combines multiple cells references into one reference |
| \<SPACE\>| Intersection.  A single space character produces cells common to two references |

## And and Or

Excel does not have logical and and or operators; rather these are functions, like this:

    =AND(A1<1, A2<10)

## Operator Precedence

| operator | semantics |
|----------|-----------|
| : , \<SPACE\> | Reference |
| -        | Negation |
| %        | Percent |
| ^        | Exponentiation |
| *  /     | Multiplication, division |
| +  -     | addition, subtraction |
| &        | text concatenation |
| = <> etc | comparison |

## Referencing cells in another worksheet

Precede the cell reference with the sheetname and !; eg:

    =Sheet7!A26 + 42

## Copy / Move Formulas

* When you copy a cell containing a formula, the cell references are updated as part of the copy
* When you move a range that contains formulas, the cell references are *not* updated.
    * this is usually what you want semantically
* To copy the formula without adjusting cell references, copy it to the clipboard as text, then paste

## Autofill

* The fill handle is the small right square at the bottom of the active cell
* Dragging that handle will fill-down or fill-right
* Option while dragging can change the fill operation
* Fill-series works from 2 cells: 10, 15 gives the series with step value 5.
* Other series that are recognized include weekday names and month names
* Custom fill values are available in Windows; but I don't see a reference to this functionality in the mac version search help

## Goal Seek

* is at
    * Tools -> Goal Seek
* goal seek can only adjust 1 input cell to find the outcome.
* for > 1 input cell, use the Solver add-in.


# Names

- All excel objects can be named; however cell and range names are handled differently that other names.
- The list of named objects can be seen in the Go To... menu
    - Edit -> Go To ...
- Looking at Go To ... can show referenced objects without a name, that may be better served by a named object.

## Name Scope

- names are scoped to one of two levels:
    - workbook scope: this is the default scope
    - worksheet scope
        - these can be useful when the same named data needs to be available across multiple worksheets, eg. in a yearly scoped workbook, one might have named data per month.
        - to use a worksheet level name, you must precede the name with the worksheet name; unless you are referring to a name from within the respective worksheet.
    - worksheet scoped names take precedence over workbook scoped names

- the Insert -> Name -> Paste dialog only shows worksheet scoped names, not workbook scoped names

- A scan of my excel menubar did not reveal an exact analog to the windows Name Manager dialog.
    - the os x equivalent is Insert -> Name

- A name may refer to a non-contiguous range of cells

## Name Syntax

- Alpha numeric, period, underscore
- Names cannot *look like* a cell reference: eg: Q4, A1.A12, May21
- not case sensitive
- predefined excel names to avoid:
    - Print_Area, Print_Titles, Consolidate_Area, Database, Criteria, Extract, FilterDatabase, and Sheet_Title

## Name Creation

- To distinguish a worksheet vs. workbook scoped name, at name creation time, prefix the name with the worksheet name to get worksheet scope.  Otherwise, you get workbook scope.

- a set of names can be created from data in columns or rows in the spreadsheet
    - select the region
    - Insert -> Name -> Create

### Name entire rows or columns

- select the column
- enter the name for that colum
    - eg: DailySales might be a name for column B: `=Sheet3!$B:$B`
    - and a use might be `=SUM(DailySales)`

### Creating Multisheet Names

- The syntax for multisheet references is

    `FirstSheet:LastSheet!RangeReference`

- worksheets later added to the workbook between FirstSheet and LastSheet will be included in the multisheet range

## Intersection operator and names

- the space character is the range intersection operator.
    - so do not use spaces in names to make the syntax simpler

### Explicit intersection

    `=Insurance Feb`

### Implicit intersection

- Use a columnar name value in a different column of the same row the name is defined in

    `=ExpenseCategories`

- eg if `=ExpenseCategories` is put in row 42, then it is as if the formula evaluated is:

    `=ExpenseCategories 42:42`

### Range operator with Names

- One can also name smaller intersections of named ranges: eg
    `SUM((Insurance Apr):(Travel Jun))`
would sum the Q2 values for the Insurance through Travel expense categories


## Named Constants

- One can define constants in the Define Name dialog
    - Insert -> Name -> Define
    - in the reference field, enter a formula that evaluates to a constant:
        - `=42`
        - `="McCarrell Org"`
- Names that do not refer to ranges do not appear in the Name box

## Relative References in Names

- a CellToRight that refers to one cell to the right of the cell containing the formula
    - first, activate cell A1
    - `=!B1`
    - the worksheet name is null, which means it will work on any worksheet
- The key is the relationship between the active cell when the name is defined, and the cell(s) in the formula.  Those 2 points define the geometry here.

### Mixed Range References

- a FirstInRow formula might be
    - `=!$A1`
    - So the column is fixed to Column A; the row varies

- FirstInColumn might be
    - `=!A$1`

## Advanced Name Techniques

### Indirection through a Name

- The excel function `INDIRECT` follows the reference through a name
- E.g. if I have a worksheet level name `IncomeByMonth` defined on each of my monthly worksheets Jan ... Dec, and I have those month names in Column A, then this formula would fetch the IncomeByMonth from each worksheet:
    - `=INDIRECT(A1&"!IncomeByMonth")`
    - which evaluates to
    - `=Jan!IncomeByMonth`

## Arrays in Named Formulas

- Arrays are syntactically defined using curly brackets
- The value separator is either comma or semicolon
    - comma to expand the array in row values
    - semicolon for column values
- eg this will define the 12 month names in 1 row of 12 columns
    - MonthsOfYear
    - `={ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" }`
    - To use this, select a 12 col wide row
    - Insert -> Name -> Paste -> MonthsOfYear
    - Ctrl-Shift-Enter
    - recall that Array formulas require the special key sequence
    - the resulting formula in all 12 cells is:
        - `={MonthsOfYear}`
    - You cannot delete any of the 12 cells
    - In effect, you have a single formula that spans 12 cells
- To put these values in a column, select 12 rows in a column, then:
    - `=TRANSPOSE(MonthsOfYear)` + Ctrl-Shift-Enter
    - which displays as `{=TRANSPOSE(MonthsOfYear)}`

# Tables

- Tables are named entities.
- The table range definition does not include the header row or the summary total row

- Some example table formulas:

    `=[@[Receive Date]]-[@[Bill Date]]`

    - in this case, there are 2 columns in the table: *Receive Date* and *Bill Date*.
    - if the column name is only alphanumeric, the inner most brackets may be dropped:

        `=[@Income] - [@Expense]`

    - the @ sign, in say @Income, means *this row*, in that it names the current row of the Income colume of the table.
    - if the column names in the table change, the table formulas names will update.
    - the formula work may be performed in any row of the table.
    - these formulas inside a table are so-called *calculated columns*.

## Table References

- to reference a column, say Income, of a table, say named Income_Detail, use:

    `=SUM(Income_Detail[Income])`

## Subtotal and Aggregate

- these functions change their behavior depending on whether rows are hidden or not.
- thus to SUM the same data but ignore hidden rows, use either of

    `=SUBTOTAL(109,Income_Detail[Income])`

    `=AGGREGATE(9,1,Income_Detail[Income])`

- where the ugly constants control the operation the subtotal or aggregate function performs.
    - the constants are best supplied by the auto-fill formula builder dialog.

## Totals References

- to refer to a value in the totals row, use something like this:

    `=Income_Detail[[#Totals], [Income]]`


### Table Syntax

| operator | semantics
|----------|-----------
|#All      | range including header, data and total rows
|#Data     | just the data; no header, no total
|#Headers  | just header
|#Totals   | just total
|@         | represents just *this* row.  returns the intersection of the column and the current row


# Pivot Tables



# Excel To Do

- try to figure out if excel for os x supports name scoping
    - worksheet and workbook
    - thus far I don't see any references to name scope in os x excel
- see if formula auto complete works in mac excel.  cf. figure 2-1.
    - it looks like Option-Command-Enter adds a newline to the formula at entry
        - however, when displayed, all the whitespace is collapsed again
    - if this is done in the formula bar however, the whitespace stays.
- how does one compute modulus?
- Excel help: "function keys" will show "Excel keyboard shortcuts".  Read this as needed.

- how do I make a table with display names for the months that sorts by date?
    - I could make 2 columns
