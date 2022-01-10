def arithmetic_arranger(problems,true=''):

  line1 = []
  line2 = []
  line3 = []
  line4 = []

  for problem in problems:
    if len(problems) > 5:
      arranged_problems = 'Error: Too many problems.'
      return(arranged_problems)
      break
    
    problem = problem.split()
    
    if '+' not in problem[1] and '-' not in problem[1]:
      arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
      return(arranged_problems)
      break
    
    if problem[0].isdigit() == False or problem[2].isdigit() == False:
      arranged_problems = 'Error: Numbers must only contain digits.'
      return(arranged_problems)
      break
    
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      arranged_problems = 'Error: Numbers cannot be more than four digits.'
      return(arranged_problems)
      break

    solution = eval(problem[0]+problem[1]+problem[2])



    if len(problem[0]) > len(problem[2]):
      length = len(problem[0]) - len(problem[2])
      line1new = ('  ' + problem[0])
      line1.append(line1new)
      line2new = (problem[1] + ' '*(length+1) + problem[2])
      line2.append(line2new)
      line3.append('-'*(len(problem[0]) + 2))
      line4new = (' '*(len(problem[0])-len(str(solution))+2)+str(solution))
      line4.append(line4new)
    else:
      length = len(problem[2]) - len(problem[0]) + 2
      line1new = (' '*length + problem[0])
      line1.append(line1new)
      line2new = (problem[1]+' '+problem[2])
      line2.append(line2new)
      line3.append('-'*(len(problem[2]) + 2))
      line4new = (' '*(len(problem[2])-len(str(solution))+2)+str(solution))
      line4.append(line4new)
    
        
  line1str = ('    '.join(line1))
  line2str = ('    '.join(line2))
  line3str = ('    '.join(line3))
  line4str = ('    '.join(line4))

  if true == True:
    arranged_problems = '\n'.join((line1str, line2str, line3str,line4str))
  else:
    arranged_problems = '\n'.join((line1str, line2str, line3str))

  return(arranged_problems)

