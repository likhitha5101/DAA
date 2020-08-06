# This is CAT-04 Final!
# Do NOT discuss this exercise with anyone during the exam
# Do NOT send your code or copy code from elsewhere
# You are free to dicuss the exercise after the exam is over!



# First version of merging two outlines
def merge1_outlines(u, v):
  outline=[]
  i=0
  j=0
  while(i!=len(u) and j!=len(v)):
    if u[i][0]<v[j][0]:
      outline+=[u[i]]
      i+=1
    else:
      outline+=[v[j]]
      j+=1
  if(i!=len(u)):
    outline+=u[i:]
  else:
    outline+=v[j:]
  return outline

# Seconf version of merging two outlines
def merge2_outlines(u, v):
  outline=[]
  i=0
  j=0
  while(i!=len(u) and j!=len(v)):
    if u[i][0]<v[j][0]:
      temp=(u[i][0],max(u[i][1],v[j][1]))
      i+=1
    else:
      temp=(v[j][0],max(u[i][1],v[j][1]))
      j+=1
    outline+=[temp]
  if(i!=len(u)):
    outline+=u[i:]
  else:
    outline+=v[j:]
  return outline

# Third and final version of merging two outlines
def merge3_outlines(u, v):
  temp_outline=merge2_outlines(u,v)
  n=len(temp_outline)
  outline=[]
  for i in range(0,len(temp_outline)-1):
    if(temp_outline[i][1]!=temp_outline[i+1][1]):
      outline+=[temp_outline[i]]
    if(i+1==len(temp_outline)-1):
      outline+=[temp_outline[i+1]]
  return outline
  
# Here is the "main" function to construct an outline of given rectangles
def construct_outline(rs):
  n=len(rs)
  if(n==0):
    return []
  if(n==1):
    return rs[0]
  else:
    l1=construct_outline(rs[:n//2])
    l2=construct_outline(rs[n//2:])
    result=merge3_outlines(l1,l2)
  return result

# As stated in the problem, a sample set of rectangles could be
rs = [ [(1,0),(5,11)], [(2,0),(7,6)], [(3,0),(9,13)], [(12,0),(16,7)], [(14,0),(25,3)], [(19,0),(22,18)], [(23,0),(29,13)], [(24,0),(28,4)] ]

# You may check the output produced
print(construct_outline(rs))

