def arithmetic_arranger(problems, show_result=False):
  if len(problems) > 5:
    return "Error: Too many problems."
    
  arranged_problems = ""
  first_row = ""
  second_row = ""
  third_row = ""
  fourth_row = ""

  for problem in problems:
    problem_array = problem.split()
    print(problem_array)
    op = problem_array[1]
    num1 = problem_array[0]
    num2 = problem_array[2]
    num1len = len(num1)
    num2len = len(num2)
    line = "-"
      
    if op not in ("+", "-"):
      return "Error: Operator must be '+' or '-'."

    if num1len > 4 or num2len > 4:
      return "Error: Numbers cannot be more than four digits."

    if num1len > num2len:
      line *= num1len + 2
    else:
      line *= num2len +2

    if num1.isdigit() and num2.isdigit():
      num1 = int(num1)
      num2 = int(num2)
    else:
      return "Error: Numbers must only contain digits."

    if first_row == "":
      first_row += str(num1).rjust(len(line))
      second_row1 = str(num2).rjust(len(line) - 2)
      second_row2 = str(op).ljust(2)
      second_row += second_row2 + second_row1
      third_row += line
    else:
      first_row += "    " + str(num1).rjust(len(line))
      second_row1 = str(num2).rjust(len(line) - 2)
      second_row2 = str(op).ljust(2)
      second_row += "    " + second_row2 + second_row1
      third_row += "    " + line

    if op == "+" and show_result == True:
      if fourth_row == "":
        fourth_row += str(num1 + num2).rjust(len(line))
      else:
          fourth_row += "    " + str(num1 + num2).rjust(len(line))
    elif op == "-" and show_result == True:
      if fourth_row == "":
        fourth_row += str(num1 - num2).rjust(len(line))
      else:
          fourth_row += "    " + str(num1 - num2).rjust(len(line))

  if show_result:
    arranged_problems = f"{first_row}\n{second_row}\n{third_row}\n{fourth_row}"
  else:
    arranged_problems = f"{first_row}\n{second_row}\n{third_row}"

  return arranged_problems
