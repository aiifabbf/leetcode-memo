"""
最少需要几个视频片段就可以覆盖0秒到T秒？
"""

from typing import *

import itertools

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # for clipCount in range(0, len(clips) + 1):
        #     combinations = itertools.combinations(clips, clipCount)
            
        #     for combination in combinations:
        #         # interval = [0] * (T + 1)
        #         interval = 0

        #         for clip in combination:
        #             clipLength = clip[1] - clip[0] + 1
        #             # interval[clip[0]: clip[0] + clipLength] = [1] * clipLength
        #             interval = interval | (int("1" * clipLength, 2) << clip[0])
        #             # print(bin(interval))

        #         temp = interval + 1
        #         if temp & (temp - 1) == 0: # interval全1
        #             if interval.bit_length() >= T + 1:
        #                 return clipCount
        #             else:
        #                 continue
        #         else:
        #             continue
        #             # print(combination)
        # else:
        #     return -1
        # 一改：暴力果然是过不了的
        


s = Solution()
# print(s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))
# print(s.videoStitching([[0,1],[1,2]], 5))
# print(s.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9))
print(s.videoStitching([[0,5],[1,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],[8,13],[9,14],[10,15],[11,16],[12,17],[13,18],[14,19],[15,20],[16,21],[17,22],[18,23],[19,24],[20,25],[21,26],[22,27],[23,28],[24,29],[25,30],[26,31],[27,32],[28,33],[29,34],[30,35],[31,36],[32,37],[33,38],[34,39],[35,40],[36,41],[37,42],[38,43],[39,44],[40,45],[41,46],[42,47],[43,48],[44,49],[45,50],[46,51],[47,52],[48,53],[49,54]], 50))