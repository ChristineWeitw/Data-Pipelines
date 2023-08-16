# Data-Pipelines

## Building a Data Pipeline
#### Functional Programming
    - In functional programming, functions (pure functions) are stateless, they rely only on their given inputs to produce an output. This helps reduce the "side effect", which occurs when changes occur within a function's operation that are outside its scope. 
    - functional programming vs. object-oriented (imperative) programming 
    - ex. Lambda Expression (can be use as anonymous function, which is extremely helpful, especially when using them as an input for another function. For example, the sorted() function takes in an optional key argument (a function) that describes how the items in a list should be sorted.
      ** we can use a lambda expression instead of the def syntax.
    - ex. first-class functions (pass in functions as arguments) : "The Map Function"
        # Note: We convert the returned map object to a list data structure.
        add_10 = list(map(lambda x: x + 10, values))
    - ex. first-class functions : "The Filter Function" (takes in an iterable, creates a new iterable object)
        # Note: We convert the returned filter object to a list data structure.
        even = list(filter(lambda x: x % 2 == 0, values))
    - ex. first-class functions : "The Reduce Function" (takes in a function and an iterable object such as a list. Then reduce the list to a single value by successively applying the given function.)    
        values = [1, 2, 3, 4]
        summed = reduce(lambda a, b: a + b, values)
        print(summed) -- 10
    - ex. "List Comprehension"
    - ex. "Function Partials" (takes in a function, and "freezes" any number of args (or kwargs), starting from the first argument, then returns a new function with the default inputs.)
        from functools import partial        
        def add(a, b):
            return a + b
            
        add_two = partial(add, 2)
        print(add_two(4)) -- 6

#### Pipeline Tasks
#### Building a Pipeline Class
#### Multiple Dependency Pipeline
#### Guided Project: Hacker News Pipeline


credit: dataquest.io
