def climbingLeaderboard(ranked, player):
    sol=[]
    positions = sorted(set(ranked), reverse = True)
    positions.append(0)

    for i in player:
        try:
            index=positions.index(i)
        except:
            index= searchInsert(positions,i)
            positions=positions[:index]+[i]+positions[index:]
            sol.append(index+1)
        else:
            sol.append(1+positions.index(i))
            
    return sol  
def searchInsert(nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left