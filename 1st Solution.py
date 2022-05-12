class Solution(object):
   def S_M(self, n):
      """
      :type n: int
      :rtype: List[str]
      """
      result = []
      for i in range(1,n+1):
         if i% 3== 0 and i%5==0:
            result.append("S&M")
         elif i %3==0:
            result.append("S")
         elif i% 5 == 0:
            result.append("M")
         else:
            result.append(str(i))
      return result
ob1 = Solution()
print(ob1.S_M(30))