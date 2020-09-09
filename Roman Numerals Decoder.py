def solution(roman):
    """
    Create a function that takes a Roman numeral as its argument and returns its value as a numeric
    decimal integer. You don't need to validate the form of the Roman numeral
    """
    md = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(roman) - 1):
        if md[roman[i]] < md[roman[i + 1]]:
            ans -= md[roman[i]]
        else:
            ans += md[roman[i]]
    ans += md[roman[len(roman) - 1]]
    return ans


assert solution('XXI') == 21  # 'XXI should == 21'
assert solution('I') == 1  # 'I should == 1'
assert solution('IV') == 4  # 'IV should == 4'
assert solution('MMVIII') == 2008  # 'MMVIII should == 2008'
assert solution('MDCLXVI') == 1666  # 'MDCLXVI should == 1666'
