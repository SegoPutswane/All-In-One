# Question 1
def get_date_of_birth(id_number: str) -> str:
    """
    STEP 2: Extract the date of birth from the ID number and return it as a string
    return format: DD/MM/YY:
    """
    #separating the date of birth from the ID number and converting it into a string
    dob = str(id_number)[0:6]
    #assign an empty string where the date of birth will be stored after generating
    result = ""

    #looping through the extracted date of birth to check where to place the forward slashes
    for i in range(len(dob)):
        result += dob[i]
        if (i + 1) % 2== 0 and i < len(dob) - 1:
            result += "/"
    return result

# Question 2
def get_gender(id_number: str) -> str:
    """
    STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
    gender_digits = str(id_number)[6:10]

    if int(gender_digits) < 5000:
        return "Female"
    return "Male"

# Question 3
def fizzbuzz(n):
    """Fizzbuzz is a programme that prints the numbers from 1 to n, 
    but for multiples of 3, it prints "Fizz" instead of the number, 
    and for multiples of 5, it prints "Buzz" instead of the number. 
    For numbers that are multiples of both 3 and 5, it prints "FizzBuzz.

    TODO: define a function called fizzbuzz and implement the fucntionality above.
    """

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Question 4
def find_even_numbers(numbers):
    """Find the even numbers in the list 'numbers' and return them in
    in a tuple

    Hint: use modulus (%)"""
    even_num = []
    for number in numbers:
        if number % 2 == 0:
            even_num.append(number)
    even_num = tuple(even_num)
    return even_num


# Question 5
def find_odd_numbers(numbers):
    """Find the odd numbers in the list 'numbers' and return them in
    in a tuple

    Hint: use modulus (%)"""
    odd_num = []
    for number in numbers:
        if number % 2 != 0:
            odd_num.append(number)
    odd_num = tuple(odd_num)
    return odd_num

# Question 6
def return_list_stats(numbers):
    """Given the list 'numbers', use the relevant functions to return a
    dictionary of statics for the list. This dictionary must have
    the following keys:
        unique_numbers : a set containing unique numbers from the list 'numbers',
        max : largest number in the list 'numbers',
        min : smallest number in the list 'numbers',
        average : average of the numbers in the list 'numbers',
        even_numbers : a tuple of all the even numbers in the list
            'numbers',
        odd_numbers : a tuple of all the odd numbers in the list
            'numbers',
        number_of_even_numbers : the total number of even numbers in the
            list 'numbers',
        number_of_odd_numbers : the total number of even numbers in the list
             'numbers'
    """
    #getting the unique numbers in the list
    unique_numbers = set(numbers)

    #minimum number
    minimum_num = min(numbers)

    #maximum number
    maximum_num = max(numbers)

    #average of the list
    ave_number = sum(numbers)/len(numbers)

    #even numbers in the list
    even_num = []
    for number in numbers:
        if number % 2 == 0:
            even_num.append(number)

    #odd numbers in the list
    odd_num = []
    for number in numbers:
        if number % 2 != 0:
            odd_num.append(number)

    #number of even numbers
    even_count = 0
    for number in numbers:
        if number % 2 != 0:
            even_count += 1

    #number of odd numbers
    odd_count = 0
    for number in numbers:
        if number % 2 != 0:
            odd_count += 1

    return {"unique_numbers" : unique_numbers,
            "min": minimum_num,
            "max": maximum_num,
            "average": ave_number,
            "even_numbers": even_num,
            "odd_numbers": odd_num,
            "number_of_even_numbers": even_count,
            "number_of_odd_numbers": odd_count,}



# Question 7
def draw_triangle_reversed(height: int) -> None:
    """
    Draw an inverted number triangle where each row begins with its position number,
    with the top row having the most repeated numbers and each row below having one fewer repetition.

    Parameters:
        height (int): The height of the triangle. Must be a positive integer.

    Returns:
        None: Prints the inverted triangle pattern directly to console.

    """
    n = 5
    for i in range(n,0,-1):
        print(""*(n-i)+"*"*i)

# Question 8
def draw_triangle_prime(height: int) -> None:
    """
    Draws a triangle of prime numbers where each row contains the first n primes
    that fit the row width.

    Parameters:
        height (int): The height of the triangle. Must be a positive integer.

    Returns:
        None: Prints the prime number triangle pattern directly to console.

    """
    pass

# Question 9
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """
    pass
